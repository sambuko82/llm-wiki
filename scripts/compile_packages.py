#!/usr/bin/env python3
"""Package Readiness Compiler v1 — skeleton + dry-run.

Reads canonical wiki package sources, runs first-pass PKG validations, and
reports a gap report. Default is dry-run (writes nothing). Use --write to emit
JSON to output/products/package-readiness/.

    python scripts/compile_packages.py --dry-run --verbose
    python scripts/compile_packages.py --write          # emit artifacts

Spec: wiki/ops/package-readiness-compiler-spec.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from package_compiler import loader, renderer, validator  # noqa: E402


def find_wiki_root(start: str | Path) -> Path:
    p = Path(start).resolve()
    for cand in [p] + list(p.parents):
        if (cand / "wiki" / "ops" / "package-readiness-compiler-spec.md").exists():
            return cand / "wiki"
    raise SystemExit("could not locate wiki/ root (spec file not found)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Package Readiness Compiler v1")
    ap.add_argument("--dry-run", action="store_true",
                    help="run + report, write nothing (default behaviour)")
    ap.add_argument("--write", action="store_true",
                    help="write JSON outputs to output/products/package-readiness/")
    ap.add_argument("--verbose", action="store_true",
                    help="print full registry + every finding")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any error-severity finding remains")
    args = ap.parse_args(argv)

    dry_run = not args.write  # dry-run unless --write is explicitly passed

    wiki_root = find_wiki_root(__file__)
    repo_root = wiki_root.parent

    src = loader.load_sources(wiki_root)
    findings = validator.validate(src)
    registry = renderer.build_registry(src)
    gap = renderer.build_gap_report(findings)
    manifest = renderer.build_manifest(src, findings, dry_run=dry_run)

    mode = "DRY-RUN" if dry_run else "WRITE"
    print(f"Package Readiness Compiler v1 — {mode}")
    print(f"  packages parsed : {len(src.packages)}")
    print("  sitemap slugs   : "
          f"surabaya={len(src.sitemap_slugs.get('surabaya', ()))} "
          f"bali={len(src.sitemap_slugs.get('bali', ()))}")
    s = gap["summary"]
    print(f"  findings        : {s['total']} ({s['errors']} error, {s['warnings']} warn)")
    print(f"  manifest.clean  : {manifest['clean']}")

    if args.verbose:
        print("\n  registry:")
        for r in registry:
            flags = []
            if r["ijen_relevant"]:
                flags.append("ijen")
            if r["visits_madakaripura"]:
                flags.append("mada")
            if r["is_specialty"]:
                flags.append("specialty")
            tag = (" [" + ",".join(flags) + "]") if flags else ""
            print(f"    - {r['package_id']:<46} {r['origin']:<8} {r['public_url']}{tag}")
        print("\n  findings:")
        if not findings:
            print("    (none)")
        for f in findings:
            print(f"    [{f['severity']:<5}] {f['rule_id']} {f['package_id']} :: {f['message']}")

    if args.write:
        out_dir = repo_root / "output" / "products" / "package-readiness"
        written = renderer.write_outputs(out_dir, registry, gap, manifest)
        print(f"\n  wrote {len(written)} files -> {out_dir}")
        for name in written:
            print(f"    - {name}")
    else:
        print("\n  (dry-run — no files written; use --write to emit)")

    if args.strict and s["errors"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
