---
type: overview
title: Operations Log
last_updated: 2026-05-14
sources: []
---

# JVTO Wiki Operations Log

*Append-only. Format: ## [YYYY-MM-DD] type | title. Most recent on top.*

---

## [2026-05-16] fix | G1 navigation gap resolved

**Trigger**: health check G1 flag — `products/packages-overview` had no in-body forward link to `products/packages-itineraries` (link to `packages-full-pricing` was already present at line 109).

**Pages updated (1)**:
- [[products/packages-overview]] — added "Day-by-day itineraries for all packages: see [[products/packages-itineraries]]" immediately after the existing full-pricing reference. Both detail pages now linked from the body, not just the footer.

**G1 status**: resolved ✅

---

## [2026-05-16] health-check | On-Demand (2nd run)

**Vault state**: 45 wiki pages · 16 raw files

---

### Contradiction Scan

No new contradictions found. All pre-existing contradictions remain correctly documented:

| Contradiction | Location | Status |
|---|---|---|
| Founding date (2015 vs 2016 vs 2023) | [[overview]] | Documented — three-era framing ✓ |
| Package count (§meta=15 vs §9_1=16) | [[overview]], [[products/packages-overview]] | Documented — 15 canonical ✓ |
| SSOT v4.0 review count (47) vs live (51) | [[credentials/trust-signals]] stale-value note | Documented ✓ |
| CLAUDE.md "mandatory screening" vs SSOT conditional | [[overview]] | Documented — conditional framing ✓ |
| Crew count §4_2=11 vs DB=14 | [[overview]] | **Resolved last run** — block updated to DB-confirmed 14 ✓ |

**PASS** ✅

---

### Orphan Detection

No true orphans. All 45 wiki pages have ≥1 inbound link from a non-index/log page.

Previous orphan `content/query-hero-claim` resolved via [[content/copy-bank]] — now has 5 inbound links. ✅

**Isolated cluster flagged (not orphans — informational):**

`ops/ingestion-profiles`, `ops/health-checks`, `ops/compilation-profiles`, and `sources/llm-kb-tooling-guide` form a closed cluster. They link to each other but have no inbound links from the main content graph (destinations, products, people, credentials, reviews, content pages). They are reachable only via [[index]] and [[log]].

- **Action**: no fix needed. Ops pages are infrastructure, not content — index + log is appropriate. Flagged for awareness.

**PASS** ✅

---

### Stale Claim Flags (>90 days)

All 45 wiki pages have `last_updated` between 2026-05-11 and 2026-05-16. No page exceeds the 90-day threshold.

**PASS** ✅

---

### Gap Page Identification

No new gaps identified. Open Gaps status:

| Gap | Status |
|---|---|
| `credentials/press-coverage` | ✅ Created 2026-05-16 |
| `credentials/medical-screening` | ✅ Created 2026-05-16 |
| `credentials/police-integration` | ✅ Created 2026-05-16 |
| `content/voice-invariants` | ⏸ Intentionally deferred — canonical in [[content/brand-voice]] |

Pre-existing navigation gap (carried from 2026-05-12 health check, no instruction to fix):
- **G1** — `products/packages-overview` has no forward links to `products/packages-full-pricing` or `products/packages-itineraries`. Both detail pages link back to overview but overview does not link forward.

---

### Summary

| Check | Result | Action taken |
|---|---|---|
| Contradiction scan | PASS | None |
| Orphan detection | PASS | None (previous O1 resolved) |
| Isolated cluster | Informational | Ops cluster flagged — no fix needed |
| Stale claims (>90 days) | PASS | None |
| Gap page identification | PASS | All 3 credential gaps resolved |

**No pages modified by this health check.**

---

## [2026-05-16] fix | content/query-hero-claim orphan resolved

**Trigger**: health check O1 flag — `content/query-hero-claim` had zero inbound links from content pages.

**Pages updated (1)**:
- [[content/copy-bank]] — added "Alternate Headlines (query-derived)" subsection under Hero Copy, embedding the two headline options from query-hero-claim with source attribution. Added footer link `-> [[content/query-hero-claim]]`.

**Why copy-bank is the right parent**: query-hero-claim's primary output is alternate hero headlines for price-skeptical travelers — a direct extension of copy-bank's Hero Copy section. Content producers browsing copy-bank now have a path to the deeper analysis.

**O1 status**: resolved ✅

---

## [2026-05-16] health-check | On-Demand

**Vault state**: 45 wiki pages · 15 raw files · 3 new credential pages created this session

---

### Contradiction Scan

**C1 — Crew count stale canonical instruction — FIXED**
`overview.md` line 135 carried the stale instruction "Treat 11/7+4 as canonical" — written before the 2026-05-12 DB export resolved the crew count to 14 (7+7). `people/crew-registry.md` correctly says "Updated canonical: 14 members total." The overview contradiction block was updated to reflect the resolved state.
- **Action taken**: `overview.md` crew contradiction block updated: stale "Treat 11 as canonical" → "Resolved 2026-05-12: DB confirmed 14 (7+7)." ✅

Pre-existing contradictions still correctly documented (no action needed):
- Package count: §meta=15 vs §9_1=16 (partially resolved by sitemap confirming 16 live — flag preserved)
- Founding date: three-era framing — preserved in overview.md
- CLAUDE.md "mandatory screening" vs SSOT conditional framing — preserved in overview.md

---

### Orphan Detection

**O1 — `content/query-hero-claim` — TRUE ORPHAN**
Grep confirms zero inbound links from any content page (excluding index.md and log.md). Page was created 2026-05-12; only index and log reference it.
- **Action**: flagged. No fix without instruction.

Previously flagged orphans (2026-05-12 health check) now resolved:
- O1 `reviews/google-tripadvisor-2026` — now linked from review-patterns + trustpilot-compilation + db-export source ✅
- O2 `content/operational-facts` — now linked from faq-master + whatsapp-playbook + db-export source ✅

---

### Stale Claim Flags (>90 days)

All 45 wiki pages have `last_updated` between 2026-05-11 and 2026-05-16. No page exceeds the 90-day threshold. **PASS** ✅

---

### Navigation Gaps (overview.md forward-link deficits) — FIXED

Three new credential pages (created today) were not linked from `overview.md`. Fixed by adding targeted forward links:
- Press Recognition section → now links to [[credentials/press-coverage]] (in addition to trust-signals)
- Founder section → now links to [[credentials/police-integration]]
- Packages section (health-screening reference) → now links to [[credentials/medical-screening]]

---

### Gap Page Identification

All 3 credential gap pages created this session. Open Gaps status:

| Gap | Status |
|---|---|
| `credentials/press-coverage` | ✅ Created 2026-05-16 |
| `credentials/medical-screening` | ✅ Created 2026-05-16 |
| `credentials/police-integration` | ✅ Created 2026-05-16 |
| `content/voice-invariants` | ⏸ Intentionally deferred — canonical in [[content/brand-voice]] |

No new gaps identified.

---

### Summary

| Check | Result | Action taken |
|---|---|---|
| Contradiction scan | 1 stale instruction found | Fixed: overview.md crew block updated |
| Orphan detection | 1 true orphan found (query-hero-claim) | Flagged — no fix without instruction |
| Previous orphans (O1/O2) | Both resolved | No action needed |
| Stale claims (>90 days) | PASS | None |
| Navigation gaps | 3 gaps in overview.md | Fixed: forward links to 3 new credential pages |
| Gap page identification | No new gaps | All 3 credential gaps resolved |

