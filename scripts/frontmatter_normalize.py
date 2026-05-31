"""Frontmatter normalization Phase B.

Adds, where missing per page:
- owner: wiki-llm
- stale_after_days: per-type default (source=90, finance=30, ops=120, else=60)

For pages with type == "source": backfill pages_updated by reverse-linking
across all wiki/**/*.md frontmatter `sources:` arrays containing this source's
slug. Slug derivation = filename basename (e.g. ssot-v6.md -> ssot-v6).

Safety:
- Body content untouched.
- Existing frontmatter keys/order untouched.
- Missing keys appended immediately before the closing `---`.
- pages_updated value: list of relative wiki paths (POSIX, no extension).
- If file has no frontmatter at all, page is skipped (logged).

Run modes:
  python scripts/frontmatter_normalize.py --dry-run   (default; emits report)
  python scripts/frontmatter_normalize.py --apply     (writes changes)
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import defaultdict

WIKI_ROOT = "wiki"
STALE_DEFAULTS = {
    "source": 90,
    "finance": 30,
    "ops": 120,
}
DEFAULT_STALE = 60
OWNER_DEFAULT = "wiki-llm"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def split_frontmatter(text: str):
    """Return (frontmatter_block_lines, body_text, full_match_str) or (None,...,None) if absent."""
    m = FM_RE.match(text)
    if not m:
        return None, text, None
    fm = m.group(1)
    body = text[m.end():]
    return fm, body, m.group(0)


def parse_simple_yaml(fm: str) -> dict:
    """Parse top-level key: value pairs from frontmatter (no nesting expected here).

    Captures arrays in `[a, b]` form as Python lists of stripped strings.
    Captures plain scalars verbatim (string).
    Lines starting with whitespace are folded into the previous key's raw value
    so multi-line blocks (e.g. nested object {...}) are not split — we treat the
    whole thing as opaque scalar.
    """
    data: dict = {}
    current_key = None
    current_lines: list[str] = []

    def commit():
        nonlocal current_key, current_lines
        if current_key is None:
            return
        joined = "\n".join(current_lines).strip()
        # try array
        if joined.startswith("[") and joined.endswith("]"):
            inner = joined[1:-1].strip()
            if not inner:
                data[current_key] = []
            else:
                items = [x.strip().strip("'\"") for x in inner.split(",")]
                data[current_key] = [x for x in items if x]
        else:
            # strip quotes
            v = joined.strip("'\"") if (joined.startswith(("'", '"')) and joined.endswith(("'", '"'))) else joined
            data[current_key] = v
        current_key = None
        current_lines = []

    for line in fm.splitlines():
        if not line.strip():
            continue
        if line[0] in (" ", "\t"):
            current_lines.append(line.strip())
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            current_lines.append(line)
            continue
        commit()
        current_key = m.group(1)
        current_lines = [m.group(2)]
    commit()
    return data


def slug_from_path(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def collect_source_index(all_files: list[str]) -> tuple[dict[str, list[str]], dict[str, dict]]:
    """Two passes: first parse every page's frontmatter; second build slug -> [pages] map."""
    parsed: dict[str, dict] = {}
    for fp in all_files:
        with open(fp, encoding="utf-8") as fh:
            text = fh.read()
        fm, _, _ = split_frontmatter(text)
        if fm is None:
            parsed[fp] = {}
            continue
        parsed[fp] = parse_simple_yaml(fm)

    reverse: dict[str, list[str]] = defaultdict(list)
    for fp, fm in parsed.items():
        srcs = fm.get("sources")
        if not isinstance(srcs, list):
            continue
        rel = fp.replace(os.sep, "/")
        # store as path without extension, relative to repo root
        rel_no_ext = os.path.splitext(rel)[0]
        for s in srcs:
            if s:
                reverse[s].append(rel_no_ext)
    # sort each list for determinism
    return {k: sorted(set(v)) for k, v in reverse.items()}, parsed


