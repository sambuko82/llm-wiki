#!/usr/bin/env python3
"""Trust Bundle Compiler — CLI entry.

Reads 6 inputs, validates with strict gate, writes 7 JSON outputs under
output/website/trust-bundle/ via atomic per-file replace.

Usage:
  python scripts/compile_trust.py                # strict mode, real write
  python scripts/compile_trust.py --dry-run      # validate only, no write
  python scripts/compile_trust.py --verbose      # print each violation
"""
from __future__ import annotations

import sys
from pathlib import Path as _PathForBoot
_REPO_ROOT_FOR_IMPORTS = _PathForBoot(__file__).resolve().parent.parent
if str(_REPO_ROOT_FOR_IMPORTS) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT_FOR_IMPORTS))

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from scripts.compiler.loader import (
    load_claims, load_evidence, load_entities, load_decisions,
    load_conflicts, load_aeo_narratives,
)
from scripts.compiler.enricher import enrich
from scripts.compiler.validator import run as validate, Severity
from scripts.compiler.renderer import (
    render_claims, render_organization_schema, render_faq_page_schema,
    render_tourist_trip_schema, render_faq, render_aeo_snippets,
    render_manifest,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

INPUT_PATHS = {
    "claim-registry.yml": REPO_ROOT / "raw" / "_manifest" / "claim-registry.yml",
    "evidence-registry.yml": REPO_ROOT / "raw" / "_manifest" / "evidence-registry.yml",
    "entity-registry.yml": REPO_ROOT / "raw" / "_manifest" / "entity-registry.yml",
    "decision-registry.yml": REPO_ROOT / "raw" / "_manifest" / "decision-registry.yml",
    "conflict-log.md": REPO_ROOT / "raw" / "_manifest" / "conflict-log.md",
    "aeo-claims.md": REPO_ROOT / "wiki" / "website" / "aeo-claims.md",
}

OUTPUT_DIR = REPO_ROOT / "output" / "website" / "trust-bundle"
LOG_PATH = REPO_ROOT / "wiki" / "log.md"

# JVTO constants (from CLAUDE.md). Hard-coded here intentionally — these are
# the canonical Organization schema fields, not bundle content.
ORG_LEGAL_NAME = "PT Java Volcano Rendezvous"
ORG_BRAND_NAME = "Java Volcano Tour Operator"
ORG_NIB = "1102230032918"
ORG_TDUP = "1102230032918"   # adjust when TDUP gets a distinct number
ORG_FOUNDER_NAME = "Agung Sambuko"
ORG_FOUNDER_JOB = "Tourist Police Officer"
ORG_URL = "https://javavolcano-touroperator.com"


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return "sha256:" + h.hexdigest()[:16]


def _atomic_write_json(target: Path, data) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    import os
    os.replace(tmp, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="validate only; do not write outputs")
    parser.add_argument("--verbose", action="store_true",
                        help="print every violation, not just the summary")
    args = parser.parse_args()

    # Load
    claims = load_claims(INPUT_PATHS["claim-registry.yml"])
    evidence = load_evidence(INPUT_PATHS["evidence-registry.yml"])
    entities = load_entities(INPUT_PATHS["entity-registry.yml"])
    decisions = load_decisions(INPUT_PATHS["decision-registry.yml"])
    conflicts = load_conflicts(INPUT_PATHS["conflict-log.md"])
    narratives = load_aeo_narratives(INPUT_PATHS["aeo-claims.md"])

    print(f"Loaded: {len(claims)} claims, {len(evidence)} evidence, "
          f"{len(entities)} entities, {len(decisions)} decisions, "
          f"{len(conflicts)} conflicts, {len(narratives)} narratives", file=sys.stderr)

    # Enrich
    enriched = enrich(claims, evidence, entities, decisions, narratives)

    # Validate
    all_claim_ids = {c.claim_id for c in claims}
    known_entity_ids = {e.entity_id for e in entities}
    report = validate(
        enriched_claims=enriched,
        decisions=decisions,
        conflicts=conflicts,
        narratives=narratives,
        all_claim_ids=all_claim_ids,
        known_entity_ids=known_entity_ids,
    )

    # Report
    summary = report.rule_summary()
    print("Validation:", file=sys.stderr)
    for rule, status in summary.items():
        marker = "✓" if status == "pass" else ("⚠" if "warning" in status and "error" not in status else "✗")
        print(f"  {marker} {rule}: {status}", file=sys.stderr)
    if args.verbose or report.has_errors:
        for v in report.violations:
            print(f"  [{v.rule_id} {v.severity.value}] {v.target_id}: {v.message}", file=sys.stderr)

    if report.has_errors:
        print(f"\n{len(report.errors)} errors, {len(report.warnings)} warnings. "
              f"Strict mode → no output written.", file=sys.stderr)
        return 1

    if args.dry_run:
        print("\n--dry-run: validation passed, no output written.", file=sys.stderr)
        return 0

    # Render
    compiled_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    claims_doc = render_claims(enriched, compiled_at=compiled_at)
    org_doc = render_organization_schema(
        legal_name=ORG_LEGAL_NAME, brand_name=ORG_BRAND_NAME,
        nib=ORG_NIB, tdup=ORG_TDUP,
        founder_name=ORG_FOUNDER_NAME, founder_job=ORG_FOUNDER_JOB,
        url=ORG_URL,
    )
    qa_pairs = [{"question": item["question"], "answer": item["answer"]}
                for item in render_faq(enriched)["items"]]
    faq_page_doc = render_faq_page_schema(qa_pairs)
    trip_doc = render_tourist_trip_schema(entities, base_url=ORG_URL)
    faq_doc = render_faq(enriched)
    aeo_doc = render_aeo_snippets(enriched)
    manifest_doc = render_manifest(
        report=report,
        inputs={
            "claims": len(claims),
            "evidence": len(evidence),
            "entities": len(entities),
            "decisions": len(decisions),
            "narratives": len(narratives),
        },
        outputs={
            "claims": len(claims_doc["claims"]),
            "schema_files": 3,
            "faq_items": len(faq_doc["items"]),
            "aeo_snippets": len(aeo_doc["snippets"]),
        },
        input_hashes={k: _sha256(p) for k, p in INPUT_PATHS.items()},
        compiled_at=compiled_at,
    )

    # Write
    _atomic_write_json(OUTPUT_DIR / "claims.json", claims_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "organization.json", org_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "faq-page.json", faq_page_doc)
    _atomic_write_json(OUTPUT_DIR / "schema" / "tourist-trip.json", trip_doc)
    _atomic_write_json(OUTPUT_DIR / "faq.json", faq_doc)
    _atomic_write_json(OUTPUT_DIR / "aeo-snippets.json", aeo_doc)
    _atomic_write_json(OUTPUT_DIR / "_manifest.json", manifest_doc)

    # Append log line
    log_line = (
        f"\n## [{compiled_at[:10]}] compile | trust-bundle v0.1.0 — "
        f"{len(claims)} claims, {len(report.errors)} errors, {len(report.warnings)} warnings\n"
    )
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"\nWrote 7 files to {OUTPUT_DIR.relative_to(REPO_ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
