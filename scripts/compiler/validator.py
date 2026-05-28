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
    # Rules added by Tasks 13–19.
    return report
