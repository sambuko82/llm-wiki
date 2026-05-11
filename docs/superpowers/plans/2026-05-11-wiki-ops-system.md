# Wiki Ops System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ingest the LLM KB Tooling Guide article as a source document, then build the `wiki/ops/` folder with Workflows 4–6 (typed ingestion profiles, compilation profiles, health checks) and wire them into CLAUDE.md and `wiki/index.md`.

**Architecture:** Phase 1 follows existing Workflow 1 (ingest). Phase 2 creates `wiki/ops/` with three new pages, adds a new `## Ops` section to `wiki/index.md`, and appends Workflows 4–6 stubs to `CLAUDE.md`. All changes are markdown-only — no scripts, no external dependencies.

**Tech Stack:** Plain markdown, Obsidian wikilinks, git

---

## File Map

| Action | Path | Purpose |
|--------|------|---------|
| Create | `raw/llm-kb-tooling-guide.md` | Immutable source — full article text |
| Create | `wiki/sources/llm-kb-tooling-guide.md` | Workflow 1 source summary page |
| Create | `wiki/ops/ingestion-profiles.md` | Workflow 4: typed source handlers |
| Create | `wiki/ops/compilation-profiles.md` | Workflow 5: named output profiles |
| Create | `wiki/ops/health-checks.md` | Workflow 6: tiered audit checklists |
| Modify | `wiki/index.md` | Add source entry + `## Ops` section; total_pages 24→28 |
| Modify | `wiki/log.md` | Append two log entries (ingest + build) |
| Modify | `CLAUDE.md` | Add `wiki/ops/` to dir structure; add Workflows 4–6 stubs; add `ops` to frontmatter types |

---

## Task 1: Save article to raw/

**Files:**
- Create: `raw/llm-kb-tooling-guide.md`

- [ ] **Step 1: Create the raw source file**

Create `raw/llm-kb-tooling-guide.md` with this exact content:

```markdown
# LLM Knowledge Base Tooling Guide

*Source: article pasted 2026-05-11. Immutable — do not edit.*

---

## Tools & Ecosystem

Several tools and projects already align with Karpathy's vision. Here's the current landscape:

### Obsidian + AI Plugins

Obsidian (1.5M+ users) is the foundation of Karpathy's setup. The Obsidian CEO, Steph Ango (kepano), responded to Karpathy's post suggesting developers keep personal vaults clean and create separate vaults for agent-generated content — preventing contamination of human-curated knowledge.

Obsidian Skills, a project by kepano, teaches AI agents to work with Obsidian's native formats: [[wikilinks]], callouts, Bases, and Canvas. It's the interface layer between AI agents and your vault.

### Knowledge Base Tools

| Tool | What It Does | Best For |
|------|-------------|---------|
| Notemd | Chunks docs, auto-generates wiki-links, creates concept notes | Obsidian users wanting AI-powered linking |
| AI Knowledge Filler | Generates structured files with validated YAML and WikiLinks | Generating Obsidian-ready content from LLMs |
| library-mcp | MCP server for exploring Markdown KBs through Claude Desktop | Querying existing knowledge bases via AI |
| Obsidian Skills | Agent skills for Markdown, Bases, Canvas, CLI | Teaching AI agents Obsidian-native formats |
| LLM Workspace | Integrates local LLMs directly into Obsidian vaults | Private, offline knowledge work |

### MCP Servers for Knowledge

The MCP ecosystem is growing fast with knowledge-focused servers. Servers like gnosis-mcp load markdown docs into SQLite for AI search, while library-mcp lets you explore markdown KBs through Claude Desktop. These turn your knowledge base into a tool that any AI assistant can use.

---

## How to Build Your Own LLM Knowledge Base

You don't need Karpathy's setup to start. Here's a practical approach using tools available today:

### The Minimum Viable Knowledge Base

**Directory structure:**

```
my-research/
  raw/                # Source documents (articles, papers, notes)
    article-1.md
    paper-2.md
    images/
  wiki/               # LLM-compiled wiki (don't edit manually)
    INDEX.md
    concepts/
      concept-a.md
      concept-b.md
  output/             # Query results, slides, charts
  _meta/              # Compile state, config
