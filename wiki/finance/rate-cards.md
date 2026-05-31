---
type: finance
title: JVTO Rate Cards — Cost Component Reference
last_updated: 2026-05-26
sources: [finance-rate-cards, backoffice-mysql]
owner: wiki-llm
stale_after_days: 30
---

# Rate Cards

*Consolidated cost components for all JVTO tour packages. All prices in IDR. Source: `raw/FINANCE/rate_cards/*.json` (manual SSOT, see -> [[sources/finance-rate-cards]]) — reconciled against live MySQL via -> [[sources/backoffice-pricing]] and -> [[sources/backoffice-finance]].*

> **Validation hook:** when a rate here disagrees with realized booking averages in [[sources/backoffice-pricing]], flag for review. The backoffice CSVs are the source of truth for "what actually happened"; this page is the source of truth for "what we quote."

---

## Crew Roles

| Role | Rate/Day (IDR) |
|------|----------------|
| Escort Guide (Senior) | 275,000 |
| Escort Guide (Junior) | 250,000 |
| Driver cum Guide | 250,000 |
| Escort Guide | 250,000 |
| Driver Only | 200,000 |

Standard deployment: 1 driver + 1 escort guide per vehicle. Senior guide assigned to premium/complex itineraries (multi-day, Ijen+Bromo combos). Driver cum Guide used for budget 1-day packages where a single crew member covers both roles.

---

## Vehicles

| Type | Min Pax | Max Pax | Rate/Day (IDR) |
|------|---------|---------|----------------|
| MPV | 1 | 3 | 250,000 |
| Innova | 3 | 3 | 350,000 |
| Hiace | 4 | 9 | 1,100,000 |
| Hiace Premio | 4 | 9 | 1,300,000 |
| Mini Bus (Elf) | 10 | 13 | 1,350,000 |
| Medium Bus | 27 | 35 | 1,800,000 |

Vehicle allocation follows the policy in -> [[products/packages-overview]]: MPV for 1-3 pax, Innova upgrade available, Hiace/Premio for 4-9 pax groups, Mini Bus for student/large groups, Medium Bus for 27+ pax.

---

## Activities

### Bromo

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Bromo Ticket | /pax | 160,000 | Widhi Bromo |
| Bromo Jeep | /unit | 500,000 | Widhi Bromo |
| Bromo Jeep TWT | /unit | 550,000 | Widhi Bromo |
| Bromo Jeep Student | /unit | 450,000 | Widhi Bromo |
| Dinner - Bromo Escapes | /pax | 100,000 | — |
| Breakfast Kecombrang | /pax | 50,000 | — |

### Ijen

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Ijen Ticket | /pax | 75,000 | Ijen Ticket |
| Local Guide (Ijen) | /unit | 250,000 | — |
| Medical Checkup | /pax | 35,000 | — |
| Gas Mask | /pax | 55,000 | — |
| Ijen Certificate | /pax | 35,000 | — |
| Coffee + Indomie | /pax | 25,000 | — |
| Kapas Biru | /pax | 20,000 | — |

### Tumpak Sewu

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Tumpak Sewu - Ticket | /pax | 100,000 | — |
| Tumpak Sewu - Ticket TWT | /pax | 150,000 | — |
| Tumpak Sewu - Local Guide | /unit | 200,000 | — |
| Tumpak Sewu - Breakfast | /pax | 50,000 | — |
| Tumpak Sewu - Lunch | /pax | 50,000 | — |

### Madakaripura

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Madakaripura Ticket | /pax | 90,000 | — |
| Madakaripura Local Guide | /unit | 100,000 | — |

### Papuma

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Papuma Beach Ticket | /pax | 44,000 | — |

### Malang

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Santerra, Goa Pinus, Taman Langit, Apple Garden | /pax | 175,000 | — |
| Jodipan Ticket | /pax | 10,000 | — |
| Taman Langit Ticket | /pax | 35,000 | — |

### General / Multi-destination

| Item | Unit | Price (IDR) | Vendor |
|------|------|-------------|--------|
| Lunch - Riverside | /pax | 65,000 | — |
| Dinner - Riverside | /pax | 65,000 | — |
| Lunch - Baratha | /pax | 60,000 | — |

---

## Other Operational Costs

| Item | Unit | Price (IDR) |
|------|------|-------------|
| Transport Allowance | /trip | 100,000 |
| Mineral Water | /bottle | 40,000 |
| T-shirt | /piece | 60,000 |
| Toll & Parking | /car | 200,000 |
| Fuel | /day | 200,000 |
| Ferry Ticket | /pax | 16,000 |
| Ferry - Guide | /unit | 100,000 |
| Meal Allowance | /day | 25,000 |
| Shuttle Airport | /unit | 200,000 |
| Police Escort | /unit | 2,000,000 |

Police Escort is the highest single-item cost at 2,000,000 IDR per engagement. Used for VIP/large-group transfers. -> [[credentials/police-integration]]

---

## Accommodation

