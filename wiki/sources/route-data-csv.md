---
type: source
title: Route Data CSVs — routes.csv + route_details.csv
last_updated: 2026-05-18
sources: [db-export-2026-05]
raw_files:
  - raw/routes.csv
  - raw/route_details.csv
---

# Route Data CSVs — Itinerary Segment Library

**Files**: `raw/routes.csv` (43 routes, 44 rows incl. header) · `raw/route_details.csv` (217 detail rows, 218 incl. header)
**Relationship to db-export**: These CSVs are supplementary exports from the same live DB. `raw/db_export_raw.json` covers `itinerary_days` (99 rows, day-level summaries); these CSVs provide **route-segment granularity** — the named day-segments a package is assembled from, plus timed activity breakdowns per segment.

The canonical itinerary structure at [[products/packages-itineraries]] draws from both sources.

---

## Data Structure

### routes.csv — Route Segments

| Column | Description |
|---|---|
| `id` | Numeric route ID (1–45, missing 13 and 18) |
| `code` | Slug (e.g. `SUB-SAFARI-BROMO`) — origin–activity–destination |
| `route` | Human-readable origin → destination |
| `itinerary_title` | Long-form day title for guest-facing copy |
| `start_area` | Departure location |
| `end_area` | Arrival/overnight location |
| `estimated_duration` | Duration string |
| `main_activities` | Comma-separated activity list |
| `accommodation_status` | Check-in / check-out / tour-ended string |
| `customer_tips` | Pre-trip guidance for guests |
| `overview` | Narrative paragraph (copywriteable) |
| `breakfast` / `lunch` / `dinner` | Boolean (t/f) — meals included |
| `meals_notes` | Exceptions or clarifications |

### route_details.csv — Timed Activity Breakdown

| Column | Description |
|---|---|
| `id` | Row primary key |
| `route_id` | Foreign key → `routes.csv.id` |
| `seq` | Sequence within the day (1, 2, 3…) |
| `time_or_label` | Scheduled time (HH:MM) or label |
| `timezone` | WIB / WITA / blank |
| `activity` | Full description of the activity |
| `type` | `TravelAction` / `TouristAttractionVisit` / `CheckInAction` |
| `location` | Location name |
| `from_location` | Departure point |
| `to_location` | Arrival point |
| `duration_minutes` | Duration in minutes |
| `name` | Short activity name |

Route 8 (SUB-YOGYA) has **no rows** in route_details — no timed breakdown available.

---

## Full Route Index

### Surabaya origin

| ID | Code | Title | Meals |
|---|---|---|---|
| 1 | SUB-BROMO-MIDNIGHT | Overnight Adventure in Bromo: Midnight Departure | B |
| 2 | SUB-BONDOWOSO | Towards the Ijen Plateau: SUB → Bondowoso | D |
| 3 | SUB-BANYUWANGI | North Coast Expedition: SUB → Banyuwangi | D |
| 4 | SUB-BROMO-TRANSFER | Gateway to the Clouds: SUB → Cemoro Lawang | — |
| 5 | SUB-LUMAJANG | Path to Waterfall Paradise: SUB → Lumajang | — |
| 6 | SUB-SAFARI-BROMO | From Wildlife to Volcano: Safari Park → Bromo | B |
| 7 | SUB-CITYTOUR | Surabaya City Tour (same-day) | B |
| 8 | SUB-YOGYA | SUB → Yogyakarta via train or car | B |
| 9 | SUB-AIRPORT | Final Transfer: SUB hotel → Juanda Airport | B |
| 37 | SUB-MALANG | SUB → Malang (transfer only) | B |

### Bali origin

| ID | Code | Title | Meals |
|---|---|---|---|
| 10 | BALI-BANYUWANGI | Bali → Gilimanuk Ferry → Banyuwangi | D |
| 11 | BALI-BONDOWOSO | Bali → Gilimanuk Ferry → Bondowoso | D |
| 12 | BALI-BROMO | Bali → Gilimanuk Ferry → Cemoro Lawang | — |

### Ijen area departures

| ID | Code | Title | Meals |
|---|---|---|---|
| 14 | IJEN-BROMO-TRANSFER | Ijen Tour → Transfer to Bromo (full day) | B · L |
| 15 | IJEN-PAPUMA-JEMBER | Ijen Tour → Papuma Beach → Jember | B · L |
| 38 | IJEN-BALI | Ijen Area → Ketapang Ferry → Bali | B |
| 39 | IJEN-SURABAYA | Ijen Area → Surabaya (return) | B |
| 40 | IJEN-LUMAJANG | Ijen Area → Lumajang (Tumpak Sewu) | B |

### Banyuwangi area

| ID | Code | Title | Meals |
|---|---|---|---|
| 16 | BWI-BANGSRING-TOUR | Bangsring Underwater Tour (day trip) | B |
| 17 | BWI-BALI-TRANSFER | Banyuwangi → Ketapang Ferry → Bali | B |

### Bromo area departures

