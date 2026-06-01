---
type: ops
title: Transformation Map — Domain → Bundle Pipeline
last_updated: 2026-06-01
sources: []
owner: wiki-llm
stale_after_days: 120
---

# Transformation Map — Domain → Bundle Pipeline

Master map for `llm-wiki`. Defines, per domain, the full transformation chain:

```
domain → canonical source → compiler/script → output → validator → consumer → status
```

Purpose: stop random compiler/output sprawl. Before building any new bundle, register it here first. This is the induk (parent) map every future wedge answers to.

## Canonical Bundle Set

Per -> [[ops/bundle-taxonomy]] (added 2026-06-01) the wiki is organised around **6 website-first bundles**. The pipeline tables below list every bundle that has a compiler or planned compiler. The 6 canonical bundles are:

1. **Trust Bundle** — claims, trust signals, evidence, verification mapping
2. **Website Logic Bundle** — FAQ, AEO, schema, wording rules, page rules
3. **Package Bundle** — package registry, pricing, itinerary, package readiness
4. **Review Bundle** — review registry, ratings, crew mentions, review patterns, social proof
5. **WhatsApp Reply Bundle** — templates, intents, routing, hard rules
6. **Asset Bundle** — image proof, proof-file usage, page usage, alt text, visual evidence

Policy Source Ownership, R065 Booking Flow, and Global Wiki Validator remain registered as cross-cutting infrastructure, not standalone bundles.

## Current Architecture

| Layer | Path | Role |
|---|---|---|
| Source (raw) | `raw/` + `raw/_manifest/` | Immutable source docs + registries. LLM reads; never hand-writes (manifest exception). |
| Canonical knowledge | `wiki/` | Single source of truth. Human + AI readable. All facts cite a wiki source. |
| Compiler / validator | `scripts/` | Python pipeline: loaders → enrich → validate → render → atomic write. |
| Generated artifacts | `output/` | Machine-readable bundles consumed by jvto-web, WhatsApp, checkout, AI. |

## Output Path Convention

**Standard:** `output/<domain>/<bundle>/`

```
output/website/trust-bundle/        ← live, proven
output/website/policy-bundle/       ← FUTURE
output/products/package-readiness/  ← NEXT
output/whatsapp/reply-intelligence/ ← FUTURE
output/reviews/review-proof-index/  ← FUTURE
output/finance/quote-helper/        ← FUTURE
```

Do **NOT** introduce a top-level `compiled/` directory. `output/` is the only artifact root. No `data/`, no parallel trees.

## Bundle Status Table

| Bundle | Canonical name (per bundle-taxonomy) | Status | Priority |
|---|---|---|---|
| Trust Bundle v1 | **Trust Bundle** (1) | **DONE — DO NOT REOPEN** without explicit user request | — |
| Policy Source Ownership | (cross-cutting infra; feeds Website Logic) | **DONE** | — |
| R065 Booking Flow ingest | (cross-cutting; feeds Website Logic + WhatsApp Reply) | **DONE** | — |
| Package Readiness Compiler | **Package Bundle** (3) | **DONE (v1.2)** — package-readiness output live | — |
| Policy Bundle Compiler | (subset of Website Logic Bundle) | FUTURE | P2 |
| WhatsApp Reply Intelligence | **WhatsApp Reply Bundle** (5) | FUTURE | P3 |
| Review Proof Index | **Review Bundle** (4) | FUTURE | P4 |
| Finance Quote Helper | (subset of Package Bundle) | FUTURE | P5 |
| Website Logic Bundle | **Website Logic Bundle** (2) | PARTIAL — aeo/faq/schema/pages output live, no consolidated compiler | — |
| Asset Bundle | **Asset Bundle** (6) | FUTURE — sources catalogued in `wiki/sources/`, no compiler, no output | P4-tie |
| Global Wiki Validator | (cross-cutting infra) | FUTURE | P6 |

## Per-Bundle Pipeline

