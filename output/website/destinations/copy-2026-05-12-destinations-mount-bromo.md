---
profile: website-copy
page: /destinations/mount-bromo
output_date: 2026-05-12
sources: [mount-bromo, packages-overview, ssot-v6]
content_source: DB
type: data-structure-spec
---

# Page Data Structure: /destinations/mount-bromo

> Data fetched from DB at runtime. This file defines display schema only.

## Section Order

1. Hero
2. Quick Facts
3. Penanjakan Sunrise
4. Sea of Sand
5. Crater Walk
6. BBKSDA Clearance + Bromo 4WD Jeep Included
7. Closure & Plan B
8. Packages That Include This Destination
9. CTA

---

## Section Definitions

### Hero

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Destination name | `destinations.name` | H1 heading | No |
| Tagline | `destinations.tagline` | Subtitle/deck text below H1 | No |
| Hero image | `destinations.hero_image_url` | Full-width background image, lazy-loaded | No |
| Hero image alt text | `destinations.hero_image_alt` | `alt` attribute on img element | No |

---

### Quick Facts

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Elevation | `destinations.elevation_m` | "2,329 m" — display with unit label | No |
| Location | `destinations.location_text` | Plain text, e.g. "Tengger Caldera, Probolinggo Regency, East Java" | No |
| National park | `destinations.national_park_name` | Plain text: "Bromo Tengger Semeru National Park" | No |
| Best season | `destinations.best_season` | Plain text, e.g. "Dry season: April–October" | No |
| Best time of day | `destinations.best_time_of_day` | Plain text, e.g. "Pre-dawn 03:00–05:00 for sunrise" | No |
| Access mode | `destinations.access_mode` | Plain text, e.g. "4WD jeep from Cemoro Lawang — Penanjakan viewpoint; horse or walk to crater rim" | No |

Display as: icon-labelled key-value list or compact table. 6 rows max.

---

### Penanjakan Sunrise

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Section heading | Static: "Penanjakan Sunrise" | H2 | No |
| Viewpoint elevation | `destinations.penanjakan_elevation_m` | "2,770 m" — inline within body copy | No |
| Departure timing | `destinations.penanjakan_departure_time` | Plain text: "03:00 departure from accommodation — jeep pre-arranged" | No |
| Description body | `destinations.penanjakan_description` | Rich text / paragraphs — covers panoramic view over caldera, sunrise light, sea of sand below | No |
| Access note | Static or `destinations.penanjakan_access_note` | Note that Penanjakan viewpoint is reached by 4WD jeep on separate access road — not the crater-floor walking trail | No |

---

### Sea of Sand

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Section heading | Static: "Sea of Sand (Pasir Berbisik)" | H2 | No |
| Description body | `destinations.sea_of_sand_description` | Rich text / paragraphs — covers caldera floor extent (~10 km²), volcanic sand, 4WD jeep traverse as experience not logistics | No |
| Temple note | `destinations.pura_luhur_poten_note` | Optional inline text: "Pura Luhur Poten — Hindu temple on the caldera floor, passed on all guided routes" | No |

---

### Crater Walk

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Section heading | Static: "Crater Walk" | H2 | No |
| Description body | `destinations.crater_walk_description` | Rich text / paragraphs — covers short walk or horse-ride from jeep drop-off to crater rim, active smoking vent visible from rim | No |
| Horse option note | `destinations.horse_option_note` | Inline note: horse available for guests preferring not to walk the crater approach | No |

---

### BBKSDA Clearance + Bromo 4WD Jeep Included

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Section heading | Static: "What's Already Arranged" | H2 | No |
| BBKSDA clearance note | `destinations.bbksda_clearance_copy` | Plain text: JVTO holds national-park operator authorization — guests enter without paperwork friction | No |
| Jeep inclusion note | `destinations.jeep_inclusion_copy` | Plain text: Bromo 4WD jeep pre-arranged, no on-the-day haggling; max ~4 guests per jeep, additional jeeps for larger groups | No |
| Credentials link | Static | Text link to /verify or /credentials page | No |

---

### Closure & Plan B

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Section heading | Static: "If Bromo Closes" | H2 | YES — render only if `destinations.closure_plan_b_enabled = true` |
| Closure SOP copy | `destinations.closure_plan_b_copy` | Plain text: describes alternative-route SOP — guests briefed in advance, no day lost | YES — same condition |
| Policy link | Static | Text link to /policy or /travel-guide/weather-and-closures page | YES — same condition |

Condition logic: `IF destinations.closure_plan_b_enabled = true THEN render section ELSE skip`
Note: The Plan-B framework exists per wiki data. Flag recommended — surface this section when there is active volcanic alert for Bromo (Level II+).

---

### Packages That Include This Destination

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Package list | `packages WHERE destinations_array CONTAINS 'mount-bromo'` | Grid of package cards | No — if 0 results show fallback |
| Package card: name | `packages.name` | Plain text link | — |
| Package card: duration | `packages.duration_label` | Badge or tag, e.g. "2D1N" | — |
| Package card: origin | `packages.origin_city` | Plain text, e.g. "Surabaya" or "Bali" | — |
| Package card: price-from | `packages.price_from_idr` | "From IDR X,XXX,XXX/person" — Rupiah only, comma thousand separators | — |

---

### CTA

| Field | DB source hint | Display format | Conditional? |
|---|---|---|---|
| Primary CTA | Static | Button: "View Bromo Packages" → links to filtered /tours?destination=mount-bromo | No |
| Secondary CTA | Static | Text link: "Contact us on WhatsApp" → `https://wa.me/6282244788833` | No |
