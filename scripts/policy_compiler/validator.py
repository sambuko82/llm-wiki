"""Validation helpers for policy bundle compilation (v2)."""
from __future__ import annotations

from policy_compiler.renderer import CANCELLATION_POLICY_ID

# Wording that must never appear in any compiled consumer copy/evidence.
# POL2-12 forbids CLAIMING the guarantee is insurance — not legitimate mentions
# that travellers should buy their own travel insurance (a standard exclusion).
_INSURANCE_MARKERS = ("insurance protection", "insurance coverage", "insured by jvto")
_WHATSAPP_BOOKING_MARKERS = (
    "whatsapp-assisted booking",
    "whatsapp assisted booking",
    "book through whatsapp",
    "book via whatsapp",
)


def _err(rule_id: str, policy_id: str, message: str) -> dict:
    return {"rule_id": rule_id, "severity": "error", "policy_id": policy_id, "message": message}


def _collect_text(policy_bundle: list[dict]) -> str:
    parts: list[str] = []
    for policy in policy_bundle:
        for ev in policy.get("evidence", []):
            parts.append(ev.get("text", ""))
        for value in (policy.get("customer_copy") or {}).values():
            parts.append(value)
    return "\n".join(parts).lower()


def validate_cancellation(
    policy_bundle: list[dict],
    cancellation_policy: dict,
    decision_matrix: dict,
    consumer_bundles: dict,
) -> list[dict]:
    """POL2-01..14 — hard failures that keep the locked policy self-consistent."""
    findings: list[dict] = []
    cid = CANCELLATION_POLICY_ID
    cp = cancellation_policy or {}
    dm = decision_matrix or {}
    rules = dm.get("rules", {})
    locks = dm.get("package_credit_locks", {})

    def in_consumer(consumer: str) -> bool:
        bundle = consumer_bundles.get(consumer, {})
        return cid in bundle.get("policy_ids", [])

    # POL2-01 — booking source must be website only.
    allowed = list(cp.get("booking_scope", {}).get("allowed_sources", []))
    if allowed != ["website"]:
        findings.append(_err("POL2-01", cid, f"Booking source is not website-only: {allowed}"))

    # POL2-02 / POL2-03 — cancellation domain must reach checkout + booking portal.
    if not in_consumer("website_checkout"):
        findings.append(_err("POL2-02", cid, "Cancellation domain missing from website_checkout consumer bundle."))
    if not in_consumer("booking_portal"):
        findings.append(_err("POL2-03", cid, "Cancellation domain missing from booking_portal consumer bundle."))

    # POL2-04 — e-voucher must carry a policy version.
    if not cp.get("policy_version") or not in_consumer("e_voucher"):
        findings.append(_err("POL2-04", cid, "E-Voucher does not carry a versioned cancellation policy."))

    # POL2-05 — full >=48h must not be a cash refund.
    gte = rules.get("full_voluntary_gte_48h", {})
    if gte.get("cash_refund_percent", 0) != 0 or gte.get("outcome") != "lifetime_package_credit":
        findings.append(_err("POL2-05", cid, "Full cancellation >=48h must yield Package Credit, not cash."))

    # POL2-06 — Package Credit cannot move to a different package.
    if locks.get("package_change_allowed"):
        findings.append(_err("POL2-06", cid, "Package Credit must be locked to the same package."))

    # POL2-07 — Package Credit cannot be split.
    if locks.get("split_allowed"):
        findings.append(_err("POL2-07", cid, "Package Credit must not be splittable."))

    # POL2-08 — at most one transfer.
    if locks.get("maximum_transfers", 1) > 1:
        findings.append(_err("POL2-08", cid, "Package Credit transfers must be capped at one."))

    # POL2-09 — original package/pax/price must be locked.
    if not (locks.get("original_package_locked") and locks.get("original_pax_locked") and locks.get("original_price_locked")):
        findings.append(_err("POL2-09", cid, "Original package/pax/price must all be locked on Package Credit."))

    # POL2-10 — partial <48h must be 50%.
    if rules.get("partial_lt_48h", {}).get("cash_refund_percent") != 50:
        findings.append(_err("POL2-10", cid, "Partial cancellation <48h must be a 50% cash refund."))

    # POL2-11 — flight recovery fee must be 50%.
    if rules.get("flight_disruption_verified", {}).get("recovery_fee_percent") != 50:
        findings.append(_err("POL2-11", cid, "Flight-disruption Recovery Fee must be 50%."))

    # POL2-12 / POL2-13 — no insurance wording, no WhatsApp-booking wording.
    text = _collect_text(policy_bundle)
    if any(marker in text for marker in _INSURANCE_MARKERS):
        findings.append(_err("POL2-12", cid, "Insurance wording found in compiled policy copy."))
    if any(marker in text for marker in _WHATSAPP_BOOKING_MARKERS):
        findings.append(_err("POL2-13", cid, "WhatsApp-assisted booking wording found in compiled policy copy."))

    # POL2-14 — no unregistered consumer aliases anywhere.
    for policy in policy_bundle:
        for token in policy.get("unregistered_consumers", []):
            findings.append(_err("POL2-14", policy["policy_id"], f"Unregistered consumer alias: {token!r}"))

    return findings


def validate(
    policy_bundle: list[dict],
    deprecated_report: dict,
    cancellation_policy: dict | None = None,
    decision_matrix: dict | None = None,
    consumer_bundles: dict | None = None,
) -> list[dict]:
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
    if cancellation_policy is not None and decision_matrix is not None and consumer_bundles is not None:
        findings.extend(
            validate_cancellation(policy_bundle, cancellation_policy, decision_matrix, consumer_bundles)
        )
    return findings
