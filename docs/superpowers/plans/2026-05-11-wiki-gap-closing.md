# Wiki Gap-Closing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the 5 highest-priority gaps identified in the Karpathy pipeline audit: resolve the only open contradiction, compile the copy bank, ingest 3 remaining press sources, prove the query workflow, and establish a recurring health check cadence.

**Architecture:** Each task is a self-contained wiki workflow (Ingest, Query, or Lint) that ends with a log.md entry. No task depends on another completing first — they can run in order within one session. All verification is grep-based (no code tests). Each "commit" is an append to wiki/log.md.

**Tech Stack:** Markdown wiki in Obsidian. Tools used: WebSearch/WebFetch for source resolution, Read/Edit/Write for file ops, Grep for verification. No git (not a repo). Log entries replace commits.

---

## Task 1: Resolve Madakaripura Height Contradiction

**Files:**
- Modify: `wiki/destinations/madakaripura.md` (lines 27–34 — remove `> Contradiction` block; line 25 — update Height field)
- Modify: `wiki/log.md` (prepend new entry)

- [ ] **Step 1: Verify current contradiction state**

  Grep for "Contradiction" in madakaripura.md — expected: 1 match (the block to be resolved).

  ```
  grep -n "Contradiction" "wiki/destinations/madakaripura.md"
  ```

- [ ] **Step 2: Web search for actual height**

  Search query: `Madakaripura waterfall height meters Indonesia`

  Accept the height only if ≥2 independent sources agree (e.g., Wikipedia, tourism authority, travel guides). Do NOT use JVTO's own website as a source.

  Expected resolution: most independent sources cite **200 m** as the total height (main drop ~100 m + upper tiers). The SSOT `~100 m` likely refers to the main curtain drop only. If sources clearly distinguish main-drop vs total height, record both with attribution.

- [ ] **Step 3: Update Quick Facts table in madakaripura.md**

  Replace:
  ```
  | Height | **Under reconciliation — see "Height contradiction" below** |
  ```

  With one of these forms (choose based on Step 2 findings):

  _If sources agree on a single figure:_
  ```
  | Height | ~[X] m ([source, e.g., "Wikipedia / Jatim tourism authority"]) |
  ```

  _If sources distinguish main drop vs total:_
  ```
  | Height | Main curtain drop: ~100 m (SSOT §9_4) · Total height incl. upper tiers: ~200 m (widely cited) |
  ```

- [ ] **Step 4: Remove the `> Contradiction` block**

  Delete lines 27–34 of madakaripura.md (the entire blockquote starting with `> Contradiction with [[sources/ssot-v6]]`).

  After deletion, the Quick Facts table should flow directly into the "Why Visitors Come" section.

- [ ] **Step 5: Update frontmatter `last_updated`**

  Change `last_updated: 2026-05-11` to today's date (already 2026-05-11 — no change needed unless session spans midnight).

- [ ] **Step 6: Verify — grep for "Contradiction" returns 0 in madakaripura.md**

  ```
  grep -n "Contradiction" "wiki/destinations/madakaripura.md"
  ```
  Expected: no matches.

- [ ] **Step 7: Append log entry to wiki/log.md (prepend, most-recent-first)**

  ```markdown
  ## [2026-05-11] lint | Madakaripura height contradiction resolved

  **Resolution**: [state what was found — e.g., "~200 m total height (upper tiers + main curtain) per Wikipedia and Jatim tourism authority; SSOT ~100 m refers to main curtain drop only"]

  **Pages updated (1)**:
  - [[destinations/madakaripura]] — Height field updated; `> Contradiction` block removed

  **Verification**:
  - ✅ 0 `> Contradiction` blocks remain in madakaripura.md
  - ✅ Height field now has attributed value (no "under reconciliation" placeholder)
  ```

---

## Task 2: Build content/copy-bank.md

