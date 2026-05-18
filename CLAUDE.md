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
    Clippings/            # Web clips from Obsidian Web Clipper. Treat as sources.
    templates/            # Obsidian page templates
    output/               # LLM-generated artifacts: website copy drafts, FAQ pages,
                          # AEO snippets, slide content, etc. Never canonical — derived
                          # from wiki/content/ on demand. Safe to delete and regenerate.
    wiki/
        overview.md       # Master synthesis
        index.md          # Content catalog — AI entry point
        log.md            # Append-only operations log
        destinations/     # One page per destination
        reviews/          # Review compilations + pattern analysis
        products/         # Tour packages, pricing, itineraries
        people/           # Founder, doctor, guides, drivers
        credentials/      # Licenses, safety compliance, trust signals
        content/          # Brand voice, FAQ master, AEO claims, copy bank
        sources/          # One summary page per ingested raw source
        ops/              # Operational workflow detail pages (Workflows 4–6)
    CLAUDE.md             # This file

---

## Frontmatter Conventions

Every wiki page starts with:

    ---
    type: destination|reviews|product|person|credential|content|source|overview|ops
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
4. File back valuable answers as new pages in wiki/content/

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

**Last completed:** Repo hygiene pass — MAGMA feed removal cleanup. Removed magma-report ingestion profile, fixed 4 downstream wiki refs, added stale flags to 3 output files, fixed dead volcano-status.md ref in jvto-verified-output skill. Committed dirty files. Open Gaps updated. System internally consistent.
**Completed date:** 2026-05-18
**Next task:** Verify faq/papuma.md pricing figures (IDR 5,100,000 / 4,900,000) against wiki/products/packages-full-pricing.md, then ingest full itinerary for taman-safari-prigen-bromo-madakaripura-3d2n into wiki/products/packages-itineraries.md and regenerate its stub schema.
**Build status:** — no code changes
**Open items:**
- `faq/papuma.md` pricing ⚠ — IDR figures unverified; check packages-full-pricing.md before publishing
- `taman-safari-prigen-bromo-madakaripura-3d2n` schema stub — needs full day-by-day itinerary ingested into `wiki/products/packages-itineraries.md`
- `priceRange` not yet added to homepage Organization schema — needs packages-full-pricing.md pass
- Tour hero image URLs missing from all 16 TouristTrip schemas — not yet in ssot-image-asset-map
- `raw/routes.csv` + `raw/route_details.csv` — unclassified; verify overlap with db-export before ingesting
- `bromo-ijen-status-today` page — Silo 3 SEO target; blocked on replacement live source for PVMBG status
- TouristAttraction + BreadcrumbList schemas not yet generated (5 destination pages)