```

### Step-by-Step Setup

1. **Install Obsidian + Web Clipper.** Obsidian is free and local-first. The Web Clipper extension lets you save any web article as a clean .md file with one click.

2. **Create your raw/ directory.** Start dropping in source material: articles you read, papers you reference, code snippets, images, screenshots. Clip web articles with Web Clipper, download images locally.

3. **Write a compilation prompt.** Give your AI agent a system prompt that tells it how to compile the wiki:

Example compilation prompt:

> You are a wiki compiler. Read all files in raw/ and compile them into wiki/ following these rules:
> 1. Identify all key concepts mentioned across documents
> 2. Create one .md article per concept in wiki/concepts/
> 3. Each article should summarize what raw/ says about it
> 4. Use [[wiki-links]] to connect related concepts
> 5. Update wiki/INDEX.md with a table of contents
> 6. Only process raw files modified since last compile
>
> Frontmatter for each article:
> ---
> title: Concept Name
> sources: [list of raw/ files referenced]
> related: [[linked-concepts]]
> last_compiled: 2026-04-03
> ---

4. **Run the compilation.** Point your agent at the directory and let it compile. For the first run, expect it to take time. After that, incremental builds are fast — only new or changed raw/ files get processed.

5. **Query your wiki.** Ask the agent questions like: "What are the key differences between X and Y based on the wiki?" or "Create a Marp slide deck summarizing the top 5 concepts."

6. **Run health checks.** Periodically ask the agent to audit the wiki: find contradictions, missing links, thin articles, and orphaned concepts.

### Agent Setup Tips

If you're using an agentic IDE, you can set up agent skills to automate the compilation. Create a skill that watches raw/ for changes and triggers incremental compilation. For multi-agent setups, dedicate one agent to ingestion, another to compilation, and a third to health checks.

---

## Advanced Patterns

Once the basic pipeline is working, these patterns take it further:

### Multi-Source Ingestion Pipeline

Go beyond manual clipping. Build automated ingestion from multiple source types:

- Web articles: Obsidian Web Clipper → raw/articles/
- PDFs (papers, reports): PDF → Claude Vision / pdf2md → raw/papers/
- YouTube videos: Transcript API → clean markdown → raw/videos/
- GitHub repos: Clone → README + key files → raw/repos/
- Podcasts / audio: Whisper → transcript → raw/audio/
- RSS feeds (automated): Cron + RSS parser → raw/feeds/

### Compilation Profiles

Different wikis need different compilation strategies. A research wiki should extract methodology and citations. A competitive intel wiki should extract pricing, features, and positioning. Define profiles with different compilation prompts:

- **Research profile:** Extract claims, evidence strength, methodology, citations, contradictions
- **Competitive profile:** Extract product features, pricing, positioning, team size, funding
- **Learning profile:** Extract concepts, prerequisites, difficulty levels, practical exercises
- **Decision log profile:** Extract decisions, alternatives considered, rationale, who decided, when

### Scheduled Health Checks

Don't wait for manual triggers. Set up scheduled health checks that run automatically:

- Daily: Check for new raw files and trigger incremental compilation
- Weekly: Run full consistency check across all articles
- Monthly: Web-verify facts in the wiki against current sources (catches outdated info)
- On-demand: Deep analysis for specific queries or decision points

### Cross-Wiki Linking

If you maintain multiple knowledge bases (e.g., one per project or research area), the LLM can find connections across them. A concept in your "ML Research" wiki might relate to something in your "Product Strategy" wiki. Cross-wiki health checks surface these non-obvious connections.

### Version Control Your Knowledge

Since the entire wiki is plain markdown, it works naturally with Git. Commit after each compilation run. This gives you:

- Full history of how your knowledge evolved
- Ability to diff between compilation runs
- Rollback if a compilation introduces errors
- Collaboration via branches and pull requests
- CI/CD for knowledge — automated health checks on every commit
```

