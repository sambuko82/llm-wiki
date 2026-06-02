---
type: ops
title: Bundle Taxonomy — 6 Website-First Bundles
last_updated: 2026-06-03
sources: []
owner: wiki-llm
stale_after_days: 120
---

# Bundle Taxonomy — 6 Website-First Bundles

Defines the 6 bundles `llm-wiki` is organised around. Used together with -> [[ops/transformation-map]] (which owns the pipeline status table) and `wiki/bundles/*.md` (which are thin index/navigation pages).

This page is **documentation only**. It does NOT move files, create scripts, or migrate outputs. It states where each existing file belongs and which bundle owns it.

## Why bundles

The wiki is organised by **content domain** (destinations, people, products, credentials, reviews, …). Production work is organised by **bundle** — a coherent slice of canonical knowledge + compiled output + consumers. Domains and bundles cut the same material at different angles; both are needed.

- **Domain folders** (`wiki/destinations/`, `wiki/people/`, etc.) — primary content pillars. Each page lives in exactly one domain folder.
- **Bundles** — coherent production slices. One file can be cited by multiple bundle indexes.
- **`wiki/bundles/<bundle>.md`** — thin index pages. Pull together the wiki pages, raw sources, and output paths for one bundle.

A bundle is not a folder rename. It is a **navigation + accountability unit**.

## The 6 bundles

| # | Bundle | One-line scope |
|---|---|---|
| 1 | **Trust Bundle** | Claims, trust signals, evidence, verification mapping |
| 2 | **Website Logic Bundle** | FAQ, AEO, schema, wording rules, page rules |
| 3 | **Package Bundle** | Package registry, pricing, itinerary, package readiness |
| 4 | **Review Bundle** | Review registry, ratings, crew mentions, review patterns, social proof |
| 5 | **WhatsApp Reply Bundle** | Templates, intents, routing, hard rules |
| 6 | **Asset Bundle** | Image proof, proof-file usage, page usage, alt text, visual evidence |

## File → bundle map

Each row lists the **as-is location** of an existing file. No file is moved by this document. The "Bundle" column records ownership for navigation and future restructuring.

### 1. Trust Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/credentials/legal-licenses.md` | Source | Licenses, NIB, TDUP |
| `wiki/credentials/medical-screening.md` | Source | Ijen health-screening evidence chain |
| `wiki/credentials/permit-requirements.md` | Source | BBKSDA permits |
| `wiki/credentials/police-integration.md` | Source | Polpar evidence chain |
| `wiki/credentials/press-coverage.md` | Source | Independent media references |
| `wiki/credentials/trust-signals.md` | Source | Aggregate trust signal index |
| `wiki/website/aeo-claims.md` | Source | 9 canonical trust pillars C1–C9 |
| `wiki/overview.md` | Source | Master synthesis (9 pillars) |
| `raw/_manifest/claim-registry.yml` | Source registry | Live |
| `raw/_manifest/evidence-registry.yml` | Source registry | Live |
| `raw/_manifest/entity-registry.yml` | Source registry | Live |
| `raw/_manifest/decision-registry.yml` | Source registry | Live |
| `raw/_manifest/conflict-log.md` | Source registry | Live |
| `output/website/trust-bundle/*.json` (9 files) | Compiled output | Canonical Trust Bundle output |
| `output/website/trust-bundle/schema/*.json` (3 files) | Compiled output | Organization / TouristTrip / FAQPage JSON-LD |
| `output/website/trust-bundle/extended-bundle-receipt.md` | Receipt | Naming-exempt operational anchor |
| `output/website/pages/verify-jvto/*` (5 files) | Page copy | URL-mirror; consumes Trust Bundle |
| `scripts/compile_trust.py` | Compiler | DONE — do not reopen |
| `bases/credentials.base` | Dashboard | Live Obsidian view |

