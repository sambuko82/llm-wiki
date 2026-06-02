---
type: index
title: JVTO Wiki Content Index — AI Entry Point
last_updated: 2026-06-02
total_pages: 96
sources: [ssot-v6, jvto-homepage-clip, trustpilot-reviews-2026, google-maps-reviews-api-2026, google-profile-media-2026, detik-polpar-2021, llm-kb-tooling-guide, jvto-policy-pack-v6, jvto-travel-guide-en, db-export-2026-05, sitemap-2026-05, radar-jember-polpar-geopark-2021, radar-jember-bau-menyengat-2021, bbksda-pelatihan-pemandu-2024, ssot-image-asset-map, geo-aeo-strategy-2026-05, eav-ai-optimization-2026-05, seo-ux-integration-2026-05, why-jvto-trust-architecture, digital-trust-fortress-blueprint, crew-strategy-integration-2026-05, competitor-design-analysis-2026-05, wa-pro-crm-api, gpx-destination-data, gemini-trust-fortress-mockup, finance-rate-cards, ijen-safety-resource-mapping, ijen-tourist-accidents, jvto-verification-dossier, ijen-safety-protocol, backoffice-mysql, guardian-authority-framework-2026-05, tango-workflow-jvto-website-booking]
owner: wiki-llm
stale_after_days: 60
---

# JVTO Wiki — Content Index

*Read this first for any query. Find relevant pages, then drill in.*

This vault is canonical for content production about Java Volcano Tour Operator (JVTO). Two sources back every page: a structured SSOT JSON and a homepage clip — see [[sources/ssot-v6]] and [[sources/jvto-homepage-clip]].

## Foundation

- [[overview]] — Master synthesis: identity, thesis, 9 trust pillars, contradictions
- [[log]] — Append-only operations log
- `index` (this page)

## Live Bases (auto-updating views)

Domain dashboards in `/bases/` — open in Obsidian for live queries (this static catalog is the narrative; Bases are the registry).

- `bases/index.base` — all wiki pages, grouped by `type`, stale-flagged
- `bases/destinations.base` — 5 destinations + schema/Ijen/GPX status
- `bases/sources.base` — ~43 sources, coverage + ingest age + orphan filter
- `bases/products.base` — package overview pages + counts
- `bases/people.base` — crew + key people, schema completeness
- `bases/credentials.base` — licenses, signals, claims supported
- `bases/ops-health.base` — stale pages, missing-sources, frontmatter gap audit

## Compiled Outputs

- [[output/website/trust-bundle/_manifest|Trust Bundle (compiled)]] — `output/website/trust-bundle/*.json`. Original 7 outputs (claims, aeo-snippets, faq, organization/tourist-trip/faq-page schemas) — **DONE/DO NOT REOPEN.** DEC-001/002/003 locked, F1–F8 pass. See -> [[ops/transformation-map]] §do-not-reopen.
- **Extended Trust Bundle (2026-06-01)** — 5 new JSON exports + updated manifest: `products.json` (22 packages, full pricing), `policies.json` (booking rules, cancellation, inclusions, vehicle allocation, FOC, health screening, forbidden wording), `destinations.json` (5 destinations with geo, facts, package lists), `people.json` (founder, medical officer, 14 crew), `operational.json` (travel times, temperatures, closures, 23 hotels). Verification receipt: `output/website/trust-bundle/extended-bundle-receipt.md`.
- **bases/website-readiness.base** — New Obsidian dashboard for all website-relevant wiki pages: type-filtered (destination/product/person/credential/website/seo), `days_since_update` formula, stale flag, health-wording mode. 4 views: all pages (staleness order), stale-only, Ijen health pages, domain cards.

## Sources

