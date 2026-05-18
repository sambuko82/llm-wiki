---
output_date: 2026-05-18
schema_file: ijen-2d1n-schema.json
profile: schema (TouristTrip + AggregateRating + FAQPage)
tour_url: /tours/from-surabaya/ijen-2d1n
---

# Verification Receipt — ijen-2d1n-schema.json

| Claim | Value used | SSOT source | Last verified | Drift risk |
|---|---|---|---|---|
| Tour name | "2 Day Ijen Blue Fire Expedition from Surabaya" | User brief 2026-05-18 | 2026-05-18 | None |
| `lowPrice` | `1550000` IDR (11+ pax) | User brief 2026-05-18 | 2026-05-18 | Medium — changes if pricing updated |
| `highPrice` | `2300000` IDR (2 pax) | User brief 2026-05-18 | 2026-05-18 | Medium |
| `offerCount` | `6` (min 2 pax, no solo tier) | User brief 2026-05-18 | 2026-05-18 | None |
| `priceCurrency` | `IDR` | SSOT canonical | 2026-05-18 | None |
| `duration` | `P2D` | User brief 2026-05-18 | 2026-05-18 | None |
| `ratingValue` (TouristTrip) | `4.8` | trust-signals.md §Schema Canonical Values | 2026-05-18 | Medium |
| `reviewCount` (Trustpilot) | `51` | trust-signals.md §Schema Canonical Values | 2026-05-18 | **High** |
| Itinerary Day 1 | SUB→Bondowoso (Riverside Homestay) + health screening | User brief 2026-05-18 | 2026-05-18 | None |
| Itinerary Day 2 | Midnight Paltuding→Ijen crater (Blue Fire)→breakfast→SUB | User brief 2026-05-18 | 2026-05-18 | None |
| Hotel Night 1 | Riverside Homestay (Bondowoso) | User brief 2026-05-18 | 2026-05-18 | Low |
| BBKSDA SE reference | SE.1658/KSA.9/2024 | faq-master.md:58 | 2026-05-18 | Low |
| Health screening wording | Conditional language — "as required under BBKSDA SE.1658/KSA.9/2024" | faq-master.md (health_wording_mode:conditional) | 2026-05-18 | None |
| subjectOf destinations | Kawah Ijen only | User brief 2026-05-18 | 2026-05-18 | None |
| Ijen geo | lat -8.0580, lon 114.2420, Banyuwangi | SSOT geo list | 2026-05-18 | None |
| NIB in provider | `1102230032918` | legal-licenses.md | 2026-05-18 | None |
| Inclusion list | Transport, crew, 1 night + breakfast, fees, gas masks, trekking poles, health screening coordination, water, T-shirt | User brief 2026-05-18 | 2026-05-18 | Low |

## Drift status

- `reviewCount=51` live-verified **2026-05-18** via JVTO homepage widget. ✓
- `lowPrice`/`highPrice` from user brief 2026-05-18 — update when pricing changes.
- Next reviewCount check: before **2026-06-18**.

## Omissions (not invented)

- `image` — no tour-specific hero image URL confirmed. Add once confirmed in ssot-image-asset-map.
- `availableLanguage` — not documented in wiki. Omitted.