**Files:**
- Read: `wiki/content/aeo-claims.md` (extract `nlp_short` fields for C1–C9)
- Read: `wiki/sources/jvto-homepage-clip.md` (extract verbatim hero copy blocks)
- Read: `wiki/content/brand-voice.md` (extract key phrases + taglines)
- Create: `wiki/content/copy-bank.md`
- Modify: `wiki/index.md` (add entry under Content Production; remove from Open Gaps)
- Modify: `wiki/log.md` (prepend new entry)

- [ ] **Step 1: Read source files**

  Read all three files listed above. Note: do NOT re-read `brand-voice.md` if already in context.

- [ ] **Step 2: Extract copy atoms**

  From `aeo-claims.md`: collect `nlp_short` (≤15 words) for each of C1–C9.

  From `jvto-homepage-clip.md`: collect verbatim hero headline, subheadline, any button CTAs, and the company bio paragraph.

  From `brand-voice.md`: collect "Voice invariants — approved phrases" list and any named taglines.

- [ ] **Step 3: Write wiki/content/copy-bank.md**

  Use this exact structure:

  ```markdown
  ---
  type: content
  title: JVTO Copy Bank — Reusable Snippets
  last_updated: 2026-05-11
  sources: [ssot-v6, jvto-homepage-clip, aeo-claims]
  ---

  # JVTO Copy Bank

  *Reusable, voice-compliant copy atoms. Paste directly into website, ads, or email copy.
  Every snippet here is source-backed — do not edit without updating the linked claim.*

  ## NLP Snippets (C1–C9, ≤15 words each)

  *From [[content/aeo-claims]]. These are the shortest extractable statements of each trust claim.*

  | ID | Snippet | Claim |
  |---|---|---|
  | C1 | [nlp_short from aeo-claims] | Police-Led |
  | C2 | … | 100% Private |
  | C3 | … | All-Inclusive |
  | C4 | … | Licensed Crew |
  | C5 | … | Proof-First |
  | C6 | … | Reviews |
  | C7 | … | Medical Screening |
  | C8 | … | Partners |
  | C9 | … | Press |

  ## Hero Copy (verbatim from live site)

  *From [[sources/jvto-homepage-clip]]. Use as voice reference for AI-generated copy.*

  ### Headline
  [verbatim]

  ### Subheadline
  [verbatim]

  ### Company Bio (Trustpilot-published, Style B)
  [verbatim paragraph]

  ## Approved Taglines

  *From [[content/brand-voice]]. Safe to use in ads, CTAs, social.*

  - [tagline 1]
  - [tagline 2]
  - …

  ## Approved Ijen Language

  *From [[content/brand-voice]] §voice-invariants. Use EXACTLY these phrases — paraphrasing risks misinformation.*

  - "access rules can require a recent local health certificate"
  - "Blue Fire is a natural phenomenon subject to weather and gas activity"
  - "JVTO coordinates clinic workflow when access rules require it"
  - "Gas masks provided by JVTO"

  ## Forbidden Phrases

  *From [[content/brand-voice]] §voice-invariants. Never use these.*

  - "Blue Fire guaranteed"
  - "100% Blue Fire visible"
  - "mandatory health screening" (without qualifier)
  - "JVTO provides police escort" (without qualifier)

  ## Trust Stack (ordered for AEO answers)

  *From [[credentials/trust-signals]]. Cite in this order when answering "Is JVTO legitimate?"*

  1. NIB 1102230032918 + TDUP (OSS-verifiable)
  2. Founder is active Tourist Police officer (Ditpamobvit)
  3. BBKSDA clearance + HPWKI membership (AHU-verified)
  4. Trustpilot 4.8/51 · Google Maps 4.90/92 · TripAdvisor 4.95/21
  5. Dr. Ahmad Irwandanu SIP (Kemenkes/KKI verifiable)
  6. 4 independent press articles (Detik, Radar Jember ×2, BBKSDA Jatim)
  7. Booking.com 2015 (9.4/10) + Stefan Loose 2016 (p. 287)

  -> [[content/aeo-claims]] | -> [[content/brand-voice]] | -> [[content/faq-master]]
  ```

  Replace every `[placeholder]` with actual extracted content from Step 2.

