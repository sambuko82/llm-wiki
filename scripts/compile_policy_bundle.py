#!/usr/bin/env python3
"""Policy Bundle Compiler v2.

Reads canonical policy sources (including the YAML-canonical cancellation domain
wiki/policies/cancellation-package-credit.yml) and emits consumer-ready policy JSON,
a rule-engine decision matrix, and canonical customer-copy blocks:

    python scripts/compile_policy_bundle.py --dry-run --verbose
    python scripts/compile_policy_bundle.py --write
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compiler_common.cli import build_dry_run_write_parser  # noqa: E402
from policy_compiler import loader, renderer, validator  # noqa: E402


def find_wiki_root(start: str | Path) -> Path:
    p = Path(start).resolve()
    for cand in [p] + list(p.parents):
        if (cand / "wiki" / "ops" / "policy-source-ownership.md").exists():
            return cand / "wiki"
    raise SystemExit("could not locate wiki/ root (policy-source-ownership.md not found)")


def main(argv=None) -> int:
    ap = build_dry_run_write_parser(
        description="Policy Bundle Compiler v2",
        write_help="write JSON outputs to output/website/policy-bundle/",
        verbose_help="print consumer coverage and findings",
    )
    args = ap.parse_args(argv)

    dry_run = not args.write
    wiki_root = find_wiki_root(__file__)
    repo_root = wiki_root.parent

    src = loader.load_sources(wiki_root)
    policy_bundle = renderer.build_policy_bundle(src)
    consumer_bundles = renderer.build_consumer_bundles(policy_bundle)
    decision_matrix = renderer.build_decision_matrix(src.cancellation_policy)
    customer_copy = renderer.build_customer_copy(src.cancellation_policy)
    deprecated = renderer.build_deprecated_report(src, consumer_bundles)
    findings = validator.validate(
        policy_bundle,
        deprecated,
        cancellation_policy=src.cancellation_policy,
        decision_matrix=decision_matrix,
        consumer_bundles=consumer_bundles,
    )
    gap = renderer.build_gap_report(policy_bundle, deprecated)
    # Preserve validator as the source of truth for counts.
    errors = [f for f in findings if f["severity"] == "error"]
    warns = [f for f in findings if f["severity"] == "warn"]
    gap["summary"] = {"total": len(findings), "errors": len(errors), "warnings": len(warns)}
    gap["findings"] = findings
    manifest = renderer.build_manifest(src, gap, dry_run=dry_run)

    artifacts = {
        "policy-bundle.json": policy_bundle,
        "consumer-bundles.json": consumer_bundles,
        "decision-matrix.json": decision_matrix,
        "customer-copy.json": customer_copy,
        "deprecated-wording-report.json": deprecated,
        "gap-report.json": gap,
        "_manifest.json": manifest,
    }

    mode = "DRY-RUN" if dry_run else "WRITE"
    print(f"Policy Bundle Compiler v2.0 — {mode}")
    print(f"  policy domains       : {len(policy_bundle)}")
    print(f"  deprecated checks    : {len(src.deprecated_rules)}")
    print(f"  cancellation policy  : {src.cancellation_policy.get('policy_version')}")
    print(f"  consumers checked    : {', '.join(renderer.CONSUMERS)}")
    print(
        "  findings             : "
        f"{gap['summary']['total']} ({gap['summary']['errors']} error, "
        f"{gap['summary']['warnings']} warn)"
    )
    print(f"  manifest.clean       : {manifest['clean']}")

    if args.verbose:
        print("\n  consumer coverage:")
        for consumer, bundle in consumer_bundles.items():
            print(f"    - {consumer:<8} {', '.join(bundle['policy_ids'])}")
        print("\n  findings:")
        if not findings:
            print("    (none)")
        for f in findings:
            print(f"    [{f['severity']:<5}] {f['rule_id']} {f['policy_id']} :: {f['message']}")

    if args.write:
        out_dir = repo_root / "output" / "website" / "policy-bundle"
        written = renderer.write_outputs(out_dir, artifacts)
        print(f"\n  wrote {len(written)} files -> {out_dir}")
        for name in written:
            print(f"    - {name}")
    else:
        print("\n  (dry-run — no files written; use --write to emit)")

    if args.strict and gap["summary"]["errors"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

