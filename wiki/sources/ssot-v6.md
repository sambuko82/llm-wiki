---
type: source
title: JVTO_FINAL_CLEAN_SSOT.json v6.0 — Source Summary
last_updated: 2026-05-11
sources: [ssot-v6]
---

# Source: JVTO_FINAL_CLEAN_SSOT.json v6.0

## Metadata

- **File**: `raw/JVTO_FINAL_CLEAN_SSOT.json`
- **Size**: 471 KB
- **Version**: 6.0
- **Status**: Canonical
- **Date**: 2026-04-22
- **Audit trail**: `JVTO_SSOT_AUDIT_v5.md`
- **Parent authority**: This file is itself the canonical authority for all downstream wiki pages.

## Authority Status

This document declares itself the **primary canonical source** for JVTO's structured data. When wiki pages conflict with this file, treat the SSOT as ground truth unless: (a) the contradiction is with a more recent fact verified in [[log]], or (b) project CLAUDE.md provides a competing canonical statement, in which case flag the contradiction.

## 13-Domain Structure

| # | Domain | Content |
|---|---|---|
| 1 | `organization_core` | Identity layer — legal entity, founder, contacts, schema-facing identity |
| 2 | `narrative_system` | Claim architecture — thesis, 9 pillars, 9 claim-to-evidence maps, voice invariants |
| 3 | `trust_proof_system` | Verification stack — 15 credentials, 9 proof groups, 58 assets, press, historical timeline |
| 4 | `people_system` | Founder + 11-member crew registry + people-facing trust data + HPWKI/BBKSDA chain |
| 5 | `page_architecture` | 50 canonical routes across 9 clusters, page types, AI page intelligence |
| 6 | `package_route_logic` | 15 packages — pricing, itineraries, inclusions/exclusions, 23 FAQs, route metadata, AI package intelligence |
| 7 | `support_policy_logic` | Booking flow, payment rules, Ijen health screening protocol, weather closures, escort rules, policy pack, FOC scheme, vehicle allocation |
| 8 | `meta_governance` | Canonical counts (26 entries), schema status (live + pending), 12 open issues, schema generator spec (5-layer architecture), codebase cleanup log |
| 9 | `ai_extraction_surfaces_v1` | Homepage entity block, why-jvto trust summary, verify proof blocks, destination entity summaries, travel-guide extraction blocks |
| 10 | `review_registry` | Trustpilot 4.8/47 aggregate (verified 2026-04-19), platform profiles, 5 review themes, schema implementation rules |
| 11 | `ai_layer` | AI-facing field extensions: ai_summary_snippet, answer_block, query_intents, schema_family, entity_anchor_text, supports_claims — added to all major entities |
| 12 | `trust_graph` | Operational trust graph — bidirectional claim↔proof↔page mapping. 9 claims, 24 proof items, 18 pages. 7 anti-drift rules. |
| 13 | `ai_extraction_surfaces` | Pre-built AI extraction surfaces — homepage, why-jvto, verify, travel-guide, policy, packages, destinations |

## Wiki Domain → SSOT Field Map

For LLM queries, this is the lookup table:

| Wiki area | SSOT domains | Key paths |
|---|---|---|
| [[overview]] / identity | 1, 11 | `domain_1_organization_core`, `domain_11_ai_layer.organization_core` |
| [[people/agung-sambuko]] | 1.2, 4.1, 11 | `domain_1.1_2_founder`, `domain_4.4_1_founder` |
| [[people/crew-registry]] | 4.2, 4.4 | `domain_4.4_2_crew_registry`, `domain_4.4_4_crew_hpwki_bbksda_chain` |
| `destinations/` (4 pages) | 9.4, 13 | `domain_9.9_4_destination_entity_summaries`, `domain_13.destination_entity_summaries` |
| [[products/packages-overview]] | 6 | `domain_6` (15 packages with pricing, itineraries, inclusions, AI intelligence, route metadata) |
| `credentials/` (2 pages) | 3, 12 | `domain_3` (15 credentials), `domain_12.proof_items` (24 items) |
| `reviews/` (2 pages) | 10 | `domain_10_review_registry` |
| [[content/brand-voice]] (§voice-invariants) | 2.4 | `domain_2.2_4_voice_invariants` |
| [[content/faq-master]] | 6.5 | `domain_6.6_5_faq_logic` (20 unique FAQs across 6 categories) |
| [[content/aeo-claims]] | 2.3, 11, 12 | `domain_2.2_3_narrative_claimmap` (9 claims with NLP snippets) |

