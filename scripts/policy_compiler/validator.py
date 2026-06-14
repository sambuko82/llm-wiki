"""Validation helpers for policy bundle compilation."""
from __future__ import annotations


def validate(policy_bundle: list[dict], deprecated_report: dict) -> list[dict]:
    findings: list[dict] = []
    policy_ids = {p["policy_id"] for p in policy_bundle}
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
    for consumer, report in deprecated_report["consumers"].items():
        for pid in report["checked_policy_ids"]:
            if pid not in policy_ids:
                findings.append({
                    "rule_id": "POL-04",
                    "severity": "error",
                    "policy_id": pid,
                    "message": f"Consumer {consumer} references unknown policy id.",
                })
        for finding in report["findings"]:
            findings.append({
                "rule_id": "POL-03",
                "severity": finding["severity"],
                "policy_id": consumer,
                "message": finding["message"],
            })
    return findings

