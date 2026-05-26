# Reference: Wiki Structure

Complete directory map, frontmatter conventions, domain taxonomy, templates, and output lifecycle for the JVTO LLM Wiki.

## Directory Layout

```
llm-wiki/
├── raw/                    # Immutable source documents. LLM reads, NEVER writes.
│   ├── FINANCE/            # Tour package cost spreadsheets + rate card JSONs
│   │   └── rate_cards/     # 5 JSON files: crew, vehicles, accommodation, activities, other
│   ├── backoffice/         # MySQL dumps (PII — gitignored)
│   │   ├── dumps/          # Raw SQL exports (gitignored)
│   │   ├── csv/            # Table CSV exports (gitignored)
│   │   ├── schema/         # DDL-only schema dump (safe to commit)
│   │   ├── _inventory.json # 210-table inventory with row counts + classification
│   │   └── _manifest.md    # Human-readable extraction manifest
│   └── _inbox/             # Drop zone for new raw items (Workflow 7 trigger)
│
├── Clippings/              # Obsidian Web Clipper output. Treat as sources.
│
├── wiki/                   # LLM-maintained knowledge base (the core product)
│   ├── index.md            # Content catalog — AI entry point for any query
│   ├── overview.md         # Master synthesis: identity, thesis, 9 trust pillars
│   ├── log.md              # Append-only operations log
│   ├── destinations/       # One page per destination (5 pages)
│   ├── products/           # Tour packages, pricing, itineraries
│   ├── people/             # Founder, doctor, crew registry
│   ├── credentials/        # Licenses, trust signals, press, medical screening, police, permits
│   ├── reviews/            # Review compilations + pattern analysis
│   ├── sources/            # One summary page per ingested raw source (30+ pages)
│   ├── website/            # Brand voice, FAQ master, AEO claims, copy bank, schemas
│   ├── seo/                # SEO strategy, GEO/AEO, competitors, redirect map
│   ├── whatsapp/           # WA ops playbook, rules engine, canned responses
│   ├── finance/            # Rate cards, package costs, profit analysis, custom tour builder
│   ├── internal-ops/       # SOPs, extraction playbooks
│   ├── ops/                # Meta-workflows: ingestion profiles, compilation profiles, health checks, intake gate
│   ├── marketing/          # (Future) campaigns, ad copy
│   └── analytics/          # (Future) metrics, tracking
│
├── output/                 # LLM-generated artifacts, organized by domain
│   ├── INDEX.md            # Master map: file → URL → source → status
│   ├── website/
│   │   ├── pages/          # Page copy (homepage, tours, destinations, travel guide, etc.)
│   │   ├── schema/         # JSON-LD structured data files + .receipt.md verification
│   │   ├── faq/            # FAQ answer pages
│   │   └── aeo/            # AEO (Answer Engine Optimization) snippets
│   ├── social/             # Social media posts
│   ├── finance/            # Profit reports, custom tour quotes
│   ├── marketing/          # (Future) campaign output
│   ├── whatsapp/           # WA dashboard output
│   └── _archive/           # Superseded output files
│
├── templates/              # Obsidian page templates (3 files)
│   ├── destination.md      # Template for wiki/destinations/ pages
│   ├── person.md           # Template for wiki/people/ pages
│   └── source.md           # Template for wiki/sources/ pages
│
├── scripts/                # Python extraction pipeline (backoffice MySQL)
│   ├── _db.py              # Shared DB connection helper
│   ├── inventory.py        # Phase A: table inventory + classification
│   ├── dump_schema.py      # Phase B1: DDL-only schema export
│   ├── dump_data.py        # Phase B2: CSV data export (PII-aware)
│   ├── build_manifest.py   # Phase B3: manifest generation
│   ├── peek.py             # Interactive column/sample inspector
│   └── analyze.py          # Phase C: CSV→wiki source page generator (PII-scrubbed)
│
├── docs/                   # Documentation (this directory)
│   └── superpowers/        # gstack plan/spec files
│
├── .firecrawl/             # Firecrawl scrape outputs (Trustpilot, reviews)
├── CLAUDE.md               # LLM operating instructions (workflows, conventions, sprint)
└── .gitignore              # PII protection: backoffice dumps, Obsidian workspace state
```

## Domain Taxonomy

Every wiki page belongs to one domain, declared via `type:` in frontmatter.

| Domain | Directory | Page count | Description |
|--------|-----------|------------|-------------|
| `destination` | `wiki/destinations/` | 5 | One page per physical destination (Ijen, Bromo, Tumpak Sewu, Madakaripura, Papuma) |
| `product` | `wiki/products/` | 3 | Tour packages, pricing tables, day-by-day itineraries |
| `person` | `wiki/people/` | 3 | Founder, doctor, 14-member crew registry |
| `credential` | `wiki/credentials/` | 6 | Licenses, trust signals, press, medical screening, police integration, permits |
| `reviews` | `wiki/reviews/` | 4 | Trustpilot compilation, Google/TripAdvisor, review patterns, all-reviews |
| `source` | `wiki/sources/` | 30+ | One summary page per ingested raw document |
| `website` | `wiki/website/` | 7+ | Brand voice, FAQ master, AEO claims, copy bank, schema templates, operational facts |
| `seo` | `wiki/seo/` | 4+ | SEO strategy, GEO/AEO strategy, competitors, redirect map |
| `whatsapp` | `wiki/whatsapp/` | 3 | Operations playbook, rules engine, canned responses |
| `finance` | `wiki/finance/` | 4 | Rate cards, package costs, profit analysis, custom tour builder |
| `ops` | `wiki/ops/` | 4 | Ingestion profiles, compilation profiles, health checks, intake gate |
| `overview` | `wiki/` | 3 | index.md, overview.md, log.md |

