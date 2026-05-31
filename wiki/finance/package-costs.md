---
type: finance
title: JVTO Package Cost Breakdown
last_updated: 2026-05-25
sources: [finance-rate-cards, db-export-2026-05]
owner: wiki-llm
stale_after_days: 30
---

# Package Cost Breakdown

*Per-package COGS analysis from 15 Excel spreadsheets. All prices in IDR.*

> **Note on pax count**: Each spreadsheet is configured for a specific group size. COGS/pax decreases with larger groups because fixed costs (vehicle, crew) are shared. Single-pax quotes show the worst-case per-person cost.

---

## Summary Table

| Package | Days | Pax Used | COGS Total (IDR) | COGS/Pax (IDR) | Selling/Pax (IDR) | Margin |
|---------|------|----------|-------------------|-----------------|---------------------|--------|
| 1D Bromo Midnight (Sby) | 1 | 1 | 2,420,000 | 2,420,000 | 1,550,000 ② | — ⁑ |
| 1D Surabaya Bromo Sunrise | 1 | 1 | 1,545,000 | 1,545,000 | 2,375,000 ᴷ | 34.9% |
| 2D Bromo Sunrise (Sby) | 2 | 11 | 14,790,000 | 1,344,545 | 1,750,000 ⓫ | 23.2% |
| 2D Ijen Blue Fire (Sby) | 2 | 2 | 3,115,000 | 1,557,500 | 2,300,000 ② | 32.3% |
| 3D Bromo-Mada-Ijen (Sby→Bali) | 3 | 11 | 20,248,500 | 1,840,772 | 2,450,000 ⓫ | 24.9% |
| 3D Ijen-Bromo-Mada (Sby) | 3 | 9 | 16,350,000 | 1,816,667 | 2,550,000 ⑧ | 28.8% |
| 3D Ijen-Bromo-Mada (Bali→Sby) | 3 | ? | — | — | 4,050,000 ② | — |
| 3D Taman Safari (Sby) | 3 | 2 | 6,630,000 | 3,315,000 | 4,350,000 ② | 23.8% |
| 4D Ijen-Bromo-Mada (Sby) | 4 | 4 | 11,275,000 | 2,818,750 | 3,950,000 ④ | 28.6% |
| 4D Ijen-Papuma-Tumpak-Bromo (Bali→Sby) | 4 | 1 | 7,046,000 | 7,046,000 | 9,050,000 ① | 22.1% |
| 4D Ijen-Papuma-Tumpak-Bromo (Sby) | 4 | 11 | 25,661,500 | 2,332,863 | 3,125,000 ⓫ | 25.3% |
| 4D Tumpak-Bromo-Ijen (Sby→Bali) | 4 | 2 | 6,907,000 | 3,453,500 | 4,550,000 ② | 24.1% |
| 5D Ijen-Bromo-Mada-Malang (Sby) | 5 | 11 | 33,180,000 | 3,016,363 | 3,850,000 ⓫ | 21.6% |
| 5D Ijen-Papuma-Tumpak-Bromo (Bali→Sby) | 5 | 1 | 7,836,000 | 7,836,000 | 5,450,000 ② | — ⁑ |
| 5D Ijen-Papuma-Tumpak-Bromo (Sby) | 5 | 1 | 6,831,500 | 6,831,500 | 9,050,000 ① | 24.5% |

**Legend:** ① = DB solo price, ② = DB 2-pax price, ④ = DB 4-5 pax, ⑧ = DB 8-10 pax, ⓫ = DB 11+ pax, ᴷ = Klook OTA price. ⁑ = COGS exceeds selling at this tier (see notes).

---

## Data Quality Notes

- **3D Ijen-Bromo-Mada (Bali to Sby)**: Different spreadsheet format; data not extractable. Pax count and COGS unknown.
- **Selling prices**: 8 from Excel spreadsheets, 7 filled from [[products/packages-full-pricing]] (DB export). All validated 2026-05-25.
- **OTA pricing**: The 1D Surabaya Bromo Sunrise selling price (2,375,000) is labeled "Harga Jual Klook / pax" — Klook OTA price, not direct-booking price.
- **Taman Safari discrepancy**: Excel shows 4,300,000, DB shows 4,350,000. Using DB price (current SSOT). Difference: 50k — likely a price adjustment after spreadsheet creation.
- **Negative margin flags** (⁑): Two packages show COGS > selling price at the listed tier. This happens when COGS is for 1 pax but selling is the 2-pax tier price. The 1D Bromo has 2,420,000 COGS (1 pax) but DB only lists 2-pax pricing starting at 1,550,000 — the spreadsheet likely uses a different cost structure (e.g., higher-spec vehicle). The 5D Bali has 7,836,000 COGS (1 pax) but no solo tier published; the 2-pax price (5,450,000) is for a pair where COGS/pax would be ~4M, giving ~26% margin.
- **Pax count variation**:
  - 1-pax quotes (5 packages): standalone cost — all fixed costs fall on one person.
  - 2-pax quotes (3 packages): typical couple/small-group scenario.
  - 4-pax quote (1 package): small group.
  - 9-pax quote (1 package): medium group.
  - 11-pax quotes (4 packages): large group with maximum cost-sharing benefit.

---

## Cost Scaling Pattern

Fixed costs are constant regardless of pax count. Variable costs scale linearly with pax.

**Fixed costs per tour** (do not change with group size):
- Vehicle: 250,000–1,800,000/day (depends on vehicle type)
- Crew: 200,000–275,000/day per crew member
- Fuel: 200,000/day
- Toll & Parking: 200,000/car
- Transport Allowance: 100,000/trip
- Ferry - Guide: 100,000/unit (if applicable)

**Variable costs per pax** (scale linearly):
- Entrance tickets: 44,000–160,000/pax per activity
- Medical checkup: 35,000/pax
- Gas mask: 55,000/pax
- Meals: 25,000–100,000/pax per meal
- Ferry ticket: 16,000/pax
- T-shirt: 60,000/pax
- Mineral water: 40,000/pax (bulk — per bottle, not per person)

**COGS formula**: `COGS = fixed_costs + (variable_costs_per_pax x N)`

**Per-pax COGS**: `COGS/pax = fixed_costs/N + variable_costs_per_pax`

This explains why:
- 1-pax 4D trip costs ~7M/pax (all fixed costs on one person)
- 11-pax 4D trip costs ~2.3M/pax (fixed costs spread across 11)
- The variable component is ~400k–800k/pax regardless of group size

---

## Cross-Reference

The selling prices and public-facing tier tables are in -> [[products/packages-full-pricing]]. Rate card components used to build each package are in -> [[finance/rate-cards]]. Margin analysis is in -> [[finance/profit-analysis]].

-> [[finance/rate-cards]] | -> [[finance/profit-analysis]] | -> [[finance/custom-tour-builder]] | -> [[products/packages-full-pricing]]
