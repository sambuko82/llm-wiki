---
type: source
title: Backoffice MySQL Extraction — Umbrella Source
slug: backoffice-mysql
owner: wiki-llm
stale_after_days: 90
ingested: 2026-05-25
last_updated: 2026-05-25
format: mysql
location: raw/backoffice/
sources: [backoffice-mysql]
pages_updated: [wiki/finance/profit-analysis, wiki/finance/rate-cards, wiki/index, wiki/internal-ops/backoffice-extraction, wiki/people/crew-registry, wiki/products/packages-full-pricing, wiki/sources/backoffice-bookings-ops, wiki/sources/backoffice-finance, wiki/sources/backoffice-master-data, wiki/sources/backoffice-pricing, wiki/sources/backoffice-schema, wiki/sources/backoffice-staff, wiki/sources/backoffice-vendors, wiki/sources/backoffice-whatsapp]
---

# Backoffice MySQL Extraction — Umbrella Source

## Role in vault

This is the **umbrella source** for the 2026-05-25 live MySQL extraction from the JVTO backoffice. The extraction was split into 8 domain-scoped source pages during ingestion. Downstream wiki pages cite slug `backoffice-mysql` as a single citation handle — this umbrella restores reachability so the orphan filter in [[bases/sources.base]] sees the split files as covered, and so future ingests can dedupe against a single canonical slug.

## Authority status

Treat as canonical for live operational data extracted from the backoffice MySQL on 2026-05-25 (snapshot date). For any field where this umbrella conflicts with [[sources/ssot-v6]] §_n, defer to SSOT — SSOT is the curated source of truth; this is the live operational mirror.

## Split sources (8 domain pages)

- [[sources/backoffice-bookings-ops]] — bookings, ops, assignments
- [[sources/backoffice-finance]] — invoices, payments, transactions, accounts
- [[sources/backoffice-master-data]] — packages, destinations, hotels, vehicles, locations
- [[sources/backoffice-pricing]] — package pricing tiers, rate cards, surcharges
- [[sources/backoffice-schema]] — table list, FK map, schema overview
- [[sources/backoffice-staff]] — guides, drivers, assignment volume
- [[sources/backoffice-vendors]] — partner hotels, transport vendors, suppliers
- [[sources/backoffice-whatsapp]] — WA message logs, template usage, customer chat history

## Provenance chain

`raw/backoffice/` (MySQL dump 2026-05-25) → 8 split source summaries → downstream wiki pages (see `pages_updated`).

## Downstream pages (14 — auto-derived from inbound `sources:` refs)

The 14 entries in `pages_updated` are the union of all wiki pages whose frontmatter `sources:` array contains the slug `backoffice-mysql`. They include the 8 split files (which back-reference the umbrella) plus 6 downstream consumers:

- [[finance/profit-analysis]]
- [[finance/rate-cards]]
- [[index]]
- [[internal-ops/backoffice-extraction]]
- [[people/crew-registry]]
- [[products/packages-full-pricing]]

## Contradictions / drift

None recorded. Any drift between umbrella and SSOT should be flagged at `[[ops/transformation-map]]` and reconciled in favour of SSOT unless the umbrella is the more recent live extract.
