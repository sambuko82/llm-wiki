---
type: index
title: JVTO Wiki Content Index — AI Entry Point
last_updated: 2026-05-11
total_pages: 30
sources: [ssot-v6, jvto-homepage-clip, trustpilot-reviews-2026, detik-polpar-2021, llm-kb-tooling-guide, jvto-policy-pack-v6, jvto-travel-guide-en]
---

# JVTO Wiki — Content Index

*Read this first for any query. Find relevant pages, then drill in.*

This vault is canonical for content production about Java Volcano Tour Operator (JVTO). Two sources back every page: a structured SSOT JSON and a homepage clip — see [[sources/ssot-v6]] and [[sources/jvto-homepage-clip]].

## Foundation

- [[overview]] — Master synthesis: identity, thesis, 9 trust pillars, contradictions
- [[log]] — Append-only operations log
- `index` (this page)

## Sources

- [[sources/ssot-v6]] — `JVTO_FINAL_CLEAN_SSOT.json` v6.0 (canonical, 13 domains, dated 2026-04-22). **Authority for all structured facts.**
- [[sources/jvto-homepage-clip]] — javavolcano-touroperator.com homepage clip (2026-05-06). Authority for voice/tone exemplars + verbatim review quotes.
- [[sources/trustpilot-reviews-2026]] — Trustpilot page clip (2026-05-09). 51 reviews, 4.8/5. Confirms 2 new unregistered crew (Derry, Sulis) + Pras in company bio.
- [[sources/detik-polpar-2021]] — Detik.com article (2021-03-14). Independent national media confirmation of Bripka Agung Sambuko as active Polpar. Direct quotes in Bahasa Indonesia.
- [[sources/llm-kb-tooling-guide]] — LLM KB Tooling Guide (2026-05-11). Karpathy-inspired patterns: typed ingestion, compilation profiles, health check tiers. Basis for Workflows 4–6.
- [[sources/jvto-policy-pack-v6]] — Customer-facing policy pack v2026-01-17 (3 policies: Booking/Payment/Cancellation, Inclusions/Exclusions, Privacy). Vehicle allocation specs, Bromo jeep capacity, bank transfer details, FOC scheme, Travel Credit terms.
- [[sources/jvto-travel-guide-en]] — Travel Guide EN publishable copy + SSOT JSON (2026-01-19). 7 routes: booking info, FAQ, Ijen screening, safety, packing, weather, police escort. Silver jewelry warning, fitness levels per destination, My Booking Portal details.

## Destinations

- [[destinations/kawah-ijen]] — 2,386 m, blue fire, BBKSDA health-screening coordination (conditional) · GPX trail data
- [[destinations/mount-bromo]] — 2,329 m, Tengger caldera, Penanjakan sunrise, BBKSDA clearance · GPX trail data + Pura Luhur Poten waypoint
- [[destinations/tumpak-sewu]] — Curtain waterfall ~120 m, Lumajang, canyon descent option · GPX trail data (rim trace)
- [[destinations/madakaripura]] — Tallest waterfall in Java (height under reconciliation — see page note), Probolinggo · GPX trail data
- [[destinations/papuma-beach]] — White-sand beach + cape headland (~86 m), Jember; coastal break on 5 Papuma-family packages · GPX trail data

## Products

- [[products/packages-overview]] — All 15 canonical packages (11 Surabaya + 4 Bali), pricing logic, inclusions, cancellation, FOC, vehicle allocation

## People

- [[people/agung-sambuko]] — Mr. Sam, founder, active Tourist Police officer (Ditpamobvit East Java) — full evidence chain (police docs SHA-256, press, historical)
- [[people/dr-ahmad-irwandanu]] — Medical Officer, Ijen health-screening coordination (SIP-licensed, conditional framing)
- [[people/crew-registry]] — 11 KTA-credentialed crew (7 guides + 4 drivers, 2024 issuance), HPWKI/BBKSDA training chain, named guides linked to review excerpts

## Credentials

- [[credentials/legal-licenses]] — NIB 1102230032918, TDUP, KBLI codes, HPWKI, BBKSDA, ISIC, SHA-256 hashes
- [[credentials/trust-signals]] — Trustpilot 4.8/47, INDECON, ISIC live provider, press, third-party recognition

## Reviews

- [[reviews/trustpilot-compilation]] — 51 reviews, 4.8/5 (verified 2026-05-09), guide/driver name index, verbatim excerpts
- [[reviews/review-patterns]] — Themes extracted: 5 SSOT-canonical + 10 derived patterns for content/AEO use

## Content Production

- [[content/brand-voice]] — Tone guide (Style A + Style B), key phrases, voice invariants (forbidden phrases + approved Ijen language)
- [[content/faq-master]] — All approved FAQ answers (AEO-formatted) — 20 canonical FAQs from SSOT §6_5 + locally derived
- [[content/aeo-claims]] — 9 canonical claim blocks (C1–C9) with NLP snippets, customer-service replies, evidence chains
- [[content/copy-bank]] — Reusable snippets: NLP atoms (C1–C9), hero copy, approved/forbidden Ijen language, trust stack order

## Ops

- [[ops/ingestion-profiles]] — Workflow 4: typed source handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip)
- [[ops/compilation-profiles]] — Workflow 5: named output profiles (aeo, website-copy, faq, social, slide-deck)
- [[ops/health-checks]] — Workflow 6: on-demand, weekly, and monthly audit checklists

## Open Gaps (no page yet — flagged by Lint)

- `credentials/medical-screening` — Ijen health-screening protocol with BBKSDA SE.1658/KSA.9/2024 + doctor verification: covered in [[people/dr-ahmad-irwandanu]] + [[destinations/kawah-ijen]], deserves its own consolidated page
- `credentials/police-integration` — SPRIN Wal Travel, SPRIN Polpar, police vehicle support: currently grouped under [[credentials/legal-licenses]] (SHA-256 table) and [[people/agung-sambuko]] (evidence chain)
- `credentials/press-coverage` — 4 cataloged press items + Stefan Loose guidebook: currently a section in [[credentials/trust-signals]]
- `content/voice-invariants` — Forbidden phrases and approved Ijen language: live as a section in [[content/brand-voice]] §voice-invariants. Promoting to its own page is optional — current location is canonical.

## Lookup Conventions

- Link format: `[[folder/page-name]]` (Obsidian wikilink — example syntax, not a real link)
- In prose, use `->` before link: `-> [[destinations/kawah-ijen]]`
- Contradictions: `> Contradiction with [[other-page]]: <detail>` (example syntax)
- Stale claims: `> [stale?] <detail>`
- Structured facts trace to [[sources/ssot-v6]] unless otherwise cited
- Tone/voice exemplars trace to [[sources/jvto-homepage-clip]]