- [[sources/ssot-v6]] — `JVTO_FINAL_CLEAN_SSOT.json` v6.0 (canonical, 13 domains, dated 2026-04-22). **Authority for all structured facts.**
- [[sources/jvto-homepage-clip]] — javavolcano-touroperator.com homepage clip (2026-05-06). Authority for voice/tone exemplars + verbatim review quotes.
- [[sources/trustpilot-reviews-2026]] — Trustpilot page clip (2026-05-09). 51 reviews, 4.8/5. Confirms 2 new unregistered crew (Derry, Sulis) + Pras in company bio.
- [[sources/detik-polpar-2021]] — Detik.com article (2021-03-14). Independent national media confirmation of Bripka Agung Sambuko as active Polpar. Direct quotes in Bahasa Indonesia.
- [[sources/llm-kb-tooling-guide]] — LLM KB Tooling Guide (2026-05-11). Karpathy-inspired patterns: typed ingestion, compilation profiles, health check tiers. Basis for Workflows 4–6.
- [[sources/jvto-policy-pack-v6]] — Customer-facing policy pack v2026-01-17 (3 policies: Booking/Payment/Cancellation, Inclusions/Exclusions, Privacy). Vehicle allocation specs, Bromo jeep capacity, bank transfer details, FOC scheme, Travel Credit terms.
- [[sources/jvto-travel-guide-en]] — Travel Guide EN publishable copy + SSOT JSON (2026-01-19). 7 routes: booking info, FAQ, Ijen screening, safety, packing, weather, police escort. Silver jewelry warning, fitness levels per destination, My Booking Portal details.
- [[sources/db-export-2026-05]] — Live DB export (2026-05). 14 categories: 22 packages with full pricing, 99 itinerary days, 157 reviews (Google+TripAdvisor+Trustpilot), 14 crew members, 23 hotels, 38 knowledge base articles.
- [[sources/sitemap-2026-05]] — Live XML sitemap (2026-05-12). 44 URLs. Confirms 16 live tour pages (12 Surabaya + 4 Bali), resolves package count contradiction, reveals Verify JVTO trust hub structure, confirms `taman-safari-prigen-bromo-madakaripura-3d2n` as active package.
- [[sources/radar-jember-polpar-geopark-2021]] — Radar Jember 2021-03-24. Polpar formation for Ijen Geopark support. Institutional role confirmation. Paywalled — title/slug only.
- [[sources/radar-jember-bau-menyengat-2021]] — Radar Jember 2021-05-27. Tourist Police patrol at Ijen crater, sulfur odor monitoring. Operational-presence proof. Paywalled — title/slug only.
- [[sources/bbksda-pelatihan-pemandu-2024]] — BBKSDA Jatim 2024-05-24. Official guide training report: 250 HPWKI guides, SAR + PPGD curriculum, 3 days at Paltuding. Validates HPWKI training chain. Full access.
- [[sources/ssot-image-asset-map]] — JVTO image asset SSOT (2026-05-16). 54 live images across 14 groups
- [[sources/seo-audit-2026-05]] — SEO audit (2026-05-17). Dual-URL issue, keyword strategy (15 targets), competitor map (3 tiers), schema requirements (7 page types), 14 QW + 14 SI action items. Ahrefs data unavailable — volumes estimated.: crew portraits (11), field operations (8), crew credentials (5), health screening (5), history/heritage (5), police docs (4), founder (3), press (3), legal docs (6), partner (1), uncertain (1). All URLs live on javavolcano-touroperator.com.
- [[sources/route-data-csv]] — Route segment library (2026-05-18).
- [[sources/comm-management-theory]] — Comm management theory (2026-05-19):
- [[sources/3d-route-viewer]] — Mapbox 3D fly-through feature + GeoJSON route data for all 5 destinations (2026-05-24). `/3d/{slug}` viewer URLs, full route stats table, tech stack. BANT, MECE, SFC/FCR, SLA standards, ISO 10002, GDPR/UU PDP, 4-stage pre-booking funnel, 6-stage customer journey. Explicitly references JVTO. 43 named day-segments (`routes.csv`) + 217 timed activity rows (`route_details.csv`). Supplement to db-export-2026-05 adding intra-day granularity. Routes 6 + 20 explicitly ingested for taman-safari package.
- [[sources/geo-aeo-strategy-2026-05]] — GEO/AEO exhaustive audit (2026-05-24, from 4 raw files). Digital Trust Fortress 5-component model, AEO per-page targets, confirmed #1 rankings, TL;DR HTML block + Organization JSON-LD + FAQPage code, llms.txt rec, OTA optimization.
- [[sources/eav-ai-optimization-2026-05]] — EAV/AI optimization audit (2026-05-24, from 3 raw files). EAV entity framework (Organization/TourPackage/HealthScreening/TravelCredit), 8-layer SSOT→JSON-LD map, NLP sharpening before/after table, StartLocation as primary discriminator.
- [[sources/seo-ux-integration-2026-05]] — SEO+UX integration analysis (2026-05-24). URL governance comparison (MBA/GA/JVTO), SSOT→DOM integration, WCAG, keyword cannibalization gaps, WAF/crawler conflict, off-page backlink opportunities.
- [[sources/why-jvto-trust-architecture]] — Why JVTO trust architecture (2026-05-24, from 4 raw files). Hub & spoke URL sitemap, Trust Asset Registry (LEG-001–HIST-002), new facts (Stefan Loose ISBN contradiction, second NIB 0220001393513), Guardian Archetype framing, HPWKI/INDECON/ISIC institutional triad.
- [[sources/digital-trust-fortress-blueprint]] — Digital Trust Fortress Next.js blueprint (2026-05-24). Full file tree, component registry (AuthorityShield/ForensicGallery/CrewCard), API endpoints, evidence asset structure, Costly Signals principle for police docs.
- [[sources/crew-strategy-integration-2026-05]] — Crew→trust-pillar strategy (2026-05-24). 7-pillar crew mapping table, crew archetypes with IDs (Joyo/Yandi/Fredi/Gufron/Anjas), 4-zone team page structure, Guardian Mindset principle.
- [[sources/competitor-design-analysis-2026-05]] — MBA + G Adventures design benchmark (2026-05-24). MBA Level 1-7 difficulty, 67% CAC reduction / 50% RPB increase 2018-2020, URL persistence `/[locale]/adventures/[slug]/`. GA REST API SSOT, `/trips/[name]/[id]/` ID persistence, looptail brand system.
- [[sources/wa-pro-crm-api]] — WhatsApp Pro CRM REST API v1 (2026-05-25). 6 endpoints (send_message, send_image_url, send_file_url, groups, send_template, checking_key), error codes, webhook formats for 6 message types. Powers WA automation playbook.
- [[sources/gpx-destination-data]] — AllTrails GPX recordings ×5 (2026-05-25). Consolidated reference: bounding boxes, elevation ranges, waypoints for Ijen/Bromo/Tumpak Sewu/Madakaripura/Papuma. Data already in destination pages.
- [[sources/gemini-trust-fortress-mockup]] — Gemini-generated HTML mockup (2026-05-25). "Digital Trust Fortress" visual concept for /why-jvto. Design tokens (police.900/accent, forensic.light/success), DM Serif Display + Inter + JetBrains Mono stack. Design reference only.
- [[sources/finance-rate-cards]] — 5 JSON rate card files (`raw/FINANCE/rate_cards/`): crew roles, vehicles, accommodation (23 hotels), activities (27 items), other costs (10 items). All IDR. Basis for package COGS analysis.
- [[sources/ijen-safety-resource-mapping]] — Safety resource mapping (Excel). 5 categories: hazards, health screening, Tourist Police, Ijen Rijik closure (est. March 2019), guide supervision. 14 source references. Supports C1, C4.
- [[sources/ijen-tourist-accidents]] — Tourist accident registry (Excel). 7 incidents 2015–2026, 4 fatalities (50% fitness-related). Validates BBKSDA health screening mandate. 6 media references. Sensitivity: public_sensitive.
- [[sources/jvto-verification-dossier]] — 14-page NotebookLM "Daylight Audit Dossier" (PDF). Visual trust deck: hazard profile, JVTO vs unregulated comparison, 4-layer Trust Stack, legal exhibits, health screening flowchart, crew, operational timeline. AI-generated (weight 8). New fact: AHU-0023020.
- [[sources/ijen-safety-protocol]] — Operational safety protocol (md). 7-section Kawah Ijen framework: regulatory foundation, incident analysis, personnel standards, gear, SAR protocol, risk flags, Ijen Rijik. AI-generated (weight 8). New facts: Lamborghini evacuation, Sengkan Gandrung braking zone, TWA Call Center.
- [[sources/guardian-authority-framework-2026-05]] — Guardian Infrastructure & authority framework synthesis (2026-05-26, from 4 raw files). ~75% overlaps existing sources. New: Personality Economy + Micro-Entity crew framing, Dream Team pairings, Digital Trust Gap evaluation table, Answer Block format spec, Sprint 0 recovery board, Definition of Done checklist (4 layers), Authority Stack comparison, ISO 3166-2:ID geospatial anchoring, Costly Signal theory, 3 psychological barriers framework, named concept glossary.
- [[sources/google-maps-reviews-api-2026]] — Google Maps Reviews API export (2026-05-26). 123 reviews (115×5★, 5×4★, 2×3★, 1×1★), full text + owner replies. Date range 2018-12-14 → 2026-05-22. Supersedes DB-sourced Google review data. All 14 crew members appear.
- [[sources/google-profile-media-2026]] — Google Business Profile media (2026-05-26). 87 items: 79 photos + 8 videos. Owner-uploaded GMB listing assets.
- [[sources/tango-workflow-jvto-website-booking]] — Tango workflow PDF (2026-05-31, R065). 18-step JVTO website self-checkout (Instant Book) flow recorded by Agung Sambuko. Documents packages-overview §booking-flow gap: WA-assisted path only; self-checkout path undocumented until now. 5 critical gaps: terms text, price anomaly (IDR 3,350,000), add-on alignment, health screening trigger, packages-overview stale.

