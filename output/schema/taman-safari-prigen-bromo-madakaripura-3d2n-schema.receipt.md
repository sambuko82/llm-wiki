---
output_date: 2026-05-18
schema_file: taman-safari-prigen-bromo-madakaripura-3d2n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/taman-safari-prigen-bromo-madakaripura-3d2n
---

# Verification Receipt — taman-safari-prigen-bromo-madakaripura-3d2n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "3 Day Taman Safari Prigen, Bromo & Madakaripura from Surabaya" | Provided in prompt | 2026-05-18 | None |
| `lowPrice` | `3450000` IDR (11+ pax) | Provided in prompt | 2026-05-18 | Medium |
| `highPrice` | `4350000` IDR (2 pax — minimum tier, no solo) | Provided in prompt | 2026-05-18 | Medium |
| `offerCount` | `6` (no solo tier) | Provided in prompt | 2026-05-18 | None |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P3D` | Provided in prompt | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Day 1 itinerary | Surabaya → Taman Safari Prigen → overnight near Bromo | Stub provided in prompt | 2026-05-18 | **High — stub only** |
| Day 2 itinerary | Mount Bromo sunrise + private 4WD jeep | Stub provided in prompt | 2026-05-18 | **High — stub only** |
| Day 3 itinerary | Madakaripura Waterfall → return Surabaya | Stub provided in prompt | 2026-05-18 | **High — stub only** |
| Ijen / health screening | NOT included | Confirmed in prompt | 2026-05-18 | None |
| Taman Safari Prigen geo | lat -7.6500, lon 112.7167, Pasuruan | Canonical geo list | 2026-05-18 | None |
| Mount Bromo geo | lat -7.9425, lon 112.9530, Probolinggo | Canonical geo list | 2026-05-18 | None |
| Madakaripura geo | lat -7.8994, lon 113.0189, Probolinggo | Canonical geo list | 2026-05-18 | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |
| End point | Returns to Surabaya | Confirmed in prompt | 2026-05-18 | None |

## Key differences from bromo-madakaripura-ijen-3d2n

| Feature | bromo-madakaripura-ijen-3d2n | taman-safari-prigen-bromo-madakaripura-3d2n |
|---|---|---|
| Sites | Bromo + Madakaripura + Kawah Ijen | Taman Safari Prigen + Bromo + Madakaripura |
| End point | Bali (overland one-way) | Returns to Surabaya |
| Ijen / health screening | Yes (Day 2 evening) | No |
| Ferry | Yes (Ketapang→Gilimanuk) | No |
| Solo tier | Yes | No (minimum 2 pax) |
| `highPrice` | 6,300,000 (solo) | 4,350,000 (2 pax) |

## Drift status

- `reviewCount=51` live-verified **2026-05-18**. ✓
- Next check: before **2026-06-18**.

## ⚠️ Omissions (not invented)

- `image` — no tour-specific hero image URL in SSOT. Add once confirmed.
- `availableLanguage` — not documented in wiki.
- **Itinerary stub** — full day-by-day itinerary (hotel names, exact transfer timings, Day 1 overnight hotel near Bromo, Day 2 hotel allocation) has NOT yet been ingested into the wiki. The three day descriptions used in this schema are stubs provided at generation time. **Verify hotel allocations and day sequencing before publishing.** Update schema once packages-itineraries.md is updated with this tour.