### 2. Website Logic Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/website/website-context-master.md` | Source (canonical master) | Single-source-of-truth doc |
| `wiki/website/faq-master.md` | Source | 20 canonical answers |
| `wiki/website/aeo-claims.md` | Source (shared w/ Trust) | |
| `wiki/website/schema-templates.md` | Source | Schema design reference |
| `wiki/website/brand-voice.md` | Source | |
| `wiki/website/copy-bank.md` | Source | Reusable snippets |
| `wiki/website/operational-facts.md` | Source | Temperatures, travel times, closures |
| `wiki/website/booking-platform-analysis.md` | Source | Booking flow analysis |
| `wiki/website/query-hero-claim.md` | Source | Hero-claim query reference |
| `wiki/website/hotels.md` | Source | Hotel partner registry |
| `wiki/seo/seo-strategy.md` | Source | Keyword silos + page rules |
| `wiki/seo/geo-aeo-strategy.md` | Source | GEO/AEO strategy |
| `wiki/seo/competitors.md` | Source | Competitor map |
| `wiki/seo/redirect-map.md` | Source | 301 map |
| `wiki/seo/why-jvto-architecture.md` | Source | Hub & spoke arch |
| `output/website/faq/*.md` (8 files) | Compiled output | FAQ blocks per topic |
| `output/website/aeo/*.md` (10 files) | Compiled output | AEO snippets |
| `output/website/schema/*.json` + `*-receipt.md` (28 + receipts) | Compiled output | JSON-LD per page; receipts naming-exempt |
| `output/website/pages/**/*.md` (~90 files) | Page copy | URL-mirror layout, naming-exempt |
| `output/website/blog/*.md` | Page copy | URL-mirror |
| `output/website/llms.txt`, `llms-full.txt` | Compiled output | LLM crawler files |
| `output/website/HANDOFF.md` | Operational anchor | Naming-exempt |
| `output/INDEX.md` | Operational anchor | Naming-exempt |
| `bases/website-readiness.base` | Dashboard | Live Obsidian view |

### 3. Package Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/products/packages-overview.md` | Source | |
| `wiki/products/packages-full-pricing.md` | Source | All 22 priced packages (16 canonical + 6 student) |
| `wiki/products/packages-itineraries.md` | Source | Day-by-day |
| `wiki/finance/rate-cards.md` | Source | Cost component reference |
| `wiki/finance/package-costs.md` | Source | COGS breakdown |
| `wiki/finance/profit-analysis.md` | Source | |
| `wiki/finance/custom-tour-builder.md` | Source | |
| `wiki/ops/package-readiness-compiler-spec.md` | Spec | |
| `raw/FINANCE/*.xlsx` (15 files) | Raw source | Per-package cost spreadsheets |
| `raw/FINANCE/rate_cards/*.json` (5 files) | Raw source | Crew, vehicle, accom, activities, other |
| `output/products/package-readiness/*.json` (6 files) | Compiled output | Live Package Readiness Bundle v1.2 |
| `output/products/package-readiness/_manifest.json` | Manifest | |
| `output/products/package-readiness/gap-report.json` | Validation output | |
| `scripts/compile_packages.py` | Compiler | |
| `scripts/package_compiler/` | Compiler module | |
| `tests/package_compiler/` | Tests | |
| `bases/products.base` | Dashboard | Live Obsidian view |

### 4. Review Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/reviews/trustpilot-all-reviews.md` | Source | Full structured catalog |
| `wiki/reviews/trustpilot-compilation.md` | Source | |
| `wiki/reviews/google-tripadvisor-2026.md` | Source | Cross-platform compilation |
| `wiki/reviews/review-patterns.md` | Source | Patterns & themes |
| `wiki/people/crew-registry.md` (§Guide / Driver review-quote excerpts) | Source (shared w/ People) | Crew-mention subsection |
| `wiki/sources/trustpilot-reviews-2026.md` | Source summary | |
| `wiki/sources/google-maps-reviews-api-2026.md` | Source summary | 123 reviews |
| `raw/google review page 1.json`, `…page 2.json`, `…page 3.json` | Raw source | |
| `raw/google profile media.json` | Raw source | (also Asset Bundle) |
| `Clippings/Java Volcano Tour Operator is rated Excellent with 4.8.md` | Raw clip | Trustpilot page |
| (no compiled output yet) | — | Future: `output/reviews/review-proof-index/` |

### 5. WhatsApp Reply Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/whatsapp/operations-playbook.md` | Source | |
| `wiki/whatsapp/rules-engine.md` | Source | |
| `wiki/whatsapp/canned-responses.md` | Source | Templates by stage |
| `wiki/sources/wa-pro-crm-api.md` | Source | API reference |
| `wiki/sources/backoffice-whatsapp.md` | Source | Conversation analytics |
| `raw/backoffice/csv/wa_chats.csv`, `wa_chat_categories.csv`, `wa_chat_summaries.csv`, `wa_itineraries.csv`, `wa_logs.csv` | Raw source | |
| (no compiled output yet) | — | Future: `output/whatsapp/reply-intelligence/` |

### 6. Asset Bundle

