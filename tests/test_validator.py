# tests/test_validator.py
"""Validator module tests."""
from datetime import date


def test_validation_report_has_zero_errors_for_clean_inputs():
    from scripts.compiler.validator import run, Severity
    report = run(
        enriched_claims=[],
        decisions=[],
        conflicts=[],
        narratives={},
        all_claim_ids=set(),
        today=date(2026, 5, 28),
    )
    assert report.violations == []
    assert report.has_errors is False


def test_severity_enum_values():
    from scripts.compiler.validator import Severity
    assert Severity.ERROR.value == "error"
    assert Severity.WARNING.value == "warning"