### Backoffice MySQL extraction (2026-05-25)

Live extraction from JVTO backoffice MariaDB (`u1805424_jvto_clone` @ Hostinger). 210 tables, ~63k rows. Schema + aggregates committed; PII raw data gitignored.

- [[sources/backoffice-schema]] — 210-table inventory, Mermaid ERD for core entities, full FK web. Entry point for all backoffice DB questions.
- [[sources/backoffice-finance]] — Revenue by month, currency mix, payment method ledger, debt outstanding, invoice line-item breakdown. **Canonical for "how much money."**
- [[sources/backoffice-pricing]] — Template `package_prices` vs realized `bookings.grand_total` per template_package_id. **Validation source for [[finance/rate-cards]].**
- [[sources/backoffice-bookings-ops]] — Booking volume by month, pax distribution, lead time, channel/agent mix, assignment counts (guide/driver/car/hotel/jeep).
- [[sources/backoffice-staff]] — `guide_drivers` aggregates: crew level, role, licenses populated, star rating, top-deployed crew. Complements [[people/crew-registry]].
- [[sources/backoffice-vendors]] — Vendor count by category, hotel partner list with rates, car fleet with pax range + driver allowance.
- [[sources/backoffice-master-data]] — Reference catalogs: accounts, payment_methods, crew_roles, booking_categories, vendor_categories, price_plans, destinations, areas, weather_codes, wa_chat_categories.
- [[sources/backoffice-whatsapp]] — Conversation analytics: 5,547 messages, direction/media breakdown, monthly volume, intent category distribution, top conversations (anonymized).

