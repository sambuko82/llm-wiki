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