| ID | Code | Title | Meals |
|---|---|---|---|
| 19 | BROMO-SUB-FINISH | Bromo Sunrise → Return to Surabaya | B |
| 20 | BROMO-MADAKARIPURA-SUB | Bromo + Madakaripura → Surabaya | B |
| 21 | BROMO-BONDOWOSO | Bromo Sunrise → Transfer to Ijen area | B · D |
| 22 | BROMO-KETAPANG | Bromo Sunrise → Ketapang (Bali ferry) | B |
| 23 | BROMO-LUMAJANG | Bromo Sunrise → Lumajang (Tumpak Sewu) | B |
| 24 | BROMO-MALANG | Bromo Sunrise → Malang city | B |
| 41 | BROMO-MADAKARIPURA-BONDOWOSO | Bromo + Madakaripura → Bondowoso/Ijen | B |
| 42 | BROMO-MADAKARIPURA-MALANG | Bromo + Madakaripura → Malang | B |
| 43 | BROMO-MADAKARIPURA-KETAPANG | Bromo + Madakaripura → Ketapang (Bali ferry) | B |
| 44 | BROMO-MADAKARIPURA-LUMAJANG | Bromo + Madakaripura → Lumajang | B |
| 45 | MLG-BROMO | Malang → Cemoro Lawang (Bromo) | — |

### Tumpak Sewu area departures

| ID | Code | Title | Meals |
|---|---|---|---|
| 25 | TUMPAKSEWU-BROMO | Tumpak Sewu → Bromo area | B · L |
| 26 | TUMPAKSEWU-BONDOWOSO | Tumpak Sewu → Bondowoso/Ijen | B · L · D |
| 27 | TUMPAKSEWU-SURABAYA | Tumpak Sewu → Surabaya (return) | B · L |
| 28 | TUMPAKSEWU-MALANG | Tumpak Sewu → Malang | B · L |

### Jember area

| ID | Code | Title | Meals |
|---|---|---|---|
| 29 | JEMBER-PAPUMA-TOUR | Papuma Beach Sunset Tour (from Jember hotel) | B |
| 30 | JEMBER-COCOAPARK-TOUR | Coffee & Cocoa Technopark Tour (from Jember hotel) | B |
| 31 | JEMBER-LUMAJANG | Jember → Lumajang (Tumpak Sewu transfer) | B |

### Malang area

| ID | Code | Title | Meals |
|---|---|---|---|
| 32 | MLG-CITYTOUR | Malang / Batu City Tour (same-day) | B |
| 33 | MLG-CITYTOUR-LUMAJANG | Malang City Tour → Lumajang | B |
| 34 | MLG-TUMPAKSEWU-BROMO | Malang → Tumpak Sewu → Bromo | B |
| 35 | MLG-TUMPAKSEWU-BONDOWOSO | Malang → Tumpak Sewu → Bondowoso | B |
| 36 | MLG-SUB-FINISH | Malang / Batu City Tour → Surabaya finish | B |

---

## Usage Status (as of 2026-05-18)

| Route | Explicitly ingested | Used in wiki itineraries |
|---|---|---|
| 6 SUB-SAFARI-BROMO | ✓ 2026-05-18 | taman-safari-prigen-bromo-madakaripura-3d2n Day 1 |
| 20 BROMO-MADAKARIPURA-SUB | ✓ 2026-05-18 | taman-safari Day 3 + bromo-2d1n Day 2 pattern |
| All others | Not explicitly ingested | Implicitly described via recurring patterns + db-export day summaries |

Routes whose detail data could directly enrich [[products/packages-itineraries]]:
- **Route 14** (IJEN-BROMO-TRANSFER) — 5 detail rows; used in all Ijen+Bromo combos
- **Route 15** (IJEN-PAPUMA-JEMBER) — 7 detail rows; used in Papuma-family packages
- **Route 21** (BROMO-BONDOWOSO) — 8 detail rows; used in bromo-madakaripura-ijen-3d2n
- **Route 41** (BROMO-MADAKARIPURA-BONDOWOSO) — 9 detail rows (most detailed); used in Bromo→Madakaripura→Ijen sequences

Routes that appear to be **optional add-ons** (not in any SSOT canonical 16 packages):
- Route 7 (SUB-CITYTOUR), Route 8 (SUB-YOGYA), Route 16 (BWI-BANGSRING-TOUR), Route 30 (JEMBER-COCOAPARK-TOUR) — offered separately; not part of the 16 live tour pages

---

## Relationship to Existing Sources

- [[sources/db-export-2026-05]] `itinerary_days` (99 rows) = day-level summaries per package. These CSVs add **intra-day granularity** (timed activities, transfer durations, location names). They are complementary, not overlapping.
- The `routes.csv` overview text and `customer_tips` columns are copywriteable for [[output]] files.
- `type` values in route_details (`TravelAction`, `TouristAttractionVisit`, `CheckInAction`) map directly to Schema.org itinerary types — useful for future JSON-LD expansion.

-> [[products/packages-itineraries]] | -> [[sources/db-export-2026-05]] | -> [[products/packages-overview]]
