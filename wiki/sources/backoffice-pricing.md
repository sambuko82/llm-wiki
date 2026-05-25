---
type: source
title: Backoffice — Pricing (Template vs Realized)
last_updated: 2026-05-25
sources: [backoffice-mysql]
---

# Backoffice Pricing — Template Rate Card vs Realized Prices

Snapshot 2026-05-25. Source: `package_prices` (template) + `bookings.grand_total` (realized).
Use this to validate `wiki/finance/rate-card-*.md` against actual booking data.

- **Distinct packages with prices:** 89
- **Total price rows (`package_prices`):** 556
- **Bookings with template_package_id set:** 0

## Template price points

Top 50 by price (template, not realized).

| Package | Plan | Category | Price | Klook retail | Klook net |
|---|---|---|---:|---:|---:|
| 5 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Nature Trip from Surabaya | Reguler | 1 | 9,050,000 | 0 | 0 |
| 4 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Expedition from Bali to Surabaya | Reguler | 33 | 9,050,000 | 0 | 0 |
| 4 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Journey from Surabaya | Reguler | 1 | 8,050,000 | 0 | 0 |
| 4 Day Tumpak Sewu, Bromo & Ijen Adventure from Surabaya to Bali | Reguler | 1 | 8,050,000 | 0 | 0 |
| 4 Day Ijen, Bromo & Madakaripura Waterfall Expedition from Surabaya | Reguler | 1 | 7,550,000 | 0 | 0 |
| 3 Day Ijen, Bromo & Madakaripura Waterfall Journey from Bali to Surabaya | Reguler | 1 | 7,500,000 | 0 | 0 |
| 5D 4N SURABAYA - BROMO TOUR - IJEN CRATER TOUR - PAPUMA BEACH - TUMPAK SEWU | Reguler | 1 | 7,400,000 | 0 | 0 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 27 | 7,050,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 27 | 7,050,000 | 0 | 0 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 28 | 6,850,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 28 | 6,850,000 | 0 | 0 |
| 4D3N Mount Bromo, Ijen Crater & Surabaya Night Market from Surabaya | Reguler | 33 | 6,715,000 | 8,393,750 | 6,715,000 |
| 4D3N Ijen Crater, Papuma Beach, Tumpak Sewu Waterfal & Mount Bromo from Surabaya | Reguler | 33 | 6,675,000 | 8,343,750 | 6,675,000 |
| 4D3N Ijen Crater, Papuma Beach, Tumpak Sewu Waterfal & Mount Bromo from Surabaya | Reguler | 1 | 6,675,000 | 8,343,750 | 6,675,000 |
| 4D3N Ijen Crater, Papuma Beach, Tumpak Sewu Waterfal & Mount Bromo from Surabaya | Reguler | 1 | 6,675,000 | 8,343,750 | 6,675,000 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 29 | 6,650,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 29 | 6,650,000 | 0 | 0 |
| Yogyakarta Heritage Tour: 4D 3N Yogyakarta - Prambanan Temple - Punthuk Setumbu Hill - Sultan Palace | Reguler | 1 | 6,550,000 | 0 | 0 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 30 | 6,350,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 30 | 6,350,000 | 0 | 0 |
| 3 Day Bromo, Madakaripura Waterfall & Ijen Overland from Surabaya to Bali | Reguler | 1 | 6,300,000 | 0 | 0 |
| 3 Day Ijen, Bromo & Madakaripura Waterfall Discovery from Surabaya | Reguler | 1 | 6,300,000 | 0 | 0 |
| 3 Day Bromo & Ijen Volcano Trip from Surabaya | Reguler | 1 | 6,300,000 | 0 | 0 |
| Explore Java's Hidden Gems: 6D 5N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 27 | 6,050,000 | 0 | 0 |
| 6 Day Ijen, Papuma Beach, Tumpak Sewu, Bromo & Malang City Discovery from Surabaya | Reguler | 27 | 6,050,000 | 0 | 0 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 31 | 6,050,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 31 | 6,050,000 | 0 | 0 |
| 4D 3N SURABAYA IJEN PAPUMA BEACH TUMPAK SEWU BROMO | Reguler | 1 | 6,035,000 | 0 | 0 |
| 4D 3N SURABAYA IJEN MT BROMO MADAKARIPURA FALL | Reguler | 1 | 6,035,000 | 0 | 0 |
| The Grand Java Expedition: 7D 6N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 32 | 5,850,000 | 0 | 0 |
| Ultimate Indonesian Experience: 7D 6N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 32 | 5,850,000 | 0 | 0 |
| 6D 5N SURABYA -IJEN - TUMPAK SEWU FALL - MALANG CITY TOUR - BROMO PRIVATE TOUR | Reguler | 11 | 5,825,000 | 0 | 0 |
| All-Inclusive Java Holiday: 5D 4N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 27 | 5,750,000 | 0 | 0 |
| Java's Land & Sea Exploration: 5D 4N Surabaya - Bangsring Underwater - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 27 | 5,750,000 | 0 | 0 |
| Explore Java's Hidden Gems: 6D 5N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 28 | 5,750,000 | 0 | 0 |
| 6 Day Ijen, Papuma Beach, Tumpak Sewu, Bromo & Malang City Discovery from Surabaya | Reguler | 28 | 5,750,000 | 0 | 0 |
| 6D 5N Surabaya - Ijen - Tumpak Sewu - Malang City Tour - Bromo | Reguler | 11 | 5,550,000 | 0 | 0 |
| All-Inclusive Java Holiday: 5D 4N Surabaya - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo - Malang City | Reguler | 28 | 5,550,000 | 0 | 0 |
| Java's Land & Sea Exploration: 5D 4N Surabaya - Bangsring Underwater - Mount Ijen - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 28 | 5,550,000 | 0 | 0 |
| Explore Java's Hidden Gems: 6D 5N Surabaya - Mount Ijen - Coffee & Cocoa Science Technopark - Papuma Beach - Tumpak Sewu Waterfall - Mount Bromo | Reguler | 29 | 5,550,000 | 0 | 0 |
| 6 Day Ijen, Papuma Beach, Tumpak Sewu, Bromo & Malang City Discovery from Surabaya | Reguler | 29 | 5,550,000 | 0 | 0 |
| 5D 4N  SURABAYA -  IJEN - BROMO - MALANG - CITY TOUR REG | Reguler | 1 | 5,510,000 | 0 | 0 |
| 5D 4N SURABAYA - IJEN - BROMO - MALANG - TUMPAKSEWU FALL REG | Reguler | 1 | 5,510,000 | 0 | 0 |
| 5D 4N  SURABAYA -  IJEN - BROMO - MALANG & SURABAYA CITY TOUR  REG | Reguler | 1 | 5,510,000 | 0 | 0 |
| 5D 4N  SURABAYA -  IJEN - TUMPAK SEWU - BROMO    REG | Reguler | 1 | 5,510,000 | 0 | 0 |
| 3D2N Mount Bromo, Madakaripura Waterfall & Ijen Crater Tour from Surabaya | Reguler | 33 | 5,460,000 | 6,825,000 | 5,460,000 |
| 3D2N Mount Bromo, Madakaripura Waterfall & Ijen Crater Tour from Surabaya | Reguler | 1 | 5,460,000 | 6,825,000 | 5,460,000 |
| 5 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Discovery from Bali to Surabaya | Reguler | 27 | 5,450,000 | 0 | 0 |
| 3D2N Mount Bromo, Madakaripura Waterfall & Ijen Crater Tour from Surabaya | Reguler | 1 | 5,310,000 | 6,825,000 | 5,460,000 |
| 5 Day Ijen, Papuma Beach, Tumpak Sewu & Bromo Discovery from Bali to Surabaya | Reguler | 28 | 5,250,000 | 0 | 0 |

## Realized prices per template package (top 30 by volume)

| Package id | Bookings | Avg total | Avg per-pax | Min per-pax | Max per-pax |
|---|---:|---:|---:|---:|---:|

## Validation hook

When updating `wiki/finance/rate-card-package.md`, cross-check that:
1. Each template price in this table has a matching entry in the rate card.
2. Realized per-pax averages fall within ±15% of the rate card price (otherwise discount layer or upsell is happening uncaptured).
3. Klook retail vs net spread matches the Klook commission assumption in `wiki/finance/`.

## Cross-references
- [[sources/backoffice-finance]] — aggregate revenue from these prices
- [[sources/backoffice-bookings-ops]] — package mix that drives volume
- [[finance/rate-card-package]] — manual rate card SSOT to reconcile against
