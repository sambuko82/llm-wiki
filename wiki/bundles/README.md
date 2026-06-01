---
type: ops
title: Bundles — Thin Index Layer
last_updated: 2026-06-01
sources: []
owner: wiki-llm
stale_after_days: 120
---

# Bundles — Thin Index Layer

This folder is the **navigation spine** for the 6 website-first bundles. Each `<bundle>.md` is a thin index page that pulls together the wiki pages, raw sources, and output paths owned by that bundle.

**These pages do not own content.** Content lives in domain folders (`wiki/destinations/`, `wiki/people/`, etc.) and compiled outputs (`output/...`). Bundle pages only index.

## The 6 bundles

| Bundle | Page | One-line scope |
|---|---|---|
| 1. Trust | -> [[bundles/trust]] | Claims, trust signals, evidence, verification mapping |
| 2. Website Logic | -> [[bundles/website-logic]] | FAQ, AEO, schema, wording rules, page rules |
| 3. Package | -> [[bundles/packages]] | Package registry, pricing, itinerary, package readiness |
| 4. Review | -> [[bundles/reviews]] | Review registry, ratings, crew mentions, social proof |
| 5. WhatsApp Reply | -> [[bundles/whatsapp]] | Templates, intents, routing, hard rules |
| 6. Asset | -> [[bundles/assets]] | Image proof, proof-file usage, page usage, alt text |

## Authority

- File→bundle ownership map: -> [[ops/bundle-taxonomy]]
- Pipeline status (sources → compiler → output): -> [[ops/transformation-map]]
- Naming-rule exemptions: root `CLAUDE.md` §Naming Rule Exemptions

## Phase status

Phase 1–2 (2026-06-01) created this folder + the 6 stub index pages. Stubs are intentionally minimal — section headers + pointer to bundle-taxonomy. Content expansion (the 8 new index/merge pages) is a deferred follow-up sprint.