| Domain | Canonical Sources | Supporting Sources | Script | Output Path | Validator | Consumers | Status |
|---|---|---|---|---|---|---|---|
| Trust | claim/evidence/entity/decision registries, conflict-log, aeo-claims | overview, credentials/* | `scripts/compile_trust.py` | `output/website/trust-bundle/` | F1–F8 (built-in) | jvto-web `/trust`, AEO, schema | **DONE — DO NOT REOPEN** |
| Policy ownership | `wiki/ops/policy-source-ownership.md` | products/packages-overview, website/faq-master | — (doc map, no compiler) | — | deprecated-wording table (manual) | all policy consumers | **DONE** |
| Booking flow | products/packages-overview §booking-flow | website/booking-platform-analysis, sources/tango-workflow-jvto-website-booking | — | — | — | website, FAQ, checkout, WhatsApp | **DONE** (structured bundle = FUTURE, via Policy/Booking Bundle) |
| Package readiness | products/packages-overview, products/packages-full-pricing, finance/rate-cards | destinations/*, crew-registry | `scripts/compile_packages.py` (NOT BUILT) | `output/products/package-readiness/` | gap-report (planned) | jvto-web package/checkout, WhatsApp, quotation, finance | **NEXT (P1)** |
| Policy bundle | `wiki/ops/policy-source-ownership.md`, products/packages-overview, website/faq-master | brand-voice | (planned) | `output/website/policy-bundle/` | deprecated-wording validator (planned) | jvto-web checkout microcopy, WhatsApp, FAQ | FUTURE (P2) |
| WhatsApp reply | whatsapp/playbook, whatsapp/rules-engine, whatsapp/canned-responses | package + policy + FAQ + trust bundles | (planned) | `output/whatsapp/reply-intelligence/` | (planned) | WhatsApp automation / CRM | FUTURE (P3) |
| Review proof | reviews/* | package-registry, destinations, crew, claim-registry | (planned) | `output/reviews/review-proof-index/` | (planned) | website proof blocks, schema, AEO | FUTURE (P4) |
| Finance quote | finance/rate-cards, finance/package-costs | package-pricing, package-itineraries | (planned) | `output/finance/quote-helper/` | (planned) | quote builder, WhatsApp, dashboard | FUTURE (P5) |
| Global validation | all `wiki/` | all registries | `scripts/validate_wiki.py` (NOT BUILT) | — (report) | self | CI / health-check, all authors | FUTURE (P6) |
| Asset Bundle | sources/ssot-image-asset-map, sources/google-profile-media-2026, sources/gpx-destination-data | raw image asset map JSON, raw GPX × 5, raw GMB media JSON | (planned) | (no output yet; future `output/asset-bundle/`) | (planned: alt-text + page-usage validators) | jvto-web image refs, schema imageObject, AEO proof blocks | FUTURE (P4-tie) |

## Do-Not-Reopen

Locked decisions — do not re-litigate without an explicit user request:

- **Trust Bundle v1 is DONE.** DEC-001/002/003 are **locked**; CONF-001/002/003 **resolved**; F1–F8 **pass**; real compile **succeeded**; 7 JSON outputs **written and pushed**; jvto-web `/trust` **integrated**. Do NOT recompile, edit `raw/_manifest/decision-registry.yml`, or reassert "F4 blocked / DQ pending." Any wiki/log text implying Trust Bundle is blocked is **stale** — superseded by this line.
- **R065 = JVTO website self-checkout (Instant Book) flow**, 18 Tango steps across 4 PDF pages. NOT Trip.com. See -> [[ops/policy-source-ownership]] §deprecated-wording.
- **Policy deprecated-wording** is owned by -> [[ops/policy-source-ownership]]. Do not duplicate or contradict it elsewhere.

## Next Recommended Wedge

**Package Readiness Compiler** (P1) — package data is the business spine. The need is not just JSON; it is a **gap report** comparing wiki package knowledge against live website/checkout behaviour. Planned outputs:

```
output/products/package-readiness/
├── package-registry.json
├── package-pricing.json
├── package-itineraries.json
├── package-route-map.json
├── booking-compatibility.json
├── gap-report.json
└── _manifest.json
```

Must answer: which packages, which slugs, which routes, pricing tiers, itineraries, inclusions/exclusions, booking path; Ijen packages → health wording present; Bali packages → ferry inclusion; Madakaripura helmet caveat intact; Instant Book reflected in package knowledge.

## Explicit Non-Goals (this map)

This page is **documentation only**. It does NOT:

- create any compiler script
- generate any JSON
- edit the Trust Bundle or its registries
- edit jvto-web
- create any DB / API / server work

Building a bundle is a **separate, later, explicitly-approved** task. Register intent here first; implement after approval.
