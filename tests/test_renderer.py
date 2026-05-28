"""Renderer module tests."""
from datetime import date


def _enriched_c1():
    from scripts.compiler.loader import (
        Claim, Evidence, Entity, Decision, AeoFields,
    )
    from scripts.compiler.enricher import EnrichedClaim
    claim = Claim(
        claim_id="C1", name="Safety-Led Operations",
        canonical_text="Volcano travel is unpredictable.",
        domain="credentials", category="trust-signal",
        verification_status="verified",
        wiki_pages=["wiki/x.md"], output_pages=["output/x"],
        evidence_ids=["E001"], evidence_count=1,
        key_proof_ids=["sprin-polpar"],
        tags=["police-led", "safety"],
        last_verified=date(2026, 5, 26),
        stale_after_days=None, entity_refs=[],
    )
    ev = Evidence(
        evidence_id="E001", claim="C1", source_file="wiki/people/agung-sambuko.md",
        evidence_type_code=2, evidence_type="jvto_verified_internal",
        description="Founder is active Tourist Police officer",
        verification_status="verified",
        last_verified=date(2026, 5, 25),
        proof_ids=["sprin-polpar"],
    )
    dec = Decision(
        decision_id="DEC-001", topic="founding_year",
        final_value=2015, secondary_facts=None,
        status="locked", decided_by="Sam",
        decided_at=date(2026, 5, 28),
        source_basis=["AHU"], applies_to_claims=["C1"],
        resolves_conflicts=[], resolves_dq=[],
        superseded_by=None, notes="",
    )
    narr = AeoFields("C1", "snippet", "short", "cs reply")
    return EnrichedClaim(claim=claim, evidence=[ev], entities=[], decisions=[dec], narrative=narr)


def test_render_claims_structure():
    from scripts.compiler.renderer import render_claims
    out = render_claims([_enriched_c1()], compiled_at="2026-05-28T00:00:00Z")
    assert out["version"] == "1.0"
    assert out["compiled_at"] == "2026-05-28T00:00:00Z"
    assert len(out["claims"]) == 1
    c = out["claims"][0]
    assert c["id"] == "C1"
    assert c["last_verified"] == "2026-05-26"
    assert c["evidence"][0]["type"] == "jvto_verified_internal"
    assert c["decisions"][0]["decision_id"] == "DEC-001"
    assert c["decisions"][0]["final_value"] == 2015
    assert c["narrative"]["ai_snippet"] == "snippet"


def test_render_organization_schema():
    from scripts.compiler.renderer import render_organization_schema
    org = render_organization_schema(
        legal_name="PT Java Volcano Rendezvous",
        brand_name="Java Volcano Tour Operator",
        nib="1102230032918",
        tdup="1102230032918",
        founder_name="Agung Sambuko",
        founder_job="Tourist Police Officer",
        url="https://javavolcano-touroperator.com",
    )
    assert org["@context"] == "https://schema.org"
    assert org["@type"] == "TravelAgency"
    assert org["legalName"] == "PT Java Volcano Rendezvous"
    identifiers = {i["propertyID"]: i["value"] for i in org["identifier"]}
    assert identifiers["NIB"] == "1102230032918"
    assert identifiers["TDUP"] == "1102230032918"
    assert org["founder"]["name"] == "Agung Sambuko"


def test_render_faq_page_schema():
    from scripts.compiler.renderer import render_faq_page_schema
    faq = render_faq_page_schema([
        {"question": "Is JVTO licensed?", "answer": "Yes, NIB 1102230032918."},
        {"question": "Do you offer private tours?", "answer": "Yes, all tours are private."},
    ])
    assert faq["@context"] == "https://schema.org"
    assert faq["@type"] == "FAQPage"
    assert len(faq["mainEntity"]) == 2
    q0 = faq["mainEntity"][0]
    assert q0["@type"] == "Question"
    assert q0["name"] == "Is JVTO licensed?"
    assert q0["acceptedAnswer"]["@type"] == "Answer"
    assert q0["acceptedAnswer"]["text"] == "Yes, NIB 1102230032918."


def test_render_tourist_trip_schema_dedupes_by_url():
    from scripts.compiler.renderer import render_tourist_trip_schema
    from scripts.compiler.loader import Entity
    entities = [
        Entity("ENT-001", "Kawah Ijen", "destination", [], [],
               "TouristAttraction", "/destinations/ijen-crater", ["C1"], []),
        Entity("ENT-001-dup", "Kawah Ijen", "destination", [], [],
               "TouristAttraction", "/destinations/ijen-crater", ["C4"], []),  # duplicate URL
        Entity("ENT-002", "Mount Bromo", "destination", [], [],
               "TouristAttraction", "/destinations/mount-bromo", ["C1"], []),
        Entity("ENT-003", "Founder Person", "person", [], [],
               "Person", "/people/founder", ["C1"], []),  # not a destination -> excluded
    ]
    trips = render_tourist_trip_schema(entities, base_url="https://javavolcano-touroperator.com")
    assert len(trips) == 2  # one per unique destination URL
    urls = [t["url"] for t in trips]
    assert "https://javavolcano-touroperator.com/destinations/ijen-crater" in urls
    assert "https://javavolcano-touroperator.com/destinations/mount-bromo" in urls
    assert all(t["@type"] == "TouristTrip" for t in trips)


def test_render_tourist_trip_excludes_entities_without_url():
    from scripts.compiler.renderer import render_tourist_trip_schema
    from scripts.compiler.loader import Entity
    entities = [
        Entity("ENT-X", "No URL Place", "destination", [], [], "TouristAttraction", None, [], []),
    ]
    trips = render_tourist_trip_schema(entities, base_url="https://x")
    assert trips == []


def test_render_faq_uses_short_preferred():
    from scripts.compiler.renderer import render_faq
    faq = render_faq([_enriched_c1()])
    assert faq["version"] == "1.0"
    assert len(faq["items"]) == 1
    item = faq["items"][0]
    assert item["question"] == "Safety-Led Operations"
    assert item["answer"] == "short"
    assert item["source_claim_id"] == "C1"


def test_render_faq_falls_back_to_cs_reply_when_short_empty():
    from scripts.compiler.renderer import render_faq
    from scripts.compiler.loader import AeoFields
    from scripts.compiler.enricher import EnrichedClaim
    ec = _enriched_c1()
    blank_short = AeoFields("C1", "snippet", "", "cs reply")
    ec2 = EnrichedClaim(claim=ec.claim, evidence=ec.evidence, entities=ec.entities,
                        decisions=ec.decisions, narrative=blank_short)
    faq = render_faq([ec2])
    assert faq["items"][0]["answer"] == "cs reply"


def test_render_aeo_snippets_topic_from_tags():
    from scripts.compiler.renderer import render_aeo_snippets
    snippets = render_aeo_snippets([_enriched_c1()])
    assert snippets["version"] == "1.0"
    assert len(snippets["snippets"]) == 1
    s = snippets["snippets"][0]
    # topic is first tag if any, else claim_id lowercased
    assert s["topic"] == "police-led"
    assert s["tldr"] == "snippet"
    assert s["claim_ids"] == ["C1"]
    assert "FAQPage" in s["use_for"]
