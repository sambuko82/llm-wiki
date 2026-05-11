# Wiki Ops System Design
**Date:** 2026-05-11
**Status:** Approved
**Scope:** Ingest LLM KB tooling article + add three operational workflows to the JVTO llm-wiki

---

## Summary

Two-phase work:
1. Ingest the LLM KB tooling article (Karpathy-inspired patterns guide) as a source document using existing Workflow 1.
2. Extend the wiki with a new `wiki/ops/` folder and Workflows 4–6 covering typed ingestion, compilation profiles, and health checks. CLAUDE.md gains short workflow stubs pointing to the ops pages.

Implementation is CLAUDE.md + markdown only — no scripts, no MCP servers.

---

## Deliverables

```
raw/
  llm-kb-tooling-guide.md              ← article saved as immutable source

wiki/
  ops/                                 ← new folder
    ingestion-profiles.md              ← Workflow 4: typed source handlers
    compilation-profiles.md            ← Workflow 5: named output profiles
    health-checks.md                   ← Workflow 6: tiered audit procedures
  sources/
    llm-kb-tooling-guide.md            ← Workflow 1 source summary page
  index.md                             ← gains "## Ops" section
  log.md                               ← ingest entry + build entry appended

CLAUDE.md                              ← gains Workflows 4–6 (stubs)
docs/superpowers/specs/
  2026-05-11-wiki-ops-system-design.md ← this file
```

---

## Phase 1: Ingest

Follow existing Workflow 1 steps:
1. Save article to `raw/llm-kb-tooling-guide.md`
2. Write `wiki/sources/llm-kb-tooling-guide.md` — key facts, patterns applicable to JVTO, content angles
3. Update `wiki/index.md` (sources section)
4. Append to `wiki/log.md`
5. Commit: `ingest | LLM KB Tooling Guide`

Source type for this article: `web-clip` (manually captured article content).

---

## Phase 2: Ops System

### Workflow 4 — Ingestion Profiles (`wiki/ops/ingestion-profiles.md`)

Extends Workflow 1 with a source type declaration. Declare type before step 1; the profile supplies type-specific extraction guidance and wiki page targets.

| Type | Raw slug convention | Key extraction targets | Wiki pages typically touched |
|------|--------------------|-----------------------|------------------------------|
| `web-clip` | `YYYY-MM-DD-[site]-[topic]` | Voice/tone exemplars, verbatim quotes, claims | `sources/`, `content/copy-bank`, `reviews/` |
| `pdf-doc` | `[doc-name]-v[N]` | Structured facts, credentials, policy text | `sources/`, `credentials/`, `products/` |
| `ssot-update` | `ssot-v[N]` | All 13 domains — full diff against prior version | All domain pages, `overview`, `index` |
| `review-feed` | `[platform]-reviews-YYYY` | New reviews, guide/driver name index, rating delta | `reviews/trustpilot-compilation`, `reviews/review-patterns` |
| `press-clip` | `[outlet]-YYYY-MM-DD` | Publication name, date, key quote, topic | `credentials/trust-signals`, `credentials/press-coverage` |

Each type entry specifies: what to extract, where to file in `raw/`, which wiki pages to update, and how to write the `wiki/sources/` summary.

CLAUDE.md stub in Workflow 4: "Declare source type from `wiki/ops/ingestion-profiles.md` before beginning Workflow 1 step 1."

### Workflow 5 — Compilation Profiles (`wiki/ops/compilation-profiles.md`)

Named profiles for content generation. Invoke by stating "Use the `[profile]` profile" before a generation request.

| Profile | Draw from | Format | Output filename |
|---------|-----------|--------|-----------------|
| `aeo` | `content/aeo-claims`, `content/faq-master`, `credentials/*` | Direct Q&A pairs, ≤40 words per answer, citable | `output/aeo-YYYY-MM-DD-[topic].md` |
| `website-copy` | `content/copy-bank`, `content/brand-voice`, `destinations/*`, `products/*` | Hero + body paragraphs, Style A voice, no invented claims | `output/copy-YYYY-MM-DD-[page].md` |
| `faq` | `content/faq-master`, `products/packages-overview`, `credentials/*` | H3 question + prose answer, AEO-compatible | `output/faq-YYYY-MM-DD-[topic].md` |
| `social` | `content/copy-bank`, `reviews/trustpilot-compilation`, `content/brand-voice` | Short-form, quote-led or claim-led, Style B voice | `output/social-YYYY-MM-DD-[topic].md` |
| `slide-deck` | `overview` + relevant domain pages (specified per request) | Marp-compatible markdown, one claim per slide | `output/slides-YYYY-MM-DD-[topic].md` |

Each profile page entry also lists forbidden patterns (e.g., `aeo`: no hedging language; `website-copy`: no invented statistics).

CLAUDE.md stub in Workflow 5: "Select a profile from `wiki/ops/compilation-profiles.md` before generating output. Save result to `output/` using the profile's filename convention."

### Workflow 6 — Health Checks (`wiki/ops/health-checks.md`)

Three tiers. Each run appends a short report to `wiki/log.md` under `## [YYYY-MM-DD] health-check | [tier]`.

**On-demand** — trigger: "Run health check" (replaces current Workflow 3 label)
- Contradiction scan across all wiki pages
- Orphan detection (no inbound links)
- Stale claim flags (`> [stale?]`)
- Gap page identification

**Weekly** — trigger: "Run weekly health check"
1. Flag claims referencing a date or rating that is >30 days old without a newer source
2. Detect wiki pages with no inbound links added since last ingest
3. Verify every page in `wiki/` has an entry in `wiki/index.md`
4. Confirm every file in `raw/` has a corresponding entry in `wiki/log.md`

**Monthly** — trigger: "Run monthly health check"
All weekly checks, plus:
1. Web-verify key credentials: NIB lookup, Trustpilot rating, POLPAR status
2. Check for new Trustpilot reviews since last `review-feed` ingest — flag if >2 uningested
3. Audit gap page list in `wiki/index.md` — remove entries for pages now created
4. Flag `output/` files >90 days old as potentially stale

---

## CLAUDE.md Changes

Add to the Directory Structure table:
- `wiki/ops/` — Operational workflow detail pages (Workflows 4–6)

Add after Workflow 3:

```
## Workflow 4: Typed Ingest
Before beginning Workflow 1, declare source type from [[ops/ingestion-profiles]].
The profile supplies type-specific extraction targets and wiki pages to update.

## Workflow 5: Compilation Profile
Before generating output, select a profile from [[ops/compilation-profiles]].
State "Use the [profile] profile" to activate it. Save output to output/ using
the profile's filename convention.

## Workflow 6: Health Check
Tiered audit procedure — see [[ops/health-checks]] for full checklists.
Triggers: "Run health check" (on-demand), "Run weekly health check",
"Run monthly health check". Append report to wiki/log.md after each run.
```

---

## `wiki/index.md` Changes

Add section after "## Content Production":

```markdown
## Ops

- [[ops/ingestion-profiles]] — Workflow 4: typed source handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip)
- [[ops/compilation-profiles]] — Workflow 5: named output profiles (aeo, website-copy, faq, social, slide-deck)
- [[ops/health-checks]] — Workflow 6: on-demand, weekly, and monthly audit checklists
```

---

## Out of Scope

- Shell scripts or scheduled automation (explicitly deferred — CLAUDE.md only)
- MCP server integration
- Cross-vault linking
- Changes to existing Workflows 1–3 beyond adding the type-declaration step to Workflow 1
