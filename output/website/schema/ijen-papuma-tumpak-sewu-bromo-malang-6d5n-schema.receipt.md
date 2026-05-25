---
output_date: 2026-05-25
schema_file: ijen-papuma-tumpak-sewu-bromo-malang-6d5n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n
---

# Verification Receipt — ijen-papuma-tumpak-sewu-bromo-malang-6d5n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "6 Day Ijen, Papuma Beach, Tumpak Sewu, Bromo & Malang City Discovery from Surabaya" | user-supplied brief 2026-05-18 | — | None |
| `lowPrice` | `4750000` IDR (11+ pax) | user-supplied brief 2026-05-18 | — | Medium — changes if pricing updated |
| `highPrice` | `6050000` IDR (2 pax — no solo tier) | user-supplied brief 2026-05-18 | — | Medium |
| `offerCount` | `6` (6 group tiers, no solo) | user-supplied brief 2026-05-18 | — | None |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P6D` | user-supplied brief 2026-05-18 | — | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1–6 | SUB→Bondowoso·Ijen·Papuma·Tumpak Sewu·Bromo·Malang→SUB | user-supplied brief 2026-05-18 | — | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | — | Low |
| FAQ health-screening | Conditional Ijen health-screening wording | faq-master.md (health_wording_mode:conditional) | — | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |
| Inclusion list | Transport, crew, 5 nights, breakfast, fees, jeep, gas masks, screening, water, T-shirt | user-supplied brief 2026-05-18 | — | Low |
| Minimum guests | 2 — no solo tier | user-supplied brief 2026-05-18 | — | None |
| subjectOf geo — Kawah Ijen | lat -8.0580, lon 114.2420 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Papuma Beach | lat -8.2167, lon 113.6167 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Tumpak Sewu | lat -8.2333, lon 112.9167 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Mount Bromo | lat -7.9425, lon 112.9530 | user-supplied SSOT 2026-05-18 | — | None |
| subjectOf geo — Malang | lat -7.9797, lon 112.6304 | user-supplied SSOT 2026-05-18 | — | None |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from user-supplied brief — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL found in SSOT. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
- Hotel names included in itinerary day descriptions per brief (Riverside Homestay, Doho Homestay, Joglo Kecombrang Bromo x2, Whiz Prime Malang, Holiday Inn Express Surabaya).
