---
type: ops
title: Package Readiness Compiler — Implementation Spec
last_updated: 2026-06-03
sources: [db-export-2026-05, sitemap-2026-05, route-data-csv, jvto-policy-pack-v6]
owner: wiki-llm
stale_after_days: 120
---

# Package Readiness Compiler — Implementation Spec

> **STATUS: IMPLEMENTED (v1.2).** `scripts/compile_packages.py` + `scripts/package_compiler/` are **built**; 6 artifacts are **live** at `output/products/package-readiness/` (`package-registry`, `package-pricing`, `package-itineraries`, `booking-compatibility`, `gap-report`, `_manifest`). This document is the **historical implementation spec** — the "No code in this phase" / "NEXT (P1)" / "NOT BUILT" framing below describes the spec-writing phase and is superseded. For current status see -> [[ops/transformation-map]] §Bundle Status Table (DONE v1.2). Note: the spec originally planned a 7th artifact (`package-route-map.json`); the shipped bundle is **6 files** (no separate route-map).

Spec only (historical). Registered as a wedge in -> [[ops/transformation-map]]; now **DONE (v1.2)**.

## 1. Purpose

Package data is the JVTO business spine (pages, pricing, itinerary, pickup/dropoff, availability, booking flow, WhatsApp reply, quotation, finance). Trust Bundle proved the registry→validate→render→artifact pattern; this applies the same pattern to packages — but the primary deliverable is a **gap report**, not just JSON.

The compiler answers: *does wiki package knowledge match the live website / DB, and is every package internally complete and policy-compliant?* It compiles a machine-readable package registry **and** flags every mismatch (slug, title, route, pricing tier, itinerary, inclusions, booking compatibility) for human resolution.

It does NOT mutate package data. It reads canonical wiki, cross-checks against the DB-export and sitemap snapshots, and emits artifacts + a gap report.

## 2. Source Files

| Role | File | Provides |
|---|---|---|
| Canonical packages | `wiki/products/packages-overview.md` | package list, slugs, standard inclusions/exclusions, booking paths, per-route additions, FOC/anti-fraud |
| Canonical pricing | `wiki/products/packages-full-pricing.md` | per-package pax-tier pricing (mirrors DB `package_prices`, 143 rows) |
| Canonical itineraries | `wiki/products/packages-itineraries.md` | day-by-day per package (mirrors DB `itinerary_days`, 99 rows) |
| Route detail | `wiki/sources/route-data-csv.md` | `routes.csv` (43) + `route_details.csv` (217) — timed legs, origins, ferry routes |
| DB snapshot | `wiki/sources/db-export-2026-05.md` | counts of truth: `packages` 22, `package_prices` 143, `package_includes` 234, `package_excludes` 126, `itinerary_days` 99, `hotels` 23 |
| Live URL snapshot | `wiki/sources/sitemap-2026-05.md` | 16 live `/tours/` URLs (12 Surabaya + 4 `/tours/from-bali/`), `/isic/student-package` |
| Policy anchors | `wiki/ops/policy-source-ownership.md` | canonical owner for Inclusions/Exclusions, Booking Paths, Ijen Health Screening; deprecated-wording rules |
| Map | `wiki/ops/transformation-map.md` | wedge status, output convention, do-not-reopen |

Canonical wiki is the source of truth. `db-export-2026-05` and `sitemap-2026-05` are **reference snapshots** the compiler compares against — divergence becomes a gap-report finding, not an auto-edit.

## 3. Canonical Package Count & Slug List

**Canonical count: 16 live tour packages** (`canonical_package_count: 16`, packages-overview frontmatter).

Reconciliation (encode in compiler): **16 canonical = 15 standard + 1 specialty (taman-safari)**. DB `packages` = 22 = 16 canonical + 6 student variants. Student packages live under `/isic/student-package`, are NOT in the canonical 16, and are validated as a separate optional set.

### Surabaya origin (12) — URL `/tours/<slug>`
```
bromo-1d1n
bromo-2d1n
ijen-2d1n
ijen-bromo-madakaripura-3d2n
bromo-madakaripura-ijen-3d2n
taman-safari-prigen-bromo-madakaripura-3d2n   (specialty)
ijen-papuma-tumpak-sewu-bromo-4d3n
ijen-bromo-madakaripura-4d3n
tumpak-sewu-bromo-ijen-4d3n
ijen-bromo-madakaripura-malang-5d4n
ijen-papuma-tumpak-sewu-bromo-5d4n
ijen-papuma-tumpak-sewu-bromo-malang-6d5n
```