## Destinations

- [[destinations/kawah-ijen]] — 2,386 m, blue fire, BBKSDA health-screening coordination (conditional) · GPX trail data · 3D viewer /3d/ijen-crater
- [[destinations/mount-bromo]] — 2,329 m, Tengger caldera, Penanjakan sunrise, BBKSDA clearance · GPX trail data + Pura Luhur Poten waypoint · 3D viewer /3d/mount-bromo
- [[destinations/tumpak-sewu]] — Curtain waterfall ~120 m, Lumajang, canyon descent option · GPX trail data (rim trace) · 3D viewer /3d/tumpak-sewu-waterfall
- [[destinations/madakaripura]] — Tallest waterfall in Java (height under reconciliation — see page note), Probolinggo · GPX trail data · 3D viewer /3d/madakaripura-waterfall
- [[destinations/papuma-beach]] — White-sand beach + cape headland (~86 m), Jember; coastal break on 5 Papuma-family packages · GPX trail data · 3D viewer /3d/papuma-beach

## Products

- [[products/packages-overview]] — 15 SSOT canonical (11 Surabaya + 4 Bali) + 1 specialty = **16 commercial tour pages**. Pricing logic, inclusions, cancellation, FOC, vehicle allocation
- [[products/packages-full-pricing]] — Complete pricing tables for all 22 priced packages (15 canonical + 1 specialty + 6 student), all pax tiers
- [[products/packages-itineraries]] — Day-by-day itineraries for all canonical packages; recurring patterns; hotel allocation per phase

