---
profile: website-copy
page: /tours/from-surabaya/bromo-2d1n
output_date: 2026-05-12
status: draft
sources: [packages-overview]
content_source: DB
type: data-structure-spec
ijen_relevant: false
origin: surabaya
duration: 2D1N
---

# Tour Page Data Structure: /tours/from-surabaya/bromo-2d1n

> Tour data fetched from DB at runtime. This file defines display schema only.
> Tour name (DB): 2 Day Bromo Sunrise Adventure from Surabaya

## Section Order

1. Hero
2. At a Glance
3. Day-by-Day Itinerary
4. What's Included / Excluded
5. Pricing Table
6. CTAs

*(Section 6 — Health Screening Note — omitted: ijen_relevant: false)*

---

## Section Definitions

### 1. Hero

| Field | Source | Notes |
|---|---|---|
| `tour_name` | DB → `tours.name` | Display as H1 |
| `origin_city` | DB → `tours.origin` | Display as badge: "From Surabaya" |
| `duration_badge` | DB → `tours.duration` | Display as badge: "2D1N" |
| `key_destinations` | DB → `tours.destinations[]` | Comma-separated list below H1 |
| `hero_image` | DB → `tours.hero_image_url` | Full-width hero |

---

### 2. At a Glance

Rendered as a summary table.

| Label | Source | Notes |
|---|---|---|
| Origin | DB → `tours.origin` | "Surabaya" |
| Duration | DB → `tours.duration` | "2 Days / 1 Night" |
| Destinations | DB → `tours.destinations[]` | Listed |
| Group Type | Static | "100% Private — dedicated vehicle, driver, guide" |
| Health Screening | Static | Not applicable (ijen_relevant: false) — field hidden |

---

### 3. Day-by-Day Itinerary

| Field | Source | Notes |
|---|---|---|
| `itinerary_days[]` | DB → `tours.itinerary_days[]` | Array of day objects |
| Each day: `day_number` | DB | e.g., "Day 1", "Day 2" |
| Each day: `title` | DB | Short day title |
| Each day: `timeline[]` | DB | Array of timed activity entries |
| Each day: `overnight_location` | DB | Hotel/location name; null if departure day |

---

### 4. What's Included / Excluded

**Inclusions** (rendered as checklist):

| Item | Source | Notes |
|---|---|---|
| Private transport | Static (Policy) | "Private AC vehicle — fuel, tolls, parking included" |
| Vehicle type | DB → `tours.vehicle_note` | Allocated by group size per policy |
| Accommodation + breakfast | DB → `tours.accommodation_note` | Per itinerary overnight stays |
| Entrance fees and permits | Static (Policy) | All confirmed itinerary sites |
| Bromo 4WD Jeep | Static (Policy) | Included on Bromo routes; max ±4 guests per jeep |
| Daily mineral water | Static (Policy) | In vehicle for all land sectors |
| JVTO travel T-shirt | Static (Policy) | 1 per participant |
| Dedicated crew | Static (Policy) | Driver-guide (1–3 pax) or driver + escort guide (4–11 pax) |

**Exclusions** (rendered as list):

| Item | Source |
|---|---|
| International/domestic flights | Static (Policy) |
| Tips for drivers and guides | Static (Policy) |
| Personal expenses (snacks, souvenirs, laundry) | Static (Policy) |
| Meals not stated in itinerary | Static (Policy) |
| Travel insurance | Static (Policy) |
| Indonesian visa (if applicable) | Static (Policy) |

> Note: Only inclusions on the official tour page AND Official E-Voucher/Invoice (PDF) are binding (Policy 2).

---

### 5. Pricing Table

| Field | Source | Notes |
|---|---|---|
| `pricing_tiers[]` | DB → `tours.pricing_tiers[]` | Array of pax-tier objects |
| Each tier: `pax_label` | DB | e.g., "2 pax", "3–4 pax" |
| Each tier: `price_idr` | DB | IDR per person, format: IDR X,XXX,XXX |
| Currency note | Static | "All prices in IDR. Pricing confirmed at booking." |

---

### 6. CTAs

| Label | Target | Notes |
|---|---|---|
| Book This Tour | WhatsApp / booking flow | Primary CTA |
| Verify JVTO | /trust | Secondary CTA |
| Browse All Tours | /tours | Tertiary CTA |

---

## Conditional Logic

- **Health Screening section**: HIDDEN — `ijen_relevant: false`
- **Bromo Jeep line in inclusions**: SHOW — Bromo is in this package
- **Ferry crossing line in inclusions**: HIDE — Surabaya origin, no ferry

---

## Notes

- No special terminus note (start and end: Surabaya).
