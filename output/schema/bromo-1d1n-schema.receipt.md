---
output_date: 2026-05-18
schema_file: bromo-1d1n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/bromo-1d1n
---

# Verification Receipt — bromo-1d1n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "1 Day Bromo Midnight Experience from Surabaya" | User brief 2026-05-18 | 2026-05-18 | None |
| `lowPrice` | `1000000` IDR (11+ pax) | User brief 2026-05-18 | 2026-05-18 | Medium — changes if pricing updated |
| `highPrice` | `1550000` IDR (2 pax) | User brief 2026-05-18 | 2026-05-18 | Medium |
| `offerCount` | `6` (min 2 pax, no solo tier) | User brief 2026-05-18 | 2026-05-18 | None |
| `priceCurrency` | `IDR` | SSOT canonical | 2026-05-18 | None |
| `duration` | `P1D` | User brief 2026-05-18 | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1 | Midnight SUB→Penanjakan→Bromo crater→SUB | User brief 2026-05-18 | 2026-05-18 | None |
| No Ijen / no health screening | Confirmed absent | User brief (Ijen: NO) | 2026-05-18 | None |
| No accommodation | Single overnight trip, no hotel | User brief 2026-05-18 | 2026-05-18 | None |
| subjectOf destinations | Mount Bromo only | User brief 2026-05-18 | 2026-05-18 | None |
| Bromo geo | lat -7.9425, lon 112.9530, Probolinggo | SSOT geo list | 2026-05-18 | None |
| NIB in provider | `1102230032918` | legal-licenses.md | 2026-05-18 | None |
| Inclusion list | Transport, crew, fees, 4WD jeep, water, T-shirt | User brief 2026-05-18 | 2026-05-18 | Low |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from user brief 2026-05-18 — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL confirmed. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
- BBKSDA SE reference — intentionally absent (non-Ijen tour).
