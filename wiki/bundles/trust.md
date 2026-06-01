---
type: ops
title: Trust Bundle — Index
last_updated: 2026-06-01
sources: [ssot-v6]
owner: wiki-llm
stale_after_days: 120
bundle: trust
---

# Trust Bundle — Index

**Scope:** claims, trust signals, evidence, verification mapping.

This is a thin navigation page. For the authoritative file→bundle map see -> [[ops/bundle-taxonomy]] §1. For pipeline status see -> [[ops/transformation-map]].

## Wiki sources

- -> [[credentials/legal-licenses]]
- -> [[credentials/medical-screening]]
- -> [[credentials/permit-requirements]]
- -> [[credentials/police-integration]]
- -> [[credentials/press-coverage]]
- -> [[credentials/trust-signals]]
- -> [[website/aeo-claims]] — 9 canonical pillars C1–C9 (shared with Website Logic Bundle)
- -> [[overview]] — master synthesis

## Raw / manifest sources

- `raw/_manifest/claim-registry.yml`
- `raw/_manifest/evidence-registry.yml`
- `raw/_manifest/entity-registry.yml`
- `raw/_manifest/decision-registry.yml`
- `raw/_manifest/conflict-log.md`
- `raw/JVTO_Verification_Dossier.pdf` (via -> [[sources/jvto-verification-dossier]])
- `raw/JVTO_FINAL_CLEAN_SSOT.json` (via -> [[sources/ssot-v6]])

## Compiled output (live)

- `output/website/trust-bundle/_manifest.json`
- `output/website/trust-bundle/claims.json`
- `output/website/trust-bundle/aeo-snippets.json`
- `output/website/trust-bundle/faq.json`
- `output/website/trust-bundle/destinations.json`
- `output/website/trust-bundle/people.json`
- `output/website/trust-bundle/products.json`
- `output/website/trust-bundle/policies.json`
- `output/website/trust-bundle/operational.json`
- `output/website/trust-bundle/extended-bundle-receipt.md`
- `output/website/trust-bundle/schema/{organization,tourist-trip,faq-page}.json`

## Compiler

- `scripts/compile_trust.py` — **DONE — DO NOT REOPEN** without explicit user request.

## Consumers

- jvto-web `/trust` (integrated)
- AEO snippets per destination
- JSON-LD schema on page templates

## Status

**DONE.** DEC-001/002/003 locked; CONF-001/002/003 resolved; F1–F8 pass. See -> [[ops/transformation-map]] §Do-Not-Reopen.

## Pending follow-up (deferred)

- `verification-mapping.md` (one of the 8 deferred index/merge pages — separate sprint)