- [ ] **Step 2: Verify the file exists**

```bash
ls "raw/llm-kb-tooling-guide.md"
```

Expected: file listed with no error.

- [ ] **Step 3: Verify immutability note is present**

```bash
grep -n "Immutable" raw/llm-kb-tooling-guide.md
```

Expected: `2:*Source: article pasted 2026-05-11. Immutable — do not edit.*`

---

## Task 2: Create wiki/sources/llm-kb-tooling-guide.md

**Files:**
- Create: `wiki/sources/llm-kb-tooling-guide.md`

- [ ] **Step 1: Create the source summary page**

Create `wiki/sources/llm-kb-tooling-guide.md` with this exact content:

```markdown
---
type: source
title: LLM Knowledge Base Tooling Guide (Karpathy-Inspired Patterns)
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# LLM Knowledge Base Tooling Guide

**Source type:** web-clip (manually captured article)
**Captured:** 2026-05-11
**Topic:** Building LLM-native knowledge bases — tools, patterns, directory structure, operational workflows

## Key Facts

- Core pattern validated: `raw/` (immutable source) → LLM compilation → `wiki/` (agent-maintained) → `output/` (derived artifacts) — matches JVTO's existing structure
- Obsidian CEO (Steph Ango) recommends separate vaults for agent-generated content to prevent contamination of human-curated knowledge
- MCP servers like gnosis-mcp load markdown docs into SQLite for AI search; library-mcp lets Claude Desktop query markdown KBs via structured tools
- Typed ingestion: naming source types (web-clip, pdf-doc, review-feed) and defining per-type extraction targets reduces missed signals
- Compilation profiles: different prompt strategies per output type (AEO, website copy, FAQ, social) produce more consistent results than generic prompts
- Tiered health checks: on-demand (lint), weekly (stale + orphan), monthly (web-verify credentials) — distinct triggers and checklists per tier
- Version control as knowledge history: git commit after each compilation run gives full rollback and diff capability

## Applicable Patterns for JVTO Wiki

1. **Typed ingestion (Workflow 4)** — declare source type (web-clip, pdf-doc, ssot-update, review-feed, press-clip) before Workflow 1; each type has defined extraction targets and default wiki pages to update
2. **Compilation profiles (Workflow 5)** — named profiles (aeo, website-copy, faq, social, slide-deck) specify which wiki pages to draw from, output format, voice constraints, and filename convention
3. **Tiered health checks (Workflow 6)** — on-demand replaces Workflow 3 (Lint); weekly adds stale sweep + index/log completeness; monthly adds credential web-verification + review count delta

## Not Applicable

- Multi-agent setups (single LLM session workflow)
- MCP server integration (CLAUDE.md-only implementation chosen)
- Cross-vault linking (single vault)
- Automated/scheduled triggers (CLAUDE.md-only; no scripts)

## Related Pages

- -> [[ops/ingestion-profiles]] (Workflow 4, derived from this source)
- -> [[ops/compilation-profiles]] (Workflow 5, derived from this source)
- -> [[ops/health-checks]] (Workflow 6, derived from this source)
```

- [ ] **Step 2: Verify frontmatter**

```bash
grep -n "type: source" wiki/sources/llm-kb-tooling-guide.md
```

Expected: `2:type: source`

- [ ] **Step 3: Verify related pages links are present**

```bash
grep -n "ops/" wiki/sources/llm-kb-tooling-guide.md
```

Expected: 3 lines, one for each ops page.

---

## Task 3: Update wiki/index.md — source entry + total_pages

**Files:**
- Modify: `wiki/index.md`