## People

- [[people/agung-sambuko]] — Mr. Sam, founder, active Tourist Police officer (Ditpamobvit East Java) — full evidence chain (police docs SHA-256, press, historical)
- [[people/dr-ahmad-irwandanu]] — Medical Officer, Ijen health-screening coordination (SIP-licensed, conditional framing)
- [[people/crew-registry]] — 14-member field team (7 guides + 7 drivers), 11 KTA-credentialed (2024 issuance), HPWKI/BBKSDA training chain, named guides linked to review excerpts

## Credentials

- [[credentials/legal-licenses]] — NIB 1102230032918, TDUP, KBLI codes, HPWKI, BBKSDA, ISIC, SHA-256 hashes
- [[credentials/trust-signals]] — Trustpilot 4.8/51, INDECON, ISIC live provider, press, third-party recognition
- [[credentials/press-coverage]] — 4 independent press items (Detik, Radar Jember ×2, BBKSDA) + Stefan Loose guidebook 2016 p. 287; entity linking analysis; AEO snippets for C9
- [[credentials/medical-screening]] — Ijen health-screening system: BBKSDA SE.1658 regulatory basis, 4-step protocol, Dr. Irwandanu (SIP-verifiable), partner facilities, 5 screening photos + BBKSDA terms screenshot; AEO snippets for C4
- [[credentials/police-integration]] — Full evidence chain: SPRIN POLPAR + SPRIN WAL-TRAVEL (SHA-256), 3 police escort photos + Geopark briefing, 3-article press corroboration, Ditpamobvit unit details, Traffic Police escort mechanics; AEO snippets for C1/C5
- [[credentials/permit-requirements]] — Operator permits (NIB, TDUP, KBLI, BBKSDA, HPWKI) + visitor entry requirements per destination (Ijen, Bromo, Tumpak Sewu, Madakaripura, Papuma) with costs. Backs Silo 3 permit-requirements output.

## Reviews

- [[reviews/trustpilot-compilation]] — 51 reviews, 4.8/5 (verified 2026-05-18), guide/driver name index, verbatim excerpts, rating distribution (94% 5-star)
- [[reviews/trustpilot-all-reviews]] — **Full structured catalog**: all 49 Trustpilot reviews with reviewer name, country, date, stars, verbatim body, inferred package, and crew tags. Live-scraped 2026-05-18.
- [[reviews/google-tripadvisor-2026]] — **Cross-platform compilation**: Google 123 (4.9/5) + Trustpilot 51 (4.8/5) + TripAdvisor 21 (4.95/5) = 195 reviews. Organized by crew (14 members) + tour package (16 packages). Best quotes per crew, review evidence per package.
- [[reviews/review-patterns]] — Themes extracted: 5 SSOT-canonical + 10 derived patterns for content/AEO use

## Website

