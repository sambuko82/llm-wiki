---
type: product
title: JVTO Package Pricing — Full Tables (All 22 Packages)
last_updated: 2026-05-25
sources: [db-export-2026-05, backoffice-mysql]
owner: wiki-llm
stale_after_days: 60
---

# JVTO Package Pricing — Full Tables

*Sourced from [[sources/db-export-2026-05]] (live DB export) and -> [[sources/backoffice-pricing]] (live MySQL extraction). All prices in IDR/person. Price format: `IDR X,XXX,XXX/person`.*

> **Realized vs template:** prices below are the template rate card. Actual booking averages per `template_package_id` live in -> [[sources/backoffice-pricing]] §"Realized prices per template package". Discounts, upsells, and channel-specific rates surface there.

**Canonical packages** = 15 standard routes (Surabaya + Bali origin). **Student packages** = 6 ISIC-eligible routes at reduced rates. **Specialty** = Taman Safari add-on package.

---

## Canonical — Surabaya Origin

### `bromo-1d1n` — 1D1N Bromo Midnight (no Ijen)

| Pax | IDR/person |
|---|---|
| 2 | 1,550,000 |
| 3–4 | 1,400,000 |
| 5–7 | 1,250,000 |
| 8–10 | 1,050,000 |
| 11+ | 1,000,000 |

### `bromo-2d1n` — 2D1N Bromo Sunrise + Madakaripura (no Ijen)

| Pax | IDR/person |
|---|---|
| 2 | 2,800,000 |
| 3 | 2,550,000 |
| 4–5 | 2,350,000 |
| 6–7 | 2,150,000 |
| 8–10 | 1,950,000 |
| 11+ | 1,750,000 |

### `ijen-2d1n` — 2D1N Ijen Blue Fire Expedition

| Pax | IDR/person |
|---|---|
| 2 | 2,300,000 |
| 3 | 2,200,000 |
| 4–5 | 2,050,000 |
| 6–7 | 1,850,000 |
| 8–10 | 1,650,000 |
| 11+ | 1,550,000 |

### `ijen-bromo-madakaripura-3d2n` — 3D2N Ijen + Bromo + Madakaripura (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 6,300,000 |
| 2 | 3,570,000 |
| 3 | 3,275,000 |
| 4–5 | 3,050,000 |
| 6–7 | 2,850,000 |
| 8–10 | 2,550,000 |
| 11+ | 2,450,000 |

### `bromo-madakaripura-ijen-3d2n` — 3D2N Bromo + Madakaripura + Ijen (SUB→BALI)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 6,300,000 |
| 2 | 3,570,000 |
| 3 | 3,275,000 |
| 4–5 | 3,050,000 |
| 6–7 | 2,850,000 |
| 8–10 | 2,550,000 |
| 11+ | 2,450,000 |

### `ijen-bromo-madakaripura-4d3n` — 4D3N Ijen + Bromo + Madakaripura Expedition (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 7,550,000 |
| 2 | 4,450,000 |
| 3 | 4,250,000 |
| 4–5 | 3,950,000 |
| 6–7 | 3,650,000 |
| 8–10 | 3,175,000 |
| 11+ | 3,025,000 |

### `ijen-papuma-tumpak-sewu-bromo-4d3n` — 4D3N Ijen + Papuma + Tumpak Sewu + Bromo (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 8,050,000 |
| 2 | 4,550,000 |
| 3 | 4,350,000 |
| 4–5 | 4,050,000 |
| 6–7 | 3,750,000 |
| 8–10 | 3,275,000 |
| 11+ | 3,125,000 |

### `tumpak-sewu-bromo-ijen-4d3n` — 4D3N Tumpak Sewu + Bromo + Ijen (SUB→BALI)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 8,050,000 |
| 2 | 4,550,000 |
| 3 | 4,350,000 |
| 4–5 | 4,050,000 |
| 6–7 | 3,750,000 |
| 8–10 | 3,275,000 |
| 11+ | 3,125,000 |

### `ijen-papuma-tumpak-sewu-bromo-5d4n` — 5D4N Full East Java Circuit (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 9,050,000 |
| 2 | 5,050,000 |
| 3 | 4,850,000 |
| 4–5 | 4,550,000 |
| 6–7 | 4,250,000 |
| 8–10 | 3,850,000 |
| 11+ | 3,650,000 |

### `ijen-bromo-madakaripura-malang-5d4n` — 5D4N Ijen + Bromo + Madakaripura + Malang (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 2 | 5,250,000 |
| 3 | 5,050,000 |
| 4–5 | 4,750,000 |
| 6–7 | 4,450,000 |
| 8–10 | 4,050,000 |
| 11+ | 3,850,000 |

### `ijen-papuma-tumpak-sewu-bromo-malang-6d5n` — 6D5N Grand East Java (SUB→SUB)

| Pax | IDR/person |
|---|---|
| 2 | 6,050,000 |
| 3 | 5,750,000 |
| 4–5 | 5,550,000 |
| 6–7 | 5,250,000 |
| 8–10 | 4,950,000 |
| 11+ | 4,750,000 |

