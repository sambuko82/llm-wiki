---
output_date: 2026-05-18
schema_file: bali-bromo-ijen-3d2n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-bali/bromo-ijen-3d2n
---

# Verification Receipt — bali-bromo-ijen-3d2n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "3 Day Bromo & Ijen Volcano Discovery from Bali" | Provided in prompt | 2026-05-18 | None |
| `lowPrice` | `2850000` IDR (11+ pax) | Provided in prompt | 2026-05-18 | Medium |
| `highPrice` | `4050000` IDR (2 pax — minimum tier, no solo) | Provided in prompt | 2026-05-18 | Medium |
| `offerCount` | `6` (no solo tier) | Provided in prompt | 2026-05-18 | None |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P3D` | Provided in prompt | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Day 1 hotel | Joglo Kecombrang Bromo | Provided in prompt | 2026-05-18 | Low |
| Day 2 hotel | Riverside Homestay | Provided in prompt | 2026-05-18 | Low |
| Day 1 itinerary | Bali → Gilimanuk–Ketapang ferry → Bromo staging | Provided in prompt | 2026-05-18 | None |
| Day 2 itinerary | Bromo sunrise (4WD jeep) → Madakaripura → Bondowoso → health screening | Provided in prompt | 2026-05-18 | None |
| Day 3 itinerary | Midnight Ijen → descent → Ketapang–Gilimanuk ferry → Bali | Provided in prompt | 2026-05-18 | None |
| Health screening timing | Day 2 evening (before Day 3 midnight Ijen climb) | Provided in prompt | 2026-05-18 | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | — | Low |
| Ferry (outbound) | Gilimanuk (Bali) → Ketapang (Java) — Day 1 | Provided in prompt | 2026-05-18 | None |
| Ferry (return) | Ketapang (Java) → Gilimanuk (Bali) — Day 3 | Provided in prompt | 2026-05-18 | None |
| Start and end point | Bali (Bali→Bali loop) | Confirmed in prompt | 2026-05-18 | None |
| Mount Bromo geo | lat -7.9425, lon 112.9530, Probolinggo | Canonical geo list | 2026-05-18 | None |
| Madakaripura geo | lat -7.8994, lon 113.0189, Probolinggo | Canonical geo list | 2026-05-18 | None |
| Kawah Ijen geo | lat -8.0580, lon 114.2420, Banyuwangi | Canonical geo list | 2026-05-18 | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |

## Key differences from bromo-madakaripura-ijen-3d2n (SUB→Bali)

| Feature | bromo-madakaripura-ijen-3d2n | bali-bromo-ijen-3d2n |
|---|---|---|
| Start point | Surabaya | Bali |
| End point | Bali (one-way overland) | Bali (loop — returns to Bali) |
| Ferry crossings | 1 (Ketapang→Gilimanuk) | 2 (Gilimanuk→Ketapang + Ketapang→Gilimanuk) |
| Solo tier | Yes (7 tiers) | No (6 tiers, minimum 2 pax) |
| `highPrice` | 6,300,000 (solo) | 4,050,000 (2 pax) |
| Day 1 activity | Transfer SUB→Bromo side | Transfer Bali→Java via ferry + Bromo staging |

## Drift status

- `reviewCount=51` live-verified **2026-05-18**. ✓
- Next check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL in SSOT. Add once confirmed.
- `availableLanguage` — not documented in wiki.
- Bali pick-up zone(s) — specific Bali areas served (Kuta, Seminyak, Ubud, etc.) not specified in source. Add to FAQ once documented.