- [[website/brand-voice]] — Tone guide (Style A + Style B), key phrases, voice invariants (forbidden phrases + approved Ijen language)
- [[website/faq-master]] — All approved FAQ answers (AEO-formatted) — 20 canonical FAQs from SSOT §6_5 + locally derived
- [[website/aeo-claims]] — 9 canonical claim blocks (C1–C9) with NLP snippets, customer-service replies, evidence chains
- [[website/copy-bank]] — Reusable snippets: NLP atoms (C1–C9), hero copy, approved/forbidden Ijen language, trust stack order
- [[website/operational-facts]] — Temperatures (Bromo/Ijen), travel times, support hours, Ijen closure schedule, trolley ojek, micro-customization policy, FOC 5% discount
- [[website/query-hero-claim]] — Query output: C3 (all-inclusive, no surprise costs) is the lead hero claim for price-skeptical solo travelers; C1/C5 justifies the premium. Evidence chain, 2 headline options, ranked secondary claims.
- [[website/hotels]] — 23 hotel partners registry; organized by itinerary phase (Bondowoso/Banyuwangi, Bromo, Tumpak Sewu, Malang, Surabaya finish)
- [[website/schema-templates]] — JSON-LD schema reference: page-type → schema map, field rules, BreadcrumbList patterns, numeric verification checklist
- [[website/booking-platform-analysis]] — JVTO website self-checkout (Instant Book) flow analysis (18 steps, 4 PDF pages). Identifies 5 critical gaps: terms checkbox content, price anomaly (IDR 3,350,000 vs SSOT), add-on validation, missing health-screening step, packages-overview booking-flow stale. Owner tasks for Sam.
- [[website/website-context-master]] — **NEW** Single implementation reference: working values table (review counts, credential IDs, contact), business logic rules (health screening conditional, cancellation, FOC, vehicle allocation), approved/forbidden wording, schema requirements per page type, open gaps. Does not duplicate HANDOFF.md — supplements it with logic and verified values.

## SEO & Strategy

- [[seo/seo-strategy]] — Keyword targets (15 terms), content silo map (4 silos, 30+ pages), title tag rewrites (10 pages), QW action tracker (14 items), GEO/AEO extension section. Source: 2026-05-17 audit.
- [[seo/competitors]] — Tiered competitor registry (4 tiers + OTAs). Tier 4: MBA + G Adventures as global UX/design benchmarks. Monitoring protocol.
- [[seo/geo-aeo-strategy]] — **NEW** GEO entity architecture (llms.txt, SHA-256 in schema, sameAs cross-press), AEO universal rules, per-page targets, EAV principles, confirmed #1 rankings, OTA/App Engine section.
- [[seo/why-jvto-architecture]] — **NEW** Dev-facing Hub & Spoke routing reference. URL map + schema injection layers + component registry (AuthorityShield/ForensicGallery/CrewCard) + evidence asset structure.
- [[seo/redirect-map]] — 301 redirect table: 13 legacy Laravel routes → canonical SSOT URLs. Dev handoff for `jvto-web`.

## WhatsApp

- [[whatsapp/operations-playbook]] — 5-channel WhatsApp ops playbook
- [[whatsapp/canned-responses]] — WhatsApp + email template scripts per stage (Triage/Discovery/Proposal/Closing + post-booking), bilingual ID/EN, BANT-tagged, objection handling (JVTO inquiry, JVTO post-booking, Klook, Window Travel, Vendor/Crew). Funnels per channel, brand voice per audience, AI intervention points, phased roadmap, success metrics. Multi-number setup (3 SIM concept). Foundation for Claude Code build.
- [[whatsapp/rules-engine]] — Companion to playbook. Pure execution logic — 7-step pipeline (receive → identify number → identify channel → identify state → classify intent → determine action → execute & log). Master action table, intent taxonomy seed, templates, hard rules, escalation destinations, fallback behavior, drift detection. AI-readable, no philosophy.

## Workflows (Meta)