| As-is location | Role | Notes |
|---|---|---|
| `wiki/sources/ssot-image-asset-map.md` | Source | 54 images across 14 groups |
| `wiki/sources/google-profile-media-2026.md` | Source | 87 GMB items (79 photos + 8 videos) |
| `wiki/sources/gpx-destination-data.md` | Source | 5 GPX recordings |
| `raw/jvto_image_asset_map.json` | Raw source | |
| `raw/JVTO SSOT Image Asset Map.md` | Raw source | |
| `raw/JVTO SSOT Image Inventory.md` | Raw source | |
| `raw/google profile media.json` | Raw source | (also Review Bundle) |
| `raw/Kawah_Ijen_Volcano.gpx` | Raw source | |
| `raw/Gunung_Bromo.gpx` | Raw source | |
| `raw/Air_Terjun_Tumpak_Sewu.gpx` | Raw source | |
| `raw/Madakaripura_Waterfalls.gpx` | Raw source | |
| `raw/Pantai_dan_Tanjung_Papuma.gpx` | Raw source | |
| `wiki/people/crew-registry.md` (§Image Assets, §KTA Card Images) | Source (shared w/ People) | Asset subsection |
| (no compiled output yet) | — | Future: `output/asset-bundle/` |
| (no wiki workspace yet) | — | Future: `wiki/assets/` (empty scaffold created in Phase 2) |

## Cross-bundle / shared files

Some files serve more than one bundle. Listed here so the index pages can cite without duplicating ownership:

| File | Primary bundle | Also cited by |
|---|---|---|
| `wiki/website/aeo-claims.md` | Website Logic | Trust |
| `wiki/people/crew-registry.md` | (People domain, not a bundle) | Trust, Review, Asset, WhatsApp |
| `wiki/people/agung-sambuko.md` | (People domain) | Trust |
| `wiki/people/dr-ahmad-irwandanu.md` | (People domain) | Trust, Website Logic |
| `wiki/destinations/*.md` | (Destinations domain) | Website Logic, Package, Asset |
| `wiki/overview.md` | (Root) | All bundles |
| `raw/JVTO_FINAL_CLEAN_SSOT.json` (via `wiki/sources/ssot-v6.md`) | (SSOT) | All bundles |
| `raw/google profile media.json` | Asset | Review |

## What is NOT a bundle

For clarity — these are domain folders or operational areas, not bundles:

- `wiki/destinations/`, `wiki/people/`, `wiki/products/`, `wiki/credentials/`, `wiki/reviews/`, `wiki/finance/` — primary content pillars (stay at `wiki/` root)
- `wiki/seo/` — meta-strategy, feeds Website Logic Bundle
- `wiki/ops/` — bundle infrastructure (this file, transformation-map, profiles, health-checks)
- `wiki/sources/` — universal raw-source summary catalog (each page feeds 1+ bundle)
- `wiki/_shared/` — cross-bundle registries/rules/glossary (empty scaffold in Phase 2)
- `raw/` and `raw/_manifest/` — immutable source; bundles consume, never restructure
- `bases/` — Obsidian dashboards over wiki frontmatter
- `scripts/`, `tests/` (incl. `tests/templates/` Obsidian page templates), `docs/`, `Clippings/` — infrastructure / source / docs

## How bundles relate to `output/`

Per -> [[ops/transformation-map]] the output path convention is `output/<domain>/<bundle>/`. Phase 1–2 does **not** create any new `output/*-bundle/` roots. Current operationally meaningful homes stay put:

- Trust Bundle output: `output/website/trust-bundle/` (live, do not reopen)
- Package Bundle output: `output/products/package-readiness/` (live)
- Website Logic Bundle output: `output/website/{aeo,faq,schema,pages,blog}` (mirrors site rendering; do not flatten)
- Review / WhatsApp / Asset Bundle outputs: future, not scaffolded yet

If/when an output migration is approved later, this taxonomy is the file→bundle source of truth that will drive the migration.

## Phase 1–2 deliverables (this scope)

1. This file (`wiki/ops/bundle-taxonomy.md`).
2. Aligned bundle naming in `wiki/ops/transformation-map.md`.
3. Naming-rule exemptions for canonical operational anchors documented in root `CLAUDE.md`.
4. `wiki/bundles/` scaffold: `README.md` + 6 stub index pages.
5. Empty `wiki/assets/` and `wiki/_shared/` scaffolds.

Explicitly **not** in this scope: any `output/` change, any content move, any rename of `output/website/HANDOFF.md` or `output/INDEX.md`, any deletion of empty domain folders, any creation of the 8 new index/merge pages (verification-mapping, crew-mentions, social-proof-map, proof-file-usage, page-usage-map, alt-text-registry, intents-routing, hard-rules).
