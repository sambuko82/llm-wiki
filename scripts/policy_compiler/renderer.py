"""Render policy bundle artifacts (v2)."""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from compiler_common.io import sha_text as _sha, atomic_write_json as _atomic_write_json, write_outputs  # noqa: E402

SCHEMA_VERSION = "policy-bundle/v2.0"
OUTPUTS = (
    "policy-bundle.json",
    "consumer-bundles.json",
    "decision-matrix.json",
    "customer-copy.json",
    "deprecated-wording-report.json",
    "gap-report.json",
    "_manifest.json",
)

# The cancellation domain is YAML-canonical; this is its stable policy_id.
CANCELLATION_POLICY_ID = "cancellation-package-credit"

# Controlled consumer vocabulary. A compiled consumer bundle may only use these
# identifiers; any ownership-table token not resolvable to one of them is an
# unregistered alias (POL2-14). whatsapp is intentionally NOT a booking consumer —
# it resolves to customer_support (read-only).
CONSUMERS = (
    "website_checkout",
    "booking_portal",
    "e_voucher",
    "invoice",
    "policy_page",
    "faq",
    "customer_support",
    "booking_confirmation",
    "package_pages",
    "payment_instructions",
    "quotation",
)

# Map raw ownership-table consumer tokens (lowercased) to controlled IDs.
CONSUMER_ALIASES = {
    "checkout": "website_checkout",
    "checkout terms": "website_checkout",
    "website": "website_checkout",
    "self-checkout": "website_checkout",
    "website_checkout": "website_checkout",
    "booking portal": "booking_portal",
    "booking_portal": "booking_portal",
    "booking confirmation": "booking_confirmation",
    "booking_confirmation": "booking_confirmation",
    "e-voucher": "e_voucher",
    "e_voucher": "e_voucher",
    "voucher": "e_voucher",
    "invoice": "invoice",
    "policy page": "policy_page",
    "policy_page": "policy_page",
    "faq": "faq",
    "customer support": "customer_support",
    "customer_support": "customer_support",
    "cs replies": "customer_support",
    "whatsapp": "customer_support",
    "whatsapp replies": "customer_support",
    "package pages": "package_pages",
    "package_pages": "package_pages",
    "student pages": "package_pages",
    "group pages": "package_pages",
    "payment instructions": "payment_instructions",
    "payment_instructions": "payment_instructions",
    "quotation": "quotation",
}

