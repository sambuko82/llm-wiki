"""Renderers — build in-memory previews; optional atomic write behind --write.

v1 emits 3 of the 6 spec artifacts: package-registry, gap-report, _manifest.
package-pricing / package-itineraries / booking-compatibility are deferred to a
later pass (spec §5). Write path is atomic (temp + os.replace), mirroring
scripts/compile_trust.py.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = "package-readiness/v1"
OUTPUTS = ("package-registry.json", "gap-report.json", "_manifest.json")


def build_registry(sources) -> list[dict]:
    return [
        {
            "package_id": pk.slug,
            "slug": pk.norm_slug,
            "origin": pk.origin,
            "title": pk.name,
            "duration": pk.duration,
            "public_url": pk.public_url,
            "ijen_relevant": pk.visits_ijen,
            "visits_madakaripura": pk.visits_madakaripura,
            "is_specialty": "taman-safari" in pk.norm_slug,
        }
        for pk in sources.packages
    ]


def build_gap_report(findings: list[dict]) -> dict:
    errors = [f for f in findings if f["severity"] == "error"]
    warns = [f for f in findings if f["severity"] == "warn"]
    return {
        "summary": {"total": len(findings), "errors": len(errors), "warnings": len(warns)},
        "findings": findings,
    }


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_manifest(sources, findings: list[dict], *, dry_run: bool) -> dict:
    by_rule: dict[str, int] = {}
    for f in findings:
        by_rule[f["rule_id"]] = by_rule.get(f["rule_id"], 0) + 1
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_by": "scripts/compile_packages.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "canonical_package_count": len(sources.packages),
        "source_hashes": {
            "packages-overview": _sha(sources.overview_text),
            "packages-full-pricing": _sha(sources.pricing_text),
            "packages-itineraries": _sha(sources.itinerary_text),
            "sitemap": _sha(sources.sitemap_text),
            "route-data": _sha(sources.routes_text),
            "policy-source-ownership": _sha(sources.policy_text),
        },
        "findings_by_rule": by_rule,
        "clean": not any(f["severity"] == "error" for f in findings),
    }


def _atomic_write_json(path: Path, data) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def write_outputs(out_dir: str | Path, registry, gap_report, manifest) -> list[str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    payloads = {
        "package-registry.json": registry,
        "gap-report.json": gap_report,
        "_manifest.json": manifest,
    }
    for name, data in payloads.items():
        _atomic_write_json(out / name, data)
    return list(payloads)