- [ ] **Step 1: Update frontmatter — add source slug and increment total_pages**

In `wiki/index.md`, change line 6:
```
sources: [ssot-v6, jvto-homepage-clip, trustpilot-reviews-2026, detik-polpar-2021]
```
to:
```
sources: [ssot-v6, jvto-homepage-clip, trustpilot-reviews-2026, detik-polpar-2021, llm-kb-tooling-guide]
```

And change line 5:
```
total_pages: 24
```
to:
```
total_pages: 28
```

(4 new pages: sources/llm-kb-tooling-guide + ops/ingestion-profiles + ops/compilation-profiles + ops/health-checks)

- [ ] **Step 2: Add source entry to Sources section**

In `wiki/index.md`, after the line:
```
- [[sources/detik-polpar-2021]] — Detik.com article (2021-03-14). Independent national media confirmation of Bripka Agung Sambuko as active Polpar. Direct quotes in Bahasa Indonesia.
```

Add:
```
- [[sources/llm-kb-tooling-guide]] — LLM KB Tooling Guide (2026-05-11). Karpathy-inspired patterns: typed ingestion, compilation profiles, health check tiers. Basis for Workflows 4–6.
```

- [ ] **Step 3: Verify total_pages updated**

```bash
grep -n "total_pages" wiki/index.md
```

Expected: `5:total_pages: 28`

- [ ] **Step 4: Verify new source entry present**

```bash
grep -n "llm-kb-tooling-guide" wiki/index.md
```

Expected: at least 2 hits (frontmatter + Sources section).

---

## Task 4: Append Phase 1 ingest log entry + commit

**Files:**
- Modify: `wiki/log.md`

- [ ] **Step 1: Prepend ingest log entry to wiki/log.md**

In `wiki/log.md`, after the opening `---` separator (after line 12), insert:

```markdown
## [2026-05-11] ingest | LLM KB Tooling Guide

**Source type**: web-clip (manually captured article)
**Raw file**: `raw/llm-kb-tooling-guide.md`

**Pages created (1)**:
- [[sources/llm-kb-tooling-guide]] — Karpathy-inspired LLM KB patterns; key facts, applicable patterns, not-applicable list

**Pages updated (1)**:
- [[index]] — sources list + total_pages 24→28 (anticipating Phase 2 ops pages); llm-kb-tooling-guide source entry added

**Key findings**:
- JVTO's existing raw/ → wiki/ → output/ structure already matches the article's recommended pattern
- Three actionable patterns identified: typed ingestion (Workflow 4), compilation profiles (Workflow 5), tiered health checks (Workflow 6)
- MCP server and automation options explicitly deferred — CLAUDE.md-only implementation chosen

**Verification**:
- ✅ raw/llm-kb-tooling-guide.md created with immutability note
- ✅ wiki/sources/llm-kb-tooling-guide.md frontmatter correct
- ✅ wiki/index.md sources list updated; total_pages 24→28

---
```

- [ ] **Step 2: Verify log entry is present**

```bash
grep -n "LLM KB Tooling Guide" wiki/log.md
```

Expected: at least one hit near the top of the file.

- [ ] **Step 3: Commit Phase 1**

```bash
git add raw/llm-kb-tooling-guide.md wiki/sources/llm-kb-tooling-guide.md wiki/index.md wiki/log.md
git commit -m "ingest | LLM KB Tooling Guide"
```

Expected: commit succeeds, 4 files changed.

---

## Task 5: Create wiki/ops/ingestion-profiles.md

**Files:**
- Create: `wiki/ops/ingestion-profiles.md`

- [ ] **Step 1: Create the file**

Create `wiki/ops/ingestion-profiles.md` with this exact content:

```markdown
---
type: ops
title: Ingestion Profiles — Workflow 4
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# Ingestion Profiles

*Workflow 4: declare source type before beginning Workflow 1 step 1.*

Select the profile matching your source. The profile supplies type-specific extraction targets and the wiki pages most likely to need updating. All other Workflow 1 steps remain unchanged.

---

## web-clip

**What it is:** Article, blog post, or web page saved via Obsidian Web Clipper or manually pasted.

**Raw slug:** `YYYY-MM-DD-[site]-[topic].md` (e.g., `2026-05-11-detik-polpar-coverage.md`)

**Extract:**
- Voice/tone exemplars and verbatim quotable phrases
- Claims that corroborate or contradict existing wiki facts
- Any new statistics, ratings, or credentials mentioned

**Wiki pages to update:** `sources/[slug]`, `content/copy-bank` (if new voice exemplars found), relevant `destinations/` or `credentials/` pages if new facts surface

---

## pdf-doc

**What it is:** PDF document — policy pack, government regulation, certificate, or report.

**Raw slug:** `[doc-name]-v[N].md` (e.g., `jvto-policy-pack-v6.md`)

**Extract:**
- Structured facts, policy text verbatim, credential details
- Version delta from prior version if updating an existing source
- Any new license numbers, dates, or named officials

**Wiki pages to update:** `sources/[slug]`, `credentials/legal-licenses`, `credentials/trust-signals`, `products/packages-overview` (if pricing or inclusions changed)

---

## ssot-update

**What it is:** A new version of the JVTO SSOT JSON (canonical structured data, 13 domains).

**Raw slug:** `ssot-v[N].md` (e.g., `ssot-v7.md`)

**Extract:**
- Full diff against prior SSOT version — note every changed field
- New or removed packages, pricing changes, credential updates, personnel changes

**Wiki pages to update:** All domain pages — treat as a full wiki audit. Update `overview`, `products/packages-overview`, all `destinations/`, `people/`, `credentials/`, and `index`. Create `sources/ssot-v[N]` and add a deprecation note to the prior SSOT source page.

---

## review-feed

**What it is:** A new batch of Trustpilot reviews (or other platform) since the last ingest.

**Raw slug:** `[platform]-reviews-YYYY.md` (e.g., `trustpilot-reviews-2027.md`)

**Extract:**
- New reviews not already in `reviews/trustpilot-compilation` — cross-check by reviewer name and date
- Guide and driver names mentioned — add to crew name index if new
- Rating delta from previous ingest
- Any new complaint patterns or standout praise patterns

**Wiki pages to update:** `sources/[slug]`, `reviews/trustpilot-compilation`, `reviews/review-patterns`, `credentials/trust-signals` (update rating and review count)

---

## press-clip

**What it is:** News article, guidebook mention, or media coverage of JVTO.

**Raw slug:** `[outlet]-YYYY-MM-DD.md` (e.g., `kompas-2026-03-15.md`)

**Extract:**
- Publication name, date, journalist name if given
- Key quote verbatim in original language
- Topic: police-led, safety, destination feature, or award
- Whether it is independent or paid placement

**Wiki pages to update:** `sources/[slug]`, `credentials/trust-signals`, `credentials/press-coverage` (create this page if it does not exist — it is a tracked gap page)
```

- [ ] **Step 2: Verify all five source types are present**

```bash
grep -n "^## " wiki/ops/ingestion-profiles.md
```

Expected output:
```
3:# Ingestion Profiles
10:## web-clip
22:## pdf-doc
34:## ssot-update
46:## review-feed
59:## press-clip
```

---

## Task 6: Create wiki/ops/compilation-profiles.md

**Files:**
- Create: `wiki/ops/compilation-profiles.md`

- [ ] **Step 1: Create the file**

Create `wiki/ops/compilation-profiles.md` with this exact content:

```markdown
---
type: ops
title: Compilation Profiles — Workflow 5
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# Compilation Profiles

*Workflow 5: state "Use the [profile] profile" before any content generation request.*

Each profile specifies which wiki pages to read, the output format, voice constraints, and the filename convention for saving to `output/`. Always cite the wiki source for every claim in the generated output.

---

## aeo

**Purpose:** Answer Engine Optimization — structured Q&A blocks for AI search ingestion.

**Draw from:** `content/aeo-claims`, `content/faq-master`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- One Q&A pair per block
- Question: ≤15 words, direct (e.g., "Is Java Volcano Tour Operator licensed?")
- Answer: ≤40 words, citable, starts with a direct claim
- Use the NLP atom structure from `content/aeo-claims` (C1–C9) as the template

**Forbidden:** hedging language ("may", "might", "could"), invented statistics, unsourced credential claims

**Output filename:** `output/aeo-YYYY-MM-DD-[topic].md`

---

## website-copy

**Purpose:** Hero paragraphs, section copy, and body text for javavolcano-touroperator.com.

**Draw from:** `content/copy-bank`, `content/brand-voice`, `destinations/[relevant]`, `products/packages-overview`

**Format:**
- Style A voice (direct, evidence-led — see `content/brand-voice` §Style-A)
- Hero: one punchy sentence + one credibility sentence
- Body: 2–4 sentences per paragraph, no bullet lists in hero sections
- All claims must trace to a wiki source; no invented statistics

**Forbidden:** invented statistics, passive voice in hero copy, "safety-focused guide" (use "Tourist Police officer"), superlatives without evidence

**Output filename:** `output/copy-YYYY-MM-DD-[page].md`

---

## faq

**Purpose:** FAQ pages — AEO-compatible, human-readable.

**Draw from:** `content/faq-master`, `products/packages-overview`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- H3 question heading
- Prose answer: 2–5 sentences, direct, citable
- Each answer ends with a trust signal where relevant (NIB, Trustpilot rating, doctor name)
- Answers must be self-contained — no reliance on adjacent questions for context

**Forbidden:** rhetorical questions, "great question!", invented pricing

**Output filename:** `output/faq-YYYY-MM-DD-[topic].md`

---

## social

**Purpose:** Social media captions, story copy, short-form posts.

**Draw from:** `content/copy-bank`, `reviews/trustpilot-compilation` (for verbatim quotes), `content/brand-voice`

**Format:**
- Style B voice (warmer, still direct — see `content/brand-voice` §Style-B)
- Quote-led: open with a verbatim review excerpt, cite reviewer name if given; or
- Claim-led: open with the strongest differentiator for this post's topic
- ≤280 characters for Twitter/X; ≤150 words for Instagram caption
- End with a call to action or question

**Forbidden:** invented quotes, hashtag spam (≤3 hashtags per post)

**Output filename:** `output/social-YYYY-MM-DD-[topic].md`

---

## slide-deck

**Purpose:** Marp-compatible markdown slide decks for presentations or pitches.

**Draw from:** `wiki/overview` by default + any domain pages specified in the request

**Format:**
- Marp frontmatter: `marp: true`, `theme: default`
- One claim per slide — no bullet walls
- Each slide: headline + ≤30 words of supporting text + one evidence anchor (source, stat, or quote)
- Title slide and summary slide required in every deck

**Forbidden:** slides with >3 bullet points, unsourced claims, placeholder images

**Output filename:** `output/slides-YYYY-MM-DD-[topic].md`
```

- [ ] **Step 2: Verify all five profiles are present**

```bash
grep -n "^## " wiki/ops/compilation-profiles.md
```

Expected output:
```
3:# Compilation Profiles
12:## aeo
27:## website-copy
42:## faq
57:## social
72:## slide-deck
```

---

## Task 7: Create wiki/ops/health-checks.md

**Files:**
- Create: `wiki/ops/health-checks.md`

- [ ] **Step 1: Create the file**

Create `wiki/ops/health-checks.md` with this exact content:

