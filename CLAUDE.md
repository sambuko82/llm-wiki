# JVTO LLM Wiki — Schema & Workflows

This vault is a persistent, compounding knowledge base for **Java Volcano Tour Operator (JVTO)**.
**Primary use**: content production — website copy, FAQs, AEO material, marketing content.
The LLM writes and maintains all `wiki/` files. You source and explore; the LLM files and cross-references.

---

## About JVTO

| Field | Value |
|-------|-------|
| Full legal name | PT Java Volcano Rendezvous |
| Brand name | Java Volcano Tour Operator (JVTO) |
| Founded | 2015 (guesthouse era) · PT incorporated 2016-01-01 (AHU) · TDUP issued 2023-02-11 |
| Founder | Agung "Mr. Sam" Sambuko — active Tourist Police officer |
| Products | Private tours: Kawah Ijen, Mount Bromo, Tumpak Sewu, Madakaripura |
| Website | javavolcano-touroperator.com |
| NIB | 1102230032918 |
| Office | Jl. Khairil Anwar No.102A, Bondowoso, East Java 68214 |
| WhatsApp | +62 822 4478 8833 |
| Email | hello@javavolcano-touroperator.com |

**Core differentiators** (always reference in content):
1. **Police-Led** — Founder is an active Tourist Police officer. No other East Java operator has this.
2. **100% Private** — Every tour: dedicated vehicle, driver, guide. No shared groups, ever.
3. **Medical Screening** — Mandatory Ijen health check by Dr. Ahmad Irwandanu, included in price.
4. **Verifiable Licenses** — NIB, TDUP, HPWKI, POLPAR, BBKSDA, ISIC. All checkable.
5. **No Hidden Costs** — Transport, accommodation+breakfast, entrance fees, Bromo jeep, screening+gear, water, T-shirt.
6. **Transparency-First** — "Read the Rulebook Before You Book." Policies published upfront.

---

## Directory Structure

    llm-wiki/
    raw/                  # Immutable source docs. LLM reads, NEVER writes here.
      FINANCE/            # Tour package cost spreadsheets + rate card JSONs
      _manifest/          # Intake governance: 13 tracking/registry files (LLM-maintained exception to raw/ immutability)
    Clippings/            # Web clips from Obsidian Web Clipper. Treat as sources.
    templates/            # Obsidian page templates
    bases/                # Obsidian Bases (.base) — auto-updating domain dashboards (read-only views over wiki/ frontmatter)
    output/               # LLM-generated artifacts, organized by domain.
      website/            # All website artifacts
        pages/            # Page copy (homepage, tours, destinations, etc.)
        schema/           # JSON-LD structured data
        faq/              # FAQ answer pages
        aeo/              # AEO snippets
      social/             # Social media posts
      whatsapp/           # WA dashboard output
      marketing/          # Campaign output
      finance/            # Profit reports, custom tour quotes
      _archive/           # Superseded files
    wiki/
        overview.md       # Master synthesis
        index.md          # Content catalog — AI entry point
        log.md            # Append-only operations log
        destinations/     # One page per destination
        reviews/          # Review compilations + pattern analysis
        products/         # Tour packages, pricing, itineraries
        people/           # Founder, doctor, guides, drivers
        credentials/      # Licenses, safety compliance, trust signals
        sources/          # One summary page per ingested raw source
        website/          # Brand voice, FAQ master, AEO claims, copy bank, schemas
        seo/              # SEO strategy, GEO/AEO, competitors, redirect map
        whatsapp/         # WA ops playbook, rules engine, canned responses
        finance/          # Rate cards, package costs, profit analysis, custom tour builder
        marketing/        # Future: campaigns, ad copy
        analytics/        # Future: metrics, tracking
        internal-ops/     # Future: SOPs, training
        ops/              # Meta-workflows: ingestion, compilation, health checks
    docs/                 # Documentation (Diataxis framework)
      tutorial-first-ingestion.md   # Walk through ingesting a source end-to-end
      howto-ingest-sources.md       # Step-by-step for each ingestion profile
      howto-generate-output.md      # Step-by-step for each compilation profile
      howto-health-checks.md        # On-demand, weekly, monthly audit procedures
      reference-wiki-structure.md   # Directory map, frontmatter, domains, templates
      reference-scripts.md          # Python extraction pipeline (7 scripts)
      explanation-architecture.md   # Why: SSOT pipeline, trust arch, design decisions
    CLAUDE.md             # This file

---

## Frontmatter Conventions

Every wiki page starts with:

    ---
    type: destination|reviews|product|person|credential|website|source|overview|ops|seo|whatsapp|finance
    title: Human-readable title
    last_updated: YYYY-MM-DD
    sources: [slug1, slug2]
    ---

---

## Workflow 1: Ingest

1. **Read** the source fully
2. **Discuss** key takeaways with user
3. **Write** wiki/sources/[slug].md — key facts, quotes, content angles
4. **Update** relevant domain pages (may touch 5-15 pages)
5. **Update** wiki/index.md
6. **Append** to wiki/log.md:

    ## [YYYY-MM-DD] ingest | Source Title
    Pages updated: [list]. Key additions: [brief].

7. **Commit**: `git add -A && git commit -m "ingest | Source Title"`

## Workflow 2: Query

1. Read wiki/index.md to find relevant pages
2. Read identified pages
3. Synthesize with citations e.g. -> [[reviews/trustpilot-compilation]]
4. File back valuable answers as new pages in wiki/website/

## Workflow 3: Lint

1. Scan for contradictions — flag with > Contradiction with [[other-page]]
2. Find orphan pages (no inbound links)
3. Flag stale claims with > [stale?]
4. Identify gap pages — concepts without their own page
5. Suggest new sources to fill gaps