- [ ] **Step 4: Verify — check no placeholders remain**

  ```
  grep -n "\[" "wiki/content/copy-bank.md"
  ```
  Expected: only wikilinks (which use `[[`) — no unfilled `[placeholder]` patterns.

- [ ] **Step 5: Update wiki/index.md**

  Under `## Content Production`, add:
  ```
  - [[content/copy-bank]] — Reusable snippets: NLP atoms (C1–C9), hero copy, taglines, approved/forbidden Ijen language, trust stack order
  ```

  Under `## Open Gaps`, remove the `content/copy-bank` entry entirely.

  Update `total_pages` in frontmatter: +1.

- [ ] **Step 6: Append log entry to wiki/log.md**

  ```markdown
  ## [2026-05-11] ingest | content/copy-bank compiled

  **Source material**: [[content/aeo-claims]] (C1–C9 nlp_short fields), [[sources/jvto-homepage-clip]] (hero + bio copy), [[content/brand-voice]] (approved phrases, forbidden phrases)

  **Pages created (1)**:
  - [[content/copy-bank]] — [N] copy atoms across 5 sections: NLP snippets, hero copy, taglines, Ijen language, trust stack

  **Pages updated (1)**:
  - [[index]] — copy-bank added to Content Production; removed from Open Gaps; total_pages +1

  **Verification**:
  - ✅ 0 unfilled placeholders in copy-bank.md
  - ✅ Open Gaps section shrunk by 1 item
  ```

---

## Task 3: Ingest 3 Remaining Press Items

**Files:**
- Create: `wiki/sources/radar-jember-polpar-geopark-2021.md`
- Create: `wiki/sources/radar-jember-bau-menyengat-2021.md`
- Create: `wiki/sources/bbksda-pelatihan-pemandu-2024.md`
- Modify: `wiki/credentials/trust-signals.md` (add source links to press table)
- Modify: `wiki/people/agung-sambuko.md` (add Radar Jember references to proof chain)
- Modify: `wiki/index.md` (add 3 source entries, update total_pages)
- Modify: `wiki/log.md` (prepend new entry)

**URLs to fetch:**
- Radar Jember 2021-03-24: `https://radarjember.jawapos.com/bondowoso/791102263/polpar-dibentuk-untuk-mendukung-ijen-geopark`
- Radar Jember 2021-05-27: `https://radarjember.jawapos.com/bondowoso/791103903/tak-seharusnya-bau-menyengat-itu-ada`
- BBKSDA Jatim 2024-05-24: `https://bbksdajatim.org/pelatihan-pemandu-kawah-ijen/`

- [ ] **Step 1: Fetch Radar Jember 2021-03-24**

  Attempt WebFetch on the URL above. Jawa Pos may paywall — if response is a login wall or <200 words, note "paywalled" and proceed with what's available from the URL slug, title, and context already in `trust-signals.md`.

- [ ] **Step 2: Create wiki/sources/radar-jember-polpar-geopark-2021.md**

  ```markdown
  ---
  type: source
  title: "Radar Jember — Polpar Dibentuk untuk Mendukung Ijen Geopark (2021-03-24)"
  last_updated: 2026-05-11
  sources: []
  slug: radar-jember-polpar-geopark-2021
  publisher: Radar Jember / Jawa Pos
  published: 2021-03-24
  url: https://radarjember.jawapos.com/bondowoso/791102263/polpar-dibentuk-untuk-mendukung-ijen-geopark
  access_status: [full | paywalled — fill in after fetch]
  claims_supported: [C1, C5, C9]
  ---

  # Source: Radar Jember — Polpar Dibentuk untuk Mendukung Ijen Geopark

  ## Provenance

  Independent regional newspaper (Radar Jember / Jawa Pos group). Published 2021-03-24. Third-party — not JVTO-authored.

  ## Key Facts

  [Fill from fetch. If paywalled: state "Content behind paywall — title and slug only accessible. See trust-signals.md for cataloged context."]

  ## Why This Source Matters

  Formation of the Tourist Police unit specifically to support the Ijen Geopark initiative. Confirms institutional role, not self-reported. Supports C1 (Police-Led), C5 (Proof-First), C9 (Press).

  ## Entity Linking Signal

  Bripka Agung Sambuko ↔ Tourist Police ↔ Ijen Geopark ↔ JVTO founder. AI engines reading this article can resolve the same entity across JVTO marketing and the journalist's independent reporting.

  ## Content Angles

  - "Even the Tourist Police formation was designed around Ijen — that's the environment Mr. Sam works in."
  - Third-party confirmation that the Polpar role is institutional, not ceremonial.

  -> [[people/agung-sambuko]] | -> [[credentials/trust-signals]]
  ```

