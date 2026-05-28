"""Trust Bundle Compiler — loader module.

Pure parse, no business logic. Reads 6 sources, returns typed dataclasses.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Optional

import yaml


# ---------- Dataclasses ----------

@dataclass(frozen=True)
class Claim:
    claim_id: str
    name: str
    canonical_text: str
    domain: str
    category: str
    verification_status: str
    wiki_pages: list[str]
    output_pages: list[str]
    evidence_ids: list[str]
    evidence_count: int
    key_proof_ids: list[str]
    tags: list[str]
    last_verified: date
    stale_after_days: Optional[int]    # None -> default 90 in validator F1
    entity_refs: list[str]             # may be empty (field not yet present in registry)


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    claim: str                          # back-ref to claim_id (cross-check only)
    source_file: str
    evidence_type_code: int             # raw numeric from YAML
    evidence_type: str                  # mapped slug
    description: str
    verification_status: str
    last_verified: date
    proof_ids: list[str]


@dataclass(frozen=True)
class Entity:
    entity_id: str
    name: str
    type: str
    aliases: list[str]
    wiki_pages: list[str]
    schema_type: Optional[str]
    canonical_url: Optional[str]
    claims: list[str]                   # forward-ref to claim_ids
    tags: list[str]


@dataclass(frozen=True)
class Decision:
    decision_id: str
    topic: str
    final_value: Any                    # scalar or dict
    secondary_facts: Optional[dict]
    status: str                         # locked / provisional / superseded
    decided_by: str
    decided_at: date
    source_basis: list[str]
    applies_to_claims: list[str]
    resolves_conflicts: list[str]
    resolves_dq: list[str]
    superseded_by: Optional[str]
    notes: str


@dataclass(frozen=True)
class Conflict:
    conflict_id: str                    # e.g. CONF-001
    detected: date
    claim_a: str
    source_a: str
    claim_b: str
    source_b: str
    status: str                         # open / resolved
    affects_claims: list[str]           # parsed from new column
    evidence_weight: str
    resolution: str


@dataclass(frozen=True)
class AeoFields:
    claim_id: str
    ai_snippet: str
    short: str
    cs_reply: str


# ---------- Loaders ----------

def _to_date(value: Any) -> date:
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        return date.fromisoformat(value)
    raise ValueError(f"Cannot coerce to date: {value!r}")


def load_claims(path: Path) -> list[Claim]:
    """Parse claim-registry.yml → list[Claim]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Claim] = []
    for item in data["claims"]:
        out.append(
            Claim(
                claim_id=item["claim_id"],
                name=item["name"],
                canonical_text=item["canonical_text"],
                domain=item["domain"],
                category=item["category"],
                verification_status=item["verification_status"],
                wiki_pages=list(item.get("wiki_pages") or []),
                output_pages=list(item.get("output_pages") or []),
                evidence_ids=list(item.get("evidence_ids") or []),
                evidence_count=int(item.get("evidence_count", 0)),
                key_proof_ids=list(item.get("key_proof_ids") or []),
                tags=list(item.get("tags") or []),
                last_verified=_to_date(item["last_verified"]),
                stale_after_days=item.get("stale_after_days"),
                entity_refs=list(item.get("entity_refs") or []),
            )
        )
    return out