**Pages modified by this health check**: [[overview]] (crew block + forward links).

---

## [2026-05-16] output | credentials/medical-screening + credentials/police-integration — 2 gap pages created

**Trigger**: user request. Both were tracked Open Gaps since [[log]] `2026-05-11` lint pass.

**Pages created (2)**:
- [[credentials/medical-screening]] — Consolidated Ijen health-screening reference: BBKSDA SE.1658/KSA.9/2024 regulatory basis, 4-step protocol (health.mountijen.com digital system), Dr. Ahmad Irwandanu details + verification URLs, 3 partner facilities, 5 screening photos + BBKSDA terms screenshot (recategorized from `uncertain`), voice invariant table (approved/forbidden), 5 content angles, 3 AEO Q&A blocks for C4.
- [[credentials/police-integration]] — Full 4-layer evidence chain for police-led claim: (1) SPRIN POLPAR + SPRIN WAL-TRAVEL with SHA-256 and image URLs; (2) 3 escort photos + Geopark briefing photo from field ops; (3) 3-article press cross-corroboration (Detik + Radar Jember ×2); (4) Ditpamobvit unit institutional detail. Traffic Police escort mechanics explained. 6 content angles, 3 AEO Q&A blocks for C1/C5.

**Pages updated (6)**:
- [[people/dr-ahmad-irwandanu]] — backlink to medical-screening added to footer
- [[people/agung-sambuko]] — backlink to police-integration added to footer
- [[credentials/legal-licenses]] — backlinks to police-integration + medical-screening added
- [[credentials/trust-signals]] — backlinks to police-integration + medical-screening added
- [[index]] — both pages added to Credentials section; Open Gap entries struck through; total_pages 43→45
- [[log]] — this entry

**Open Gaps status**: all 3 credential gap pages now resolved. Only `content/voice-invariants` remains in Open Gaps (intentionally deferred — currently canonical in brand-voice).

---

## [2026-05-16] output | credentials/press-coverage — gap page created

**Trigger**: user request. Was an Open Gap since [[log]] `2026-05-11` lint pass.

**Pages created (1)**:
- [[credentials/press-coverage]] — consolidated press intelligence: 4 independent press items (Detik.com 2021-03-14 full + Radar Jember ×2 paywalled + BBKSDA Jatim 2024 full), Stefan Loose guidebook 2016 p. 287, entity linking analysis, content angles, AEO-ready snippets for C9. Screenshot image URLs from [[sources/ssot-image-asset-map]].

**Pages updated (3)**:
- [[credentials/trust-signals]] — backlink to press-coverage added to navigation footer
- [[index]] — press-coverage added to Credentials section; Open Gap entry struck through; total_pages 42→43
- [[log]] — this entry

**Sources drawn from**: [[sources/detik-polpar-2021]], [[sources/radar-jember-polpar-geopark-2021]], [[sources/radar-jember-bau-menyengat-2021]], [[sources/bbksda-pelatihan-pemandu-2024]], [[sources/ssot-v6]], [[sources/ssot-image-asset-map]]

**Content value added**:
- Entity linking table: maps each source → entity named → independence level — synthesizes the 3-article cross-corroboration argument in one place
- Stefan Loose guidebook page now has 3 image URLs for content production use
- 5 named content angles with placement guidance
- 2 AEO-ready Q&A blocks for C9 claim

---

## [2026-05-16] ingest | JVTO Image Asset Map — 54 Images Across 14 Groups

**Source type**: ssot-update (Workflow 4 — structured image SSOT, closest existing profile)
**Raw files**: `raw/JVTO SSOT Image Asset Map.md` · `raw/JVTO SSOT Image Inventory.md` · `raw/jvto_image_asset_map.json`

**Pages created (1)**:
- [[sources/ssot-image-asset-map]] — full catalog: 54 images, 14 groups, every URL + caption + alt text + recommended_filename + recommended_pages

**Pages updated (4)**:
- [[people/crew-registry]] — added `## Image Assets` section: 11 portrait URLs (all named KTA crew) + 5 KTA card image URLs (Kiki, Anjas, Taufik, Gufron, Rendi)
- [[people/agung-sambuko]] — expanded `## Image` → `## Image Assets`: 3 founder images (formal portrait, Tourist Police portrait, Wikipedia copy) with captions and alt text
- [[credentials/legal-licenses]] — added `## Document Image Assets`: NIB, TDUP, HPWKI, SPRIN POLPAR, SPRIN WAL-TRAVEL — all in PNG + WebP; office photo URL added
- [[credentials/trust-signals]] — expanded historical recognition table (5 rows, now with direct image URLs); added press screenshot image table (3 images: Detik, BBKSDA, Radar Jember)
- [[index]] — ssot-image-asset-map added to sources; total_pages 41→42