DOMAIN_EVIDENCE = {
    "Booking Paths": {
        "packages": ["Booking Flow"],
        "faq": ["Q15"],
    },
    "Payment Rules": {
        "packages": ["Payment Rules"],
        "faq": ["Q16"],
    },
    "Cancellation / Package Credit": {
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


def _normalize_consumers(raw_consumers: list[str]) -> tuple[list[str], list[str]]:
    """Return (controlled_ids, unregistered_tokens) for a row's raw consumers."""
    controlled: list[str] = []
    unregistered: list[str] = []
    for token in raw_consumers:
        key = token.strip().lower()
        if not key:
            continue
        mapped = CONSUMER_ALIASES.get(key)
        if mapped is None:
            unregistered.append(token)
        elif mapped not in controlled:
            controlled.append(mapped)
    return controlled, unregistered


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
        consumers, unregistered = _normalize_consumers(row.consumers)
        policy_id = _policy_id(row.domain)
        entry = {
            "policy_id": policy_id,
            "domain": row.domain,
            "canonical_sources": row.canonical_sources,
            "supporting_sources": row.supporting_sources,
            "consumers": consumers,
            "consumers_raw": row.consumers,
            "unregistered_consumers": unregistered,
            "notes": row.notes,
            "evidence": evidence,
        }
        # The cancellation domain carries the YAML-derived customer copy so
        # downstream consumers get canonical wording, not only prose excerpts.
        if policy_id == CANCELLATION_POLICY_ID and sources.cancellation_policy:
            entry["canonical_policy"] = sources.cancellation_policy
            entry["customer_copy"] = build_customer_copy(sources.cancellation_policy)
        out.append(entry)
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


def build_decision_matrix(cancellation_policy: dict) -> dict:
    """Rule-engine-ready outcome matrix derived from the canonical YAML."""
    cp = cancellation_policy
    partial = cp["partial_cancellation"]
    credit = cp["package_credit"]
    flight = cp["flight_disruption"]
    fm = cp["force_majeure"]
    return {
        "schema_version": cp["schema_version"],
        "policy_version": cp["policy_version"],
        "effective_from": cp["effective_from"],
        "cutoff_hours": cp["cutoff"]["hours"],
        "cutoff_comparison": cp["cutoff"].get("comparison", "inclusive"),
        "cutoff_based_on": cp["cutoff"].get("based_on", "day_1_start_at"),
        "rules": {
            "full_voluntary_gte_48h": {
                "outcome": cp["full_cancellation"]["before_cutoff"]["outcome"],
                "cash_refund_percent": 0,
                "package_credit_eligible": True,
            },
            "full_voluntary_lt_48h": {
                "outcome": cp["full_cancellation"]["after_cutoff"]["outcome"],
                "cash_refund_percent": 0,
                "package_credit_eligible": False,
            },
            "partial_gte_48h": {
                "outcome": "cash_refund",
                "cash_refund_percent": partial["before_cutoff"]["cash_refund_percent"],
            },
            "partial_lt_48h": {
                "outcome": "cash_refund",
                "cash_refund_percent": partial["after_cutoff"]["cash_refund_percent"],
            },
            "partial_after_day_1": {
                "outcome": "cash_refund",
                "cash_refund_percent": partial["after_day_1"]["cash_refund_percent"],
            },
            "no_show": {
                "outcome": cp["full_cancellation"].get("no_show", {}).get("outcome", "forfeited"),
                "cash_refund_percent": 0,
            },
            "flight_disruption_verified": {
                "outcome": "package_reactivation",
                "recovery_fee_percent": flight["recovery_fee_percent"],
                "maximum_uses": flight["maximum_uses"],
            },
            "flight_disruption_unverified": {
                "outcome": flight.get("unverified_outcome", "voluntary_late_cancellation"),
            },
            "force_majeure_full_tour": {
                "options": fm["full_tour"]["options"],
            },
            "force_majeure_partial_tour": {
                "first_remedy": fm["partial_tour"]["first_remedy"],
                "second_remedy": fm["partial_tour"]["second_remedy"],
            },
            "jvto_operational": {
                "options": cp.get("jvto_operational", {}).get(
                    "options", ["accepted_alternative", "full_cash_refund"]
                ),
            },
        },
        "partial_thresholds": {
            "minimum_remaining_pax": partial["minimum_remaining_pax"],
            "minimum_remaining_percent": partial["minimum_remaining_percent"],
            "reprice_remaining_guests": partial.get("reprice_remaining_guests", False),
            "threshold_fail_behaviour": partial.get(
                "threshold_fail_behaviour", "reclassify_as_full_cancellation"
            ),
            "foc_passenger_refund_percent": partial.get("foc_passenger_refund_percent", 0),
        },
        "package_credit_locks": {
            "expires": credit["expires"],
            "cash_value": credit["cash_value"],
            "package_change_allowed": credit["package_change_allowed"],
            "split_allowed": credit["split_allowed"],
            "transfer_allowed": credit["transfer_allowed"],
            "maximum_transfers": credit["maximum_transfers"],
            "original_package_locked": credit["original_package_locked"],
            "original_pax_locked": credit["original_pax_locked"],
            "original_price_locked": credit["original_price_locked"],
        },
        "booking_scope": cp["booking_scope"],
    }


def build_customer_copy(cancellation_policy: dict) -> dict:
    """Canonical customer-facing copy blocks generated from the YAML numbers.

    Numbers are interpolated from the SSOT so surface copy can never drift from
    the rules. Wording follows the approved phrasing in the implementation plan.
    """
    cp = cancellation_policy
    h = cp["cutoff"]["hours"]
    partial = cp["partial_cancellation"]
    before = partial["before_cutoff"]["cash_refund_percent"]
    after = partial["after_cutoff"]["cash_refund_percent"]
    after_day1 = partial["after_day_1"]["cash_refund_percent"]
    min_pax = partial["minimum_remaining_pax"]
    recovery = cp["flight_disruption"]["recovery_fee_percent"]
    max_transfers = cp["package_credit"]["maximum_transfers"]
    transfer_word = "once" if max_transfers == 1 else f"up to {max_transfers} times"
    return {
        "package_guarantee_summary": (
            "Your confirmed package does not disappear when plans change early. Cancel your "
            f"entire booking at least {h} hours before Day 1 and the same package, your original "
            "number of travellers, and your original confirmed package price remain available for "
            "future use as Lifetime Package Credit."
        ),
        "before_48_full_cancellation": (
            f"Cancel the complete booking {h} hours or more before Day 1: you receive Lifetime "
            "Package Credit. It never expires and preserves the same package, original pax "
            f"entitlement, and original confirmed price, and can be transferred {transfer_word}. "
            "Package Credit is not cash and cannot be exchanged for cash."
        ),
        "after_48_full_cancellation": (
            f"Cancel the complete booking less than {h} hours before Day 1: the booking is "
            "forfeited and no Package Credit is created."
        ),
        "partial_cancellation": (
            "If one or more travellers cancel but the tour continues, the cancelled travellers "
            f"receive a cash refund of their confirmed price: {before}% at {h} hours or more before "
            f"Day 1, {after}% within {h} hours, and {after_day1}% after Day 1. At least {min_pax} "
            "paying travellers must remain, otherwise it is treated as a full cancellation."
        ),
        "flight_disruption": (
            "If a verified natural transport disruption (for example volcanic ash) cancels your "
            f"flight, your package can be reactivated once for a {recovery}% Recovery Fee of the "
            "original confirmed package price."
        ),
        "destination_force_majeure": (
            "If a verified official event affects your destination and the whole tour is impossible, "
            "you can choose Lifetime Package Credit or a cash refund less any non-recoverable vendor "
            "cost. If only part is affected, JVTO first offers an alternative route, then a refund of "
            "the affected component."
        ),
        "package_transfer": (
            f"Package Credit may be transferred {transfer_word} to another person. The old credit "
            "code is closed and a new one is issued to the recipient. A second transfer is not "
            "permitted."
        ),
        "package_redemption": (
            "To use Package Credit, choose a new date for the same package. Your original pax "
            "entitlement appears automatically; fewer travellers yields no refund, and more "
            "travellers are charged the incremental website price."
        ),
    }


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


def build_manifest(sources, gap_report: dict, *, dry_run: bool) -> dict:
    cp = sources.cancellation_policy or {}
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_by": "scripts/compile_policy_bundle.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "cancellation_policy_version": cp.get("policy_version"),
        "cancellation_policy_hash": _sha(sources.cancellation_policy_text) if sources.cancellation_policy_text else None,
        "source_hashes": {
            "policy-source-ownership": _sha(sources.policy_text),
            "packages-overview": _sha(sources.packages_text),
            "faq-master": _sha(sources.faq_text),
            "cancellation-package-credit": _sha(sources.cancellation_policy_text) if sources.cancellation_policy_text else None,
        },
        "policy_domains": len(sources.ownership_rows),
        "deprecated_checks": len(sources.deprecated_rules),
        "consumers_checked": list(CONSUMERS),
        "artifacts": [name for name in OUTPUTS if name != "_manifest.json"],
        "sync_contract": {
            "recommended_consumer": "jvto-web",
            "source_path": "output/website/policy-bundle/",
            "target_path": "src/data/policy-bundle/",
            "required_gate": {
                "schema_version": SCHEMA_VERSION,
                "clean": True,
            },
            "required_files": list(OUTPUTS),
            "consumer_entrypoint": "consumer-bundles.json",
            "consumer_keys": list(CONSUMERS),
            "validation_files": [
                "deprecated-wording-report.json",
                "gap-report.json",
            ],
            "failure_rule": "Refuse sync if schema_version mismatches, clean is not true, any required file is missing, or any requested consumer is not present.",
        },
        "clean": gap_report["summary"]["errors"] == 0,
    }
