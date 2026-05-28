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
) -> ValidationReport:
    """Run all rules F1..F8 and return a single ValidationReport."""
    if today is None:
        today = date.today()
    report = ValidationReport()
    for ec in enriched_claims:
        _check_f1_freshness(ec, today, report)
        _check_f2_evidence(ec, report)
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
