#!/usr/bin/env python3
"""Claim-boundary linter for JVTO content.

Scans generated/active JVTO copy (a draft, stdin, or named files) and fails when a
material claim breaks its evidence boundary or uses stale/forbidden wording:

  STEFAN-EDITION    Stefan Loose year/edition/publisher (superseded by DEC-001)
  BOOKING-CONTINUITY Booking framed as address continuity / legal succession
  DETIK-IJEN        Detik attributed to Kawah-Ijen-specific duty (it is Bondowoso-area)
  BBKSDA-CERTIFIED  "BBKSDA certified JVTO" over-claim
  MEDICAL-UNIVERSAL screening stated as a universal rule, not the conditional BBKSDA rule
  ISIC-PARTNER      ISIC asserted as partner / official provider listing
  STALE-REVIEW      a retired review count near its platform name (Google 92 / Trustpilot 47)

Rules + canonical values live in scripts/claim_boundaries.yml (mirrors the locked SSOT:
decision-registry DEC-001, trust-signals.md, CLAUDE.md). This is the llm-wiki analog of the
bootstrap repo's validate_okf.py boundary checks; the `verified-content` skill calls it.

Usage:
  python scripts/verify_claims.py <file> [<file> ...]   # scan named files
  python scripts/verify_claims.py --stdin               # scan a draft piped on stdin
  python scripts/verify_claims.py --all                 # scan the active public copy (default scope)
  python scripts/verify_claims.py --all --quiet         # CI mode: print only on failure

Exit codes: 0 = clean, 1 = boundary violation(s) found, 2 = config/usage error.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "claim_boundaries.yml"

# Default scope for --all: the published copy + the wiki credential pages that feed it.
DEFAULT_SCAN_GLOBS = [
    "output/website/**/*.md",
    "output/website/*.txt",
    "output/social/**/*.md",
    "wiki/credentials/*.md",
    "wiki/people/*.md",
    "wiki/website/*.md",
]


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(f"ERROR: missing config {CONFIG_PATH}", file=sys.stderr)
        raise SystemExit(2)
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
    rules = cfg.get("boundaries") or []
    if not rules:
        print("ERROR: claim_boundaries.yml defines no boundaries", file=sys.stderr)
        raise SystemExit(2)
    for rule in rules:
        rule["_re"] = re.compile(rule["pattern"])
    return cfg


def is_excluded(rel_path: str, exclude_globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel_path, g) for g in exclude_globs)


def is_context_line(line: str, markers: list[str]) -> bool:
    low = line.lower()
    return any(m in low for m in markers)


def is_allowed(rule_id: str, rel_path: str, line: str, allow: list[dict]) -> bool:
    for a in allow:
        if a.get("rule") == rule_id and a.get("path") == rel_path and str(a.get("text", "")) in line:
            return True
    return False


def scan_text(text: str, rel_path: str, cfg: dict) -> list[dict]:
    """Return a list of violation dicts for one document."""
    markers = [str(m).lower() for m in (cfg.get("context_markers") or [])]
    allow = cfg.get("allow") or []
    rules = cfg["boundaries"]
    stale = cfg.get("stale_review_claims") or []
    violations: list[dict] = []

    for n, raw in enumerate(text.splitlines(), start=1):
        if is_context_line(raw, markers):
            continue
        low = raw.lower()
        for rule in rules:
            m = rule["_re"].search(raw)
            if not m:
                continue
            unless = [str(u).lower() for u in (rule.get("unless") or [])]
            if any(u in low for u in unless):
                continue
            if not is_allowed(rule["id"], rel_path, raw, allow):
                violations.append({
                    "path": rel_path, "line": n, "rule": rule["id"],
                    "message": rule["message"], "fix": rule["fix"], "match": m.group(0).strip(),
                })
        for claim in stale:
            platform = str(claim.get("platform", "")).lower().strip()
            count = str(claim.get("count", "")).strip()
            if not platform or not count:
                continue
            for pm in re.finditer(re.escape(platform), low):
                window = low[pm.start(): pm.end() + 40]
                if re.search(rf"\b{re.escape(count)}\b", window):
                    violations.append({
                        "path": rel_path, "line": n, "rule": "STALE-REVIEW",
                        "message": f"Stale review count {count} near '{platform}'.",
                        "fix": "Use the current canonical count (Google 123 / Trustpilot 51).",
                        "match": raw.strip()[:80],
                    })
                    break
    return violations


def iter_targets(args, cfg) -> list[tuple[str, str]]:
    """Return (rel_path, text) pairs to scan."""
    exclude = cfg.get("exclude_globs") or []
    if args.stdin:
        return [("<stdin>", sys.stdin.read())]
    paths: list[Path] = []
    if args.all:
        for g in DEFAULT_SCAN_GLOBS:
            paths.extend(REPO_ROOT.glob(g))
    for f in args.files:
        paths.append(Path(f) if Path(f).is_absolute() else REPO_ROOT / f)
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for p in sorted(set(paths)):
        if not p.is_file():
            continue
        try:
            rel = p.resolve().relative_to(REPO_ROOT).as_posix()
        except ValueError:
            rel = p.as_posix()
        if rel in seen or is_excluded(rel, exclude):
            continue
        seen.add(rel)
        out.append((rel, p.read_text(encoding="utf-8")))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help="files to scan")
    parser.add_argument("--stdin", action="store_true", help="scan a draft from stdin")
    parser.add_argument("--all", action="store_true", help="scan the active public copy (default scope)")
    parser.add_argument("--quiet", action="store_true", help="print only on failure")
    args = parser.parse_args()

    if not (args.files or args.stdin or args.all):
        parser.error("give files, --stdin, or --all")

    cfg = load_config()
    targets = iter_targets(args, cfg)
    violations: list[dict] = []
    for rel, text in targets:
        violations.extend(scan_text(text, rel, cfg))

    if violations:
        print(f"Claim verification: {len(violations)} boundary violation(s) across {len(targets)} file(s).", file=sys.stderr)
        for v in violations:
            print(f"  {v['rule']} {v['path']}:{v['line']}: {v['message']}", file=sys.stderr)
            print(f"      matched: {v['match']!r}", file=sys.stderr)
            print(f"      fix: {v['fix']}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"Claim verification: clean ({len(targets)} file(s) scanned).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
