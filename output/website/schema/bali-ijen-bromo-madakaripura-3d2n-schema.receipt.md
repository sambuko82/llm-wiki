---
output_date: 2026-05-25
schema_file: bali-ijen-bromo-madakaripura-3d2n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-bali/ijen-bromo-madakaripura-3d2n
---

# Verification Receipt — bali-ijen-bromo-madakaripura-3d2n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "3 Day Ijen, Bromo & Madakaripura Waterfall Journey from Bali to Surabaya" | pre-loaded SSOT | 2026-05-18 | None |
| `lowPrice` | `2850000` IDR (11+ pax) | pre-loaded SSOT | 2026-05-18 | Medium |
| `highPrice` | `7500000` IDR (solo) | pre-loaded SSOT | 2026-05-18 | Medium |
| `priceCurrency` | `IDR` | pre-loaded SSOT | 2026-05-18 | None |
| `offerCount` | `7` | pre-loaded SSOT (7 group-size tiers) | 2026-05-18 | None |
| `duration` | `P3D` | pre-loaded SSOT | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | pre-loaded SSOT §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | pre-loaded SSOT §Schema Canonical Values | 2026-05-18 | **High** |
| Day 1 hotel | Luminor Hotel Banyuwangi | pre-loaded SSOT | 2026-05-18 | Low |
| Day 2 hotel | Joglo Kecombrang Bromo | pre-loaded SSOT | 2026-05-18 | Low |
| Itinerary Day 1–3 | Bali+ferry→Banyuwangi+screening→Ijen climb→transfer→Bromo sunrise+Madakaripura→SUB | pre-loaded SSOT | 2026-05-18 | None |
| Health screening timing | Day 1 evening (before Day 2 midnight Ijen climb) | pre-loaded SSOT | 2026-05-18 | None |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | pre-loaded SSOT | 2026-05-18 | Low |
| Ferry included | Gilimanuk–Ketapang (Bali→Java) | pre-loaded SSOT | 2026-05-18 | None |
| NIB in provider | `1102230032918` | pre-loaded SSOT | 2026-05-18 | None |
| End point | Surabaya (one-way Bali→SUB) | pre-loaded SSOT | 2026-05-18 | None |

## Key differences from bromo-madakaripura-ijen-3d2n (SUB→Bali)

| Feature | bali-ijen-bromo-madakaripura-3d2n | bromo-madakaripura-ijen-3d2n |
|---|---|---|
| Start point | Bali | Surabaya |
| End point | Surabaya | Bali |
| Order | Ijen → Bromo → Madakaripura | Bromo → Madakaripura → Ijen |
| Health screening | Day 1 evening | Day 2 evening |
| Ferry direction | Gilimanuk→Ketapang (Bali→Java) | Ketapang→Gilimanuk (Java→Bali) |
| highPrice | 7,500,000 IDR | 6,300,000 IDR |

## Drift status

- `reviewCount=51` live-verified **2026-05-18**. ✓
- Next check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL in SSOT. Add once confirmed.
- `availableLanguage` — not documented in wiki.
