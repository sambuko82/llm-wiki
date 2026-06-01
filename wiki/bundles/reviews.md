---
type: ops
title: Review Bundle — Index
last_updated: 2026-06-01
sources: [trustpilot-reviews-2026, google-maps-reviews-api-2026]
owner: wiki-llm
stale_after_days: 120
bundle: reviews
---

# Review Bundle — Index

**Scope:** review registry, ratings, crew mentions, review patterns, social proof.

Thin navigation page. File ownership in -> [[ops/bundle-taxonomy]] §4. Pipeline status in -> [[ops/transformation-map]].

## Wiki sources

- -> [[reviews/trustpilot-all-reviews]] — full structured catalog
- -> [[reviews/trustpilot-compilation]]
- -> [[reviews/google-tripadvisor-2026]] — cross-platform compilation
- -> [[reviews/review-patterns]] — patterns & themes
- -> [[sources/trustpilot-reviews-2026]] — source summary
- -> [[sources/google-maps-reviews-api-2026]] — 123 reviews
- -> [[people/crew-registry]] §"Guide / Driver review-quote excerpts" — shared with People domain (crew-mention subsection)

## Raw sources

- `raw/google review page 1.json`, `…page 2.json`, `…page 3.json`
- `raw/google profile media.json` (also Asset Bundle)
- `Clippings/Java Volcano Tour Operator is rated Excellent with 4.8.md` (Trustpilot clip)
- `raw/backoffice/csv/jvto_reviews.csv`, `jvto_review_crews.csv`, `review_guides.csv`

## Compiled output

**None yet.** Future path: `output/reviews/review-proof-index/`.

## Compiler

**Not built.** Planned: Review Proof Index (P4).

## Consumers (planned)

- jvto-web proof blocks
- AEO proof snippets
- JSON-LD `Review` schema
- WhatsApp reply intelligence (review citations)

## Status

**FUTURE (P4).** Sources catalogued and structured; compiler + output deferred.

## Pending follow-up (deferred)

- `crew-mentions.md` (one of the 8 deferred index/merge pages — separate sprint).
- `social-proof-map.md` (one of the 8 deferred index/merge pages — separate sprint).