def render_value(key: str, value) -> str:
    if key == "pages_updated":
        if not value:
            return "pages_updated: []"
        body = ", ".join(value)
        return f"pages_updated: [{body}]"
    if isinstance(value, str):
        return f"{key}: {value}"
    return f"{key}: {value}"


def determine_inserts(fp: str, fm_dict: dict, reverse: dict[str, list[str]]) -> list[tuple[str, object]]:
    inserts: list[tuple[str, object]] = []
    type_ = fm_dict.get("type", "")
    # owner
    if "owner" not in fm_dict:
        inserts.append(("owner", OWNER_DEFAULT))
    # stale_after_days
    if "stale_after_days" not in fm_dict:
        sad = STALE_DEFAULTS.get(type_, DEFAULT_STALE)
        inserts.append(("stale_after_days", sad))
    # pages_updated for sources only
    if type_ == "source" and "pages_updated" not in fm_dict:
        slug = fm_dict.get("slug") or slug_from_path(fp)
        # we backfill regardless of whether slug field exists — derive from filename
        derived = slug_from_path(fp)
        # prefer explicit slug if set
        keys_to_try = [slug, derived]
        matches: list[str] = []
        for k in keys_to_try:
            if k and k in reverse:
                matches = reverse[k]
                break
        # exclude self
        self_rel = os.path.splitext(fp.replace(os.sep, "/"))[0]
        matches = [m for m in matches if m != self_rel]
        inserts.append(("pages_updated", matches))
    return inserts


def apply_inserts(text: str, inserts: list[tuple[str, object]]) -> str:
    m = FM_RE.match(text)
    if not m:
        return text
    fm_block = m.group(1).rstrip()
    body = text[m.end():]
    appended = "\n".join(render_value(k, v) for k, v in inserts)
    new_fm = f"---\n{fm_block}\n{appended}\n---\n"
    return new_fm + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    args = ap.parse_args()

    all_files = sorted(glob.glob(f"{WIKI_ROOT}/**/*.md", recursive=True))
    reverse, parsed = collect_source_index(all_files)

    no_fm: list[str] = []
    changes_by_type: dict[str, int] = defaultdict(int)
    inserts_by_kind: dict[str, int] = defaultdict(int)
    orphan_sources: list[str] = []
    backfilled_sources: list[tuple[str, int]] = []
    files_changed = 0

    for fp in all_files:
        with open(fp, encoding="utf-8") as fh:
            text = fh.read()
        fm, _, _ = split_frontmatter(text)
        if fm is None:
            no_fm.append(fp)
            continue
        fm_dict = parsed[fp]
        inserts = determine_inserts(fp, fm_dict, reverse)
        if not inserts:
            continue
        files_changed += 1
        t = fm_dict.get("type", "untyped")
        changes_by_type[t] += 1
        for k, v in inserts:
            inserts_by_kind[k] += 1
            if k == "pages_updated":
                count = len(v) if isinstance(v, list) else 0
                backfilled_sources.append((fp, count))
                if count == 0:
                    orphan_sources.append(fp)
        if args.apply:
            new_text = apply_inserts(text, inserts)
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(new_text)

    print("=" * 60)
    print(f"MODE: {'APPLY' if args.apply else 'DRY-RUN'}")
    print("=" * 60)
    print(f"Files scanned:  {len(all_files)}")
    print(f"Files changed:  {files_changed}")
    print(f"No frontmatter: {len(no_fm)}")
    if no_fm:
        for f in no_fm:
            print(f"  - {f}")
    print()
    print("Inserts by kind:")
    for k, v in inserts_by_kind.items():
        print(f"  {k}: {v}")
    print()
    print("Changes by type:")
    for t, n in sorted(changes_by_type.items()):
        print(f"  {t}: {n}")
    print()
    print(f"Sources backfilled (with reverse-link counts):")
    for fp, n in backfilled_sources:
        flag = " [ORPHAN]" if n == 0 else ""
        print(f"  {fp}: {n} pages{flag}")
    print()
    print(f"Orphan sources (0 reverse links): {len(orphan_sources)}")


if __name__ == "__main__":
    main()
