---
type: finance
title: Custom Tour Cost Builder
last_updated: 2026-05-25
sources: [finance-rate-cards]
---

# Custom Tour Cost Builder

*Step-by-step template for composing custom tour quotes from rate card components. All prices in IDR.*

---

## COGS Formula

```
COGS = crew_cost + vehicle_cost + accommodation_cost + activity_cost + other_cost
```

Where:
- `crew_cost` = (crew_rate x days) x number_of_crew
- `vehicle_cost` = vehicle_rate x days
- `accommodation_cost` = sum of (hotel_rate x nights) for each hotel used
- `activity_cost` = sum of per-pax items x pax + sum of per-unit items
- `other_cost` = fuel + tolls + water + T-shirts + ferry + meal allowances + transport allowance

---

## Step-by-Step Process

### Step 1: Pick Destinations
Select from: Ijen, Bromo, Tumpak Sewu, Madakaripura, Papuma, Malang attractions, Taman Safari Prigen.

### Step 2: Map the Route (Days)
Determine number of travel days. Standard patterns from existing packages:
- 1D: Single destination (Bromo only)
- 2D: Single destination with overnight (Ijen or Bromo)
- 3D: Two destinations (Ijen+Bromo+Mada, or Taman Safari combo)
- 4D: Three+ destinations (Ijen+Papuma+Tumpak+Bromo)
- 5D: Full circuit (all destinations + Malang)

### Step 3: Select Vehicle
Based on group size — see -> [[finance/rate-cards]] vehicle table.

| Pax | Vehicle | Rate/Day |
|-----|---------|----------|
| 1–3 | MPV | 250,000 |
| 3 (upgrade) | Innova | 350,000 |
| 4–9 | Hiace | 1,100,000 |
| 4–9 (premium) | Hiace Premio | 1,300,000 |
| 10–13 | Mini Bus (Elf) | 1,350,000 |
| 27–35 | Medium Bus | 1,800,000 |

### Step 4: Select Hotels
One hotel per overnight stop. Use -> [[finance/rate-cards]] accommodation table.

Typical routing:
- **Night 1 (Bondowoso/Banyuwangi)**: Doho/Baratha/Riverside (budget) or Luminor/Aston/Santika (mid)
- **Night 2 (Bromo area)**: Whizz/Artha (budget) or Joglo Kecombrang/ARTOTEL (mid-premium) or Bromo Terrace/Lava View (premium-luxury)
- **Night 3 (Lumajang/Tumpak Sewu)**: Yanto Homestay or Grand Padis
- **Night 4 (Malang)**: Whiz Prime (budget) or Atria/THE 1O1 (mid) or Shanaya (luxury)
- **Night 5 (Surabaya finish)**: Hotel 88 (budget) or Holiday Inn Express/Harris (mid-premium)

### Step 5: List Activities
Sum all entrance tickets, local guides, meals, and experience items per destination visited.

**Per-destination activity bundles (typical):**

| Destination | Items | Per-Pax Cost | Per-Unit Cost |
|-------------|-------|-------------|---------------|
| Ijen (full) | Ticket + Local Guide + Medical + Gas Mask + Certificate + Coffee | 245,000/pax | 250,000/unit (guide) |
| Bromo (standard) | Ticket + Jeep | 160,000/pax | 500,000/unit (jeep) |
| Bromo (TWT) | Ticket + Jeep TWT | 160,000/pax | 550,000/unit (jeep) |
| Tumpak Sewu | Ticket + Local Guide + Breakfast | 150,000/pax | 200,000/unit (guide) |
| Madakaripura | Ticket + Local Guide | 90,000/pax | 100,000/unit (guide) |
| Papuma | Ticket | 44,000/pax | — |

### Step 6: Add Operational Costs
Standard operational line items:

| Item | How to Calculate |
|------|-----------------|
| Fuel | 200,000 x days |
| Toll & Parking | 200,000 x cars |
| Transport Allowance | 100,000 x 1 (per trip) |
| Mineral Water | 40,000 x bottles needed |
| T-shirt | 60,000 x pax |
| Meal Allowance (crew) | 25,000 x days x crew |
| Ferry (if Bali route) | 16,000 x pax + 100,000 (guide) |
| Shuttle Airport (if needed) | 200,000 x units |
| Police Escort (if VIP) | 2,000,000 x units |

### Step 7: Sum COGS and Apply Markup

