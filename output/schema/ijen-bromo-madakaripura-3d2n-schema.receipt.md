---
output_date: 2026-05-25
schema_file: ijen-bromo-madakaripura-3d2n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/ijen-bromo-madakaripura-3d2n
---

# Verification Receipt — ijen-bromo-madakaripura-3d2n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "3 Day Ijen, Bromo & Madakaripura Waterfall Discovery from Surabaya" | packages-overview.md:27 | — | None |
| `lowPrice` | `2450000` IDR (11+ pax) | packages-full-pricing.md:60 | — | Medium — changes if pricing updated |
| `highPrice` | `6300000` IDR (solo) | packages-full-pricing.md:54 | — | Medium |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P3D` | packages-itineraries.md:50 | — | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1–3 | SUB→Bondowoso·Ijen·Bromo+Madakaripura→SUB | packages-itineraries.md:58–60 | — | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | — | Low |
| FAQ Q6+Q7 | Conditional Ijen health-screening wording | faq-master.md (health_wording_mode:conditional) | — | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |
| Inclusion list | Transport, crew, fees, jeep, gas masks, screening, water, breakfast, T-shirt | packages-overview.md:113–126 | — | Low |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from packages-full-pricing.md — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL found in SSOT. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
- Hotel names for accommodation — in packages-itineraries.md but not mapped to this receipt; add to schema if needed.
