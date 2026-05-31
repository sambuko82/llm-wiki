---
type: ops
title: Transformation Map — Domain → Bundle Pipeline
last_updated: 2026-05-31
sources: []
---

# Transformation Map — Domain → Bundle Pipeline

Master map for `llm-wiki`. Defines, per domain, the full transformation chain:

```
domain → canonical source → compiler/script → output → validator → consumer → status
```

Purpose: stop random compiler/output sprawl. Before building any new bundle, register it here first. This is the induk (parent) map every future wedge answers to.

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

| Bundle | Status | Priority |
|---|---|---|
| Trust Bundle v1 | **DONE — DO NOT REOPEN** without explicit user request | — |
| Policy Source Ownership | **DONE** | — |
| R065 Booking Flow ingest | **DONE** | — |
| Package Readiness Compiler | **NEXT** | P1 |
| Policy Bundle Compiler | FUTURE | P2 |
| WhatsApp Reply Intelligence | FUTURE | P3 |
| Review Proof Index | FUTURE | P4 |
| Finance Quote Helper | FUTURE | P5 |
| Global Wiki Validator | FUTURE | P6 |

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