## Workflow 4: Typed Ingest

Before beginning Workflow 1, declare source type from [[ops/ingestion-profiles]].
The profile supplies type-specific extraction targets and the wiki pages most likely to need updating.

## Workflow 5: Compilation Profile

Before generating output, select a profile from [[ops/compilation-profiles]].
State "Use the [profile] profile" to activate it. Save result to output/ using
the profile's filename convention.

## Workflow 6: Health Check

Tiered audit procedure — see [[ops/health-checks]] for full checklists.
Triggers: "Run health check" (on-demand), "Run weekly health check",
"Run monthly health check". Append report to wiki/log.md after each run.

---

## Content Production Guidelines

- **Voice**: Direct, evidence-led. "Tourist Police officer" not "safety-focused guide."
- **Language**: English for tourist copy; Bahasa Indonesia fine for internal notes
- **Claims**: Always cite a wiki source. Never invent credentials or statistics.
- **AEO format**: Structure FAQ answers as direct, quotable statements
- **Trust signals**: NIB 1102230032918, POLPAR, BBKSDA, Trustpilot Excellent, Dr. Irwandanu SIP, founded 2015

## Cross-Reference Conventions

- Link wiki pages: [[folder/page-name]]
- In prose, use -> before links: -> [[destinations/kawah-ijen]]
- Always update wiki/index.md after changes

---

## Current Sprint

**Last completed:** Obsidian Bases infrastructure — 3 PRs merged in sequence: (#7) added 7 domain dashboards in `bases/` (index, destinations, sources, products, people, credentials, ops-health) w/ null-guarded formulas; (#8) Phase B frontmatter normalization via `scripts/frontmatter_normalize.py` — added `owner: wiki-llm` + per-type `stale_after_days` (source=90, finance=30, ops=120, else=60) across 97 wiki pages + backfilled `pages_updated` for 35 source pages via reverse-link grep; (#9) fixed orphan source aliases — created umbrella `wiki/sources/backoffice-mysql.md` so the 14 downstream pages citing slug `backoffice-mysql` reach the 8 split files, back-linked the 8 splits, absorbed 7 bases linter rewrites (formatting-only). Orphan source count: 9 → 1. Normalizer idempotent (Files changed: 0).
**Completed date:** 2026-06-01
**Next task:** NOT STARTED — awaiting selection. Top 3 immediate candidates: (a) attribute `wiki/sources/3d-route-viewer.md` to absorbing destination pages OR mark auxiliary (final orphan); (b) delete root `BASE.base` stub (superseded by `bases/index.base`); (c) slim `wiki/index.md` (191 lines, ~10 sections replaceable by Bases embeds). Longer wedges still open below.
**Build status:** — wiki-only (no code build). YAML parse OK on all 7 bases; normalizer idempotent.
**Open items:**
- **URGENT**: Homepage H2 "92 on Google Maps" stale — now 123. Fix in jvto-web (not Trust-Bundle-related).
- R065 gap #1: verify JVTO website Terms checkbox (Step 15) shows Travel Credit policy text.
- R065 gap #2: price anomaly IDR 3,350,000 vs SSOT — Sam to verify pax tier / discount (compiler now emits package-pricing.json for cross-check).
- `3d-route-viewer` last orphan source — needs attribution to destinations (likely mount-bromo + kawah-ijen) or auxiliary mark.
- Root `BASE.base` stub still present (3-line dead file; superseded but not deleted per prior phase scope).
- `wiki/index.md` slim deferred — manual catalog still 191 lines; Bases embeds available via `bases/*.base`.
- Package Readiness residual limits: `instant_book=True` derived from sitemap presence (not per-package checkout probe); PKG-11 count-based; full-repo wording sweep deferred to Global Validator wedge.
- robots.txt Cloudflare/custom conflict — contradictory AI crawler directives.
- `bromo-ijen-status-today` page — Silo 3 SEO target; blocked on replacement live PVMBG status source.
- Geographic landing pages (/markets/singapore, /markets/malaysia) — need flight/logistics data.
- `yadnya-kasada-2026` — need Tengger calendar source.

**Next-phase candidates (not started — pick one):** (1) Policy Bundle; (2) WhatsApp Reply Intelligence; (3) Review Proof Index; (4) Finance Quote Helper; (5) Global Wiki Validator. Priority order in `wiki/ops/transformation-map.md`.

**Resolved (do not reopen):** Trust Bundle v1, Policy Source Ownership, R065 Booking Flow, Transformation Map, Package Readiness Compiler (v1 → v1.2, full 6-artifact bundle), Obsidian Bases v1 (7 dashboards), Phase B frontmatter normalization (owner / stale_after_days / pages_updated), Backoffice source alias coverage — all DONE. Trust Bundle: DEC-001/002/003 locked, CONF-001/002/003 resolved, F1–F8 pass, outputs pushed, jvto-web `/trust` integrated; DQ-001/002/003 resolved via DEC locks. See `wiki/ops/transformation-map.md` §do-not-reopen.

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.

Key routing rules:
- Product ideas/brainstorming → invoke /office-hours
- Strategy/scope → invoke /plan-ceo-review
- Architecture → invoke /plan-eng-review
- Design system/plan review → invoke /design-consultation or /plan-design-review
- Full review pipeline → invoke /autoplan
- Bugs/errors → invoke /investigate
- QA/testing site behavior → invoke /qa or /qa-only
- Code review/diff check → invoke /review
- Visual polish → invoke /design-review
- Ship/deploy/PR → invoke /ship or /land-and-deploy
- Save progress → invoke /context-save
- Resume context → invoke /context-restore