- [ ] **Step 3: Fetch Radar Jember 2021-05-27**

  Same approach as Step 1. Paywalled handling: use title, slug, and context from trust-signals.md.

- [ ] **Step 4: Create wiki/sources/radar-jember-bau-menyengat-2021.md**

  ```markdown
  ---
  type: source
  title: "Radar Jember — Tak Seharusnya Bau Menyengat Itu Ada (2021-05-27)"
  last_updated: 2026-05-11
  sources: []
  slug: radar-jember-bau-menyengat-2021
  publisher: Radar Jember / Jawa Pos
  published: 2021-05-27
  url: https://radarjember.jawapos.com/bondowoso/791103903/tak-seharusnya-bau-menyengat-itu-ada
  access_status: [full | paywalled — fill in after fetch]
  claims_supported: [C1, C9]
  ---

  # Source: Radar Jember — Tak Seharusnya Bau Menyengat Itu Ada

  ## Provenance

  Independent regional newspaper (Radar Jember / Jawa Pos group). Published 2021-05-27. Third-party — not JVTO-authored.

  ## Key Facts

  [Fill from fetch. If paywalled: state "Content behind paywall — title and slug only accessible."]

  ## Why This Source Matters

  Tourist Police patrol at Ijen crater area monitoring sulfuric odor conditions and visitor safety. Evidence of on-ground operational presence — not just an official title. Supports C1 (Police-Led), C9 (Press).

  ## Entity Linking Signal

  Bripka Agung Sambuko ↔ active patrol at Ijen crater ↔ sulfur safety monitoring. Proves presence is operational, not ceremonial.

  ## Content Angles

  - "The Tourist Police don't just hold a badge — they patrol the crater when conditions change."
  - Evidence that Mr. Sam's police role extends to real-time visitor safety, not desk work.

  -> [[people/agung-sambuko]] | -> [[credentials/trust-signals]] | -> [[destinations/kawah-ijen]]
  ```

- [ ] **Step 5: Fetch BBKSDA Jatim 2024-05-24**

  Fetch `https://bbksdajatim.org/pelatihan-pemandu-kawah-ijen/`. This is an institutional site — expect full access.

- [ ] **Step 6: Create wiki/sources/bbksda-pelatihan-pemandu-2024.md**

  ```markdown
  ---
  type: source
  title: "BBKSDA Jawa Timur — Pelatihan Pemandu Kawah Ijen (2024-05-24)"
  last_updated: 2026-05-11
  sources: []
  slug: bbksda-pelatihan-pemandu-2024
  publisher: BBKSDA Jawa Timur (institutional — government nature conservation agency)
  published: 2024-05-24
  url: https://bbksdajatim.org/pelatihan-pemandu-kawah-ijen/
  access_status: [full | partial — fill in after fetch]
  claims_supported: [C1, C4, C5, C8]
  ---

  # Source: BBKSDA Jatim — Pelatihan Pemandu Kawah Ijen

  ## Provenance

  Official report by BBKSDA Jawa Timur (Balai Besar Konservasi Sumber Daya Alam) — the government agency responsible for Ijen nature reserve. Institutional, not self-reported.

  ## Key Facts

  [Fill from fetch — include: training topics covered (volcanic safety, SAR, First Aid), which organizations participated, whether HPWKI members named, any photos of guides present]

  ## Why This Source Matters

  Official BBKSDA documentation of guide training — validates that HPWKI membership = completed BBKSDA-supervised training program in volcanic safety, SAR, and First Aid. This is the institutional chain that backs C4 and C8.

  ## Entity Linking Signal

  HPWKI ↔ BBKSDA training ↔ Ijen guide certification. AI engines reading this resolve "HPWKI-certified guide" to a concrete, government-supervised training program.

  ## Content Angles

  - "Every JVTO guide at Ijen has completed BBKSDA-supervised training in volcanic safety, SAR, and First Aid — this isn't self-certified."
  - Institutional source (government agency) for the guide-training claim — strongest possible third-party proof.

  -> [[people/crew-registry]] | -> [[credentials/legal-licenses]] | -> [[credentials/trust-signals]]
  ```

