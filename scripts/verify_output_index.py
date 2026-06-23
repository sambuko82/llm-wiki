#!/usr/bin/env python3
"""Semantic guard for output/INDEX.md — the master output catalog.

Invariant: a commit that changes output topology must keep output/INDEX.md
accurate. This validator enforces, against the catalog's table entries (the
first column of each table — URL slugs and "superseded-by" references sit in
later columns and are intentionally ignored):

  - every indexed path exists on disk            (catches stale / renamed / deleted entries)
  - no path is indexed more than once            (duplicate entry)
  - every tracked output *.md file is indexed     (new output file missing from the index)
    unless it is listed in scripts/output_index_exclude.txt

Usage:
  python scripts/verify_output_index.py            # validate, exit 1 on problems
  python scripts/verify_output_index.py --quiet     # only print on failure
  python scripts/verify_output_index.py --hook      # Claude Code PreToolUse gate (reads stdin)

Exit codes: 0 = clean, 1 = problems found, 2 = blocked git commit (hook mode).
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"
INDEX_PATH = OUTPUT_DIR / "INDEX.md"
EXCLUDE_FILE = REPO_ROOT / "scripts" / "output_index_exclude.txt"

# Path-like tokens are only treated as catalog entries when they carry one of
# these content extensions; URL slugs (e.g. `/tours/...`) have none and are skipped.
INDEXABLE_SUFFIXES = (".md", ".json", ".html", ".txt")
BACKTICK = re.compile(r"`([^`]+)`")
SEPARATOR_CHARS = set("-: ")


def parse_indexed_paths(index_text: str) -> list[str]:
    """Return the catalog's file-path entries (first backticked token per table row)."""
    paths: list[str] = []
    for line in index_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells:
            continue
        first = cells[0]
        if not first or set(first) <= SEPARATOR_CHARS:  # header/separator row
            continue
        if "~~" in first:  # struck-through = resolved/removed note, not a live entry
            continue
        match = BACKTICK.search(first)
        if not match:
            continue
        token = match.group(1).strip().lstrip("./")
        if not token or token.startswith("/") or " " in token:
            continue
        if not token.lower().endswith(INDEXABLE_SUFFIXES):
            continue
        paths.append(token)
    return paths


def is_excluded(rel_path: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        if pattern.endswith("/**"):
            base = pattern[:-3]
            if rel_path == base or rel_path.startswith(base + "/"):
                return True
        elif fnmatch.fnmatch(rel_path, pattern):
            return True
    return False


def find_problems(
    indexed_paths: list[str],
    existing: set[str],
    tracked_md: set[str],
    exclude_patterns: list[str],
) -> list[str]:
    """Pure core: return concise, actionable problem messages (empty = clean)."""
    problems: list[str] = []

    seen: set[str] = set()
    for path in indexed_paths:
        if path in seen:
            problems.append(
                f"[duplicate] indexed more than once: {path} "
                f"-> remove the extra row in output/INDEX.md"
            )
        seen.add(path)

    for path in sorted(seen):
        if path not in existing:
            problems.append(
                f"[stale] indexed path does not exist: output/{path} "
                f"-> fix the path in output/INDEX.md or restore the file"
            )

    for md in sorted(tracked_md):
        if md in seen or is_excluded(md, exclude_patterns):
            continue
        problems.append(
            f"[uncovered] tracked output markdown not in index: output/{md} "
            f"-> add it to output/INDEX.md or list it in scripts/output_index_exclude.txt"
        )

    return problems


def load_exclude_patterns() -> list[str]:
    patterns = ["INDEX.md"]  # the catalog never indexes itself
    if EXCLUDE_FILE.exists():
        for raw in EXCLUDE_FILE.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns


def collect_existing() -> set[str]:
    return {
        p.relative_to(OUTPUT_DIR).as_posix()
        for p in OUTPUT_DIR.rglob("*")
        if p.is_file()
    }


def collect_tracked_md() -> set[str]:
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "--", "output"],
        capture_output=True,
        text=True,
        check=True,
    )
    tracked = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.endswith(".md") and line.startswith("output/"):
            tracked.add(line[len("output/"):])
    return tracked


def validate() -> list[str]:
    if not INDEX_PATH.exists():
        return [f"[stale] catalog missing: {INDEX_PATH.relative_to(REPO_ROOT)}"]
    indexed = parse_indexed_paths(INDEX_PATH.read_text(encoding="utf-8"))
    return find_problems(indexed, collect_existing(), collect_tracked_md(), load_exclude_patterns())


def run_cli(quiet: bool) -> int:
    problems = validate()
    if problems:
        print(f"output/INDEX.md is out of sync ({len(problems)} problem(s)):", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    if not quiet:
        print("output/INDEX.md is in sync with output/ ✓")
    return 0


def run_hook() -> int:
    """Claude Code PreToolUse gate: block a git commit when the index is stale."""
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # never block on a malformed payload
    if payload.get("tool_name") != "Bash":
        return 0
    command = str(payload.get("tool_input", {}).get("command", ""))
    if not re.search(r"\bgit\b.*\bcommit\b", command):
        return 0
    problems = validate()
    if not problems:
        return 0
    print(
        "Blocked: output/INDEX.md is out of sync with output/. "
        "Run `python scripts/verify_output_index.py` and fix before committing:",
        file=sys.stderr,
    )
    for problem in problems:
        print(f"  {problem}", file=sys.stderr)
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="Only print on failure.")
    parser.add_argument("--hook", action="store_true", help="Run as a Claude Code PreToolUse commit gate (reads stdin).")
    args = parser.parse_args()
    if args.hook:
        return run_hook()
    return run_cli(args.quiet)


if __name__ == "__main__":
    sys.exit(main())