```markdown
---
type: ops
title: Health Checks — Workflow 6
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# Health Checks

*Workflow 6: tiered audit procedure. Append a short report to `wiki/log.md` after each run under `## [YYYY-MM-DD] health-check | [tier]`.*

---

## On-Demand

**Trigger:** "Run health check"

This is the updated name for Workflow 3 (Lint). Same procedure, now formally documented with the full checklist.

1. **Contradiction scan** — read all wiki pages; flag any claim that directly contradicts a claim on another page with `> Contradiction with [[other-page]]: <detail>`
2. **Orphan detection** — list all wiki pages with no inbound `[[wikilinks]]` from other pages; flag each as `> Orphan: no inbound links`
3. **Stale claim flags** — flag claims referencing a specific date, rating, or statistic where the sourcing page has `last_updated` >90 days ago: `> [stale?] <claim>`
4. **Gap page identification** — list concepts referenced in multiple pages that have no dedicated wiki page; add to the "Open Gaps" section of `wiki/index.md`
5. **Append report to `wiki/log.md`**

---

## Weekly

**Trigger:** "Run weekly health check"

Run all on-demand checks, plus:

1. **30-day stale sweep** — flag any claim referencing a date or rating where the sourcing page has `last_updated` >30 days ago; use `> [stale?]` inline on the claim
2. **New orphan detection** — check for pages created since the last log entry that have no inbound links from any page other than `wiki/index.md`
3. **Index completeness** — verify every `.md` file under `wiki/` (excluding `index.md`, `log.md`, `overview.md`) has a corresponding entry in `wiki/index.md`; list any missing entries in the report
4. **Log completeness** — verify every file under `raw/` has a corresponding `## [date] ingest | [title]` entry in `wiki/log.md`; list any raw files with no log entry

---

## Monthly

**Trigger:** "Run monthly health check"

Run all weekly checks, plus:

1. **Credential web-verification** — use web search to verify:
   - NIB 1102230032918 is still active (OSS Indonesia registry)
   - Trustpilot rating and review count against values recorded in `wiki/credentials/trust-signals`
   - Bripka Agung Sambuko's Polpar status against the evidence chain in `wiki/people/agung-sambuko`
   Flag any discrepancy inline with `> [stale?] Web-check [date]: <finding>`

2. **Trustpilot new review sweep** — compare current Trustpilot review count against the count recorded in `wiki/reviews/trustpilot-compilation`; if >2 new reviews exist that have not been ingested, add to the report: `> Action needed: [N] new Trustpilot reviews since last review-feed ingest`

3. **Gap page audit** — for each entry in the "Open Gaps" section of `wiki/index.md`, check if a page now exists; remove entries that have been filled and note them in the report

4. **Output staleness** — list all files under `output/` with a date in the filename >90 days old; flag each with `> [stale?] Output may no longer reflect current wiki`
```

- [ ] **Step 2: Verify all three tiers are present**

```bash
grep -n "^## " wiki/ops/health-checks.md
```

Expected output:
```
3:# Health Checks
10:## On-Demand
25:## Weekly
38:## Monthly
```

---

## Task 8: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add `ops/` line to directory structure**

In `CLAUDE.md`, find the directory structure block. After the line:
```
        sources/          # One summary page per ingested raw source
```
Add:
```
        ops/              # Operational workflow detail pages (Workflows 4–6)
```

- [ ] **Step 2: Add `ops` to frontmatter type list**

In `CLAUDE.md`, find:
```
    type: destination|reviews|product|person|credential|content|source|overview
```
Change to:
```
    type: destination|reviews|product|person|credential|content|source|overview|ops
