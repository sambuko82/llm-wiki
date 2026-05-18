---
output_date: 2026-05-18
schema_file: ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n
---

# Verification Receipt — ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "5 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Nature Trip from Surabaya" | user-supplied brief 2026-05-18 | — | None |
| `lowPrice` | `3650000` IDR (11+ pax) | user-supplied brief 2026-05-18 | — | Medium — changes if pricing updated |
| `highPrice` | `9050000` IDR (solo) | user-supplied brief 2026-05-18 | — | Medium |
| `offerCount` | `7` (solo + 6 group tiers) | user-supplied brief 2026-05-18 | — | None |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P5D` | user-supplied brief 2026-05-18 | — | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1–5 | SUB→Bondowoso·Ijen·Papuma·Tumpak Sewu·Bromo→SUB | user-supplied brief 2026-05-18 | — | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | — | Low |
| FAQ health-screening | Conditional Ijen health-screening wording | faq-master.md (health_wording_mode:conditional) | — | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |
| Inclusion list | Transport, crew, 4 nights, breakfast, fees, jeep, gas masks, screening, water, T-shirt | user-supplied brief 2026-05-18 | — | Low |
| subjectOf geo — Kawah Ijen | lat -8.0580, lon 114.2420 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Papuma Beach | lat -8.2167, lon 113.6167 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Tumpak Sewu | lat -8.2333, lon 112.9167 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Mount Bromo | lat -7.9425, lon 112.9530 | user-supplied SSOT 2026-05-18 | — | None |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from user-supplied brief — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL found in SSOT. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
- Hotel names included in itinerary day descriptions per brief (Riverside Homestay, Doho Homestay, Joglo Kecombrang Bromo, Holiday Inn Express Surabaya).
