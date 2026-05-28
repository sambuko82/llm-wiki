"""Trust Bundle Compiler — enricher module.

Joins loader outputs into EnrichedClaim list. Pure data shaping, no I/O.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from scripts.compiler.loader import (
    Claim, Evidence, Entity, Decision, AeoFields,
)


@dataclass(frozen=True)
class EnrichedClaim:
    claim: Claim
    evidence: list[Evidence]
    entities: list[Entity]
    decisions: list[Decision]            # locked only
    narrative: Optional[AeoFields]


def enrich(
    claims: list[Claim],
    evidence: list[Evidence],
    entities: list[Entity],
    decisions: list[Decision],
    narratives: dict[str, AeoFields],
) -> list[EnrichedClaim]:
    """Join sources by claim_id. Evidence resolved by claim.evidence_ids (whitelist)."""
    evidence_by_id = {e.evidence_id: e for e in evidence}
    out: list[EnrichedClaim] = []
    for claim in claims:
        ev = [evidence_by_id[eid] for eid in claim.evidence_ids if eid in evidence_by_id]
        ents = [e for e in entities if claim.claim_id in e.claims]
        decs = [
            d for d in decisions
            if d.status == "locked" and claim.claim_id in d.applies_to_claims
        ]
        narr = narratives.get(claim.claim_id)
        out.append(EnrichedClaim(claim=claim, evidence=ev, entities=ents, decisions=decs, narrative=narr))
    return out
