# scripts/compiler/validator.py
"""Trust Bundle Compiler — validator module.

Strict gate. Takes enriched claims + decisions + conflicts + narratives,
returns ValidationReport with rule violations F1..F8.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

from scripts.compiler.loader import Decision, Conflict, AeoFields
from scripts.compiler.enricher import EnrichedClaim


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class Violation:
    rule_id: str
    severity: Severity
    target_id: str                     # claim_id, decision_id, or conflict_id
    message: str


@dataclass
class ValidationReport:
    violations: list[Violation] = field(default_factory=list)

    @property
    def errors(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == Severity.ERROR]

    @property
    def warnings(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == Severity.WARNING]

    @property
    def has_errors(self) -> bool:
        return any(v.severity == Severity.ERROR for v in self.violations)

    def rule_summary(self) -> dict[str, str]:
        """Map rule prefix → 'pass' / 'N errors' / 'M warnings'."""
        rule_status: dict[str, dict[str, int]] = {}
        for v in self.violations:
            prefix = v.rule_id.rstrip("abcd")  # F2a → F2
            bucket = rule_status.setdefault(prefix, {"error": 0, "warning": 0})
            bucket[v.severity.value] += 1
        out: dict[str, str] = {}
        for rule in ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"):
            if rule not in rule_status:
                out[rule] = "pass"
            else:
                b = rule_status[rule]
                parts = []
                if b["error"]:
                    parts.append(f"{b['error']} errors")
                if b["warning"]:
                    parts.append(f"{b['warning']} warnings")
                out[rule] = ", ".join(parts) if parts else "pass"
        return out


def run(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    narratives: dict[str, AeoFields],
    all_claim_ids: set[str],
    today: Optional[date] = None,
    known_entity_ids: Optional[set[str]] = None,
) -> ValidationReport:
    """Run all rules F1..F8 and return a single ValidationReport."""
    if today is None:
        today = date.today()
    if known_entity_ids is None:
        known_entity_ids = set()
    report = ValidationReport()
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
        _check_f2_evidence(ec, report)
        _check_f3_entities(ec, known_entity_ids, report)
        _check_f5_narratives(ec, report)
        _check_f6_f7_crosschecks(ec, report)
    _check_f4_conflicts(enriched_claims, decisions, conflicts, report)
    return report


def _check_f1_freshness(ec: EnrichedClaim, today: date, report: ValidationReport) -> None:
    window = ec.claim.stale_after_days if ec.claim.stale_after_days is not None else 90
    age_days = (today - ec.claim.last_verified).days
    if age_days > window:
        report.violations.append(
            Violation(
                rule_id="F1",
                severity=Severity.ERROR,
                target_id=ec.claim.claim_id,
                message=(
                    f"stale: last_verified {ec.claim.last_verified} is {age_days} days old "
                    f"(limit {window})"
                ),
            )
        )


def _check_f2_evidence(ec: EnrichedClaim, report: ValidationReport) -> None:
    declared = ec.claim.evidence_ids
    resolved_ids = {e.evidence_id for e in ec.evidence}

    # F2a: at least one evidence_id declared
    if not declared:
        report.violations.append(
            Violation("F2a", Severity.ERROR, ec.claim.claim_id,
                      "claim has no evidence_ids declared")
        )

    # F2b: every declared id resolves
    for eid in declared:
        if eid not in resolved_ids:
            report.violations.append(
                Violation("F2b", Severity.ERROR, ec.claim.claim_id,
                          f"evidence_id {eid} declared but not found in evidence-registry")
            )

    # F2c: every resolved evidence is verified
    for e in ec.evidence:
        if e.verification_status != "verified":
            report.violations.append(
                Violation("F2c", Severity.ERROR, ec.claim.claim_id,
                          f"evidence {e.evidence_id} has status={e.verification_status!r}, expected 'verified'")
            )


def _check_f3_entities(ec: EnrichedClaim, known: set[str], report: ValidationReport) -> None:
    for eid in ec.claim.entity_refs:
        if eid not in known:
            report.violations.append(
                Violation("F3", Severity.WARNING, ec.claim.claim_id,
                          f"entity_ref {eid} unresolved in entity-registry")
            )


def _check_f5_narratives(ec: EnrichedClaim, report: ValidationReport) -> None:
    n = ec.narrative
    if n is None:
        report.violations.append(
            Violation("F5", Severity.ERROR, ec.claim.claim_id,
                      "no narrative block found in aeo-claims.md")
        )
        return
    missing = [f for f in ("ai_snippet", "short", "cs_reply") if not getattr(n, f)]
    if missing:
        report.violations.append(
            Violation("F5", Severity.ERROR, ec.claim.claim_id,
                      f"narrative missing fields: {', '.join(missing)}")
        )


def _check_f6_f7_crosschecks(ec: EnrichedClaim, report: ValidationReport) -> None:
    # F6: every resolved evidence has back-ref matching this claim's id
    for e in ec.evidence:
        if e.claim != ec.claim.claim_id:
            report.violations.append(
                Violation("F6", Severity.WARNING, ec.claim.claim_id,
                          f"evidence {e.evidence_id} back-ref claim={e.claim!r} but listed under {ec.claim.claim_id}")
            )
    # F7: evidence_count field matches actual count
    if ec.claim.evidence_count != len(ec.claim.evidence_ids):
        report.violations.append(
            Violation("F7", Severity.WARNING, ec.claim.claim_id,
                      f"evidence_count={ec.claim.evidence_count} but len(evidence_ids)={len(ec.claim.evidence_ids)}")
        )


def _check_f4_conflicts(
    enriched_claims: list[EnrichedClaim],
    decisions: list[Decision],
    conflicts: list[Conflict],
    report: ValidationReport,
) -> None:
    # Build set of conflict_ids resolved by locked decisions
    locked_resolves: set[str] = set()
    for d in decisions:
        if d.status == "locked":
            locked_resolves.update(d.resolves_conflicts)

    enriched_ids = {ec.claim.claim_id for ec in enriched_claims}
    for c in conflicts:
        if c.status != "open":
            continue
        for cid in c.affects_claims:
            if cid not in enriched_ids:
                continue
            if c.conflict_id in locked_resolves:
                continue
            report.violations.append(
                Violation("F4", Severity.ERROR, cid,
                          f"unresolved conflict {c.conflict_id} touches {cid} and no locked decision covers it")
            )