---

## Canonical — Bali Origin

### `tours/from-bali/bromo-ijen-3d2n` — 3D2N Bromo + Ijen (BALI→BALI)

| Pax | IDR/person |
|---|---|
| 2 | 4,050,000 |
| 3 | 3,800,000 |
| 4–5 | 3,550,000 |
| 6–7 | 3,350,000 |
| 8–10 | 3,050,000 |
| 11+ | 2,850,000 |

### `tours/from-bali/ijen-bromo-madakaripura-3d2n` — 3D2N Ijen + Bromo + Madakaripura (BALI→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 7,500,000 |
| 2 | 4,050,000 |
| 3 | 3,800,000 |
| 4–5 | 3,550,000 |
| 6–7 | 3,350,000 |
| 8–10 | 3,050,000 |
| 11+ | 2,850,000 |

### `tours/from-bali/ijen-papuma-tumpak-sewu-bromo-4d3n` — 4D3N Full Circuit (BALI→SUB)

| Pax | IDR/person |
|---|---|
| 1 (solo) | 9,050,000 |
| 2 | 4,900,000 |
| 3 | 4,700,000 |
| 4–5 | 4,400,000 |
| 6–7 | 4,100,000 |
| 8–10 | 3,625,000 |
| 11+ | 3,475,000 |

### `tours/from-bali/ijen-papuma-tumpak-sewu-bromo-5d4n` — 5D4N Full Circuit Extended (BALI→SUB)

| Pax | IDR/person |
|---|---|
| 2 | 5,450,000 |
| 3 | 5,250,000 |
| 4–5 | 4,950,000 |
| 6–7 | 4,650,000 |
| 8–10 | 4,250,000 |
| 11+ | 4,050,000 |

---

## Student Packages (ISIC-eligible)

*Available via `/tours/student-package/*` routes. Verified ISIC card required. Same safety standards and inclusions as canonical packages — pricing adjusted for student accessibility.*

### `tours/student-package/bromo-ijen-3d2n` and `bromo-ijen-3d2n-to-bali`

| Pax | IDR/person |
|---|---|
| 1 (solo) | 5,400,000 |
| 2 | 3,050,000 |
| 3 | 2,850,000 |
| 4–5 | 2,650,000 |
| 6–7 | 2,450,000 |
| 8–10 | 2,250,000 |
| 11+ | 2,050,000 |

### `tours/student-package/ijen-bromo-3d2n` (Bali origin)

| Pax | IDR/person |
|---|---|
| 2 | 2,900,000 |
| 3 | 2,700,000 |
| 4–5 | 2,500,000 |
| 6–7 | 2,300,000 |
| 8–10 | 2,100,000 |
| 11+ | 1,900,000 |

### `tours/student-package/ijen-bromo-madakaripura-night-market-4d3n`

| Pax | IDR/person |
|---|---|
| 1 (solo) | 6,500,000 |
| 2 | 3,700,000 |
| 3 | 3,500,000 |
| 4–5 | 3,300,000 |
| 6–7 | 3,100,000 |
| 8–10 | 2,900,000 |
| 11+ | 2,700,000 |

### `tours/student-package/ijen-papuma-tumpak-sewu-bromo-4d3n`

| Pax | IDR/person |
|---|---|
| 1 (solo) | 7,150,000 |
| 2 | 4,100,000 |
| 3 | 3,900,000 |
| 4–5 | 3,600,000 |
| 6–7 | 3,350,000 |
| 8–10 | 3,000,000 |
| 11+ | 2,900,000 |

### `tours/student-package/ijen-papuma-tumpak-sewu-bromo-5d4n`

| Pax | IDR/person |
|---|---|
| 2 | 4,050,000 |
| 3 | 3,850,000 |
| 4–5 | 3,650,000 |
| 6–7 | 3,450,000 |
| 8–10 | 3,250,000 |
| 11+ | 3,050,000 |

---

## Specialty Package

### `taman-safari-prigen-bromo-madakaripura-3d2n`

| Pax | IDR/person |
|---|---|
| 2 | 4,350,000 |
| 3 | 4,150,000 |
| 4–5 | 3,950,000 |
| 6–7 | 3,750,000 |
| 8–10 | 3,550,000 |
| 11+ | 3,450,000 |

---

## Pricing Notes

- All prices per person in IDR
- Solo supplement applies for select packages (1 pax tier listed where available)
- Bali-origin packages include ferry crossing (Gilimanuk–Ketapang) in base price
- Student pricing requires valid ISIC card — verified via Alive Verify API at checkout
- Prices do not include: flights, travel insurance, personal expenses, tips

See [[products/packages-overview]] for inclusions/exclusions per package. Full itineraries: [[products/packages-itineraries]].

-> [[products/packages-overview]] | -> [[products/packages-itineraries]] | -> [[sources/db-export-2026-05]]
