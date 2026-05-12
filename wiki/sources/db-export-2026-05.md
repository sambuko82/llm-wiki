---
type: source
title: DB Export — Live Database Snapshot (2026-05)
last_updated: 2026-05-12
sources: [db-export-2026-05]
---

# Source: DB Export — Live Database Snapshot

## Metadata

- **File**: `raw/db_export_raw.json`
- **Status**: Live DB export — structured operational data
- **Authority**: Canonical for pricing, itineraries, crew, reviews, hotels, and knowledge base content

## 14 Data Sections

| Section | Count | Wiki impact |
|---|---|---|
| `narrative_claims` | 9 | Already in [[content/aeo-claims]] (C1–C9) — confirmed match |
| `packages` | 22 | Full registry — 15 canonical + 6 student + 1 specialty |
| `destinations` | 9 | 5 published (matches wiki); 4 unpublished (Bali, Surabaya, Malang city refs + Taman Safari) |
| `crew_members` | 14 | 7 guides + 7 drivers — 3 new confirmed vs SSOT v6.0 |
| `content_pages` | 75 | Full route inventory across 9 clusters |
| `reviews` | 157 | 44 Trustpilot + 92 Google + 21 TripAdvisor |
| `review_stats` | 3 | Platform aggregate ratings |
| `package_prices` | 143 | Full pricing for all 22 packages |
| `faqs` | 23 | Matches wiki FAQ master — 3 duplicate weather FAQs flagged |
| `package_includes` | 234 | Per-package inclusion items |
| `package_excludes` | 126 | Per-package exclusion items |
| `itinerary_days` | 99 | Day-by-day for all packages |
| `hotels` | 23 | Named hotel partners with area/facilities |
| `knowledge_bases` | 38 | Operational Q&A articles |

## Key New Data vs Prior Wiki State

### Crew (14 vs 11 KTA)

Three drivers now confirmed in DB (were soft-data in wiki):
- **Yusuf** — new driver not previously in wiki
- **Dika** — confirmed Driver (was "soft-data, probably rotation" in crew-registry)
- **Pras** — confirmed Driver (was only in Trustpilot bio note)

DB also provides self-quotes for all 14 crew. See [[people/crew-registry]] update.

### Reviews (157 vs 51)

Prior wiki state: only 51 Trustpilot reviews compiled.

DB provides:
- **Google**: 92 reviews, avg 4.90/5 — now compiled in [[reviews/google-tripadvisor-2026]]
- **TripAdvisor**: 21 reviews, avg 4.95/5 — now compiled in [[reviews/google-tripadvisor-2026]]
- **Trustpilot**: 44 reviews at 4.93 avg in DB (wiki shows 51 at 4.8 — DB and live clip differ; DB may be an older snapshot)

> Contradiction: DB `review_stats.Trustpilot` = 44 reviews / 4.93 avg. Wiki canonical (from 2026-05-09 live clip) = 51 reviews / 4.8 avg. DB snapshot predates the live clip. Treat the live clip count (51) as canonical for Trustpilot; use DB reviews as content source for individual excerpts.

### Package Pricing

Prior wiki: only 4 sample tables. DB provides complete pricing for all 22 packages → [[products/packages-full-pricing]].

### Itinerary Days (99 rows)

All day-by-day itineraries — previously zero in wiki → [[products/packages-itineraries]].

### Operational Facts (knowledge bases)

38 KB articles with new facts not previously in wiki:
- Temperature: Bromo 5–15°C, Ijen 10–15°C
- Travel times: SUB→Bromo ~3h, Ijen→SUB 5–6h, etc.
- Support hours: 08:00–22:00 WIB daily
- Ijen closure: first Friday of every month
- Trolley ojek at Ijen (extra cost, on-site)
- FOC 5% group discount at 50+ pax (not in prior wiki)
- Micro-customization policy
See [[content/operational-facts]].

## Contradictions — Resolved

1. **Cancellation policy (KB vs Policy Pack)**: ✅ RESOLVED — KB `cancellation-policy` says "50% fee for <48h" but this is an older/simplified version. [[sources/jvto-policy-pack-v6]] is canonical: 100% forfeiture for <48h cancellation. KB data ignored for policy purposes.

2. **FOC 5% discount**: ✅ CONFIRMED CANONICAL — 50+ paying pax = 3 FOC + 5% group discount on total price. Updated in [[products/packages-overview]], [[content/operational-facts]], [[sources/jvto-policy-pack-v6]], and [[content/faq-master]].

3. **Trustpilot count**: ✅ RESOLVED — Live clip (51 reviews / 4.8, verified 2026-05-09) is canonical. DB snapshot (44 / 4.93) is an older snapshot. All wiki pages use the live clip values.

## Pages Generated from This Source

- **NEW**: [[products/packages-full-pricing]] — complete pricing for 22 packages
- **NEW**: [[products/packages-itineraries]] — all 99 day itinerary entries
- **NEW**: [[reviews/google-tripadvisor-2026]] — 92 Google + 21 TripAdvisor reviews
- **NEW**: [[content/hotels]] — 23 hotel partners registry
- **NEW**: [[content/operational-facts]] — temperatures, travel times, KB facts
- **UPDATED**: [[people/crew-registry]] — 14 members, self-quotes, Yusuf/Dika/Pras confirmed

## Provenance Chain

`raw/db_export_raw.json` → this summary → all pages listed above. Pricing, itinerary, and hotel facts should trace back here when not sourced from [[sources/ssot-v6]].
