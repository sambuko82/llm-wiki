"""Render policy bundle artifacts."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = "policy-bundle/v1.0"
OUTPUTS = (
    "policy-bundle.json",
    "consumer-bundles.json",
    "deprecated-wording-report.json",
    "gap-report.json",
    "_manifest.json",
)

CONSUMERS = ("checkout", "invoice", "whatsapp")

DOMAIN_EVIDENCE = {
    "Booking Paths": {
        "packages": ["Booking Flow"],
        "faq": ["Q15"],
    },
    "Payment Rules": {
        "packages": ["Payment Rules"],
        "faq": ["Q16"],
    },
    "Cancellation / Travel Credit": {
        "packages": ["Cancellation Policy", "Rescheduling"],
        "faq": ["Q17"],
    },
    "Inclusions / Exclusions": {
        "packages": ["Standard Inclusions (all 15 packages)", "Standard Exclusions (all 15 packages)"],
        "faq": ["Q14"],
    },
    "Ijen Health Screening": {
        "packages": [],
        "faq": ["Q6", "Q7"],
    },
    "Natural Phenomena": {
        "packages": [],
        "faq": ["Q19", "Q20"],
    },
    "ISIC": {
        "packages": ["Student Pricing (ISIC)"],
        "faq": ["Q11"],
    },
    "Police Escort": {
        "packages": ["Free-of-Charge (FOC) Group Incentive"],
        "faq": ["Q12", "Q12b"],
    },
    "Anti-Fraud": {
        "packages": ["Anti-Fraud Policy"],
        "faq": ["Q1", "Q16"],
    },
}


def _policy_id(domain: str) -> str:
    value = domain.lower()
    value = value.replace("/", " ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


def _section(sources, name: str) -> str | None:
    if name in sources.package_sections:
        return sources.package_sections[name]
    # Markdown headings include parenthetical suffixes; allow a prefix match.
    for key, value in sources.package_sections.items():
        if key.lower().startswith(name.lower()):
            return value
    return None


def _evidence_for(sources, domain: str) -> list[dict]:
    spec = DOMAIN_EVIDENCE.get(domain, {})
    evidence: list[dict] = []
    for section_name in spec.get("packages", []):
        text = _section(sources, section_name)
        if text:
            evidence.append({
                "source": "wiki/products/packages-overview.md",
                "section": section_name,
                "text": text,
            })
    for qid in spec.get("faq", []):
        text = sources.faq_answers.get(qid)
        if text:
            evidence.append({
                "source": "wiki/website/faq-master.md",
                "section": qid,
                "text": text,
            })
    return evidence


def build_policy_bundle(sources) -> list[dict]:
    out: list[dict] = []
    for row in sources.ownership_rows:
        evidence = _evidence_for(sources, row.domain)
        out.append({
            "policy_id": _policy_id(row.domain),
            "domain": row.domain,
            "canonical_sources": row.canonical_sources,
            "supporting_sources": row.supporting_sources,
            "consumers": row.consumers,
            "notes": row.notes,
            "evidence": evidence,
        })
    return out


def build_consumer_bundles(policy_bundle: list[dict]) -> dict:
    bundles: dict[str, dict] = {}
    for consumer in CONSUMERS:
        domains = [p for p in policy_bundle if consumer in p["consumers"]]
        bundles[consumer] = {
            "consumer": consumer,
            "policy_ids": [p["policy_id"] for p in domains],
            "domains": domains,
        }
    return bundles


def build_deprecated_report(sources, consumer_bundles: dict) -> dict:
    checks = [
        {
            "deprecated": rule.deprecated,
            "correct": rule.correct,
        }
        for rule in sources.deprecated_rules
    ]
    consumers: dict[str, dict] = {}
    for consumer, bundle in consumer_bundles.items():
        text = "\n".join(
            evidence["text"]
            for domain in bundle["domains"]
            for evidence in domain["evidence"]
        ).lower()
        findings = []
        for rule in sources.deprecated_rules:
            phrase = rule.deprecated.lower()
            if phrase and phrase in text:
                findings.append({
                    "severity": "error",
                    "deprecated": rule.deprecated,
                    "correct": rule.correct,
                    "message": f"Deprecated wording appears in {consumer} bundle: {rule.deprecated}",
                })
        consumers[consumer] = {
            "checked_policy_ids": bundle["policy_ids"],
            "findings": findings,
            "clean": not findings,
        }
    total = sum(len(c["findings"]) for c in consumers.values())
    return {
        "checks": checks,
        "summary": {
            "consumers_checked": list(consumers),
            "total_findings": total,
            "errors": total,
        },
        "consumers": consumers,
    }


def build_gap_report(policy_bundle: list[dict], deprecated_report: dict) -> dict:
    findings: list[dict] = []
    for policy in policy_bundle:
        if not policy["canonical_sources"]:
            findings.append({
                "rule_id": "POL-01",
                "severity": "error",
                "policy_id": policy["policy_id"],
                "message": "Policy domain has no canonical source.",
            })
        if not policy["evidence"]:
            findings.append({
                "rule_id": "POL-02",
                "severity": "warn",
                "policy_id": policy["policy_id"],
                "message": "Policy domain has no extracted evidence excerpt.",
            })
    for consumer, result in deprecated_report["consumers"].items():
        for finding in result["findings"]:
            findings.append({
                "rule_id": "POL-03",
                "severity": finding["severity"],
                "policy_id": consumer,
                "message": finding["message"],
            })
    errors = [f for f in findings if f["severity"] == "error"]
    warns = [f for f in findings if f["severity"] == "warn"]
    return {
        "summary": {"total": len(findings), "errors": len(errors), "warnings": len(warns)},
        "findings": findings,
    }


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_manifest(sources, gap_report: dict, *, dry_run: bool) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_by": "scripts/compile_policy_bundle.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "source_hashes": {
            "policy-source-ownership": _sha(sources.policy_text),
            "packages-overview": _sha(sources.packages_text),
            "faq-master": _sha(sources.faq_text),
        },
        "policy_domains": len(sources.ownership_rows),
        "deprecated_checks": len(sources.deprecated_rules),
        "consumers_checked": list(CONSUMERS),
        "artifacts": [name for name in OUTPUTS if name != "_manifest.json"],
        "clean": gap_report["summary"]["errors"] == 0,
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


def write_outputs(out_dir: str | Path, artifacts: dict) -> list[str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, data in artifacts.items():
        _atomic_write_json(out / name, data)
    return list(artifacts)