```
Total COGS = all items summed
Selling Price = COGS / (1 - margin_target)
```

---

## Markup Guidelines

Derived from 8 packages with known selling prices:

| Margin Band | Use Case | Example |
|-------------|----------|---------|
| 30–35% | Short trips (1D), high-value single destinations | 1D Bromo Sunrise: 34.9% |
| 25–30% | Standard 3D–4D multi-destination packages | 3D Ijen-Bromo-Mada: 28.8%, 4D Ijen-Bromo-Mada: 28.6% |
| 20–25% | Premium/luxury packages, long routes | 3D Taman Safari: 22.9% (Baobab Safari Resort) |
| 13–20% | Long-haul routes with ferry, maximum destinations | 5D Bali-to-Sby: 12.9% (floor — avoid going below 15%) |

**Rule of thumb**: Target 25% as the default. Adjust up for short/simple tours, down for premium hotels or Bali routes. Never price below 15% margin — the 5D Bali package at 12.9% is the observed floor and should be repriced.

---

## Worked Example: 3D2N Ijen-Bromo for 2 Pax (Budget Hotel Tier)

**Route**: Day 1 Surabaya pickup → Bondowoso (Night 1). Day 2 Ijen blue fire → Bromo area (Night 2). Day 3 Bromo sunrise → Surabaya drop-off.

### Line Items

| Category | Item | Qty | Unit Cost | Subtotal |
|----------|------|-----|-----------|----------|
| **Crew** | Driver cum Guide x 3 days | 1 | 250,000 | 750,000 |
| **Vehicle** | MPV x 3 days | 1 | 250,000 | 750,000 |
| **Accommodation** | Baratha Deluxe Double (Night 1) | 1 | 275,000 | 275,000 |
| | Doho Deluxe Double (Night 2) | 1 | 260,000 | 260,000 |
| **Activities** | Ijen Ticket x 2 pax | 2 | 75,000 | 150,000 |
| | Local Guide Ijen | 1 | 250,000 | 250,000 |
| | Medical Checkup x 2 pax | 2 | 35,000 | 70,000 |
| | Gas Mask x 2 pax | 2 | 55,000 | 110,000 |
| | Ijen Certificate x 2 pax | 2 | 35,000 | 70,000 |
| | Coffee + Indomie x 2 pax | 2 | 25,000 | 50,000 |
| | Bromo Ticket x 2 pax | 2 | 160,000 | 320,000 |
| | Bromo Jeep | 1 | 500,000 | 500,000 |
| **Operational** | Fuel x 3 days | 3 | 200,000 | 600,000 |
| | Toll & Parking | 1 | 200,000 | 200,000 |
| | Transport Allowance | 1 | 100,000 | 100,000 |
| | Mineral Water | 1 | 40,000 | 40,000 |
| | T-shirt x 2 pax | 2 | 60,000 | 120,000 |
| | Meal Allowance x 3 days | 3 | 25,000 | 75,000 |

### Totals

| Metric | Value |
|--------|-------|
| **Total COGS** | **4,690,000** |
| **COGS per pax** | **2,345,000** |
| **Selling price/pax at 25% margin** | **3,125,000** |
| **Selling price/pax at 30% margin** | **3,350,000** |
| **Profit per pax at 25%** | **780,000** |
| **Profit per pax at 30%** | **1,005,000** |
| **Total booking value (2 pax, 25%)** | **6,250,000** |

### Sensitivity

Upgrading to mid-tier hotels (Luminor 500k + Artha Cottage 467k = 967k vs. 535k budget):
- COGS increases by ~432k → 5,122,000 total
- Per-pax COGS: 2,561,000
- At 25% margin: 3,415,000/pax (+290k vs. budget tier)

---

## Template Checklist

- [ ] Destinations selected
- [ ] Route mapped (days counted)
- [ ] Vehicle selected (pax-appropriate)
- [ ] Hotel selected per night (budget/mid/premium tier)
- [ ] All activity tickets and local guides listed
- [ ] Operational costs added (fuel, tolls, water, T-shirt, meals)
- [ ] Ferry costs added (if Bali route)
- [ ] Police escort added (if VIP)
- [ ] COGS totaled
- [ ] Margin applied (25% default, adjust per guidelines)
- [ ] Final selling price rounded to nearest 50k

---

-> [[finance/rate-cards]] | -> [[finance/profit-analysis]] | -> [[finance/package-costs]] | -> [[products/packages-full-pricing]]