## Frontmatter Specification

Every wiki page starts with YAML frontmatter between `---` fences.

### Required fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Domain type from the taxonomy above |
| `title` | string | Human-readable page title |
| `last_updated` | date | `YYYY-MM-DD` format. Update on every edit. |
| `sources` | list | Slugs of source pages this page draws from (e.g., `[ssot-v6, trustpilot-reviews-2026]`) |

### Optional fields

| Field | Type | Used by | Description |
|-------|------|---------|-------------|
| `aliases` | list | destinations | Alternative spellings for Obsidian search |
| `schema_type` | string | destinations | Schema.org type (e.g., `TouristAttraction`) |
| `canonical_url` | string | destinations | URL path on the live site |
| `ijen_relevant` | boolean | destinations | Whether Ijen health-screening wording applies |
| `health_wording_mode` | string | destinations | `conditional` or `none` |
| `geo_bbox` | object | destinations | Bounding box from GPX data |
| `slug` | string | sources | Slug used in other pages' `sources:` arrays |
| `original_url` | string | sources | URL of the web-clipped source |
| `ingested` | date | sources | Date the source was first ingested |
| `format` | string | sources | `json`, `web-clip`, `gpx`, `pdf`, `other` |
| `location` | string | sources | Path to the raw file (e.g., `raw/filename.json`) |
| `total_pages` | number | index | Current wiki page count |

### Example frontmatter

```yaml
---
type: destination
title: Kawah Ijen (Ijen Crater)
last_updated: 2026-05-25
sources: [ssot-v6, jvto-homepage-clip, gpx-destination-data]
aliases: [Ijen, Kawah Ijen, Ijen Crater]
schema_type: TouristAttraction
canonical_url: /destinations/ijen-crater
ijen_relevant: yes
health_wording_mode: conditional
---
```

## Cross-Reference Conventions

- Link between wiki pages using Obsidian wikilinks: `[[folder/page-name]]`
- In prose, prefix links with `->`: `-> [[destinations/kawah-ijen]]`
- After any page change, update `wiki/index.md` to keep the catalog current
- Source attribution: every factual claim links back to its source page

## Output Lifecycle

Output files progress through four statuses, tracked in `output/INDEX.md`:

| Status | Meaning | Next action |
|--------|---------|-------------|
| `draft` | Generated, not reviewed | Copy-check against wiki sources |
| `reviewed` | Copy-checked, accurate | Ready for developer integration |
| `published` | Live on the website | Monitor for staleness |
| `stale` | Source wiki updated after output generation | Regenerate from current wiki |

### Staleness detection

An output file is stale when:
- Its `output_date` is older than the `last_updated` of any wiki page it drew from
- A `review-feed` ingest changed review counts referenced in schema output
- A health check flags it with `> [stale?]`

## Templates

Three Obsidian templates in `templates/` provide the section structure for new wiki pages:

| Template | Creates | Key sections |
|----------|---------|-------------|
| `destination.md` | `wiki/destinations/` page | Entity summary, quick facts, packages, trail data, content angles, AI query intents, trust anchors |
| `person.md` | `wiki/people/` page | (Crew member or key person profile) |
| `source.md` | `wiki/sources/` page | Metadata, role in vault, authority status, content map, key facts, contradictions, provenance chain |

## Trust Architecture (C1-C9)

Nine canonical claims form the trust graph. Each claim is owned by a primary page on the public site and backed by SHA-256-verifiable proof items.

| ID | Pillar | Primary page |
|----|--------|-------------|
| C1 | Safety-led operations | /why-jvto/community-standards |
| C2 | Private tours (execution control) | /why-jvto/community-standards |
| C3 | All-inclusive clarity | /policy/booking-payment-cancellation |
| C4 | Ijen Health Screening | /travel-guide/ijen-health-screening |
| C5 | Proof-first trust | /verify-jvto |
| C6 | Reviews registry | /why-jvto/reviews |
| C7 | Our Team (personality economy) | /why-jvto/our-team |
| C8 | Partners (HPWKI/INDECON/ISIC) | /verify-jvto |
| C9 | Press & Recognition | /verify-jvto/press-recognition |

See `wiki/website/aeo-claims.md` for NLP snippets and full evidence chains per claim.

## Related

- [Tutorial: First Ingestion](tutorial-first-ingestion.md) — walk through your first source ingestion
- [How-to: Ingest Sources](howto-ingest-sources.md) — step-by-step for each source type
- [How-to: Generate Output](howto-generate-output.md) — compilation profiles in action
- [Explanation: Architecture](explanation-architecture.md) — why this system works the way it does
- [Reference: Scripts](reference-scripts.md) — Python extraction pipeline