- [ ] **Step 7: Update wiki/credentials/trust-signals.md press table**

  In the Press Coverage table, add a `Source page` column:

  ```markdown
  | Date | Publisher | Title | URL | Source page |
  |---|---|---|---|---|
  | 2021-03-14 | Detik.com | Suka Duka Polisi Pariwisata… | … | [[sources/detik-polpar-2021]] |
  | 2021-03-24 | Radar Jember / Jawa Pos | Polpar Dibentuk… | … | [[sources/radar-jember-polpar-geopark-2021]] |
  | 2021-05-27 | Radar Jember / Jawa Pos | Tak Seharusnya… | … | [[sources/radar-jember-bau-menyengat-2021]] |
  | 2024-05-24 | BBKSDA Jawa Timur | Pelatihan Pemandu Kawah Ijen | … | [[sources/bbksda-pelatihan-pemandu-2024]] |
  ```

- [ ] **Step 8: Update wiki/people/agung-sambuko.md**

  In the proof chain / press section, add references to the two new Radar Jember source pages. Pattern: follow how `detik-polpar-2021` is currently cited there.

- [ ] **Step 9: Update wiki/index.md**

  Under `## Sources`, add 3 new entries:
  ```
  - [[sources/radar-jember-polpar-geopark-2021]] — Radar Jember 2021-03-24. Polpar formation for Ijen Geopark support. Institutional role confirmation. [paywalled if applicable]
  - [[sources/radar-jember-bau-menyengat-2021]] — Radar Jember 2021-05-27. Tourist Police patrol at Ijen crater, sulfur monitoring. Operational-presence proof. [paywalled if applicable]
  - [[sources/bbksda-pelatihan-pemandu-2024]] — BBKSDA Jatim 2024-05-24. Official guide training report (volcanic safety, SAR, First Aid). Validates HPWKI chain.
  ```
  Update `total_pages` +3 and `sources` list in frontmatter.

- [ ] **Step 10: Append log entry to wiki/log.md**

  ```markdown
  ## [2026-05-11] ingest | 3 press source pages

  **Sources ingested**:
  - Radar Jember 2021-03-24 (Polpar + Geopark) — [full | paywalled]
  - Radar Jember 2021-05-27 (bau menyengat) — [full | paywalled]
  - BBKSDA Jatim 2024-05-24 (pelatihan pemandu) — [full | partial]

  **Pages created (3)**:
  - [[sources/radar-jember-polpar-geopark-2021]]
  - [[sources/radar-jember-bau-menyengat-2021]]
  - [[sources/bbksda-pelatihan-pemandu-2024]]

  **Pages updated (3)**:
  - [[credentials/trust-signals]] — Source page column added to press table
  - [[people/agung-sambuko]] — Radar Jember references added to proof chain
  - [[index]] — 3 new source entries; total_pages updated

  **Verification**:
  - ✅ All 4 press items now have a [[sources/]] page
  - ✅ trust-signals.md press table links to all 4 source pages
  - ✅ 0 voice-invariant violations introduced
  ```

---

## Task 4: Run Query Workflow — Hero Claim for Price-Skeptical Traveler