## Voice Invariants (CRITICAL — copied verbatim from SSOT §2_4)

**Price format**: `IDR X,XXX,XXX/person` — Rupiah only, comma thousand separators.

**Forbidden phrases**:
1. "Blue Fire guaranteed"
2. "mandatory health screening" (without conditional qualifier)
3. "100% Blue Fire visible"
4. "JVTO provides police escort" (without conditional context)

**Approved Ijen language**:
1. "Ijen access rules can require a recent local health certificate"
2. "Blue Fire is a natural phenomenon subject to weather and gas activity"
3. "JVTO coordinates clinic workflow when access rules require it"
4. "Gas masks provided by JVTO"
5. "Health-certificate screening coordination for Ijen routes when current access rules require it"

See [[content/brand-voice]] §voice-invariants for enforcement examples.

## Key Numeric Facts (cite this source)

| Fact | Value | SSOT path |
|---|---|---|
| Aggregate rating | 4.8 / 5 | §10.aggregate_rating.rating_value |
| Review count | 47 | §10.aggregate_rating.review_count |
| Rating last verified | 2026-04-19 | §10.aggregate_rating.last_verified_iso |
| Canonical packages | 15 (11 Surabaya + 4 Bali) | §meta.canonical_package_count |
| Canonical routes | 50 | §meta.canonical_route_count |
| Total crew | 11 (7 guides + 4 drivers) | §4_2._meta |
| KTA-credentialed crew | 11 / 11 (KTA-G/D-2024-001 → -011) | §4_4 |
| Press articles cataloged | 4 | §3_4_press_coverage |
| Proof items in trust graph | 24 | §12.proof_items |
| NIB / TDUP | 1102230032918 | §1_1, §3_1 |
| TDUP issue date | 2023-02-11 | §3_1 |
| BBKSDA Ijen regulation | SE.1658/KSA.9/2024 | §11.entity_anchors.ijen_screening |

## Internal SSOT Contradictions (flagged for source revision)

> Self-contradiction in SSOT §meta vs §9_1 vs §13: package count recorded as 15 in metadata, 16 in homepage/AI surface blocks. Surabaya count differs (11 vs 12). [[overview]] treats 15 as canonical.

> Self-contradiction in SSOT §4_2 vs §13.team_block: crew count 11 (7+4) vs 14 (7+7). [[overview]] treats 11 as canonical.

> Stale-value drift noted in SSOT §8_5_1: 18 `page copy.tsx` backup files in Next.js codebase contain stale `ratingValue: "4.9"` and `reviewCount: "112"`. Canonical is 4.8/47. Schedule cleanup (SSOT open issue CB-1).

## Anti-Drift Rules (SSOT §12.anti_drift_checks)

1. No claim may appear as a major trust assertion unless proven in the trust graph.
2. No page may be listed as owner for a claim it does not canonically own.
3. No trust signal may be implemented in schema if the underlying proof status is deferred.
4. No support page may accumulate proof items that belong to /verify-jvto.
5. No package page may have trust_mode = `forensic-proof` — package pages are not proof-owners.
6. `health_wording_mode = conditional` must be set on all Ijen-relevant pages.
7. Proof items listed in `visible_on_pages` must not exceed owner-page proof allocation.

These rules also apply to wiki pages: any wiki content production that emits trust claims should respect anti-drift rule 6 (conditional wording for Ijen) and rule 3 (don't cite deferred-schema proofs as live).

## Content Angles This Source Unlocks

- **FAQ production**: 20 canonical FAQs ready for re-use across destinations/policies (SSOT §6_5)
- **AEO answer blocks**: 9 claim-to-NLP-snippet maps (§2_3) + 6 travel-guide extraction blocks (§7_7) + 6 policy/FAQ extraction blocks (§9, §13)
- **Schema.org generation**: Pre-built JSON-LD fragments for AggregateRating, NewsArticle, Book schemas
- **Package marketing copy**: Each of 15 packages has `_ai_summary_snippet`, `query_intents`, `unique_selling_points`, `safety_positioning`, `perfect_for`, `physicality`, `ideal_arrival`, `last_day_safe_flight` (SSOT §6_8 + §6_9)
- **Destination one-liners**: 5 destinations with `ai_summary_40w` ready (SSOT §9_4)

## Provenance Chain

`raw/JVTO_FINAL_CLEAN_SSOT.json` → this summary → all downstream wiki pages. Any factual claim in this vault not anchored in CLAUDE.md or in clearly-cited press should trace back to a path inside this JSON via the field map above.
