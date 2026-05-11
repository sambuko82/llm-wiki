---
type: overview
title: Operations Log
last_updated: 2026-05-11
sources: []
---

# JVTO Wiki Operations Log

*Append-only. Format: ## [YYYY-MM-DD] type | title. Most recent on top.*

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