- [[ops/ingestion-profiles]] — Workflow 4: typed source handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip, seo-audit)
- [[ops/compilation-profiles]] — Workflow 5: named output profiles (aeo, website-copy, faq, social, slide-deck, schema)
- [[ops/health-checks]] — Workflow 6: on-demand, weekly, and monthly audit checklists
- [[ops/intake-gate]] — Workflow 7: universal raw intake gate
- [[ops/policy-source-ownership]] — Canonical owner per policy domain (booking, payment, cancellation, inclusions, health, ISIC, police escort, anti-fraud) + deprecated-wording guardrails
- [[ops/transformation-map]] — Master domain→bundle pipeline map (canonical source → compiler → output → validator → consumer → status). Output convention `output/<domain>/<bundle>/`. Trust Bundle DONE/do-not-reopen; Package Readiness is next wedge.
- [[ops/package-readiness-compiler-spec]] — Spec (no code) for the NEXT wedge: compiles 16 canonical packages → `output/products/package-readiness/` (registry, pricing, itineraries, booking-compatibility, gap-report, manifest) with 12 validation rules PKG-01–12. Primary deliverable = gap report.
- [[ops/whatsapp-reply-intelligence-compiler-spec]] — Spec (no code) for wedge P3 (WhatsApp Reply Bundle): compiles channel × state × intent → action + pre-rendered bilingual template + claim/policy citation, plus a coverage/contradiction gap report over playbook + rules-engine + canned-responses. Deterministic skeleton only; runtime LLM replies stay in WA Pro CRM consumer.

## Internal Ops

- [[internal-ops/backoffice-extraction]] — How to re-run the MySQL → CSV → wiki pipeline. PII rules, scripts, connection fallback. End-to-end runtime ~3 min for 63k rows.
- [[internal-ops/2026-06-02-chatbot-llmwiki-integration-audit]] — Integration audit of `chatbot-web-jvto` (live admin UI + WA webhook + chat API) against llm-wiki SSOT/bundles. 10 critical findings + 3-phase consolidation roadmap. Phase 1/2/3 preserved as long-term ambition (§5 superseded by slim-feed doc below).
- [[internal-ops/2026-06-02-chatbot-slim-feed-pattern]] — Near-term slim path distilled from the audit: minimal feed pattern covering main risks while respecting the chatbot as a running production system. Supersedes audit §5 planning.

## Finance

- [[finance/rate-cards]] — Consolidated cost components: 5 crew roles, 6 vehicle types, 27 activity items, 10 operational costs, 23 hotels (100+ room configs). All IDR.
- [[finance/package-costs]] — Per-package COGS from 15 Excel spreadsheets. 1-pax to 11-pax scaling. 8 packages with selling prices.
- [[finance/profit-analysis]] — Margin analysis (12.9%–34.9%), cost driver breakdown, pax-count impact, optimization opportunities, suggested prices for 7 unpriced packages.
- [[finance/custom-tour-builder]] — Step-by-step custom quote template with COGS formula, markup guidelines (25% default), worked example (3D2N Ijen-Bromo 2 pax).

## Open Gaps (no page yet — flagged by Lint)

- ~~`credentials/medical-screening`~~ — **created 2026-05-16** → [[credentials/medical-screening]]
- ~~`credentials/police-integration`~~ — **created 2026-05-16** → [[credentials/police-integration]]
- ~~`credentials/press-coverage`~~ — **created 2026-05-16** → [[credentials/press-coverage]]
- `content/voice-invariants` — Forbidden phrases and approved Ijen language: live as a section in [[website/brand-voice]] §voice-invariants. Promoting to its own page is optional — current location is canonical.
- ~~`content/schema-templates`~~ — **created 2026-05-18** → [[website/schema-templates]]
- `bromo-ijen-status-today` page — Silo 3 SEO target (keyword #7). Needs replacement live source for PVMBG/BBKSDA status; MAGMA feed not active. See [[seo/seo-strategy]] §Silo 3.
- ~~`raw/routes.csv` + `raw/route_details.csv`~~ — **ingested 2026-05-18** → [[sources/route-data-csv]]

## Lookup Conventions

- Link format: `[[folder/page-name]]` (Obsidian wikilink — example syntax, not a real link)
- In prose, use `->` before link: `-> [[destinations/kawah-ijen]]`
- Contradictions: `> Contradiction with [[other-page]]: <detail>` (example syntax)
- Stale claims: `> [stale?] <detail>`
- Structured facts trace to [[sources/ssot-v6]] unless otherwise cited
- Tone/voice exemplars trace to [[sources/jvto-homepage-clip]]
