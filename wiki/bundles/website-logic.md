---
type: ops
title: Website Logic Bundle — Index
last_updated: 2026-06-01
sources: [ssot-v6]
owner: wiki-llm
stale_after_days: 120
bundle: website-logic
---

# Website Logic Bundle — Index

**Scope:** FAQ, AEO, schema, wording rules, page rules.

Thin navigation page. File ownership lives in -> [[ops/bundle-taxonomy]] §2. Pipeline status in -> [[ops/transformation-map]].

## Wiki sources

### Canonical master
- -> [[website/website-context-master]] — single-source-of-truth implementation doc

### Voice + copy
- -> [[website/brand-voice]]
- -> [[website/copy-bank]]
- -> [[website/query-hero-claim]]

### Content rules
- -> [[website/faq-master]] — 20 canonical answers
- -> [[website/aeo-claims]] — C1–C9 (shared with Trust Bundle)
- -> [[website/schema-templates]]
- -> [[website/operational-facts]]
- -> [[website/booking-platform-analysis]]
- -> [[website/hotels]]

### SEO / strategy
- -> [[seo/seo-strategy]]
- -> [[seo/geo-aeo-strategy]]
- -> [[seo/competitors]]
- -> [[seo/redirect-map]]
- -> [[seo/why-jvto-architecture]]

## Compiled output (live)

- `output/website/faq/*.md` (8 files — slug-mirror, naming-exempt)
- `output/website/aeo/*.md` (10 files — slug-mirror, naming-exempt)
- `output/website/schema/*-schema.json` + matching `*-schema.receipt.md` (~45 pairs — slug-mirror, naming-exempt)
- `output/website/pages/**/*.md` (~90 files — URL-mirror hierarchy, naming-exempt)
- `output/website/blog/*.md`
- `output/website/llms.txt`, `output/website/llms-full.txt`
- `output/website/HANDOFF.md` (developer integration anchor — naming-exempt)
- `output/INDEX.md` (master output catalog — naming-exempt)

## Compiler

No consolidated compiler. Outputs are authored per page using ingestion/compilation profiles -> [[ops/ingestion-profiles]], -> [[ops/compilation-profiles]].

## Consumers

- jvto-web (all routes)
- AEO answer engines
- LLM crawlers (via `llms.txt`)

## Status

**PARTIAL.** Output side mature; no consolidated compiler. Policy Bundle compiler (P2) is the next planned wedge inside this bundle's scope.

## Pending follow-up (deferred)

- Consolidated `wording-rules.md` and `page-rules.md` index pages — separate sprint.
