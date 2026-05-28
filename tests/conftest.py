"""Shared pytest fixtures and path helpers."""
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GOLDEN_DIR = Path(__file__).resolve().parent / "golden"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture
def golden_dir() -> Path:
    return GOLDEN_DIR


@pytest.fixture
def repo_root() -> Path:
    return REPO_ROOT