**Files:**
- Read: `wiki/reviews/review-patterns.md`, `wiki/content/aeo-claims.md`, `wiki/credentials/trust-signals.md`, `wiki/products/packages-overview.md`
- Create: `wiki/content/query-hero-claim.md`
- Modify: `wiki/index.md` (add entry under Content Production)
- Modify: `wiki/log.md` (prepend new entry)

This task proves the Query workflow in CLAUDE.md works. The query is:

> "What single trust claim — with the strongest third-party proof — should anchor the homepage hero copy when the visitor is a first-time solo traveler who is price-skeptical?"

- [ ] **Step 1: Read the 4 relevant pages**

  Read `reviews/review-patterns.md`, `content/aeo-claims.md`, `credentials/trust-signals.md`, `products/packages-overview.md`.

- [ ] **Step 2: Synthesize across pages**

  Answer these sub-questions using only content from the wiki (cite each with `-> [[page]]`):

  a. Which review patterns map most directly to price-skepticism? (e.g., "worth it", "value", "no hidden costs")
  b. Which claims (C1–C9) have the most third-party proof (independent sources, not JVTO-authored)?
  c. Which claims appear unprompted in guest reviews (i.e., guests mention it without being asked)?
  d. Intersection: which claim scores highest on all three dimensions?

- [ ] **Step 3: Write wiki/content/query-hero-claim.md**

  Use this structure:

  ```markdown
  ---
  type: content
  title: Query — Hero Claim for Price-Skeptical Solo Traveler
  last_updated: 2026-05-11
  sources: [ssot-v6, jvto-homepage-clip, trustpilot-reviews-2026]
  query: "What single trust claim should anchor the homepage hero for a price-skeptical first-time solo traveler?"
  ---

  # Query: Hero Claim for Price-Skeptical Solo Traveler

  *Filed from Query workflow (CLAUDE.md §Workflow 2). Synthesized from 4 wiki pages.*

  ## Answer

  **Lead claim:** [answer — e.g., C3 (No Hidden Costs) backed by review-pattern unprompted mentions]

  **Rationale:** [2–3 sentences citing the wiki pages that support this]

  ## Evidence Chain

  [Cite each supporting data point with -> [[page]] attribution]

  ## Recommended Hero Copy

  **Headline option A:** [draft using copy-bank approved language]
  **Headline option B:** [alternative]

  **Supporting subheadline:** [draft]

  ## Second and Third Claims (for below the fold)

  | Rank | Claim | Reason |
  |---|---|---|
  | 2nd | [claim] | [why] |
  | 3rd | [claim] | [why] |

  ## Caveats

  [Any limitations in the analysis — e.g., "review-patterns.md patterns are SSOT-derived; Trustpilot verbatim not fully cross-checked against all 51 reviews"]

  -> [[content/aeo-claims]] | -> [[reviews/review-patterns]] | -> [[content/copy-bank]]
  ```

- [ ] **Step 4: Update wiki/index.md**

  Under `## Content Production`, add:
  ```
  - [[content/query-hero-claim]] — Query output: best trust claim for price-skeptical solo traveler hero copy. Synthesized from reviews, AEO claims, trust signals.
  ```
  Update `total_pages` +1.

- [ ] **Step 5: Append log entry to wiki/log.md**

  ```markdown
  ## [2026-05-11] query | Hero claim for price-skeptical traveler

  **Query**: "What single trust claim should anchor homepage hero copy for a price-skeptical first-time solo traveler?"

  **Pages read**: [[reviews/review-patterns]], [[content/aeo-claims]], [[credentials/trust-signals]], [[products/packages-overview]]

  **Pages created (1)**:
  - [[content/query-hero-claim]] — Answer: [leading claim], evidence chain, 2 headline options, ranked secondary claims

  **Pages updated (1)**:
  - [[index]] — query-hero-claim added to Content Production; total_pages +1

  **Verification**:
  - ✅ Answer cites at least 3 distinct wiki pages (not just aeo-claims alone)
  - ✅ Headline options use copy-bank approved language (0 voice-invariant violations)
  - ✅ Filed as content/ page — first Query workflow output in the vault
  ```