| Hotel | Location | Rate Range (IDR) | Room Types |
|-------|----------|------------------|------------|
| Doho Homestay | Bondowoso | 150,000 – 440,000 | Superior, Deluxe, Executive, Emerald, Platinum, Family |
| Baratha Hotel and Resto | Bondowoso | 250,000 – 625,000 | Superior, Deluxe, Family, Apartment |
| Riverside Homestay | Bondowoso | 200,000 – 562,500 | Deluxe, Executive, Emerald, Platinum, Family |
| Luminor Hotel | Banyuwangi | 250,000 – 500,000 | Deluxe, Extra Bed |
| Aston Banyuwangi | Banyuwangi | 525,000 – 625,000 | Double, Premiere |
| Hotel Santika Banyuwangi | Banyuwangi | 300,000 – 990,000 | Superior, Deluxe, Executive Suite |
| Whizz Bromo | Bromo | 200,000 – 550,000 | Capsule, Superior |
| Artha Cottage | Bromo | 467,500 – 595,000 | Double, Twin, VIP Double |
| Joglo Kecombrang Bromo | Bromo | 300,000 – 950,000 | Double, Twin, Family |
| ARTOTEL Cabin Bromo | Bromo | 1,150,000 | Cabin King, Cabin Twin |
| Bromo Terrace | Bromo | 300,000 – 1,350,000 | Double, Twin, Hillview |
| Lava View Lodge | Bromo | 250,000 – 2,762,500 | Superior, Deluxe, Family, Suite, Cottages (WD/WE tiers) |
| Manis Ae Cabin & Resto Bromo | Bromo | 350,000 – 2,220,000 | Single Cabin, Family Cabin (WD/WE/HS tiers) |
| Yanto Homestay Anugerah | Lumajang | 350,000 – 550,000 | Deluxe, Cottage |
| Grand Padis Hotel | Lumajang | 300,000 – 735,000 | Superior, Deluxe, Family |
| Baobab Safari Resort | Prigen | 500,000 – 4,700,000 | Deluxe Hill/Safari View, Premium, Junior Suite |
| Whiz Prime Malang | Malang | 200,000 – 517,000 | Superior, Deluxe (B&B / room-only options) |
| Atria Malang | Malang | 350,000 – 610,000 | Double, Twin, Connecting |
| THE 1O1 Malang OJ | Malang | 300,000 – 800,000 | Deluxe (WD/WE tiers) |
| Shanaya Resort Malang | Malang | 695,000 – 5,200,000 | 2-Bed, 3-Bed, Singhasari Riverview, Royal Villa |
| Hotel 88 Kedungsari | Surabaya | 330,000 | Deluxe |
| Holiday Inn Express Surabaya | Surabaya | 350,000 – 550,000 | Double, Twin |
| Harris Hotel Satelit | Surabaya | 350,000 – 1,420,000 | Double, Twin, Connecting |

**Tier summary:**
- **Budget** (150k–450k): Doho, Baratha, Riverside, Whizz Bromo, Hotel 88, Whiz Prime
- **Mid** (450k–750k): Grand Padis, Luminor, Aston, Artha Cottage, Joglo Kecombrang, Holiday Inn Express, Atria
- **Premium** (750k–1.5M): ARTOTEL, Bromo Terrace, Harris, Hotel Santika, THE 1O1, Manis Ae
- **Luxury** (1.5M+): Lava View Lodge (suites/cottages), Baobab Safari Resort, Shanaya Resort

Some hotels have weekday/weekend/high-season tiered pricing (Lava View, Manis Ae, THE 1O1, Shanaya). See raw JSON for full room-level detail.

---

## OTA Channel Pricing — Klook

Source: [[sources/backoffice-pricing]] — 5 packages with Klook pricing in `package_prices` table.

**Commission model**: Klook retails at **template price × 1.25** (25% markup). JVTO receives the full template price (Klook net = template).

| Package | Template (IDR) | Klook Retail (IDR) | Klook Net (IDR) | Markup |
|---------|---------------|-------------------|----------------|--------|
| 3D2N Bromo-Mada-Ijen (Sby) | 5,460,000 | 6,825,000 | 5,460,000 | 25.0% |
| 4D3N Ijen-Papuma-Tumpak-Bromo (Sby) | 6,675,000 | 8,343,750 | 6,675,000 | 25.0% |
| 4D3N Bromo-Ijen-Night Market (Sby) | 6,715,000 | 8,393,750 | 6,715,000 | 25.0% |

Only 3 distinct packages (5 rows) have Klook pricing populated. Remaining packages either not listed on Klook or pricing not entered in backoffice.

**Margin impact**: JVTO margin is identical whether booking is direct or via Klook — the tourist pays 25% more, Klook absorbs the spread. No JVTO discount for OTA channel.

---

-> [[finance/package-costs]] | -> [[finance/profit-analysis]] | -> [[finance/custom-tour-builder]] | -> [[products/packages-full-pricing]]