### Bali origin (4) — URL `/tours/from-bali/<slug>`
```
bromo-ijen-3d2n
ijen-bromo-madakaripura-3d2n
ijen-papuma-tumpak-sewu-bromo-4d3n
ijen-papuma-tumpak-sewu-bromo-5d4n
```

> **Known slug-path variance** (gap-report input): packages-overview uses a `bali/` prefix; sitemap uses `/tours/from-bali/`. Compiler must normalise to the sitemap URL form and flag any package whose derived URL does not resolve in the sitemap snapshot.

## 4. Output Path

```
output/products/package-readiness/
```

Per the `output/<domain>/<bundle>/` convention in -> [[ops/transformation-map]]. No `compiled/`. No `data/`.

## 5. Output Files

| File | Content |
|---|---|
| `package-registry.json` | One record per canonical package: `package_id`, `slug`, `origin` (surabaya/bali), `title`, `duration` (days/nights), `public_url`, `destinations[]`, `route_codes[]`, `is_specialty` flag |
| `package-pricing.json` | Per package: `pax_tiers[]` each `{min_pax, max_pax, idr_per_person}`, `currency: "IDR"`, `ferry_included` (bool, Bali only) |
| `package-itineraries.json` | Per package: `days[]` each `{day, title, meals[], hotel}`; meal codes B/L/D normalised |
| `package-operational-days.json` | **(v1.3)** One record per package-day: `package_id, slug, day, title, meal_codes, hotel_label, overnight_status, source_basis, missing_fields, notes`. Explicit, conservative operational semantics for downstream `jvto-itinerary-core` Phase 6 — see §5.1 |
| `booking-compatibility.json` | Per package: `instant_book` (bool), `whatsapp_assisted` (bool, always true), `booking_paths[]`, notes on add-ons / health-screening collection requirement |
| `gap-report.json` | All findings: `{rule_id, severity, package_id, field, wiki_value, reference_value, message}`. The primary deliverable. |
| `_manifest.json` | Compile metadata: source file hashes, canonical count asserted, counts emitted per file, rule pass/fail summary, generated-by, schema_version. Mirrors trust-bundle `_manifest.json` shape. |

### 5.1 Package Operational Days (v1.3)

`package-operational-days.json` is derived from the itinerary days and makes
overnight / meal / hotel semantics **explicit and conservative** so downstream
`jvto-itinerary-core` Phase 6 never re-implements JVTO domain rules. llm-wiki is
the canonical public itinerary/day source ONLY: no `hotel_area`, `destination_id`,
`route_node_id`, `room_type`, cost, or time fields — area/node/cost mapping
belongs to `jvto-itinerary-core` / backoffice. Records preserve registry order
then day ascending; **consumers MUST join by `package_id` + `day`, never by array
index.**

`overnight_status` controlled vocabulary:

| value | when |
|---|---|
| `hotel` | itinerary `hotel` is a real hotel name → `hotel_label` = that name verbatim |
| `overnight_in_vehicle` | `hotel` text explicitly says overnight in vehicle → `hotel_label` null, original text kept in `notes` |
| `no_overnight` | `hotel` null AND final day AND title indicates return/finish/airport/drop/handoff/departure |
| `unknown` | `hotel` null but source does not clearly prove no overnight → `missing_fields` set |
| `return_same_day` | allowed but UNUSED unless source explicitly states same-day return |

Hotel labels are never invented; `hotel_label` is either a verbatim itinerary
hotel name or null. Validation (`validator.validate_operational_days`): all 16
packages + every itinerary day present, day-count parity with
`package-itineraries.json`, `meal_codes ⊆ {B,L,D}`, `overnight_status ∈` enum, no
invented hotel labels, exactly the 10 allowed keys (no cost/room/area/node/PII).

## 6. Validation Rules

Each rule has an ID (`PKG-01`…), a severity (`error` blocks a clean compile under `--strict`; `warn` reports only), and writes findings to `gap-report.json`. Modeled on Trust Bundle's F1–F8.

