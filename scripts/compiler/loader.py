"""Trust Bundle Compiler — loader module.

Pure parse, no business logic. Reads 6 sources, returns typed dataclasses.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Optional


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
