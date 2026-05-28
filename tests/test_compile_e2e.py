"""End-to-end compile tests using synthetic fixture sets."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _setup_e2e_repo(tmp_path, source_dir):
    """Copy compiler code + fixtures into tmp_path so we get isolated output."""
    work = tmp_path / "work"
    work.mkdir()
    # Copy compiler scripts and tests modules
    shutil.copytree(REPO_ROOT / "scripts", work / "scripts")
    # Layout fixture inputs
    (work / "raw" / "_manifest").mkdir(parents=True)
    (work / "wiki" / "website").mkdir(parents=True)
    src = REPO_ROOT / "tests" / "fixtures" / source_dir
    shutil.copy(src / "claim-registry.yml", work / "raw" / "_manifest" / "claim-registry.yml")
    shutil.copy(src / "evidence-registry.yml", work / "raw" / "_manifest" / "evidence-registry.yml")
    shutil.copy(src / "entity-registry.yml", work / "raw" / "_manifest" / "entity-registry.yml")
    shutil.copy(src / "decision-registry.yml", work / "raw" / "_manifest" / "decision-registry.yml")
    shutil.copy(src / "conflict-log.md", work / "raw" / "_manifest" / "conflict-log.md")
    shutil.copy(src / "aeo-claims.md", work / "wiki" / "website" / "aeo-claims.md")
    (work / "wiki" / "log.md").write_text("# Log\n", encoding="utf-8")
    return work


def test_e2e_happy_path(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0, f"stderr:\n{result.stderr}"
    bundle = work / "output" / "website" / "trust-bundle"
    expected = [
        "claims.json",
        "faq.json",
        "aeo-snippets.json",
        "_manifest.json",
        "schema/organization.json",
        "schema/faq-page.json",
        "schema/tourist-trip.json",
    ]
    for rel in expected:
        f = bundle / rel
        assert f.exists(), f"missing output: {rel}"
        # parses as JSON
        json.loads(f.read_text(encoding="utf-8"))
    manifest = json.loads((bundle / "_manifest.json").read_text(encoding="utf-8"))
    assert manifest["inputs"]["claims"] == 2
    assert manifest["validation"]["F1"] == "pass"
    assert manifest["validation"]["F2"] == "pass"
    assert manifest["validation"]["F4"] == "pass"
    # Log was appended
    log_text = (work / "wiki" / "log.md").read_text(encoding="utf-8")
    assert "compile | trust-bundle v0.1.0" in log_text


def test_e2e_strict_fail_writes_nothing(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e-stale")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 1
    assert "F1" in result.stderr
    assert "stale" in result.stderr.lower()
    bundle = work / "output" / "website" / "trust-bundle"
    assert not bundle.exists(), "strict-fail should not write any output"


def test_e2e_dry_run_writes_nothing_even_when_clean(tmp_path):
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py", "--dry-run"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0
    bundle = work / "output" / "website" / "trust-bundle"
    assert not bundle.exists(), "dry-run should not write any output"


def test_e2e_atomic_write_leaves_no_tmp_files(tmp_path):
    """A successful run leaves zero .tmp files behind."""
    work = _setup_e2e_repo(tmp_path, source_dir="e2e")
    result = subprocess.run(
        [sys.executable, "scripts/compile_trust.py"],
        cwd=work, capture_output=True, text=True,
    )
    assert result.returncode == 0
    tmps = list((work / "output").rglob("*.tmp"))
    assert tmps == []
