"""Tests for scripts/verify_claims.py — the claim-boundary linter."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_claims.py"


def _run_stdin(text: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--stdin"],
        input=text, capture_output=True, text=True, cwd=REPO_ROOT,
    )


def test_clean_draft_passes():
    text = (
        "Stefan Loose Reiseführer Indonesien (ISBN-13 9783770167654, p. 287) identifies Agung.\n"
        "Booking is historical address context only, not legal succession.\n"
        "Detik covers his Tourist Police duties in the Bondowoso area.\n"
        "Trustpilot 4.8 / 51 reviews; Google 4.9 / 123.\n"
    )
    r = _run_stdin(text)
    assert r.returncode == 0, r.stderr


def test_canonical_isbn_is_not_flagged():
    # The dropped ISBN (978-3-7701-7881-0) and the canonical (9783770167654) share a digit
    # prefix; the canonical must never trip STEFAN-EDITION.
    r = _run_stdin("Stefan Loose, ISBN-13 9783770167654, p. 287.\n")
    assert r.returncode == 0, r.stderr


def test_each_boundary_fails():
    cases = {
        "STEFAN-EDITION": "Stefan Loose 4th Edition (2018), ISBN 978-3-7701-7881-0.",
        "BOOKING-CONTINUITY": "This is the address-continuity evidence.",
        "DETIK-IJEN": "Detik names him in duties at Ijen.",
        "STALE-REVIEW": "Google Maps 4.90 / 92 reviews.",
    }
    for rule, text in cases.items():
        r = _run_stdin(text + "\n")
        assert r.returncode == 1, f"{rule}: expected failure, got 0"
        assert rule in r.stderr, f"{rule}: not reported in stderr:\n{r.stderr}"


def test_medical_attributed_to_bbksda_passes():
    # The QR rule attributed to BBKSDA (not presented as JVTO's universal mandate) is allowed.
    r = _run_stdin("No valid QR code means no access — that rule is BBKSDA's, not ours.\n")
    assert r.returncode == 0, r.stderr


def test_context_note_is_not_flagged():
    # A resolution/guard note ABOUT a superseded value is context, not an assertion.
    r = _run_stdin("CONF-001 dropped the Stefan 2018 / 978-3-7701-7881-0 values (superseded).\n")
    assert r.returncode == 0, r.stderr
