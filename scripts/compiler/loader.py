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


def load_decisions(path: Path) -> list[Decision]:
    """Parse decision-registry.yml → list[Decision]."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    out: list[Decision] = []
    for item in data["decisions"]:
        out.append(
            Decision(
                decision_id=item["decision_id"],
                topic=item["topic"],
                final_value=item["final_value"],
                secondary_facts=item.get("secondary_facts"),
                status=item["status"],
                decided_by=item["decided_by"],
                decided_at=_to_date(item["decided_at"]),
                source_basis=list(item.get("source_basis") or []),
                applies_to_claims=list(item.get("applies_to_claims") or []),
                resolves_conflicts=list(item.get("resolves_conflicts") or []),
                resolves_dq=list(item.get("resolves_dq") or []),
                superseded_by=item.get("superseded_by"),
                notes=item.get("notes", "") or "",
            )
        )
    return out


import re

_CONFLICT_ROW_RE = re.compile(r"^\|\s*CONF-\w+", re.MULTILINE)


def load_conflicts(path: Path) -> list[Conflict]:
    """Parse the markdown table in conflict-log.md → list[Conflict].

    Expected columns (order matters):
      ID | Detected | Claim A | Source A | Claim B | Source B | Status |
      Affects Claims | Evidence Weight | Resolution
    """
    text = path.read_text(encoding="utf-8")
    out: list[Conflict] = []
    for line in text.splitlines():
        if not _CONFLICT_ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 10:
            raise ValueError(f"conflict row has {len(cells)} cells, expected 10: {line!r}")
        affects = cells[7]
        affects_list = [c.strip() for c in affects.split(",")] if affects else []
        affects_list = [c for c in affects_list if c]
        out.append(
            Conflict(
                conflict_id=cells[0],
                detected=_to_date(cells[1]),
                claim_a=cells[2],
                source_a=cells[3],
                claim_b=cells[4],
                source_b=cells[5],
                status=cells[6],
                affects_claims=affects_list,
                evidence_weight=cells[8],
                resolution=cells[9],
            )
        )
    return out


_H2_CLAIM_RE = re.compile(r"^##\s+(C\d+)\b", re.MULTILINE)
_FIELD_RE = re.compile(
    r"^\*\*(AI snippet|Short|CS reply)\*\*:\s*\*?\"?(.*?)\"?\*?\s*$",
    re.MULTILINE,
)


def _strip_wrappers(text: str) -> str:
    """Strip leading/trailing `*` italics and `"` quote wrappers if present."""
    text = text.strip()
    while text and text[0] in '*"' and text[-1:] in '*"':
        text = text[1:-1].strip()
    return text


def load_aeo_narratives(path: Path) -> dict[str, AeoFields]:
    """Parse wiki/website/aeo-claims.md → dict[claim_id, AeoFields].

    Splits by H2 headers matching `## C<N>` and extracts three bold-labeled
    fields per block: `AI snippet`, `Short`, `CS reply`.
    """
    text = path.read_text(encoding="utf-8")
    starts = [(m.group(1), m.start()) for m in _H2_CLAIM_RE.finditer(text)]
    starts.append(("__END__", len(text)))
    out: dict[str, AeoFields] = {}
    for i, (cid, pos) in enumerate(starts[:-1]):
        block = text[pos:starts[i + 1][1]]
        fields: dict[str, str] = {}
        for fm in _FIELD_RE.finditer(block):
            fields[fm.group(1)] = _strip_wrappers(fm.group(2))
        out[cid] = AeoFields(
            claim_id=cid,
            ai_snippet=fields.get("AI snippet", ""),
            short=fields.get("Short", ""),
            cs_reply=fields.get("CS reply", ""),
        )
    return out
