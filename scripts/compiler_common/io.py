"""Shared hashing + atomic-write helpers for the package/policy compilers."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def atomic_write_json(path: Path, data) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def write_outputs(out_dir: str | Path, artifacts: dict) -> list[str]:
    """Atomically write each {filename: data} pair. Caller controls the set."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, data in artifacts.items():
        atomic_write_json(out / name, data)
    return list(artifacts)