| ID | Severity | Rule |
|---|---|---|
| PKG-01 | error | **Slug exists** — every canonical package has a non-empty unique slug |
| PKG-02 | error | **Title exists** — every package has a human title |
| PKG-03 | error | **Public route exists** — derived `public_url` resolves to a URL present in `sitemap-2026-05` (Bali → `/tours/from-bali/`) |
| PKG-04 | error | **Pricing tier exists** — every package has ≥1 pax tier with a positive IDR per-person value; tier ranges are contiguous and non-overlapping |
| PKG-05 | error | **Itinerary exists** — every package has `days[]` count == duration; each day has a title; meals only from {B,L,D}; min breakfast present |
| PKG-06 | warn | **Inclusions/exclusions aligned** — package inclusion/exclusion set is consistent with the standard list + its route additions; count sanity vs DB `package_includes`/`package_excludes` |
| PKG-07 | error | **Ijen health-screening wording conditional** — any package whose route includes Ijen carries the conditional health-screening line; wording is conditional ("where BBKSDA rules require"), never "universally mandatory" (per -> [[ops/policy-source-ownership]]) |
| PKG-08 | error | **Bali-origin ferry inclusion** — every Bali-origin package lists the Gilimanuk–Ketapang ferry as included |
| PKG-09 | error | **Madakaripura helmet NOT a JVTO inclusion** — no package that visits Madakaripura lists a helmet as a JVTO-provided inclusion (local site management only) |
| PKG-10 | error | **Booking path compatibility documented** — every package records both booking paths; `whatsapp_assisted` true for all; `instant_book` recorded; deprecated wording (WA-only, Trip.com) absent |
| PKG-11 | warn | **DB count reconciliation** — emitted canonical count == 16; canonical+student == DB `packages` (22); price-row and itinerary-day counts within tolerance of DB snapshot (143 / 99) |
| PKG-12 | warn | **Forbidden-phrase scan** — no package text contains deprecated wording from -> [[ops/policy-source-ownership]] §deprecated (Blue Fire guaranteed, helmet-included, police-escort-default, 50% fee, cash-refund) |

## 7. Compiler Architecture

Mirror `scripts/compile_trust.py` structure for consistency (do not reuse its registries):

```
scripts/compile_packages.py        (NOT BUILT — implementation phase)
├── loaders        parse the 8 source files → in-memory package model
│                  (markdown table parsers for overview/pricing/itineraries;
│                   CSV-block parser for route-data; snapshot readers for
│                   db-export + sitemap as reference sets)
├── enricher       derive public_url from slug+origin; attach route_codes;
│                  resolve destinations[]; flag is_specialty / Ijen / Bali /
│                  Madakaripura route membership
├── validators     PKG-01…PKG-12 → findings list (each yields gap-report rows)
├── renderers      emit the 5 artifact JSONs + _manifest.json
└── CLI orchestrator
    --dry-run      run loaders+validators, print gap-report summary, write nothing
    --strict       exit non-zero if any `error`-severity finding remains
    (default)      atomic write of all 6 outputs to output/products/package-readiness/
```

Write semantics: atomic (temp + rename), all-or-nothing, same as trust compiler. `--dry-run` is the safe default for the first real run — it surfaces the gap report without producing artifacts.

## 8. Non-Goals (this phase)

- Do **not** implement `scripts/compile_packages.py` or any code.
- Do **not** generate any JSON or create `output/products/package-readiness/`.
- Do **not** touch the Trust Bundle, its registries, or `decision-registry.yml`.
- Do **not** touch jvto-web.
- Do **not** touch DB / API / server.
- Do **not** edit canonical package data to "pre-fix" gaps — the compiler's job is to *report* them; fixes are a later, separate decision.

## 9. Next Implementation Phase

After this spec is confirmed:

1. **Build `scripts/compile_packages.py`** — loaders + model first, TDD per the trust-compiler precedent (unit tests for each parser + each PKG rule, E2E happy-path + strict-fail).
2. **First `--dry-run` against real wiki** — produce `gap-report.json`; triage findings with Sam (slug-path variance, any pricing/itinerary mismatch vs DB snapshot).
3. **Resolve gaps in canonical wiki** (separate task), then re-run without `--dry-run` to emit the first real Package Readiness bundle.
4. **Register consumers** — jvto-web package/checkout, WhatsApp quotation, finance quote-helper read from the bundle (downstream wedges P3/P5 in the transformation map).

Implementation does not begin until explicitly approved.
