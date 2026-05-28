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


EVIDENCE_TYPE_SLUGS: dict[int, str] = {
    1: "official_authority",
    2: "jvto_verified_internal",
    4: "reputable_media",
    5: "structured_dataset",
    6: "customer_review",
    8: "ai_generated",
}


def load_evidence(path: Path) -> list[Evidence]:
    """Parse evidence-registry.yml → list[Evidence] with numeric→slug type mapping."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Evidence] = []
    for item in data["evidence"]:
        code = int(item["evidence_type"])
        slug = EVIDENCE_TYPE_SLUGS.get(code)
        if slug is None:
            raise ValueError(
                f"unknown evidence_type code {code} for {item['evidence_id']}; "
                f"add it to EVIDENCE_TYPE_SLUGS in loader.py"
            )
        out.append(
            Evidence(
                evidence_id=item["evidence_id"],
                claim=item["claim"],
                source_file=item["source_file"],
                evidence_type_code=code,
                evidence_type=slug,
                description=item["description"],
                verification_status=item["verification_status"],
                last_verified=_to_date(item["last_verified"]),
                proof_ids=list(item.get("proof_ids") or []),
            )
        )
    return out


def load_entities(path: Path) -> list[Entity]:
    """Parse entity-registry.yml → list[Entity]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Entity] = []
    for item in data["entities"]:
        out.append(
            Entity(
                entity_id=item["entity_id"],
                name=item["name"],
                type=item["type"],
                aliases=list(item.get("aliases") or []),
                wiki_pages=list(item.get("wiki_pages") or []),
                schema_type=item.get("schema_type"),
                canonical_url=item.get("canonical_url"),
                claims=list(item.get("claims") or []),
                tags=list(item.get("tags") or []),
            )
        )
    return out