---

## Task 5: Add Workflow 4 (Health Check Cadence) to CLAUDE.md

**Files:**
- Modify: `CLAUDE.md` (add Workflow 4 section after Workflow 3: Lint)
- Modify: `wiki/log.md` (prepend new entry)

- [ ] **Step 1: Read current CLAUDE.md**

  Locate the end of Workflow 3: Lint (currently the last workflow). Note the exact line number where the new workflow will be inserted.

- [ ] **Step 2: Add Workflow 4 to CLAUDE.md**

  After the Workflow 3 block, insert:

  ```markdown
  ## Workflow 4: Health Check (Monthly or Post-Ingest)

  Run after every 3+ source ingests, or at minimum monthly.

  1. **Contradiction scan** — `grep -rn "> Contradiction" wiki/` → resolve each or document why unresolvable
  2. **Stale value scan** — `grep -rn "\[stale?\]" wiki/` → web-search each flagged claim to confirm or update
  3. **Voice invariant scan** — `grep -rn "mandatory health screening\|Blue Fire guaranteed\|100% Blue Fire\|provides police escort" wiki/` → 0 unqualified hits expected
  4. **Orphan check** — for each wiki page, verify at least 1 inbound wikilink exists (or it appears in index.md)
  5. **Web-search imputation** — for each Open Gap in index.md: attempt 1 targeted web search; if found, ingest immediately; if not found, update gap note with date + "searched YYYY-MM-DD, not found"
  6. **Interesting connections** — ask: "What non-obvious connection between two wiki pages could become a content angle?" File as a `content/` page if actionable.
  7. **Append to log.md** — entry type: `lint`

  ### Health Check Triggers (run when any of these happen)

  - 3+ sources ingested since last lint
  - An unresolved `> Contradiction` is older than 2 weeks
  - Trustpilot count changes by 5+ reviews
  - A new claim is added to CLAUDE.md core differentiators
  ```

- [ ] **Step 3: Verify insertion**

  Read the modified CLAUDE.md. Confirm Workflow 4 appears after Workflow 3 and before any trailing sections.

- [ ] **Step 4: Append log entry to wiki/log.md**

  ```markdown
  ## [2026-05-11] lint | Health check cadence established in CLAUDE.md

  **Change**: Added Workflow 4 (Health Check) to CLAUDE.md — monthly cadence or after 3+ ingests. Includes 7-step checklist: contradiction scan, stale scan, voice-invariant scan, orphan check, web-search imputation, interesting-connections discovery, log entry.

  **Pages updated (1)**:
  - `CLAUDE.md` — Workflow 4 section added

  **Verification**:
  - ✅ Workflow 4 present and correctly numbered after Workflow 3
  - ✅ 7 steps enumerated with exact grep commands where applicable
  - ✅ Health check triggers documented (so future agent knows when to self-trigger)
  ```

---

## Self-Review

**Spec coverage check:**
- [x] Task 1: Madakaripura contradiction resolved ✓
- [x] Task 2: copy-bank compiled ✓
- [x] Task 3: 3 press items ingested ✓
- [x] Task 4: Query workflow proven with filed output ✓
- [x] Task 5: Health check cadence in CLAUDE.md ✓

**Placeholder scan:** All tasks include exact file paths, exact grep commands, exact frontmatter templates, and exact log entry formats. Paywall handling is specified. The only unfilled content is wiki body text that must be derived from sources at execution time — these are labeled `[Fill from fetch]` or `[Fill from Step N]`, which is the correct behavior for content derived during runtime.

**Consistency check:** Slug names (`radar-jember-polpar-geopark-2021`, `radar-jember-bau-menyengat-2021`, `bbksda-pelatihan-pemandu-2024`) are consistent across Tasks 3 and 4 file paths, log entries, and index entries. `total_pages` increments: +1 (Task 2), +3 (Task 3), +1 (Task 4) = 23 → 27.
