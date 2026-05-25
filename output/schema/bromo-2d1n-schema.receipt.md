---
output_date: 2026-05-25
schema_file: bromo-2d1n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/bromo-2d1n
---

# Verification Receipt — bromo-2d1n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "2 Day Bromo Sunrise Adventure from Surabaya" | User brief 2026-05-18 | 2026-05-18 | None |
| `lowPrice` | `1750000` IDR (11+ pax) | User brief 2026-05-18 | 2026-05-18 | Medium — changes if pricing updated |
| `highPrice` | `2800000` IDR (2 pax) | User brief 2026-05-18 | 2026-05-18 | Medium |
| `offerCount` | `6` (min 2 pax, no solo tier) | User brief 2026-05-18 | 2026-05-18 | None |
| `priceCurrency` | `IDR` | SSOT canonical | 2026-05-18 | None |
| `duration` | `P2D` | User brief 2026-05-18 | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1 | SUB→Joglo Kecombrang Bromo | User brief 2026-05-18 | 2026-05-18 | None |
| Itinerary Day 2 | 02:00 Penanjakan→Bromo crater→Madakaripura→SUB | User brief 2026-05-18 | 2026-05-18 | None |
| Hotel Night 1 | Joglo Kecombrang Bromo | User brief 2026-05-18 | 2026-05-18 | Low |
| No Ijen / no health screening | Confirmed absent | User brief (Ijen: NO) | 2026-05-18 | None |
| subjectOf destinations | Mount Bromo + Madakaripura | User brief 2026-05-18 | 2026-05-18 | None |
| Bromo geo | lat -7.9425, lon 112.9530, Probolinggo | SSOT geo list | 2026-05-18 | None |
| Madakaripura geo | lat -7.8994, lon 113.0189, Probolinggo | SSOT geo list | 2026-05-18 | None |
| NIB in provider | `1102230032918` | legal-licenses.md | 2026-05-18 | None |
| Inclusion list | Transport, crew, 1 night + breakfast, fees, 4WD jeep, water, T-shirt | User brief 2026-05-18 | 2026-05-18 | Low |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from user brief 2026-05-18 — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL confirmed. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
- BBKSDA SE reference — intentionally absent (non-Ijen tour).
