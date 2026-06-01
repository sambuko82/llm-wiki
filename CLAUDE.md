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

**Last completed:** Phase 2 optimization (commit `e0982fc`) — closed GAP-01/02/07 per source authority (cross-platform reviewCount 164→195 in `trust-signals.md` + `HANDOFF.md` + `homepage-organization-schema.json` + receipt + `schema-templates.md`; IDR 3,350,000 confirmed canonical for `bali/bromo-ijen-3d2n` 6–7 pax; "Transport to Medewi" add-on unauthorized per `packages-overview.md`), strengthened `website-context-master.md` (KBLI codes + Dr STR + BBKSDA citation + bank accounts in §1.2; `/team` + `/team/[slug]` + `/tours/student-package/*` in §2.1; canonical sentences in §3.1/§3.3/§3.6/§3.9; new §3.11 Solo-Pricing Rule + §3.12 Tipping Rule; bestRating/worstRating schema checks), reconciled canonical package count to **15 SSOT + 1 specialty = 16 commercial + 6 student = 22 priced** across `packages-full-pricing.md` / `wiki/index.md` / `HANDOFF.md`, removed Tumpak Sewu helmet self-contradiction in `operational-facts.md`, promoted v5 canonical-version note in `jvto-policy-pack-v6.md`. Workflow gap-reclassification (read-only) verified zero true `BLOCKED BY MISSING SOURCE` remain: GAP-03/04/05 are EXECUTION-OUT-OF-SCOPE BUT LOGIC-RESOLVABLE (canonical wording in repo, only live UI/jvto-web deployment outside scope); GAP-06/08/09 are STATIC-FALLBACK-SOURCEABLE (closure schedules, Plan-B SOP, JVTO differentiators, country-tagged reviews all in repo; only live feeds + flight data outside scope).
**Completed date:** 2026-06-01
**Next task:** Fix `output/website/pages/homepage.md:183` — still carries stale "92 on Google Maps" (jvto-web deployment will mirror this); change to "123 on Google Maps". Then publish static fallback v1 of one of: (a) `/travel-guide/bromo-ijen-status-today` (closure schedule + Plan-B SOP + alert-level meanings + authority URLs from `operational-facts.md` + `mount-bromo.md`), (b) `/travel-guide/yadnya-kasada-2026` (definition + impact + Plan-B SOP minus exact 2026 date), (c) `/markets/singapore` + `/markets/malaysia` v1 (differentiators + 3D2N package + entry choice + country-tagged reviews; defer flight schedules to v2). Use `seo/seo-strategy.md` §Silo 3 + §Geographic Landing Pages for spec.
**Build status:** — wiki-only (no code build). 7/7 JSON files valid; master doc + schema verified; 9/9 price spot-checks match SSOT; 10/10 legal/trust identifiers cross-checked.
**Open items:**
- `output/website/pages/homepage.md:183` — stale "92 on Google Maps" still in repo. In-repo fix possible (separate from jvto-web deployment).
- GAP-03 (EXECUTION-OUT-OF-SCOPE BUT LOGIC-RESOLVABLE): canonical Step 15 Terms wording defined in `jvto-policy-pack-v6.md` + master §3.3; only live UI verification of jvto-web checkout outside scope.
- GAP-04 (EXECUTION-OUT-OF-SCOPE BUT LOGIC-RESOLVABLE): post-booking screening workflow + 4-step protocol + conditional wording defined in `dr-ahmad-irwandanu.md` + master §3.1 + policies.json; only jvto-web confirmation-page notice + WhatsApp trigger wiring outside scope.
- GAP-05 (EXECUTION-OUT-OF-SCOPE BUT LOGIC-RESOLVABLE): canonical H2 = "123 on Google Maps" per `trust-signals.md`; `output/website/pages/homepage.md` still has stale 92 (in-repo fix); jvto-web deployment separate.
- GAP-06 (STATIC-FALLBACK-SOURCEABLE): `/travel-guide/bromo-ijen-status-today` static advisory shippable from `operational-facts.md` + `mount-bromo.md` + `kawah-ijen.md`; only live auto-refreshing PVMBG/MAGMA feed outside scope.
- GAP-08 (STATIC-FALLBACK-SOURCEABLE): `/travel-guide/yadnya-kasada-2026` static explainer shippable from `operational-facts.md` §Bromo Practical Facts + §Yadnya Kasada; only exact 2026 lunar date pending Tengger calendar ingest.
- GAP-09 (STATIC-FALLBACK-SOURCEABLE): `/markets/{singapore|malaysia}` v1 shippable from differentiators + 3D2N package + entry choice + country-tagged reviews; defer airline schedules + halal SOP to v2.
- `wiki/index.md` slim deferred — manual catalog ~196 lines; Bases embeds available.
- Package Readiness residual limits: `instant_book=True` derived from sitemap presence; PKG-11 count-based; full-repo wording sweep deferred to Global Validator wedge.
- robots.txt Cloudflare/custom conflict — contradictory AI crawler directives.

**Next-phase candidates (not started — pick one):** (1) Policy Bundle; (2) WhatsApp Reply Intelligence; (3) Review Proof Index; (4) Finance Quote Helper; (5) Global Wiki Validator. Priority order in `wiki/ops/transformation-map.md`.

**Resolved (do not reopen):** Trust Bundle v1, Policy Source Ownership, R065 Booking Flow, Transformation Map, Package Readiness Compiler (v1 → v1.2, full 6-artifact bundle), Obsidian Bases v1 (7 dashboards), Phase B frontmatter normalization, Backoffice source alias coverage, Final source orphan closure + root BASE.base removal, Website Context Consolidation v1 (master doc + 5 JSON exports + readiness.base), **Website Context Consolidation Phase 2 (GAP-01/02/07 closure + strengthen + canonical count reconciliation)**, **Gap Reclassification (zero true blockers remain)** — all DONE. Trust Bundle: DEC-001/002/003 locked, CONF-001/002/003 resolved, F1–F8 pass, outputs pushed, jvto-web `/trust` integrated. See `wiki/ops/transformation-map.md` §do-not-reopen.

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