```

- [ ] **Step 3: Add Workflows 4–6 after Workflow 3**

In `CLAUDE.md`, find the block ending with:
```
4. Identify gap pages — concepts without their own page
5. Suggest new sources to fill gaps
```

After that block (before the `---` separator), add:

```
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
```

- [ ] **Step 4: Verify ops/ appears in directory structure**

```bash
grep -n "ops/" CLAUDE.md
```

Expected: at least 4 hits (directory structure + 3 workflow references).

- [ ] **Step 5: Verify Workflow 6 is present**

```bash
grep -n "Workflow 6" CLAUDE.md
```

Expected: `Workflow 6: Health Check` line present.

- [ ] **Step 6: Verify frontmatter type list updated**

```bash
grep -n "ops" CLAUDE.md | grep "type:"
```

Expected: line containing `type: destination|...|ops`

---

## Task 9: Update wiki/index.md — Ops section

**Files:**
- Modify: `wiki/index.md`

- [ ] **Step 1: Add Ops section after Content Production section**

In `wiki/index.md`, find the section heading:
```
## Open Gaps (no page yet — flagged by Lint)
```

Before that heading, insert:

```markdown
## Ops

- [[ops/ingestion-profiles]] — Workflow 4: typed source handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip)
- [[ops/compilation-profiles]] — Workflow 5: named output profiles (aeo, website-copy, faq, social, slide-deck)
- [[ops/health-checks]] — Workflow 6: on-demand, weekly, and monthly audit checklists

```

- [ ] **Step 2: Verify Ops section is present**

```bash
grep -n "## Ops" wiki/index.md
```

Expected: one hit with the `## Ops` heading.

- [ ] **Step 3: Verify all three ops pages are linked**

```bash
grep -n "ops/" wiki/index.md
```

Expected: 3 hits (one per ops page).

---

## Task 10: Append Phase 2 log entry + final commit

**Files:**
- Modify: `wiki/log.md`

- [ ] **Step 1: Prepend Phase 2 build log entry**

In `wiki/log.md`, after the opening `---` separator, insert (above the Phase 1 ingest entry added in Task 4):

```markdown
## [2026-05-11] build | Wiki Ops System — Workflows 4–6

**Spec**: `docs/superpowers/specs/2026-05-11-wiki-ops-system-design.md`

**Pages created (3)**:
- [[ops/ingestion-profiles]] — Workflow 4: 5 source type handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip)
- [[ops/compilation-profiles]] — Workflow 5: 5 named profiles (aeo, website-copy, faq, social, slide-deck) with draw-from lists, format constraints, forbidden patterns, output filename conventions
- [[ops/health-checks]] — Workflow 6: 3-tier audit (on-demand replaces Workflow 3/Lint, weekly adds stale sweep + completeness checks, monthly adds credential web-verification)

**Files modified (2)**:
- [[index]] — Ops section added; total_pages confirmed at 28
- `CLAUDE.md` — `wiki/ops/` added to dir structure; `ops` added to frontmatter type list; Workflows 4–6 stubs added after Workflow 3

**Verification**:
- ✅ 3 ops pages created with correct frontmatter (type: ops)
- ✅ All 5 ingestion profiles present in ingestion-profiles.md
- ✅ All 5 compilation profiles present in compilation-profiles.md
- ✅ All 3 health check tiers present in health-checks.md
- ✅ wiki/index.md Ops section links all 3 pages
- ✅ CLAUDE.md Workflows 4–6 wired; ops/ in directory structure

---
```

- [ ] **Step 2: Verify build log entry is present**

```bash
grep -n "Wiki Ops System" wiki/log.md
```

Expected: hit near the top of the file.

- [ ] **Step 3: Final commit**

```bash
git add wiki/ops/ingestion-profiles.md wiki/ops/compilation-profiles.md wiki/ops/health-checks.md wiki/index.md wiki/log.md CLAUDE.md
git commit -m "build | Wiki Ops System — Workflows 4–6 (ingestion profiles, compilation profiles, health checks)"
```

Expected: commit succeeds, 6 files changed.

- [ ] **Step 4: Verify clean working tree**

```bash
git status
```

Expected: `nothing to commit, working tree clean`
