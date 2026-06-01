---
type: ops
title: WhatsApp Reply Bundle — Index
last_updated: 2026-06-01
sources: [wa-pro-crm-api, backoffice-whatsapp]
owner: wiki-llm
stale_after_days: 120
bundle: whatsapp
---

# WhatsApp Reply Bundle — Index

**Scope:** templates, intents, routing, hard rules.

Thin navigation page. File ownership in -> [[ops/bundle-taxonomy]] §5. Pipeline status in -> [[ops/transformation-map]].

## Wiki sources

- -> [[whatsapp/operations-playbook]]
- -> [[whatsapp/rules-engine]]
- -> [[whatsapp/canned-responses]] — templates by stage
- -> [[sources/wa-pro-crm-api]] — REST API v1 reference
- -> [[sources/backoffice-whatsapp]] — conversation analytics

## Raw sources

- `raw/backoffice/csv/wa_chats.csv`, `wa_chat_categories.csv`, `wa_chat_summaries.csv`, `wa_itineraries.csv`, `wa_logs.csv`

## Compiled output

**None yet.** Future path: `output/whatsapp/reply-intelligence/`.

## Compiler

**Not built.** Planned: WhatsApp Reply Intelligence (P3). Will consume Trust + Package + Policy + FAQ bundles.

## Consumers (planned)

- WhatsApp Pro CRM (send_message, send_template endpoints)
- Owner-facing reply triage UI

## Status

**FUTURE (P3).** Sources structured; rules engine documented; compiler + structured output deferred.

## Pending follow-up (deferred)

- `intents-routing.md` (one of the 8 deferred index/merge pages — separate sprint).
- `hard-rules.md` (one of the 8 deferred index/merge pages — separate sprint).