**Key findings**:
- 54 live images confirmed on javavolcano-touroperator.com — full visual evidence library now catalogued in wiki
- Police presence visually documented across 8 field operations photos (escort day/night, vehicle, Geopark briefing, Baratha Hotel departure)
- 5 health screening images exist — enough for a complete "How Ijen Screening Works" visual section
- Booking.com 2015 shipping label image is an address continuity proof (Jl. Khairil Anwar No.102 = same address as today's PT office)
- 1 uncertain image: BBKSDA ticket T&C screenshot — likely `health_screening` but needs manual categorization
- 1 external-hosted image: Mr. Sam on Wikimedia Commons (only asset not on JVTO server)

**Inventory discrepancy noted**: Image Inventory counts 55 URLs; Asset Map and JSON count 54. Inventory misclassifies Stefan Loose history photos and BBKSDA screenshot into `crew` group. JSON is authoritative at 54.

**Gap pages strengthened by this ingest** (not yet created — see Open Gaps in [[index]]):
- `credentials/medical-screening` — now has 5 photo URLs ready to embed
- `credentials/police-integration` — now has 4 SPRIN document images + 3 field operations police photos
- `credentials/press-coverage` — now has 3 press screenshot URLs

---

## [2026-05-14] output | WhatsApp Rules Engine + Playbook expansion
Pages created: [[ops/2026-05-14-whatsapp-rules-engine]] — companion document to playbook, contains pure execution logic for AI/system consumption. Structure: 7-step pipeline (receive → identify number → identify channel → identify state → classify intent → determine action → execute), master action table with confidence+risk routing, intent taxonomy seed (35+ intents across 5 channels), template examples (multi-language), 12 hard rules (never-cross), escalation destinations, fallback behavior, drift detection thresholds. Pages updated: [[ops/2026-05-14-whatsapp-operations-playbook]] — added Section 7.5 (multi-number setup with 3-SIM concept: customer / B2B partner / internal ops; migration path; routing rules; risks), added companion reference in frontmatter and intro. [[index]] — entry for rules engine added under Ops section. Trigger context: user requested (1) more systematic flow that AI/anyone can follow without interpretation, (2) explanation of why Window B2B = manual (answered in chat), (3) multi-number concept (added to playbook §7.5), (4) simple DB password rotation guidance (answered in chat — delegated to David).

---

## [2026-05-14] output | WhatsApp Operations Playbook
Profile: ops-playbook (operational design doc, non-technical). Pages created: [[ops/2026-05-14-whatsapp-operations-playbook]]. Scope: 5 WhatsApp channels (JVTO inquiry, JVTO post-booking, Klook, Window Travel, Vendor/Crew) mapped as funnels with stages, entry/exit triggers, system vs human actions, and per-stage AI automation eligibility. Includes: inventory of existing assets (people, tech, content, workflows), 13-item pin-point diagnosis (strategic/operational/risk), unified customer state machine, channel resolution rules, escalation/authority paths, brand voice matrix per audience, SLA matrix, success metrics (response time + automation ratio + business outcome), risk register, 8-phase roadmap from inbox visibility through strategic migration. Pages updated: [[index]] (entry added under Ops section). Source dependencies: [[content/brand-voice]], [[content/faq-master]], [[content/operational-facts]], [[products/packages-full-pricing]], [[products/packages-itineraries]], [[sources/jvto-policy-pack-v6]], [[people/dr-ahmad-irwandanu]], [[people/crew-registry]], destinations pages. Note: complements technical implementation spec to be built in Claude Code; this doc is the operational design that spec must serve.

---

## [2026-05-12] query | Hero claim for price-skeptical solo traveler
Query: "What single trust claim should anchor homepage hero copy for a price-skeptical first-time solo traveler?" Pages read: [[reviews/review-patterns]], [[content/aeo-claims]], [[credentials/trust-signals]], [[products/packages-overview]]. Answer: C3 (All-inclusive clarity, no surprise costs) leads — T5 review pattern (unprompted "no unexpected costs" mentions) is the strongest third-party corroboration for price-skeptics. C1/C5 follows to justify the premium through the verifiable police-credentials chain. Headline option A (C3-first departure from live site) and option B (C1+C3 combined, closer to live site) provided. Pages created: [[content/query-hero-claim]]. Pages updated: [[index]] (entry added; total_pages 40→41). Caveat: "price-skeptical" is inferred by claim/pattern alignment, not behavioral segmentation data.

---

## [2026-05-12] ingest | 3 press source pages
Sources ingested: Radar Jember 2021-03-24 (Polpar + Geopark) — paywalled; Radar Jember 2021-05-27 (bau menyengat) — paywalled; BBKSDA Jatim 2024-05-24 (pelatihan pemandu) — full access. Pages created: [[sources/radar-jember-polpar-geopark-2021]], [[sources/radar-jember-bau-menyengat-2021]], [[sources/bbksda-pelatihan-pemandu-2024]]. Key BBKSDA findings: 3-day training (May 20–22, 2024) at Paltuding; 250 HPWKI-affiliated guides targeted; curriculum: conservation awareness, guide responsibilities, SAR, PPGD (emergency medical); government-hosted — validates HPWKI training chain as BBKSDA-supervised, not self-certified. Pages updated: [[credentials/trust-signals]] (Source page column added to press table), [[people/agung-sambuko]] (Radar Jember sources linked in proof chain), [[index]] (3 new entries; total_pages 37→40).

---

## [2026-05-12] output | website-copy — Homepage
Profile: website-copy. Output: `output/copy-2026-05-12-homepage.md`. Style B voice with Style A fact inserts. 9 sections: Hero, Why JVTO (6 differentiators), Destinations (4), Tour Packages (Surabaya 12 + Bali 4), Reviews (3-platform counts), Trust & Verification (5-item trust stack), Our Story, CTA, Footer. All claims source-cited inline. Voice invariants enforced: conditional Ijen health-screening language, conditional Blue Fire language, no forbidden phrases. Production notes included (package count, Bali finish warning, review date freshness). Sources: copy-bank, brand-voice, aeo-claims C1–C9, packages-overview, kawah-ijen, mount-bromo, legal-licenses, trust-signals, agung-sambuko, sitemap-2026-05.

---

## [2026-05-12] ingest | JVTO Website Sitemap — May 2026
Profile: pdf-doc (structured XML document). Pages updated: sources/sitemap-2026-05 (created), products/packages-overview, credentials/trust-signals, index. Key additions: 44-URL sitemap reveals 16 live tour pages (12 Surabaya + 4 Bali); resolves package-count contradiction in favor of SSOT §9_1/§13 (was disputed as 15 vs 16); `taman-safari-prigen-bromo-madakaripura-3d2n` confirmed as active 12th Surabaya package; Verify JVTO trust verification hub documented (4 sub-pages: legal, press-recognition, history-artifacts, police-safety); ISIC student package confirmed as dedicated /isic/ path; `/travel-guide/best-time-to-visit` identified as most recently updated page (2026-05-12).

---

## [2026-05-12] output | aeo — Why JVTO
Profile: aeo. Output: `output/aeo-2026-05-12-why-jvto.md`. 22 Q&A blocks across 9 sections covering full C1–C9 claim set. Sections: Legitimacy/Licensing (3Q), Tourist Police (4Q), Private Tours (2Q), All-Inclusive (3Q), Ijen Screening (3Q), Reviews (2Q), Team (2Q), Partners (3Q), Press (3Q). All answers ≤40 words, citation-first, no hedging. Sources: aeo-claims, faq-master, legal-licenses, trust-signals.

---

## [2026-05-12] output | faq — Madakaripura FAQ
Profile: faq. Output: `output/faq-2026-05-12-madakaripura.md`. 20 questions across 7 sections: About Madakaripura (incl. height reconciliation + Gajah Mada history), The Visit (approach, timing, wetness, horse), Safety & Equipment (helmets attributed to local site mgmt), Packages (6 packages with pricing), Fitness/Suitability, Weather, Booking. health_wording_mode: none. Sources: madakaripura, faq-master, operational-facts, packages-overview, packages-full-pricing, credentials.

---

## [2026-05-12] output | faq — Tumpak Sewu FAQ
Profile: faq. Output: `output/faq-2026-05-12-tumpak-sewu.md`. 19 questions across 7 sections: About Tumpak Sewu, Two Vantage Points (rim vs canyon), Safety & Equipment (helmets attributed to local site mgmt, water shoes, wetness), Packages (6 packages listed; no standalone tour noted), Fitness/Suitability, Weather/Conditions, Booking. health_wording_mode: none. Sources: tumpak-sewu, faq-master, operational-facts, packages-overview, packages-full-pricing, credentials.

---

## [2026-05-12] output | faq — Bromo FAQ
Profile: faq. Output: `output/faq-2026-05-12-bromo.md`. 24 questions across 8 sections: About Bromo, Sunrise Experience, Jeep & Caldera Floor (5 Qs), Milky Way, Packages (pricing both origins + combos), Fitness/Packing, Closures/Kasada/Plan B, Booking. No health screening section (health_wording_mode: none). Sources: mount-bromo, faq-master, operational-facts, packages-overview, packages-full-pricing, packages-itineraries, credentials.

---

## [2026-05-12] output | faq — Ijen FAQ
Profile: faq. Output: `output/faq-2026-05-12-ijen.md`. 22 questions across 8 sections: About Kawah Ijen, The Hike, Blue Fire, Health Screening (Q6/Q7 canonical + expanded), JVTO Ijen Packages (pricing from both origins), Fitness/Children, Closures/Weather, Booking. All Ijen voice invariants applied (conditional framing, no blue-fire guarantee). Sources: faq-master, kawah-ijen, dr-ahmad-irwandanu, operational-facts, packages-overview, packages-full-pricing, credentials.

---

## [2026-05-12] output | website-copy — Bali Landing Page
Profile: website-copy. Output: `output/copy-2026-05-12-bali-landing.md`. Sections: Hero, route overview (Bali→Bali vs Bali→SUB distinction), 4 packages with day-by-day itinerary tables + pricing (solo/2 pax/11+ pax), inclusions (ferry noted), Why JVTO, trust signals, booking. Sources: packages-overview, packages-full-pricing, packages-itineraries, copy-bank, brand-voice, aeo-claims, credentials.

---

## [2026-05-12] output | website-copy — Surabaya Landing Page
Profile: website-copy. Output: `output/copy-2026-05-12-surabaya-landing.md`. Sections: Hero, 11 packages with per-person pricing (2 pax + 11+ pax), inclusions, Why JVTO (4 differentiators), trust signals table, booking steps. Sources: packages-overview, packages-full-pricing, copy-bank, brand-voice, aeo-claims, credentials.

---

## [2026-05-12] health-check | Weekly (2nd run — post DB ingest)

**Vault state**: 36 wiki pages · 12 raw files · 2 Clippings (already ingested)

---

### Stale Claims (30-Day Sweep)

All 36 wiki pages carry `last_updated: 2026-05-11` or `2026-05-12`. No sourcing pages exceed the 30-day threshold. **PASS** ✅

---

### New Orphan Detection (pages created since last health check)

Six pages were created by the [2026-05-12] DB Export ingest, after the prior health check ran. Inbound-link status (excluding index.md and log.md):

| Page | Inbound links (non-index/log) | Status |
|---|---|---|
| sources/db-export-2026-05 | overview, crew-registry, operational-facts, hotels, google-tripadvisor-2026, packages-full-pricing, packages-itineraries | ✅ Well-connected |
| products/packages-full-pricing | db-export-2026-05, packages-itineraries | ✅ Connected |
| products/packages-itineraries | db-export-2026-05, packages-full-pricing, hotels | ✅ Connected |
| reviews/google-tripadvisor-2026 | db-export-2026-05 only | ⚠ Soft orphan |
| content/hotels | db-export-2026-05, packages-itineraries | ✅ Connected |
| content/operational-facts | db-export-2026-05 only | ⚠ Soft orphan |

**Two soft orphans flagged (no fix without instruction):**

- **O1 — `reviews/google-tripadvisor-2026`**: Only non-index inbound link is the DB source page. Not cross-referenced from [[reviews/trustpilot-compilation]] or [[reviews/review-patterns]] — the two pages in the same cluster. A reader navigating the reviews cluster has no in-cluster path to the Google/TripAdvisor data.
- **O2 — `content/operational-facts`**: Only non-index inbound link is the DB source page. Not referenced from [[content/faq-master]], [[content/aeo-claims]], or [[content/copy-bank]], despite being the authoritative source for temperatures, travel times, and closure data those pages draw on.

**Navigation gap flagged (not a true orphan, no fix without instruction):**

- **G1 — `products/packages-overview` has no forward links to `packages-full-pricing` or `packages-itineraries`**: The overview is the natural entry point for the products section. Both detailed pages link back to the overview (correct), but the overview does not link forward to them. A reader following the Products section of the index hits the overview and has no in-page path to the pricing tables or itineraries.

---

### Index Completeness

All 36 wiki pages verified against [[index]] section listings. No missing entries. **PASS** ✅

**Index frontmatter count — CORRECTED:**

`wiki/index.md` frontmatter read `total_pages: 38`. Actual page count (directory listing): **36**. Root cause: the [2026-05-12] DB ingest log entry stated "Pages created (8)" but listed only 6 pages, producing a +2 overcounting that propagated into the index frontmatter (`30→38` instead of `30+6=36`). The log entry itself is append-only and unchanged; the index frontmatter has been corrected.

- **Action taken**: `wiki/index.md` `total_pages: 38 → 36`. ✅

---

### Log Completeness

12 raw files audited:

| Raw file | Log entry |
|---|---|
| `Tourist Police-Led Private Volcano Tours in East Java.md` | [2026-05-11] init (jvto-homepage-clip) ✓ |
| `JVTO_FINAL_CLEAN_SSOT.json` | [2026-05-11] ingest \| SSOT v6.0 ✓ |
| `*.gpx` (×5) | [2026-05-11] ingest \| GPX Trail Data Enrichment ✓ |
| `llm-kb-tooling-guide.md` | [2026-05-11] ingest \| LLM KB Tooling Guide ✓ |
| `JVTO_Policy_Pack_REVISED_v6_2026-01-26_3POLICIES_ONLY.md` | [2026-05-12] ingest \| JVTO Policy Pack ✓ |
| `JVTO_Travel_Guide_PUBLISHABLE_EN_2026-01-18.md` | [2026-05-12] ingest \| JVTO Travel Guide EN ✓ |
| `JVTO_Travel_Guide_SSOT_EN.json` | [2026-05-12] ingest \| JVTO Travel Guide EN ✓ |
| `db_export_raw.json` | [2026-05-12] ingest \| DB Export ✓ |

**PASS** ✅

**Clippings**: 2 files present, both already ingested ([2026-05-11] Clippings ingest). No uningested Clippings. ✅

---

### Summary

| Check | Result | Action taken |
|---|---|---|
| Stale claims (30-day) | PASS | None |
| New orphan detection | 2 soft orphans (O1, O2) | Flagged — no fix without instruction |
| Navigation gap | 1 gap G1 (packages-overview ↛ pricing/itineraries) | Flagged — no fix without instruction |
| Index completeness (listing) | PASS | None |
| Index total_pages count | FAIL → FIXED | `total_pages: 38 → 36` in [[index]] |
| Log completeness | PASS | None |

**Pages modified by this health check**: [[index]] (frontmatter count only).

---

## [2026-05-12] ingest | DB Export — Live Database Snapshot

**Source type**: ssot-update (Workflow 4) — structured DB export covering 14 data categories
**Raw file**: `raw/db_export_raw.json`

**Pages created (8)**:
- [[sources/db-export-2026-05]] — source summary; contradictions flagged; cross-reference map
- [[products/packages-full-pricing]] — complete pricing for all 22 packages (all pax tiers)
- [[products/packages-itineraries]] — all 99 day-by-day itinerary entries; recurring patterns; hotel allocation per phase
- [[reviews/google-tripadvisor-2026]] — 92 Google reviews (4.90/5) + 21 TripAdvisor reviews (4.95/5); crew mentions; themes mapped
- [[content/hotels]] — 23 hotel partners by phase (Bondowoso/Banyuwangi, Bromo, Tumpak Sewu/Jember, Malang, Surabaya finish)
- [[content/operational-facts]] — temperatures, travel times, support hours, Ijen monthly closure, trolley ojek, micro-customization policy, FOC 5% discount

**Pages updated (5)**:
- [[people/crew-registry]] — total_crew 11→14 (7+7); Yusuf/Dika/Pras confirmed as active drivers; self-quotes for all 14; soft-data table revised; Dika + Pras resolved from soft-data
- [[products/packages-overview]] — FOC table updated with 5% group discount at 50+ pax
- [[overview]] — crew count updated to 14 (7+7)
- [[index]] — total_pages 30→38; db-export-2026-05 source added; 5 new pages registered
- [[log]] — this entry

**Key new data vs prior wiki state**:
- **Full pricing**: was 4 sample tables → now 22 complete tables (143 price rows)
- **Itineraries**: was zero → now 99 day entries covering all packages
- **Reviews**: was 51 Trustpilot only → now 164 total (44 TP + 92 Google + 21 TripAdvisor)
- **Crew**: was 11 KTA → now 14 confirmed (3 new drivers: Yusuf, Dika, Pras)
- **Hotels**: was unnamed → now 23 named partners with area and itinerary phase mapping
- **Operational facts**: NEW — temperatures, travel times, Ijen closure schedule, support hours

**Contradictions flagged**:
1. `kb.cancellation-policy` says "50% fee <48h" vs policy pack canonical "100% forfeiture" — KB is stale
2. `kb.group-benefits-foc` adds 5% discount at 50+ pax — not in prior wiki sources; verify with owner
3. DB Trustpilot = 44 reviews / 4.93 avg vs live clip = 51 reviews / 4.8 — DB snapshot is older

---

## [2026-05-12] health-check | Weekly

**Vault state**: 30 wiki pages · 11 raw files · 5 output files

---

### On-Demand Checks (Contradiction Scan)

**C1 — Review count: FIXED**
`wiki/overview.md`, `wiki/credentials/trust-signals.md`, `wiki/content/aeo-claims.md`, and `wiki/index.md` all referenced "47 reviews (verified 2026-04-19)". The canonical count was updated to **51** (verified 2026-05-09) in `wiki/reviews/trustpilot-compilation.md` during the 2026-05-11 Trustpilot ingest, but the fix was not propagated to these 4 pages.
- **Action taken**: All 4 pages updated to `51 reviews, verified 2026-05-09`. ✅

**C2 — Founding date (pre-existing, no new action)**
`wiki/overview.md` carries a `> Contradiction with project CLAUDE.md` block distinguishing the three founding eras (2015 guesthouse, 2016 PT operational, 2023 TDUP). No change required.

**C3 — Crew count (pre-existing, no new action)**
`wiki/overview.md` carries a `> Contradiction within SSOT` note: §4_2 = 11 canonical vs §13 = 14. No change required.

**C4 — Package count (pre-existing, no new action)**
`wiki/overview.md` and `wiki/products/packages-overview.md` carry `> Contradiction` blocks: §meta = 15 canonical vs §9_1/§13 = 16. No change required.

---

### Orphan Detection

**O1 — `destinations/papuma-beach` — FIXED**
The page was only linked from `wiki/index.md` and `wiki/log.md`. No other content page used a `[[destinations/papuma-beach]]` wikilink. `wiki/overview.md` had a stale "gap" note ("Papuma Beach (gap — see [[index]])") written before the page existed.
- **Action taken**: Updated `wiki/overview.md` destinations table to use `[[destinations/papuma-beach]]`. ✅

**New orphan check (pages created since last log entry):**
- `wiki/sources/jvto-policy-pack-v6.md` — linked from log.md + index.md + jvto-travel-guide-en.md ✓
- `wiki/sources/jvto-travel-guide-en.md` — linked from log.md + index.md ✓
- Neither is an orphan. ✅

---

### Stale Claim Flags (30-Day Sweep)

All wiki pages have `last_updated: 2026-05-11` or `2026-05-12` (within 30 days of 2026-05-12). No pages exceed the 30-day sourcing threshold.

The review-count mismatch (47 vs 51) was an intra-wiki contradiction, not a stale-by-age claim — resolved under C1 above.

**Stale value note still in `wiki/sources/ssot-v6.md`**: The SSOT snapshot records `review_count: 47` — this correctly reflects the SSOT v6.0 document date (2026-04-22). Historical record; no update warranted on the source summary page.

---

### Index Completeness

All 27 non-root wiki pages (sources ×7, destinations ×5, products ×1, people ×3, credentials ×2, reviews ×2, content ×4, ops ×3) verified against `wiki/index.md`. **PASS** ✅

---

### Log Completeness

All 11 raw files verified against log entries:

| Raw file | Log entry |
|---|---|
| `Tourist Police-Led Private Volcano Tours in East Java.md` | `[2026-05-11] init | Wiki Initialization` (as jvto-homepage-clip) ✓ |
| `JVTO_FINAL_CLEAN_SSOT.json` | `[2026-05-11] ingest | JVTO_FINAL_CLEAN_SSOT.json v6.0` ✓ |
| `*.gpx` (×5) | `[2026-05-11] ingest | GPX Trail Data Enrichment` ✓ |
| `llm-kb-tooling-guide.md` | `[2026-05-11] ingest | LLM KB Tooling Guide` ✓ |
| `JVTO_Policy_Pack_REVISED_v6_2026-01-26_3POLICIES_ONLY.md` | `[2026-05-12] ingest | JVTO Policy Pack` ✓ |
| `JVTO_Travel_Guide_PUBLISHABLE_EN_2026-01-18.md` | `[2026-05-12] ingest | JVTO Travel Guide EN` ✓ |
| `JVTO_Travel_Guide_SSOT_EN.json` | `[2026-05-12] ingest | JVTO Travel Guide EN` ✓ |

**PASS** ✅

---

### Summary

| Check | Result | Action taken |
|---|---|---|
| Contradiction scan | 1 new issue found | Fixed: 47→51 Trustpilot count in 4 pages |
| Orphan detection | 1 orphan found | Fixed: papuma-beach wikilink added to overview.md |
| Stale claim flags (30-day) | PASS | No sourcing pages >30 days old |
| New orphan check | PASS | Both new source pages have inbound links |
| Index completeness | PASS | All 27 non-root pages listed |
| Log completeness | PASS | All 11 raw files have log entries |

**Pages modified by this health check**: `wiki/overview.md` · `wiki/credentials/trust-signals.md` · `wiki/content/aeo-claims.md` · `wiki/index.md`

---

## [2026-05-12] output | AEO Blocks — Policy & Travel Guide

**Profile**: aeo (Workflow 5)
**Output file**: `output/aeo-2026-05-12-policy-travel-guide.md`

**Sources drawn from**: [[sources/jvto-policy-pack-v6]], [[sources/jvto-travel-guide-en]], [[content/aeo-claims]] C1–C9, [[content/faq-master]]

**30 Q&A blocks across 9 sections**:
- Booking confirmation & payments (6 blocks)
- Cancellation & Travel Credit (5 blocks)
- Inclusions & vehicle allocation (6 blocks)
- Ijen health screening (5 blocks)
- Packing & fitness by destination (6 blocks) — includes silver jewelry warning
- Safety & tour management (3 blocks)
- Weather & closures (3 blocks)
- Police escort (3 blocks)
- My Booking Portal & privacy (2 blocks)

**New AEO angles not previously in output/**:
- Silver jewelry warning for Ijen
- Fitness level per destination (Bromo/Ijen/Tumpak Sewu)
- QR screening system + non-JVTO travelers
- Vehicle allocation specs (MPV/Hiace/Hiace+MPV thresholds)
- Bromo jeep capacity (max ±4 guests)
- FOC scheme (18/35/50 pax thresholds)
- My Booking Portal capabilities
- Alcohol/substance safety rule
- Police escort formal channel (Traffic Police request, not proprietary)

---

## [2026-05-12] ingest | JVTO Travel Guide EN — Publishable Copy + SSOT JSON

**Source type**: pdf-doc (Workflow 4)
**Raw files**: `raw/JVTO_Travel_Guide_PUBLISHABLE_EN_2026-01-18.md` + `raw/JVTO_Travel_Guide_SSOT_EN.json`

**Pages created (1)**:
- [[sources/jvto-travel-guide-en]] — 7-route travel guide: booking info, FAQ (15 Qs), Ijen screening, safety framework, packing by destination, weather/closures, police escort

**Pages updated (1)**:
- [[index]] — sources list updated; total_pages 28→30; jvto-travel-guide-en entry added

**Key new material**:
- Silver jewelry warning for Ijen (§6.7) — not previously in wiki
- Fitness levels per destination (Bromo/Ijen/Tumpak Sewu)
- My Booking Portal post-payment feature list
- QR verification purpose for screening (anti-forgery, available to non-JVTO travelers)
- Police escort: JVTO submits formal Traffic Police request (does not provide own escorts)
- Guest alcohol/substance rule (hike refusal)
- 5-step booking process verbatim

---

## [2026-05-12] ingest | JVTO Policy Pack — 3 Customer-Facing Policies v2026-01-17

**Source type**: pdf-doc (Workflow 4)
**Raw file**: `raw/JVTO_Policy_Pack_REVISED_v6_2026-01-26_3POLICIES_ONLY.md`

**Pages created (1)**:
- [[sources/jvto-policy-pack-v6]] — 3 policies (Booking/Payment/Cancellation, Inclusions/Exclusions, Privacy); bank transfer details, vehicle allocation specs, FOC scheme, Travel Credit terms, force majeure rules

**Pages updated (1)**:
- [[index]] — sources list updated; jvto-policy-pack-v6 entry added

**Key facts confirmed / first-ingested**:
- Bank details: BRI 001301001779564 (SWIFT BRINIDJAXXX), BCA 1200944352 (SWIFT CENAIDJAXXX)
- Vehicle allocation: 2–3 guests = MPV; 4–9 = Hiace; 10–11 = Hiace + MPV
- Bromo jeep max: ±4 guests per jeep
- FOC: 18 pax = 1 FOC, 35 pax = 2 FOC, 50 pax = 3 FOC
- Travel Credit: IDR, non-expiring, transferable with written confirmation
- Cancellation: 48h cut-off local Indonesia time (≥48h = 100% Travel Credit; <48h = forfeit)
- Payment: deposit 20%; balance card 5 days; balance transfer 3 days before Day 1
- SSL + PCI DSS checkout; JVTO never stores card details

---

## [2026-05-11] build | Wiki Ops System — Workflows 4–6

**Spec**: `docs/superpowers/specs/2026-05-11-wiki-ops-system-design.md`

**Pages created (3)**:
- [[ops/ingestion-profiles]] — Workflow 4: 5 source type handlers (web-clip, pdf-doc, ssot-update, review-feed, press-clip)
- [[ops/compilation-profiles]] — Workflow 5: 5 named profiles (aeo, website-copy, faq, social, slide-deck) with draw-from lists, format constraints, forbidden patterns, output filename conventions
- [[ops/health-checks]] — Workflow 6: 3-tier audit (on-demand replaces Workflow 3/Lint, weekly adds stale sweep + completeness checks, monthly adds credential web-verification)

**Files modified (2)**:
- [[index]] — Ops section added; total_pages confirmed at 28
- `CLAUDE.md` — `wiki/ops/` added to dir structure; `ops` added to frontmatter type list; Workflows 4–6 stubs added after Workflow 3

**Verification**:
- ✅ 3 ops pages created with correct frontmatter (type: ops)
- ✅ All 5 ingestion profiles present in ingestion-profiles.md
- ✅ All 5 compilation profiles present in compilation-profiles.md
- ✅ All 3 health check tiers present in health-checks.md
- ✅ wiki/index.md Ops section links all 3 pages
- ✅ CLAUDE.md Workflows 4–6 wired; ops/ in directory structure; ops added to frontmatter type list

---

## [2026-05-11] ingest | LLM KB Tooling Guide

**Source type**: web-clip (manually captured article)
**Raw file**: `raw/llm-kb-tooling-guide.md`

**Pages created (1)**:
- [[sources/llm-kb-tooling-guide]] — Karpathy-inspired LLM KB patterns; key facts, applicable patterns, not-applicable list

**Pages updated (1)**:
- [[index]] — sources list + total_pages 24→28 (anticipating Phase 2 ops pages); llm-kb-tooling-guide source entry added

**Key findings**:
- JVTO's existing raw/ → wiki/ → output/ structure already matches the article's recommended pattern
- Three actionable patterns identified: typed ingestion (Workflow 4), compilation profiles (Workflow 5), tiered health checks (Workflow 6)
- MCP server and automation options explicitly deferred — CLAUDE.md-only implementation chosen

**Verification**:
- ✅ raw/llm-kb-tooling-guide.md created with immutability note
- ✅ wiki/sources/llm-kb-tooling-guide.md frontmatter correct (type: source)
- ✅ wiki/index.md sources list updated; total_pages 24→28

---

## [2026-05-11] ingest | content/copy-bank compiled

**Source material**: [[content/aeo-claims]] (C1–C9 nlp_short), [[sources/jvto-homepage-clip]] (hero + bio copy), [[content/brand-voice]] (approved/forbidden phrases)

**Pages created (1)**:
- [[content/copy-bank]] — 9 NLP snippets, hero headline/subheadline/bio, approved Ijen language, forbidden phrases, trust stack order

**Pages updated (2)**:
- [[index]] — copy-bank added to Content Production; removed from Open Gaps; total_pages 23→24
- [[log]] — this entry

**Verification**:
- ✅ 0 unfilled placeholders in copy-bank.md
- ✅ Open Gaps section shrunk by 1 item

---

## [2026-05-11] lint | Madakaripura height contradiction resolved

**Resolution**: External web research confirms ~200 m as the widely-accepted total height of Madakaripura Waterfall across multiple independent sources: Indonesia's official tourism portal (indonesia.travel), indonesia-tourism.com, javatourism.co.id, backpackmoments.com, borobudursunrise.net, and others. The SSOT §9_4 figure of ~100 m likely refers to the main visible curtain drop only. Both values are now attributed in the Quick Facts table: main curtain drop ~100 m (SSOT §9_4) and total height ~200 m (indonesia.travel official portal; multiple independent travel sources).

**Pages updated (1)**:
- [[destinations/madakaripura]] — Height field updated with attributed dual-value; `> Contradiction` block removed; Trail Data dead-reference to "Height contradiction section" updated

**Verification**:
- ✅ 0 `> Contradiction` blocks remain in madakaripura.md
- ✅ Height field now has attributed value (no "under reconciliation" placeholder)

---

## [2026-05-11] ingest | Clippings — Trustpilot 51 Reviews + Detik.com Polpar Article

**Sources ingested**:
- `Clippings/Java Volcano Tour Operator is rated Excellent with 4.8.md` — Trustpilot page clip, snapshot 2026-05-09
- `Clippings/Suka Duka Polisi Pariwisata Bondowoso Tegakkan Prokes Sambil Lawan Dingin.md` — Detik.com article, published 2021-03-14

**Pages created (2)**:
- [[sources/trustpilot-reviews-2026]] — Trustpilot clip summary: 51 reviews, 4.8/5, new crew names, selected excerpts, content angles
- [[sources/detik-polpar-2021]] — Detik.com article summary: direct quotes from Bripka Agung Sambuko, proof analysis, content angles

**Pages updated (5)**:
- [[reviews/trustpilot-compilation]] — review_count 47→51, last_verified 2026-04-19→2026-05-09, added Fauzi to guides table, added Derry/Darry/Terry to drivers table, expanded soft-data note (Derry, Sulis, Pras), added 3 new excerpts
- [[people/agung-sambuko]] — added sources: detik-polpar-2021; added two verbatim Bahasa Indonesia quotes from Detik article with deployment context
- [[people/crew-registry]] — added sources: trustpilot-reviews-2026; expanded Soft-Data Notes to table format with Derry, Sulis, Pras
- [[index]] — sources updated (4 entries), total_pages 21→23
- [[log]] — this entry

**Key findings**:
- Trustpilot count grew +4 (47→51) in ~3 weeks (April 19 → May 9)
- 2 new unregistered crew identified from guest reviews: **Derry/Darry/Terry** (guide or driver, pairs with Kiki) and **Sulis** (waterfall guide, video editing)
- **Pras** (driver) named in JVTO's own Trustpilot bio — not in KTA registry
- Detik.com article now ingested with direct quotes — first time verbatim Mr. Sam quotes available in the wiki
- Trustpilot company bio (JVTO-authored) is strong content asset — Style B voice, covers all core differentiators

**Verification**:
- ✅ 2 new source pages created with correct frontmatter
- ✅ review_count canonical: 51, last_verified: 2026-05-09
- ✅ Fauzi (KTA-G-2024-010) now appears in trustpilot-compilation guides table
- ✅ Derry/Sulis/Pras documented in both trustpilot-compilation soft-data and crew-registry soft-data table
- ✅ Direct Detik quotes added to agung-sambuko proof chain
- ✅ index total_pages and sources updated
- ✅ 0 voice-invariant violations introduced

---

## [2026-05-11] cleanup | Vault audit cleanup — frontmatter + templates + leftovers

**Triggered by**: comprehensive audit (zero unilateral changes, user-approved actions only).

**Actions executed**:
- 🔴 Added frontmatter to `log.md` (this page) — was the only wiki page without frontmatter, now consistent with convention
- 🟡 Backtick-wrapped 4 doc-placeholder wikilinks (`[[folder/page-name]]`, `[[other-page]]` in [[index]]; `[[CLAUDE.md]]`, `[[...]]` in this log) — they now render as inline code, not broken links
- 🟡 Deleted `_audit.py` (ephemeral audit script) and `Welcome.md` (Obsidian default note)
- 🟢 Populated `templates/` with 3 skeletons: `destination.md`, `person.md`, `source.md` — locks in Style A format + frontmatter convention for future ingests

**Kept as-is (intentional)**:
- `BASE.base` (Obsidian Bases plugin file, user-managed)
- `Clippings/` empty (Web Clipper inbox, expected state)

**Verification** (per Karpathy #4):
- ✅ 0 frontmatter issues post-cleanup
- ✅ 0 real broken wikilinks (doc placeholders now backticked)
- ✅ vault-root has 2 files (`CLAUDE.md`, `BASE.base`) — down from 4
- ✅ `templates/` populated with 3 skeleton files
- ✅ all 21 wiki pages structurally clean

**Vault inventory final**:
- 21 wiki pages (3 root, 2 sources, 5 destinations, 1 products, 3 people, 2 credentials, 2 reviews, 3 content)
- 3 templates
- 7 raw source files
- 0 Clippings (expected)

Ready for content production. Future-agent onboarding: read [[index]] → grep templates → write new pages with locked-in format.

---

## [2026-05-11] ingest | GPX Trail Data Enrichment — 5 AllTrails files

**Source ingested**: 5 GPX files in `raw/` (timestamps 12:26, post-SSOT-ingest):

- `Kawah_Ijen_Volcano.gpx` (59 KB · 673 trkpts · 2 named waypoints)
- `Gunung_Bromo.gpx` (71 KB · 809 trkpts · 1 named waypoint: Pura Luhur Poten)
- `Air_Terjun_Tumpak_Sewu.gpx` (11 KB · 125 trkpts · 0 waypoints)
- `Madakaripura_Waterfalls.gpx` (36 KB · 417 trkpts · 0 waypoints)
- `Pantai_dan_Tanjung_Papuma.gpx` (15 KB · 169 trkpts · 0 waypoints)

**Source attribution**: AllTrails community-recorded trail data — cited inline on each page, not treated as canonical JVTO route data.

**Strategy (per user direction — Option A, light enrichment)**: extract summary metadata (bounding box, named waypoints, elevation min/max, cumulative ascent, track-point density) into each destination page; full GPS traces remain in `raw/` only (not embedded in wiki to avoid bloat).

**Pages updated**:

- [[destinations/kawah-ijen]] — added Trail Data section + `geo_bbox` frontmatter. Confirmed GPX peak (2,380 m) ≈ official rim (2,386 m).
- [[destinations/mount-bromo]] — added Trail Data section + `geo_bbox` + **Pura Luhur Poten** waypoint reference. Noted GPX peak (2,277 m) below summit-ridge (2,329 m) because trace stays in caldera-floor corridor.
- [[destinations/tumpak-sewu]] — added Trail Data section. Noted trace covers rim only (not 300-step canyon descent).
- [[destinations/madakaripura]] — added Trail Data section. Noted 269 m elevation range reflects approach terrain (parking → basin), not waterfall height.

**Page created**:

- [[destinations/papuma-beach]] **NEW** — closed prior gap. Full destination template: entity summary (from SSOT §9_4), 5 Papuma-family packages, cape headland (~86 m) trail data.

**Index updates**:
- Destinations section: 4 → 5 entries; each with GPX trail-data note
- Open Gaps: papuma-beach removed (now exists)
- `total_pages: 20 → 21`

**Verification (Karpathy goal-driven criteria)**:
- ✅ 5 GPX summaries extracted
- ✅ 4 surgical edits succeed (each adds one new section + frontmatter `geo_bbox`, no rewrites elsewhere)
- ✅ 1 new file (papuma-beach.md) — 5 SSOT packages cited, GPX section included, cross-linked
- ✅ [[index]] gap list shrunk; total page count updated
- ✅ 0 new broken wikilinks (papuma-beach reference in [[overview]] now resolves)
- ⚠ Madakaripura height contradiction still unresolved — GPX data clarifies that the 269 m range is **approach terrain**, not waterfall height; original ~100m / ~200m question untouched

---

## [2026-05-11] ingest-complete | SSOT v6.0 Big-Bang Enrichment — All 8 Batches

Eight-batch enrichment of vault completed in one session. Source: `raw/JVTO_FINAL_CLEAN_SSOT.json` v6.0 (canonical, 13 domains).

**File operations summary**: 17 wiki pages touched + 1 new page created + 1 duplicate deleted.

| Batch | Files |
|---|---|
| 1. Foundation | [[index]], [[overview]], [[log]] rewritten Style A; [[sources/ssot-v6]] **new**; [[sources/jvto-homepage-clip]] rewritten; `sources/homepage-clip.md` deleted (redundant) |
| 2. Destinations | [[destinations/kawah-ijen]], [[destinations/mount-bromo]], [[destinations/tumpak-sewu]], [[destinations/madakaripura]] |
| 3. Products | [[products/packages-overview]] (full rewrite — 15 packages with pricing, inclusions, FOC, vehicle allocation) |
| 4. People | [[people/agung-sambuko]] (evidence chain + Ditpamobvit), [[people/dr-ahmad-irwandanu]] (conditional framing + SIP), [[people/crew-registry]] **new** (11 KTA-credentialed) |
| 5. Credentials | [[credentials/legal-licenses]] (KBLI + SHA-256 expansion + INDECON), [[credentials/trust-signals]] (4 press articles + partner verification URLs + 5-platform review table) |
| 6. Reviews | [[reviews/trustpilot-compilation]] (4.8/47 verified, cross-platform), [[reviews/review-patterns]] (SSOT 5 themes + 10 derived) |
| 7. Content | [[content/brand-voice]] (Style A/B registers + voice invariants), [[content/faq-master]] (20 SSOT FAQs), [[content/aeo-claims]] (C1–C9 with NLP snippets) |
| 8. Lint | Wikilink validation (4 remaining "broken" refs are documentation placeholders); voice-invariant grep (0 unqualified hits); index gap list refreshed |

**Lint verification (Batch 8)**:
- ✅ 0 unqualified "mandatory health screening" hits
- ✅ 0 unqualified "Blue Fire guaranteed" violations (only inside voice-invariant teaching blocks)
- ✅ 0 stale "4.9/112" hits outside the explicit stale-value note
- ✅ All canonical proof-item IDs and SHA-256 hashes traceable to [[sources/ssot-v6]]
- ✅ Founder name variants resolved consistently (Agung Sambuko / Mr. Sam / Bripka Agung Sambuko / Agung)
- ✅ 12 of 15 Ijen-relevant packages flagged for conditional health-screening framing
- ⚠ Madakaripura height contradiction unresolved (~100m SSOT vs ~200m prior wiki) — preserved as `> Contradiction` in [[destinations/madakaripura]] for source verification

**Contradictions surfaced and resolved**:
1. Founding date — three-era framing in [[overview]]
2. Health-screening "mandatory" → "conditional" — applied across [[destinations/kawah-ijen]], [[people/dr-ahmad-irwandanu]], [[products/packages-overview]], [[content/faq-master]], [[content/aeo-claims]]
3. Crew count §4_2=11 vs §13=14 — 11 canonical
4. Package count §meta=15 vs §9_1=16 — 15 canonical
5. Trustpilot 4.9/112 (v4.0) → 4.8/47 (v6.0) — applied across [[reviews/trustpilot-compilation]] and [[credentials/trust-signals]]
6. Madakaripura height — preserved as unresolved

**Open gaps tracked** (see [[index]] §open-gaps):
- `destinations/papuma-beach`
- `credentials/medical-screening` (consolidation candidate)
- `credentials/police-integration` (consolidation candidate)
- `credentials/press-coverage` (consolidation candidate)
- `content/copy-bank`

**Vault state**: 21 wiki pages canonical · 2 source-of-truth summaries · all 9 trust claims (C1–C9) mapped · all 20 SSOT FAQs documented · all 15 packages registered · 11 crew named with KTA codes · 24 proof items cross-referenced.

The vault is now ready for content production workflows per `CLAUDE.md` primary use case.

---

## [2026-05-11] ingest | JVTO_FINAL_CLEAN_SSOT.json v6.0 — Canonical SSOT enrichment

**Source ingested**: `raw/JVTO_FINAL_CLEAN_SSOT.json` (471 KB, v6.0, status Canonical, dated 2026-04-22, 13 domains).

**Decisions captured this session**:
- Canonicity hierarchy: cross-reference both sources; flag contradictions with `> Contradiction with [[...]]` (Decision 1b).
- Style: Style A (Authoritative dossier) for all wiki pages; Style B reserved for public-site copy generation.
- Scope: enrichment of existing 18 pages (from prior init) + 2 new source-summary pages.
- Duplicate JSON `Clippings/JVTO_FINAL_CLEAN_SSOT.json` deleted (identical to `raw/` copy).

**Pages updated (Batch 1)**:
- Created: [[sources/ssot-v6]] (new, canonical SSOT summary).
- Replaced: [[sources/jvto-homepage-clip]] (expanded from 46→200 lines with provenance chain, voice patterns, named-staff catalog).
- Replaced: [[overview]] (Style A rebuild, 9 trust pillars, all SSOT fact upgrades).
- Replaced: [[index]] (expanded catalog, new gap-tracking section).

**Contradictions flagged in this session**:
1. **Founding date**: CLAUDE.md "2015 guesthouse" vs SSOT `2016-01-01` PT. Resolved by distinguishing three eras: guesthouse (2015–), JVTO PT launch (2016), TDUP formalization (2023). Flagged in [[overview]].
2. **Health-screening framing**: CLAUDE.md "Mandatory" vs SSOT forbidden-phrase voice invariant. Canonical: **conditional**, BBKSDA SE.1658/KSA.9/2024 thresholds, JVTO coordinates. Flagged in [[overview]]. Triggers downstream fixes in: [[destinations/kawah-ijen]], [[people/dr-ahmad-irwandanu]], [[products/packages-overview]], [[content/faq-master]], [[content/aeo-claims]] (Batches 2, 3, 4, 7).
3. **Crew count**: SSOT §4_2 `11 (7+4)` vs §13 `14 (7+7)`. Treating §4_2 as canonical. Flagged in [[overview]].
4. **Package count**: SSOT §meta `15` vs §9_1/§13 `16`. Treating `15` as canonical. Flagged in [[overview]].
5. **Trustpilot rating drift**: v4.0 `4.9/112` superseded by v6.0 `4.8/47` (verified 2026-04-19). Affects [[reviews/trustpilot-compilation]] + [[credentials/trust-signals]] (Batch 5, 6).
6. **Madakaripura height**: Existing page records ~200m; SSOT §9_4 records ~100m. Unresolved — will be flagged in destination page (Batch 2) and surfaced for verification.

**Voice invariants now in effect (from SSOT §2_4)**:
- Forbidden: "Blue Fire guaranteed" · "100% Blue Fire visible" · "mandatory health screening" (without qualifier) · "JVTO provides police escort" (without qualifier).
- Approved Ijen language: "access rules can require a recent local health certificate" / "Blue Fire is a natural phenomenon subject to weather and gas activity" / "JVTO coordinates clinic workflow when access rules require it" / "Gas masks provided by JVTO".
- Price format: `IDR X,XXX,XXX/person` — Rupiah only, comma thousand separators.

**Batches pending**:
- Batch 2: destinations/{kawah-ijen, mount-bromo, tumpak-sewu, madakaripura} — enrich with SSOT entity data, fix mandatory→conditional, flag Madakaripura height.
- Batch 3: products/packages-overview — full 15-package registry, pricing logic, vehicle allocation, FOC, anti-fraud.
- Batch 4: people/{agung-sambuko, dr-ahmad-irwandanu} + new people/crew-registry — evidence chains, KTA codes.
- Batch 5: credentials/{legal-licenses, trust-signals} — proof items, SHA-256, INDECON live URL, press, partner detail.
- Batch 6: reviews/{trustpilot-compilation, review-patterns} — 4.8/47 verified, 5 SSOT themes + 10 derived.
- Batch 7: content/{brand-voice, faq-master, aeo-claims} — voice invariants, 20 canonical FAQs, C1–C9 with NLP snippets.
- Batch 8: cross-ref pass + lint + update [[index]] + final [[log]] entry.

---

## [2026-05-11] init | Wiki Initialization

Seeded from: `jvto-web` `CLAUDE.md`, `DESIGN.md`, `docs/STRATEGIC_REFERENCE.md`, Clippings homepage clip.

Pages created (18): overview, index, log, destinations/kawah-ijen, destinations/mount-bromo, destinations/tumpak-sewu, destinations/madakaripura, reviews/trustpilot-compilation, reviews/review-patterns, products/packages-overview, people/agung-sambuko, people/dr-ahmad-irwandanu, credentials/legal-licenses, credentials/trust-signals, content/brand-voice, content/faq-master, content/aeo-claims, sources/jvto-homepage-clip.

Known gaps at init: individual guide/driver profiles, pricing details, competitor data, press mentions. Many gaps resolved by 2026-05-11 SSOT ingest above.
