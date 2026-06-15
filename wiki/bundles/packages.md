---
type: ops
title: Package Bundle — Index
last_updated: 2026-06-01
sources: [ssot-v6, db-export-2026-05, finance-rate-cards]
owner: wiki-llm
stale_after_days: 120
bundle: packages
---

# Package Bundle — Index

**Scope:** package registry, pricing, itinerary, package readiness.

Thin navigation page. File ownership in -> [[ops/bundle-taxonomy]] §3. Pipeline status in -> [[ops/transformation-map]].

## Wiki sources

### Products
- -> [[products/packages-overview]]
- -> [[products/packages-full-pricing]] — all 22 packages
- -> [[products/packages-itineraries]] — day-by-day

### Finance
- -> [[finance/rate-cards]]
- -> [[finance/package-costs]]
- -> [[finance/profit-analysis]]
- -> [[finance/custom-tour-builder]]

### Spec
- -> [[ops/package-readiness-compiler-spec]]

## Raw sources

- `raw/FINANCE/*.xlsx` (17 per-package cost spreadsheets)
- `raw/FINANCE/rate_cards/*.json` (crew, vehicle, accommodation, activities, other)
- `raw/backoffice/csv/packages.csv`, `package_prices.csv`, `package_*.csv` (12+ package tables)
- `raw/backoffice/csv/itineraries.csv`, `itinerary_*.csv`

## Compiled output (live)

- `output/products/package-readiness/_manifest.json`
- `output/products/package-readiness/package-registry.json`
- `output/products/package-readiness/package-pricing.json`
- `output/products/package-readiness/package-itineraries.json`
- `output/products/package-readiness/package-operational-days.json`
- `output/products/package-readiness/booking-compatibility.json`
- `output/products/package-readiness/gap-report.json`

## Compiler

- `scripts/compile_packages.py`
- `scripts/package_compiler/` (module)
- `tests/package_compiler/` (golden + unit tests)

## Consumers

- jvto-web package/checkout
- WhatsApp reply intelligence (planned)
- Quotation builder (planned)
- Finance dashboards (planned)

## Status

**DONE (v1.2).** Full 6-artifact bundle live. Finance Quote Helper (P5) is a planned subset compiler inside this bundle's scope.

## Pending follow-up (deferred)

- `package-route-map.json` — declared but not yet built (low priority).
