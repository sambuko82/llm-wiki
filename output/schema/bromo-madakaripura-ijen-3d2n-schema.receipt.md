---
output_date: 2026-05-18
schema_file: bromo-madakaripura-ijen-3d2n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/bromo-madakaripura-ijen-3d2n
---

# Verification Receipt — bromo-madakaripura-ijen-3d2n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "3 Day Bromo, Madakaripura & Ijen Overland from Surabaya to Bali" | packages-overview.md:28 | — | None |
| `lowPrice` | `2450000` IDR (11+ pax) | packages-full-pricing.md:72 | — | Medium |
| `highPrice` | `6300000` IDR (solo) | packages-full-pricing.md:66 | — | Medium |
| `priceCurrency` | `IDR` | compilation-profiles.md §schema | — | None |
| `duration` | `P3D` | packages-itineraries.md:64 | — | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Day 1 hotel | Joglo Kecombrang Bromo | packages-itineraries.md:68 | — | Low |
| Day 2 hotel | Riverside Homestay | packages-itineraries.md:69 | — | Low |
| Itinerary Day 1–3 | SUB→Bromo side·Bromo+Madakaripura+health screening→Ijen climb+ferry→Bali | packages-itineraries.md:72–74 | — | None |
| Health screening timing | Day 2 evening (before Day 3 midnight Ijen climb) | packages-itineraries.md + Ijen-relevant flag | — | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | — | Low |
| Ferry included | Ketapang–Gilimanuk (Java→Bali) | packages-itineraries.md:74 | — | None |
| NIB in provider | `1102230032918` | legal-licenses.md | — | None |

## Key differences from ijen-bromo-madakaripura-3d2n

| Feature | ijen-bromo-madakaripura-3d2n | bromo-madakaripura-ijen-3d2n |
|---|---|---|
| Order | Ijen → Bromo → Madakaripura | Bromo → Madakaripura → Ijen |
| End point | Returns to Surabaya | Ends in Bali |
| Health screening | Day 1 evening | Day 2 evening |
| Ferry | No | Yes (Ketapang→Gilimanuk) |

## Drift status

- `reviewCount=51` live-verified **2026-05-18**. ✓
- Next check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL in SSOT. Add once confirmed.
- `availableLanguage` — not documented in wiki.
