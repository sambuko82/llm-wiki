---
type: overview
title: Operations Log
last_updated: 2026-06-07
sources: []
owner: wiki-llm
stale_after_days: 60
---

# JVTO Wiki Operations Log

*Append-only. Format: ## [YYYY-MM-DD] type | title. Most recent on top.*

---

## [2026-06-03] fix | GAP-01 stale review-count cluster — secondary-file sweep

Closed the GAP-01 blast radius the weekly health check surfaced. SSOT confirmed current (`trust-signals.md §Live Review Platforms` + §Schema Canonical = Google 4.9/123, Trustpilot 4.8/51, TripAdvisor 4.95/21, cross-platform 195). The 2026-06-01 GAP-01 pass fixed only the core anchors (trust-signals, HANDOFF, homepage-org-schema); these secondary mentions still carried Google `92` / cross-platform `164`:

Conformed → 123 / 195:
- `wiki/website/copy-bank.md` (trust-stack snippet, added "195 cross-platform")
- `wiki/reviews/trustpilot-compilation.md` (platform table: Google 92→123 + dates 04-22→05-26/05-12)
- `wiki/seo/competitors.md` (164→195)
- `output/website/aeo/why-jvto.md` (92→123, Trustpilot date 05-09→05-18)
- `output/website/pages/{bali,surabaya}-landing.md` (92→123, dates)
- `output/website/pages/homepage.md` (Trustpilot date 05-09→05-18; count already 123)
- `raw/_manifest/evidence-registry.yml` E010 (92→123, last_verified→05-26) → **regenerated trust-bundle via `compile_trust.py`** (F1–F8 pass, 7 files) so `claims.json` description now reads 123.

Tracking docs reconciled:
- `website-context-master.md`: GAP-01 +2026-06-03 follow-up note; GAP-05 reframed to RESOLVED-in-repo (homepage 92→123, commit `63ab1eb`) + live-jvto FLAG ONLY (EXECUTION-OUT-OF-SCOPE).
- `extended-bundle-receipt.md`: 2 stale ⚠️ drift warnings ("trust-signals still 164", "HANDOFF shows 92") → ✅ resolved.

Schema layer verified clean (no regen needed): `homepage-organization-schema.json` reviewCount=195 ✓; per-tour schemas reviewCount=51 (Trustpilot, correct per SSOT). Snapshots left intact by design: `db-export-2026-05` (DB had 92 at export), `seo-audit-2026-05` (audit-time 164 + drift caveat). Final sweep: zero active 92/164 review claims remain (only the trust-signals "don't-use-92" warning + fix-history receipt reference them).

---

## [2026-06-03] health-check | weekly

Scope: 110 wiki/*.md. Cutoffs from 2026-06-03 → 30-day = 2026-05-04, 90-day = 2026-03-05.

**On-demand tier**

1. Contradiction scan:
   - **FIXED this run** — `wiki/index.md` lines 163/164 said Package Readiness "next wedge / NEXT / no code"; contradicted the 2026-06-03 ops reconcile (Package Readiness DONE v1.2). Conformed → "Policy Bundle (P2) next"; spec entry marked IMPLEMENTED (6 files). Line 37 trust-bundle count clarified (v1 7 → now 9 root JSON + 3 `schema/`). This was reconcile fallout — the ops commit `652547a` did not propagate to index.md.
   - **PRIOR FLAG CLOSED** — KBLI `79120` (trust-signals) vs `79121+79911` (permit-requirements), flagged 2026-05-26. Now reconciled: trust-signals no longer carries 79120; `legal-licenses.md` lists 79121 (Travel Agency) + 79911 (Tour Operator) primary, 79120 (related); permit-requirements 79121+79911. No active conflict.
   - **OPEN — GAP-01 cluster (wider than tracked)**: stale Google Maps count `92` (current 123, API-verified 2026-05-26) and cross-platform `164` (current 195 = 51+123+21) persist as ACTIVE claims in: `website/copy-bank.md:86` (production copy — HIGH), `reviews/trustpilot-compilation.md:41` (platform table, dated 2026-04-22 — MED), `seo/competitors.md:100` ("164 reviews" — MED), `credentials/trust-signals.md §Schema Canonical Values` (known GAP-01 — HIGH). Historical/snapshot mentions are NOT defects: log.md, db-export-2026-05, google-maps-reviews-api source, website-context-master (documents drift), jvto-homepage-clip/trustpilot-reviews-2026 (47).
2. Orphan detection (zero inbound `[[link]]`, excl index.md): 4 — `sources/backoffice-mysql.md` (umbrella source; also had no `last_updated`), `internal-ops/2026-06-02-chatbot-llmwiki-integration-audit.md`, `internal-ops/2026-06-02-chatbot-slim-feed-pattern.md`, `bundles/README.md` (nav stub, acceptable).
3. Stale-claim flags (90-day): **NONE**. Earliest content page 2026-05-11 (23 days).
4. Gap pages: none new; GAP-01 cluster is the active gap.

**Weekly tier**

1. 30-day stale sweep: **NONE** older than 30 days. Sole anomaly: `sources/backoffice-mysql.md` had no `last_updated` field (used `ingested` only) — **FIXED** (`last_updated: 2026-05-25`).
2. New-orphan detection (created since last log): 2 internal-ops chatbot docs (2026-06-02) are in the index catalog but have zero inbound `[[links]]` from content pages — standalone audit notes, link or accept.
3. Index completeness: `ops/bundle-taxonomy.md` not in `index.md` catalog (sibling ops pages are listed); `bundles/website-logic.md` + `bundles/README.md` absent (bundles/ pages generally not path-linked from index — index-slim deferred per CLAUDE.md open item).
4. Log completeness: raw/ = 222 files vs 29 `ingest` entries. raw is batch-ingested via ~60 `wiki/sources/` summary pages; per-file 1:1 ingest logging not maintained by design — not a defect.

**Actions taken**: fixed index.md 37/163/164 (reconcile fallout); added `last_updated` to backoffice-mysql.md.

**Flag-only (not auto-fixed)**: GAP-01 blast radius (copy-bank/trustpilot-compilation/competitors/trust-signals) → needs review-feed live-verify + schema regen; 2 chatbot docs orphan links; bundle-taxonomy.md → add to index catalog.

---

## [2026-06-03] lint | wiki/ops contradiction reconcile — force-conform to repo truth

Full read of all 9 `wiki/ops/*.md`; cross-checked every status/count claim against live repo state (scripts/, output/, frontmatter). Fixed every divergence so the ops layer stops contradicting itself ("tidak bolak-balik"). All values below are verified, not assumed.

Conformed:
- **transformation-map.md** — Package Readiness was internally contradictory: Bundle Status Table said "DONE (v1.2)" but the Per-Bundle Pipeline row + the entire "Next Recommended Wedge" section still said `compile_packages.py` "NOT BUILT" / "NEXT (P1)". Verified built (`scripts/compile_packages.py` + `scripts/package_compiler/` + tests + 6 live artifacts). Pipeline row → BUILT / gap-report.json live / DONE (v1.2); rewrote Next-Wedge to **Policy Bundle (P2)** with P3–P6 queue. Trust Bundle "7 JSON outputs" → **9 canonical JSON (+3 schema/)** (manifest confirms). WhatsApp row → "FUTURE (spec written)".
- **bundle-taxonomy.md** — trust-bundle `*.json (10 files)` → **9** (+ added `schema/*.json (3)` row). `packages-full-pricing` "All 22 packages" → "22 priced (16 canonical + 6 student)". schema output `~45` → **28** (actual). FINANCE xlsx `17` → **15** (actual). aeo=10 / faq=8 / package-readiness=6 / verify-jvto=5 / rate_cards=5 verified correct.
- **whatsapp-reply-intelligence-compiler-spec.md** — §7 renderer count "11 artifact JSONs / all 12 outputs" → **12 artifacts / 13 outputs** (§5 lists 12 JSON + _manifest). Removed duplicate `last_updated` key.
- **package-readiness-compiler-spec.md** — added top **STATUS: IMPLEMENTED (v1.2)** banner; flagged shipped bundle is 6 files (spec's planned 7th `package-route-map.json` never shipped).
- **CLAUDE.md** build status — "7/7 JSON files valid" → "9/9 trust-bundle JSON (+3 schema/)".

No-fix confirmed: WhatsApp canonical files genuinely use `stale_after_days: 60` (WA-W5 "(60)" correct); `compile_whatsapp.py` absent (FUTURE P3 correct); `validate_wiki.py` NOT BUILT correct (P6 future).

Carried forward (out of ops scope): GAP-01 cross-platform reviewCount 164↔195 drift in `trust-signals.md §Schema Canonical Values` — already tracked in website-context-master.md, not re-touched.

---

## [2026-06-02] cleanup-governor Phase B | Archive 3 output/website-root orphans

governance-maintainer D1 (lower-priority residual): 3 orphaned 2026-05-27 files at `output/website/` root (not in a bundle subfolder, zero inbound citations, not on naming-exempt list). git mv → `output/_archive/`:
- `2026-05-27-evidence-registry-receipt.md` (Cowork generation receipt for jvto-web `evidenceRegistry.ts`)
- `2026-05-27-llms-files-receipt.md` (generation receipt for llms.txt/llms-full.txt)
- `2026-05-27-jvto-exposure-board.html` (orphaned gridjs viz artifact)

`output/website/` root now holds only `HANDOFF.md` anchor; all else in subfolders. D1 fully clean across `output/`. Schema `*-schema.receipt.md` pairs + `extended-bundle-receipt.md` untouched (naming-exempt). `pages/**` + `blog/**` dated files are URL-mirror exempt, not drift.

---

## [2026-06-02] cleanup-governor Phase B | Archive 4 output-root strategy docs

governance-maintainer D1+D3: 4 orphaned strategy/blueprint docs (dated 2026-05-27, zero inbound citations) sat in `output/` root, violating `output/<domain>/<bundle>/` and the no-strategy-in-output rule. Moved (git mv, filenames + content preserved) to `docs/superpowers/specs/` — the D3-designated home for `type: blueprint|synthesis|strategy`:
- `2026-05-27-jvto-agentic-response-system-blueprint.md` (blueprint)
- `2026-05-27-jvto-knowledge-compiler-blueprint.md` (blueprint)
- `2026-05-27-jvto-system-holistic-synthesis.md` (synthesis)
- `2026-05-27-jvto-tooling-ecosystem-analysis.md` (strategy)

Superseded by canonical bundle-taxonomy + transformation-map; kept for provenance (R6 archive-before-delete). `output/` root now D1-clean. Residual lower-priority D1: `output/website/2026-05-27-*` receipts + exposure-board.html (not in this scope).

---

## [2026-06-02] cleanup-governor Mode B | Phase A safe cleanup

Per /llm-wiki:decision-map audit (Mode A, whole-repo), executed approved Phase A:
- **Deleted** `policy/inclusions-exclusions.md` — 0-byte empty file; inclusions policy owned by `wiki/ops/policy-source-ownership.md` (R-LOCK). `policy/` dir now empty/removed.
- **Removed** empty `templates/` dir — 3 Obsidian templates relocated to `tests/templates/` in commit `10f6f28` (intentional, committed). Doc drift: `CLAUDE.md` §Directory Structure + `bundle-taxonomy.md` §"not a bundle" still list `templates/` — flagged, not edited this pass.
- **Indexed** 3 previously-uncatalogued pages in `wiki/index.md`: `ops/whatsapp-reply-intelligence-compiler-spec` (§Workflows), `internal-ops/2026-06-02-chatbot-llmwiki-integration-audit` + `…-slim-feed-pattern` (§Internal Ops).

No LOCK files touched. No bundle migration. No jvto-web/chatbot runtime drift.

---

## [2026-06-02] fix | Homepage stale Google Maps review count 92 → 123

Stale value corrected in `output/website/pages/homepage.md` (L183 heading + L187 intro). Canonical = **123** per `wiki/credentials/trust-signals.md` §Live Review Platforms (Google Maps 4.9/5, verified 2026-05-26 via API); SSOT explicitly flags 92 as stale. Sprint named only L183; grep found stale 92 in both spots — both fixed. Other counts (TP 51, TA 21) and ratings already matched SSOT, untouched. jvto-web live deploy mirrors this file — separate push, out of scope (GAP-05 EXECUTION-OUT-OF-SCOPE BUT LOGIC-RESOLVABLE; in-repo source now correct).

---

## [2026-06-01] cleanup | Phase A governance — stray file + plugins/ exemption

**Scope:** Phase A safe cleanup. Zero content changes. Zero wiki page moves.

**Deleted:**
- `output/faq-2026-05-12-bromo.md` — empty 1-line untracked file at wrong path (`output/` root). Violates location rule (slug-mirror files must be in `output/website/faq/`) and naming convention (no date prefix for slug-mirror files). No content lost.

**Updated:**
- `CLAUDE.md §Naming Rule Exemptions` — added `plugins/llm-wiki/` as named exemption; file names are referenced by Claude Code routing.
- `CLAUDE.md §Analysis Defaults` — new section; lists `plugins/`, `raw/`, and `output/_archive/` as R-IGNORE scope for routine audit passes.

---

## [2026-06-01] restructure | Bundle-first restructure Phase 2 — wiki scaffold

**Scope:** Wiki-side scaffold only. Zero output/ changes. Zero content moves.

**Created:**
- `wiki/bundles/README.md` — thin index layer README.
- `wiki/bundles/trust.md` — Trust Bundle stub index.
- `wiki/bundles/website-logic.md` — Website Logic Bundle stub index.
- `wiki/bundles/packages.md` — Package Bundle stub index.
- `wiki/bundles/reviews.md` — Review Bundle stub index.
- `wiki/bundles/whatsapp.md` — WhatsApp Reply Bundle stub index.
- `wiki/bundles/assets.md` — Asset Bundle stub index.
- `wiki/assets/.gitkeep` — Asset Bundle workspace placeholder.
- `wiki/_shared/.gitkeep` — cross-bundle registries/rules placeholder.

**Not in scope (deferred):** `output/*-bundle/` roots; migration of `output/website/{aeo,faq,schema,pages,blog}` → `output/website-bundle/`; rename of `HANDOFF.md` / `INDEX.md`; deletion of empty `wiki/{analytics,marketing}/`; move of `wiki/internal-ops/backoffice-extraction.md`; move of `wiki/sources/{ssot-image-asset-map,google-profile-media-2026,gpx-destination-data}.md` to `wiki/assets/`; creation of the 8 new index/merge pages.

**Commit:** `restructure | wiki/bundles + wiki/assets + wiki/_shared scaffold (Phase 2)` — to be run by user (sandbox git unable to commit through Windows worktree pointer).

---

## [2026-06-01] restructure | Bundle-first restructure Phase 1 — docs

**Scope:** Documentation-only. Zero file moves. Zero output/ changes.

**Created:**
- `wiki/ops/bundle-taxonomy.md` — defines 6 website-first bundles (Trust, Website Logic, Package, Review, WhatsApp Reply, Asset); full file→bundle map; cross-bundle shared files; explicit Phase 1–2 non-goals.

**Updated:**
- `wiki/ops/transformation-map.md` — added "Canonical Bundle Set" intro section; aligned Bundle Status Table to 6-bundle naming; added Asset Bundle row to Per-Bundle Pipeline; promoted Package Readiness Compiler to DONE (v1.2) and Website Logic Bundle to PARTIAL.
- `CLAUDE.md` (root) — added §Bundle Mapping (6-bundle list + pointers); added §Naming Rule Exemptions listing canonical operational anchors that keep current names (`output/INDEX.md`, `output/website/HANDOFF.md`, all trust-bundle JSONs, all schema/aeo/faq/pages URL-mirrors, all bundle index pages, etc.).

**Not in scope (deferred):** any output/ scaffold, any content move, any rename of HANDOFF.md or INDEX.md, deletion of empty domain folders, creation of the 8 new index/merge pages.

**Commit:** `docs | bundle taxonomy + transformation-map alignment + naming exemptions (Phase 1)` — to be run by user (sandbox git unable to commit through Windows worktree pointer).

---

## [2026-06-01] ops | close final source orphan and remove base stub
Attributed `wiki/sources/3d-route-viewer.md` to the 5 destination pages whose data it visualizes (Mapbox 3D fly-through built on the same AllTrails GPX raw data already cited via `gpx-*` slugs). Frontmatter-only change in destinations; no body edits.

Files updated (5 destinations): `wiki/destinations/{kawah-ijen,mount-bromo,madakaripura,papuma-beach,tumpak-sewu}.md` — appended `3d-route-viewer` to `sources:` array. Files updated (1 source): `wiki/sources/3d-route-viewer.md` — populated `pages_updated` with the 5 destination paths. Files deleted (1): root `BASE.base` (3-line dead stub, superseded by [[bases/index.base]]).

Verification: `python scripts/frontmatter_normalize.py` → `Files changed: 0` (idempotent). Orphan source count: **1 → 0**. Bases YAML still valid (untouched this commit). Obsidian Bases v1 + Phase B + alias fix + final orphan close — all DONE.


## [2026-06-01] ops | fix backoffice source alias coverage
Created umbrella source `wiki/sources/backoffice-mysql.md` and back-linked the 8 split files so downstream pages keep the existing `backoffice-mysql` citation while the orphan filter in [[bases/sources.base]] now sees the splits as covered.

Files created (1): `wiki/sources/backoffice-mysql.md` — frontmatter (type=source, slug=backoffice-mysql, owner=wiki-llm, stale_after_days=90, ingested=2026-05-25, format=mysql) + `pages_updated` of 14 (auto-derived: 8 splits + 6 downstream consumers).

Files updated (8): `wiki/sources/backoffice-{bookings-ops,finance,master-data,pricing,schema,staff,vendors,whatsapp}.md` — single-line change, `pages_updated: []` → `pages_updated: [wiki/sources/backoffice-mysql]`. No body edits.

Bases formatting absorbed (7): `bases/{credentials,destinations,index,ops-health,people,products,sources}.base` — pre-existing dirty state from Obsidian canonicalizer (quote stripping + blank-line collapse). Diff was semantic-equivalent; committed to clear working tree.

Orphan count: 9 → 1 (`3d-route-viewer.md` remains, deferred). Idempotency: `python scripts/frontmatter_normalize.py` → `Files changed: 0` still holds (umbrella created with required fields; 8 splits already had owner+stale_after_days, only pages_updated changed value).


## [2026-06-01] ops | Phase B — frontmatter normalization
Normalized frontmatter across all 97 `wiki/**/*.md` pages via `scripts/frontmatter_normalize.py`. Added `owner: wiki-llm` + `stale_after_days` (per-type defaults: source=90, finance=30, ops=120, else=60) to every page missing them. Backfilled `pages_updated` on all 43 source pages via deterministic reverse-link grep across all `sources:` frontmatter arrays. Body content untouched.

Inserts: owner=97, stale_after_days=97, pages_updated=43. Files changed: 97. No frontmatter losses.

Orphan sources surfaced (9 — 0 reverse links): backoffice-bookings-ops, backoffice-finance, backoffice-master-data, backoffice-pricing, backoffice-schema, backoffice-staff, backoffice-vendors, backoffice-whatsapp, 3d-route-viewer. Backoffice batch never referenced by individual slug in downstream pages — backoffice-extraction.md uses meta-slug `backoffice-mysql`. Either rewire `wiki/internal-ops/backoffice-extraction.md` to cite all 8 by slug, or extend reverse-link logic to handle meta-slug aliases. Deferred.

Top reverse-link counts: ssot-v6=28, db-export-2026-05=12, guardian-authority-framework-2026-05=10, seo-audit-2026-05=9, ssot-image-asset-map=8.

Verification: dry-run + apply both ran without write errors; `git diff --stat` = 97 wiki files modified; spot-check ssot-v6.md + transformation-map.md confirms only frontmatter block changed.


## [2026-06-01] ops | add Obsidian Bases domain dashboards
Added 7 `.base` files in new `bases/` folder (`index`, `destinations`, `sources`, `products`, `people`, `credentials`, `ops-health`). All formulas null-guarded against missing frontmatter — works with current data, no normalization required. Coverage: `wiki/**` only. Root `BASE.base` stub kept untouched. `wiki/index.md` gained a Live Bases section linking the 7 dashboards.

Frontmatter gaps surfaced (report only, not fixed this phase):
- sources missing `slug`: 38/43; missing `ingested`: 43; missing `format`: 43; missing `pages_updated`: 43
- credentials missing `credential_category`: 6/6
- pages with empty `sources: []`: 26
- `wiki/sources/3d-route-viewer.md` missing `sources:` field entirely
- `wiki/people/crew-registry.md` missing `role`

Pages updated: [wiki/index.md, wiki/log.md, CLAUDE.md]. Files created: [bases/index.base, bases/destinations.base, bases/sources.base, bases/products.base, bases/people.base, bases/credentials.base, bases/ops-health.base]. Verification: all 7 parse as valid YAML.

---

## [2026-05-31] feat | Package Readiness Compiler v1.2 — detail artifacts (pricing/itineraries/booking)
Extended the compiler to emit the three deferred artifacts. Bundle now complete at 6 files. Still Package Readiness — no new wedge.

Files updated (5): scripts/package_compiler/loader.py (parse_slug_tables + origin-aware detail_for — resolves the 3 Surabaya/Bali slug collisions via enclosing H2 section; loads pricing + itinerary detail tables), validator.py (PKG-04/05 now require a parseable tier/day table, not just a slug mention), renderer.py (build_pricing / build_itineraries / build_booking_compatibility + pax/price/meals parsers; OUTPUTS=6; dict-based atomic write; schema v1.2; manifest gains artifacts list), compile_packages.py (build + write all 6; pricing/itinerary counts in report), tests/package_compiler/test_package_compiler.py (now 17 tests — added pricing/itineraries/booking builders + collision-resolved-by-origin).
Files created (3): output/products/package-readiness/package-pricing.json, package-itineraries.json, booking-compatibility.json. Regenerated: package-registry.json (unchanged content), gap-report.json, _manifest.json.

Verification: `pytest` → 17 passed. `--dry-run --strict` and `--write --strict` → 16 packages, 0 findings, manifest.clean=True; 103 pricing tiers + 57 itinerary days parsed across all 16 (incl. colliding Bali variants). Bundle = 6 artifacts + manifest.
Notes: pricing pax tiers parse solo/range/N+ forms ({min_pax,max_pax,idr_per_person}); Bali packages flagged ferry_included; booking-compatibility marks all 16 instant_book + whatsapp_assisted (live sitemap pages). Non-goals honored: no Trust Bundle / decision-registry / jvto-web / DB / Policy-Bundle / WhatsApp / Review / Finance / package-source-content edits.

## [2026-05-31] feat | Package Readiness Compiler v1.1 — tests + PKG-06/11/12
Hardened the compiler: added a test suite and the three remaining validation rules. Behaviour change → output regenerated; result stayed clean.

Files updated (4): scripts/package_compiler/loader.py (load db-export-2026-05 as a source), validator.py (PKG-06 inclusion/exclusion readiness, PKG-11 DB-export reconciliation, PKG-12 forbidden-wording sweep), renderer.py (manifest source_hashes now include db-export), output/products/package-readiness/_manifest.json (regenerated — new timestamp + db-export hash; registry/gap-report byte-identical).
Files created (2): tests/package_compiler/__init__.py, tests/package_compiler/test_package_compiler.py (13 tests — loader 16 packages, sitemap 12+4, Bali slug/url normalisation, validator 0-findings on clean source, PKG-12 fires on injected forbidden wording, PKG-11 errors when canonical>DB, renderer registry=16, manifest clean true/false, write emits 3 files, dry-run does not write, --write calls write path).

Verification: `pytest tests/package_compiler/` → 13 passed. `python scripts/compile_packages.py --dry-run --verbose --strict` → 16 packages, 0 findings, manifest.clean=True. `--write --strict` → regenerated, clean, registry=16, 7 source hashes.
Scope note: PKG-12 scans ACTIVE package source (overview/pricing/itineraries) only; the policy-source-ownership deprecated table and wiki/log.md history are guardrail/audit containers and intentionally not scanned — a full-repo sweep is the Global Validator wedge (transformation-map P6). v1.1 still emits 3 of 6 artifacts (pricing/itineraries/booking-compatibility deferred).
Non-goals honored: no Trust Bundle / decision-registry / jvto-web / DB / Policy-Bundle / WhatsApp / package-source-content edits.

## [2026-05-31] data | Package Readiness Compiler v1 — first bundle output
Ran the compiler with `--write` to generate the first real package-readiness bundle. No compiler logic changed — `--write` succeeded on the existing v1 code.

Command: `python scripts/compile_packages.py --write --verbose`.
Output created (3): output/products/package-readiness/package-registry.json (16 packages), gap-report.json (0 findings), _manifest.json (clean=True, canonical_package_count=16, dry_run=false, source hashes recorded).
Files updated (1): wiki/log.md.

Result: 16 packages, sitemap 12 Surabaya + 4 Bali, 0 findings (0 error / 0 warn), manifest.clean=True. v1 emits registry/gap-report/manifest only — package-pricing/itineraries/booking-compatibility deferred per v1 design. No tests added; PKG-06/11/12 not implemented this phase.
Non-goals honored: no Trust Bundle / decision-registry / jvto-web / DB edits.

## [2026-05-31] feat | Package Readiness Compiler v1 — skeleton + dry-run
Implemented the v1 skeleton of the Package Readiness Compiler per wiki/ops/package-readiness-compiler-spec.md. Dry-run only — no JSON written.

Files created (5): scripts/compile_packages.py (CLI: --dry-run default, --write, --verbose, --strict), scripts/package_compiler/__init__.py, loader.py (pure markdown-table parsing: registry + sitemap, no business logic), validator.py (rules PKG-01–05, 07–10), renderer.py (registry/gap-report/manifest previews + atomic --write path).
Files updated (1): wiki/log.md.

Dry-run result (`python scripts/compile_packages.py --dry-run --verbose`): PASSED — 16 packages parsed; sitemap matched 12 Surabaya + 4 Bali; 0 findings (0 error, 0 warn); manifest.clean=True; no JSON output written. PKG-03 confirms Bali slugs resolve (`bali/x` → `/tours/from-bali/x`). PKG-06/11/12 deferred to next pass; v1 renders 3 of 6 spec artifacts (registry, gap-report, manifest).
Non-goals honored: no --write, no output/products/package-readiness/ files, no Trust Bundle / decision-registry / jvto-web / DB edits.

## [2026-05-31] ops | Package Readiness Compiler — Spec (no code)
Wrote the implementation spec for the NEXT (P1) wedge from the transformation map. Spec only — no compiler, no JSON.

Pages created (1): wiki/ops/package-readiness-compiler-spec.md — purpose, 8 source files, canonical 16-package slug list (12 Surabaya + 4 Bali; 16 = 15 standard + 1 specialty; DB 22 = 16 + 6 student), output path `output/products/package-readiness/`, 6 output files (package-registry/pricing/itineraries/booking-compatibility/gap-report/_manifest), 12 validation rules PKG-01–12, compiler architecture (loaders→enricher→validators→renderers→CLI, --dry-run/--strict mirroring compile_trust.py), non-goals, next implementation phase.
Pages updated (2): wiki/index.md — added [[ops/package-readiness-compiler-spec]] under Workflows (Meta), total_pages 94→95; (this) wiki/log.md.

Grounding: read packages-overview/full-pricing/itineraries, db-export (22 pkgs / 143 prices / 99 itinerary-days), sitemap (16 live /tours/ URLs), route-data-csv (43 routes), policy-source-ownership. Primary deliverable of the future compiler = gap-report.json. Non-goals honored: no scripts, no JSON, no Trust Bundle/jvto-web/DB edits.

## [2026-05-31] ops | Transformation Map — Domain→Bundle Pipeline
Created the master transformation map so future compiler/bundle work follows one structure and completed work is not reopened.

Pages created (1): wiki/ops/transformation-map.md — per-domain chain (canonical source → script → output → validator → consumer → status), bundle status table, output convention `output/<domain>/<bundle>/` (no `compiled/`), do-not-reopen section, next-wedge spec.
Pages updated (2): wiki/index.md — added [[ops/transformation-map]] under Workflows (Meta), corrected stale Trust Bundle "blocked" status to DONE/do-not-reopen, total_pages 93→94; (this) wiki/log.md.

Status recorded: Trust Bundle v1 DONE (DEC-001/002/003 locked, CONF-001/002/003 resolved, F1–F8 pass, outputs pushed, jvto-web integrated) — DO NOT REOPEN. Policy Source Ownership DONE. R065 Booking Flow DONE. Package Readiness Compiler = NEXT (P1). Policy Bundle, WhatsApp Reply Intelligence, Review Proof Index, Finance Quote Helper, Global Wiki Validator = FUTURE.
Non-goals honored: no compiler scripts, no JSON, no Trust Bundle/registry/jvto-web/DB edits.

## [2026-05-31] policy | JVTO Policy Consolidation + Stale Data Cleanup
Updated policy sources for dual booking paths, all-inclusive/inclusions, payment, Travel Credit, health screening, natural-phenomena guarantee wording, and R065 booking-flow alignment. Added policy-source-ownership map and deprecated wording guardrails.

Pages created (1): wiki/ops/policy-source-ownership.md — canonical owner per policy domain + deprecated-wording table.
Pages updated (3): wiki/products/packages-overview.md — §booking-flow split into Path A (Website Instant Book) + Path B (WhatsApp-assisted); wiki/website/faq-master.md — Q15 rewritten to dual-path; wiki/index.md — ops reference added.

Audit note: 3-agent sweep confirmed booking-platform-analysis, cash-refund/Travel-Credit, Blue Fire/sunrise, Madakaripura helmet, police-escort, ISIC/UNESCO, INDECON/HPWKI ("HPI" = zero matches), and Ijen health-screening wording all already correct — no edits required. Stale "Trip.com" survives only in this log's history (audit trail, left unchanged per append-only) and a raw/ snapshot; stale "50% fee" only in raw/db_export_raw.json. Both now guarded by the deprecated-wording section. Q14/Q16/Q17 left untouched (already correct).

## [2026-05-31] ingest | Tango Workflow — JVTO Website Booking Flow (R065)

**New file:** [[sources/tango-workflow-jvto-website-booking]] — R065. 4-page Tango screenshot PDF of JVTO website self-checkout (Instant Book) flow, 18 steps, recorded by Agung Sambuko.

**Key finding:** This is the website self-checkout path — parallel to and distinct from the WhatsApp-assisted booking flow. First time this path is formally documented in wiki. [[products/packages-overview]] §booking-flow currently describes WA-only path — stale gap flagged.

**Corrections applied:** [[website/booking-platform-analysis]] retitled from "Trip.com Booking Platform Workflow Analysis" to "JVTO Website Booking Flow Analysis". Sources field updated from `tango-workflow-trip-com` → `tango-workflow-jvto-website-booking`.

**Gaps registered (5):**
1. Terms checkbox content must show JVTO Travel Credit policy — needs UI audit
2. Price anomaly: IDR 3,350,000 displayed vs SSOT reference
3. Add-on "Transport to Medewi" not in authorised inclusions list
4. Health screening not collected in checkout — confirm post-booking trigger
5. packages-overview §booking-flow stale — Instant Book path undocumented

**Pages updated:** `sources/tango-workflow-jvto-website-booking` (new), `website/booking-platform-analysis` (corrected), `index.md` (source added, booking-platform-analysis entry updated), `_manifest/raw-files-index.csv` (R065), `_manifest/ingest-status.csv` (R065).

---

## [2026-05-31] analysis | Trip.com Booking Platform Workflow

**New file:** [[website/booking-platform-analysis]] — 18-step Tango workflow on Trip.com mapped to JVTO booking flow across 5 phases (Package Selection, Add-ons, Trip Configuration, Terms & Payment, Post-Payment).

**Gaps identified:**
1. Cancellation policy mismatch: JVTO Travel Credit (100% ≥48h, forfeited <48h) vs Trip.com standard OTA terms
2. Price anomaly: IDR 3,350,000 displayed vs SSOT pricing (IDR 3,570,000 for 2 pax or IDR 6,300,000 solo)
3. Add-on alignment: Medewi transport upsell not in JVTO standard inclusions
4. Health screening missing: BBKSDA-required for Ijen routes — no Trip.com workflow step for Dr. Irwandanu coordination

**Owner tasks (Sam):** Verify pricing, audit upsells, confirm cancellation alignment, verify health-screening collection method, test e2e flow.

**Pages updated:** `index.md` (added booking-platform-analysis link to Website section).

---

## [2026-05-26] health-check | on-demand

**Stale claims fixed:**
- `aeo-claims.md` C6 aggregate: Google 92→123 reviews (superseded by google-maps-reviews-api-2026)
- `index.md` packages line: 15 (11+4) → 16 (12+4) (resolved since sitemap ingest)
- `db-export-2026-05.md:51` still says Google 92 — correct for DB export date, noted as superseded

**Orphans (known, pending REC-003 + REC-004):**
- `credentials/permit-requirements.md` — no inbound domain page links
- `sources/finance-rate-cards.md` — no inbound link from finance/rate-cards

**Open gaps (2 remaining):**
- `content/voice-invariants` — lives in brand-voice §voice-invariants (optional promotion)
- `bromo-ijen-status-today` — blocked on PVMBG/BBKSDA live source

**Governance layer:** 9 claims registered, 50 entities, 18 evidence items, 3 open conflicts, 5 decision queue items, 9 pending recommendations. All registries consistent.

**No stale pages** — all 92 wiki pages updated within 90 days (most recent: 2026-05-26).

---

## [2026-05-26] enhance | Intake correlation governance layer

New files: `raw/_manifest/claim-registry.yml` (9 claims C1-C9 with evidence chains), `raw/_manifest/entity-registry.yml` (50 entities ENT-001–ENT-050 across 10 types).

Enhanced: `decision-queue.md` (table structure + 5 seeded items from conflicts/recs), `wiki/ops/intake-gate.md` (Entity Registration + Claim Linkage subsections, 12-row manifest table, 8-item correlation checklist), `intake-audit.md` (Governance Layer Counts section, evidence count fix 14→18).

Documentation updated: `docs/reference-wiki-structure.md` (added `_manifest/` to directory tree + claim/entity registry references), `docs/howto-ingest-sources.md` (added entity registration + claim linkage to Workflow 7 section).

---

## [2026-05-26] ingest | Google Maps Reviews API (123) + Profile Media (87) — 3-platform compilation

Sources: `raw/google review page [1-3].json` (123 Google reviews via API), `raw/google profile media.json` (87 GMB media items).
Profile: review-feed + custom (media).

Pages created: sources/google-maps-reviews-api-2026, sources/google-profile-media-2026.
Pages updated: reviews/google-tripadvisor-2026 (rebuilt as unified 3-platform compilation: 195 reviews organized by crew + package), people/crew-registry (all 14 crew enriched with cross-platform review quotes + counts), products/packages-overview (review evidence section per package family), reviews/review-patterns (4 new derived patterns: multi-language, photography, accommodation variance, schedule tightness), credentials/trust-signals (Google 92→123, total 164→195), index.

Key additions: 31 new Google reviews since DB export; full text+replies for all 123; combined 195-review cross-platform compilation; all 14 crew have multi-platform review quotes; review evidence mapped to 15 of 16 packages (Taman Safari: 0 reviews); accommodation feedback pattern identified (Baratha, Joglo Kecombrang, Grand Whiz).

---

## [2026-05-26] compile | JSON-LD schema for 6 student packages

Profile: `schema` compilation. 6 TouristTrip + AggregateRating + AggregateOffer schemas generated. All prices verified against packages-full-pricing.md §Student Packages. All canonical values verified against trust-signals.md §Schema Canonical Values (ratingValue=4.8, reviewCount=51, NIB=1102230032918, ISIC=259268). Student-specific fields: eligibleCustomerType=Student, touristType=ISIC-verified. Receipt: output/website/schema/student-schemas.receipt.md.

Also: updated seo/seo-strategy Silo 1 status from "needs schema" to "DONE" (16 canonical schemas generated 2026-05-18, 6 student schemas generated today).

---

## [2026-05-26] audit | Backoffice pricing validation — template vs realized

Pages updated: sources/backoffice-pricing (validation findings + DATA GAP flag), finance/rate-cards (Klook 25% commission model), finance/profit-analysis (OTA impact + realized validation BLOCKED note).

Key findings:
- Template prices match wiki at solo tier (5/5 spot checks pass)
- Klook commission = flat 25% retail markup, JVTO receives full template price — now documented
- `bookings.template_package_id` unpopulated for all 1,453 bookings — realized price comparison structurally impossible
- 89 backoffice packages vs 22 published (67 unpublished — status unknown)
- `price_categories` names missing — pax-tier mapping blocked, needs live DB query

---

## [2026-05-26] review | Silo 3 draft output files — draft → reviewed (5 files)

5 Silo 3 travel-guide output files promoted from `draft` to `reviewed`:
- output/website/pages/travel-guide/bbksda-regulations-ijen.md — Fixed: unsourced clinic names removed, SIP→STR credential naming corrected
- output/website/pages/travel-guide/bbksda-regulations-bromo.md — Clean, no changes needed
- output/website/pages/travel-guide/ijen-gas-mask-equipment.md — Fixed: removed dead link to non-existent what-to-pack page
- output/website/pages/travel-guide/permit-requirements-east-java.md — Fixed: llms.txt reference removed (not yet live), Tumpak Sewu helmet note added, SIP→STR corrected
- output/website/pages/travel-guide/sulfur-mining-cultural-guide.md — Added unsourced-data disclaimer for mining statistics (load weights, income, PT Candi Ngrimbi, colonial history)

Wiki discrepancy flagged: KBLI code 79120 (trust-signals) vs 79121+79911 (permit-requirements) — reconcile in next health check.

---

## [2026-05-26] ingest | Guardian Infrastructure & Authority Framework — 4-file strategy synthesis

**Source type**: Workflow 4 typed ingest. Profile: seo-audit.
**Raw files (4)**: Guardian Infrastructure (Wild West), Institutional Authority Framework (Costly Signals), JVTO Digital Trust Fortress (GEO Blueprint), Guardian Infrastructure (Strategic Authority & Risk Mitigation).
**Overlap**: ~75% reconfirms existing sources (geo-aeo-strategy-2026-05, why-jvto-trust-architecture, digital-trust-fortress-blueprint, crew-strategy-integration-2026-05). Only genuinely new concepts extracted.

Pages created (1):
- sources/guardian-authority-framework-2026-05 — 4-file synthesis. New: Personality Economy + Micro-Entity framing, Dream Team pairings, Digital Trust Gap table, Answer Block format spec, Sprint 0 recovery board, Definition of Done checklist, Authority Stack comparison, ISO 3166-2:ID anchoring, Costly Signal theory, 3 psychological barriers framework, named concept glossary (13 entries).

Pages updated (10):
- people/crew-registry — Added Personality Economy / Micro-Entity section + Dream Team Pairings table + Anjas archetype contradiction note
- seo/geo-aeo-strategy — Added Digital Trust Gap evaluation table + ISO 3166-2:ID geospatial anchoring section
- website/brand-voice — Added Answer Block Format specification
- website/aeo-claims — Added 3 Answer Block exemplars (Ijen Health, Bromo Inclusions, Cancellation) with voice-invariant warning
- website/copy-bank — Added Authority Stack table + 3 Psychological Barriers framework + Named Concept Glossary (7 terms)
- credentials/trust-signals — Added Costly Signal Theory section + Partnership Value Matrix table
- seo/seo-strategy — Added Sprint 0 Recovery cross-reference (with [stale?] flags)
- ops/compilation-profiles — Added Definition of Done checklist (Trust Fortress Ready, 4 layers)
- website/schema-templates — Added ISO 3166-2:ID geospatial anchoring rule with JSON-LD example
- index — Added source entry, total_pages 87→88

Contradictions flagged:
- Anjas archetype: "Gen Z Ambassador" (crew-strategy-integration) vs "Content Architect" (institutional-authority-framework). Both valid framings; noted in crew-registry.

---

## [2026-05-25] ingest | Backoffice MySQL extraction (Tier 1: finance + ops)

Live extraction from `u1805424_jvto_clone @ 153.92.9.37` (MariaDB 10.11, Hostinger). 210 tables inventoried; 148 non-empty tables dumped to CSV; ~63k rows total.

Pages created (9):
- sources/backoffice-schema — 210-table inventory + Mermaid ERD for core entities + full FK web
- sources/backoffice-finance — revenue by month, currency mix, payment methods, invoice line-items, debt outstanding
- sources/backoffice-pricing — template `package_prices` vs realized `bookings.grand_total` per template_package_id
- sources/backoffice-bookings-ops — booking volume, pax distribution, lead time, channel/agent mix, assignment counts
- sources/backoffice-staff — `guide_drivers` aggregates: crew level, role, licenses populated, top-deployed crew
- sources/backoffice-vendors — vendor count by category, hotel + car fleet inventory with rates
- sources/backoffice-master-data — reference catalogs: accounts, payment_methods, crew_roles, weather_codes, wa_chat_categories, etc.
- sources/backoffice-whatsapp — 5,547 message analytics; direction/media breakdown; intent category distribution
- internal-ops/backoffice-extraction — pipeline playbook + scripts + PII rules + connection fallback

Pages updated (3 cross-refs):
- finance/rate-cards — added validation hook pointing at backoffice-pricing for realized prices
- people/crew-registry — added pointer to backoffice-staff for assignment volume
- products/packages-full-pricing — added realized vs template note pointing at backoffice-pricing
- index — added Backoffice MySQL extraction subsection + Internal Ops section
- overview — pending

Manifests updated: raw-files-index (+R062, R063, R064)

Scripts added: scripts/_db.py, inventory.py, build_manifest.py, dump_schema.py, dump_data.py, peek.py, analyze.py

Raw layer:
- raw/backoffice/schema/full-schema.sql (committed — DDL only)
- raw/backoffice/_manifest.md (committed)
- raw/backoffice/csv/*.csv (148 files, gitignored — contains PII)
- raw/backoffice/_inventory.json (gitignored — table metadata)

PII handling: aggregate-only at wiki layer; defense-in-depth `pii_scrub()` in analyzer. Manual grep verification: 0 emails, 0 phone numbers leaked into committed wiki pages. Full data lives only in gitignored raw/backoffice/csv/.

Key new facts surfaced:
- 5,547 WhatsApp messages tracked in `wa_chats` — previously not in wiki at all
- 2,985 itineraries shared via WA (`wa_itineraries`) — new operational channel
- `tw_calculations` (295 rows) + `tw_calculation_details` (5,317 rows) — internal pricing calculator that pre-dates and feeds bookings
- `tw_invoices*` family — separate B2B/Klook invoice subsystem
- 35 `user_partners` — agent/partner records

---

## [2026-05-25] health-check | weekly

| Metric | Count |
|--------|-------|
| Total wiki pages | 75 |
| Orphans | 7 |
| Stale >90 days | 0 |
| Stale >30 days | 0 |
| Contradictions (actionable) | 3 fixed |
| Contradictions (tracked/blocked) | 3 unchanged |
| Gap pages | 0 |
| Missing from index | 0 |
| Unlogged raw files | 37 |

**Contradictions fixed:**
- C1: `wiki/index.md:75` — Trustpilot 4.8/47 → 4.8/51
- C2: `wiki/website/faq-master.md:109` — Trustpilot 4.8/47 → 4.8/51
- C3: `wiki/seo/competitors.md:98` — "160+ reviews" → "164 reviews"

**Orphans (7, all source pages or new pages):**
- `credentials/permit-requirements` (new, needs cross-refs from destination pages)
- `sources/finance-rate-cards` (needs link from finance/rate-cards)
- `sources/gemini-trust-fortress-mockup`, `sources/gpx-destination-data`, `sources/llm-kb-tooling-guide`, `sources/route-data-csv`, `sources/wa-pro-crm-api` (structural source orphans — reachable via index)

**Tracked contradictions (unchanged):**
- Stefan Loose year/ISBN — blocked on physical book check
- Madakaripura height — under reconciliation
- Second NIB 0220001393513 — blocked on OSS portal

**Unlogged raw files:** 37 files in raw/ (including 23 FINANCE/ files and 14 strategy/audit docs) have no individual ingest log entry. Many were batch-ingested under consolidated source pages (e.g., finance rate cards, SEO audit consolidation). Consider a batch-log entry to clear these.

---

## [2026-05-25] expand | Silo 3 wiki backing — sulfur mining, BBKSDA Bromo, permits, seasonal data

Pages updated: [[destinations/kawah-ijen]] (sulfur mining expanded to ~200 words: history, working conditions, cultural significance, tourist etiquette, safety note), [[destinations/mount-bromo]] (new BBKSDA Regulations section: authority, entry requirements, jeep mandate, closure rules, no health screening), [[website/operational-facts]] (new Best Time to Visit seasonal guide: dry/shoulder/wet season, Yadnya Kasada, Ramadan), [[index]] (permit-requirements entry added). Page created: [[credentials/permit-requirements]] (operator permits + visitor entry requirements per destination with costs).

---

## [2026-05-25] restructure | Domain separation + finance ingestion

Full restructure of wiki/ and output/ into domain-separated folders. 14 commits.

**Wiki moves:**
- `content/` → `website/` (8 files: brand-voice, copy-bank, faq-master, aeo-claims, schema-templates, query-hero-claim, operational-facts, hotels)
- `ops/` split: 3 files → `whatsapp/` (operations-playbook, rules-engine, canned-responses), 5 files → `seo/` (seo-strategy, geo-aeo-strategy, competitors, why-jvto-architecture, redirect-map), 3 files stay in `ops/` (ingestion-profiles, compilation-profiles, health-checks)

**Output moves:**
- `schema/`, `faq/`, `aeo/` → consolidated under `output/website/`
- Existing `output/website/*` → `output/website/pages/`

**New domains created:**
- `wiki/finance/` — 4 pages: [[finance/rate-cards]], [[finance/package-costs]], [[finance/profit-analysis]], [[finance/custom-tour-builder]]
- `wiki/sources/finance-rate-cards.md` — source summary for raw/FINANCE/ rate cards
- Empty placeholders: `wiki/marketing/`, `wiki/analytics/`, `wiki/internal-ops/`, `output/whatsapp/`, `output/marketing/`, `output/finance/`

**Profile additions:**
- `finance-spreadsheet` ingestion profile added to [[ops/ingestion-profiles]]
- `custom-tour-quote` compilation profile added to [[ops/compilation-profiles]]

**Cross-references:** All `[[content/...]]` → `[[website/...]]`, all moved `[[ops/...]]` → `[[seo/...]]` or `[[whatsapp/...]]`. `wiki/log.md` unchanged (historical). Frontmatter types updated. CLAUDE.md, index.md, HANDOFF.md rewritten.

**Final counts:** 74 wiki pages, 147 output files, 24 sources.

---

## [2026-05-25] review | Bulk status upgrade — 99 output files draft → reviewed

Scanned all output files against brand-voice.md and trust-signals.md criteria:
- **Forbidden phrases**: 1 violation found + fixed ("world-class" → "dramatic" in bromo-vs-ijen-comparison.md)
- **Avoid phrases**: 0 violations
- **Price format**: 0 violations (all IDR with commas)
- **Rating conflation**: 0 violations (Trustpilot/Google/TA correctly attributed everywhere)
- **NIB consistency**: 0 violations (all = 1102230032918)
- **Schema "mandatory" language**: noted in 8 schema JSON files — acceptable because BBKSDA SE.1658 regulatory qualifier present in each instance

99 files updated `status: draft` → `status: reviewed`. INDEX.md updated (81 status entries). Archive and schema files excluded from status change.

---

## [2026-05-25] generate | Silo 4 travel guides — itinerary guide + Surabaya vs Bali

Pages created: `output/website/travel-guide/bromo-ijen-itinerary-guide.md` (duration comparison 1D–6D, day-by-day breakdowns, transfer times, pricing table), `output/website/travel-guide/surabaya-vs-bali-starting-point.md` (origin comparison, ferry logistics, cross-island route matrix, price difference breakdown). All prices verified against [[products/packages-full-pricing]], transfer times against [[content/operational-facts]].

---

## [2026-05-25] generate | Student tour pages ×6 + team member pages ×15

Pages created: 6 student tour detail pages (`output/website/tours/student/`), 15 individual team member pages (`output/website/team/`). All prices verified against [[products/packages-full-pricing]] via jvto-verified-output skill. ISIC Provider ID 259268 verified against [[credentials/legal-licenses]]. Crew data verified against [[people/crew-registry]]. All files status: draft.

---

## [2026-05-25] phase-3 | Structural Gap Fill + Developer Handoff

**Scope**: Route-to-content gap analysis, developer handoff document, missing output generation.

### Deliverables

1. **`output/HANDOFF.md`** — Complete developer handoff document:
   - Full route → output file → schema map (56 website pages, 22 schemas, 10 AEO blocks, 8 FAQ blocks)
   - Missing pages inventory (5 ready-to-generate, 3 partially sourceable, 6 blocked)
   - SEO quick wins action list (7 dev-actionable items)
   - Content status summary (12 reviewed, 44 draft)
   - Key wiki reference files for dev

2. **`output/website/team.md`** — Team hub page for `/team` route:
   - All 14 crew members (7 guides + 7 drivers) with bios, KTA credentials, review quotes
   - Founder section with police authority evidence
   - Credential chain explanation (KTA → HPWKI → BBKSDA)
   - Verified via jvto-verified-output skill

### Gap Inventory (documented in HANDOFF.md)

**Ready to generate**: `/team/[slug]` member pages, student tour detail pages ×6, `bromo-ijen-itinerary-guide`, `surabaya-vs-bali-starting-point`

**Blocked**: `bromo-ijen-status-today` (PVMBG), `yadnya-kasada-2026` (no source), geographic market pages (no logistics data)

---

## [2026-05-25] health-check | on-demand (Phase 2 Lint)

**Scope**: Full Workflow 3 / Workflow 6 on-demand audit across 69 wiki pages.

### Results

| Check | Result |
|---|---|
| Contradiction scan | **1 found, 1 fixed** |
| Orphan detection | **0 orphans** |
| Stale claims (>90 days) | **0 stale** |
| Index completeness | **0 gaps** (69 files, all indexed) |
| Gap pages | **1 real gap**: `[[ops/volcano-status]]` (bromo-ijen-status-today, blocked on PVMBG live source) |

### Contradiction Fixed

**Crew count in aeo-claims.md** (C7 section): was "11 members (7 guides + 4 drivers)" — stale SSOT v6.0 §4_2 value. DB export (2026-05-12) confirmed **14 members (7 guides + 7 drivers)**. Updated to "14 members (7+7), 11 KTA-credentialed". Also updated index.md crew-registry description.

### Pre-existing (not resolved — requires owner action)

- **Stefan Loose year/ISBN**: wiki says 2016 / ISBN 9783770167654; raw audit docs say 2018 / ISBN 978-3-7701-7881-0. jvto-web publishes 2018 version. Resolution requires physical book check by Sam. Tracked in [[credentials/press-coverage]].
- **Madakaripura height**: "tallest in Java" — height under reconciliation. Flagged in [[destinations/madakaripura]].
- **Second NIB 0220001393513**: flagged as possible historical OSS record. Verification blocked on OSS portal access. Tracked in [[sources/why-jvto-trust-architecture]].

### Gap page

`[[ops/volcano-status]]` — planned as `/travel-guide/bromo-ijen-status-today`. Blocked: PVMBG MAGMA feed not programmatically accessible. Listed in [[ops/seo-strategy]] Silo 3 targets.

---

## [2026-05-25] ingest | Gemini Trust Fortress HTML Mockup

Pages created: [[sources/gemini-trust-fortress-mockup]]. Key additions: extracted design tokens (police/forensic color system), typography stack (DM Serif Display / Inter / JetBrains Mono), visual effects (scanline, noise texture), embedded schema pattern. Flagged as design reference only — not canonical design system.

---

## [2026-05-25] ingest | GPX Trail Data — Formal Source Page

Pages created: [[sources/gpx-destination-data]]. Key additions: consolidated reference for all 5 AllTrails GPX recordings — bounding boxes, track point counts, elevation ranges, named waypoints. Data already extracted to destination pages during prior session; this formalizes the source page for index completeness.

---

## [2026-05-25] ingest | WhatsApp Pro CRM API Documentation

Pages created: [[sources/wa-pro-crm-api]]. Pages updated: [[ops/2026-05-14-whatsapp-operations-playbook]], [[ops/2026-05-14-whatsapp-rules-engine]] (added source reference). Key additions: 6 REST endpoints (send_message, send_image_url, send_file_url, groups, send_template, checking_key), error codes (200/1002-1006), webhook payload formats for 6 message types (text, image, audio, document, location, contact). API credentials redacted from wiki — stored in WA Dashboard only.

---

## [2026-05-25] sync | wiki → jvto-web — Workstream B (audit revealed near-complete)

**Source type**: Workflow 5 follow-up — fourth and final leg of the 2026-05-24 raw-folder ingest plan (`~/.claude/plans/modular-kindling-clock.md` §Workstream B). **Audit pass discovered the parent plan's "8+ file" scope was 95% already-done** by prior Workflow 5 syncs (`f8ae382` and earlier). Real scope: 1 DB row + 1 schema description line.

**Patched in jvto-web (committed)**:
- **Workstream B** — `7800e48` + `6bd4011`: EAV NLP sharpening on the AEO surface for `/travel-guide/ijen-health-screening` + `/why-jvto` ItemList:
  - `narrative_claims` id='C4' (primary_page=/travel-guide/ijen-health-screening): `pillar` + `core_claim` + 4 `nlp_variants` arrays (short, cs_reply, ai_snippet, customer_friendly) now cite **BBKSDA SE.1658/KSA.9/2024** + **Dr. Ahmad Irwandanu (SIP verifiable on satusehat.kemkes.go.id)**. Source: [[content/aeo-claims]] lines 228–241 + [[content/brand-voice]] lines 60–66.
  - `buildWhyJvtoSchemas.ts:137` ItemList.description: folds in `"PT Java Volcano Rendezvous (NIB 1102230032918, trading as Java Volcano Tour Operator)"` for entity-resolution density on the /why-jvto hub schema graph.
- **Mechanism**: new helper `scripts/ingest-workstream-b.mjs` (Prisma `narrative_claims.update`, dry-run default, `INGEST_CONFIRM=1` to apply, idempotency guard via SE.1658-substring check). Run via `node --env-file=.env.local`.
- **No snapshot regen needed**: `narrative_claims` is a separate table from `content_pages` — resolver reads it at SSR/SSG time, no `dbPageSnapshots.json` mirror exists.

**Audit findings (no patch needed — already canonical from prior commits)**:
- `entityGraph.ts:30` `legalName: 'PT Java Volcano Rendezvous'` ✓
- 5 schema-builder NIB 1102230032918 references (`buildHomepageSchemas.ts:49`, `entityGraph.ts:31/38`, `buildVerifySchemas.ts:249`, image-asset captions) ✓
- 9 FAQ-file NIB / PT references (`homepageFaqs.ts:14,26,44,51`, `tourFaqs.ts:89`, `verifyFaqs.ts:17–28,35`) ✓
- All schema/FAQ "mandatory"/"screening" surfaces already cite SE.1658 (`buildTourSchemas.ts:107-109`, `buildTravelGuideSchemas.ts:79,81,109`, `tourFaqs.ts:124-127`, `homepageFaqs.ts:24-27`, `verifyFaqs.ts:32-36`) ✓
- 4 Dr. Irwandanu citations across schemas + FAQs (`entityGraph.ts:287`, `buildTravelGuideSchemas.ts:82`, `homepageFaqs.ts:26-27`, `tourFaqs.ts:127`) ✓
- `narrative_claims` C1 (police-safety pillar) + C5 (verification-approach meta-claim) — clean, scope-correct as-is ✓

**Verification**:
- DB SAFETY CHECK pass: dry-run → 6-field diff preview confirmed → `INGEST_CONFIRM=1` write → 1 row updated cleanly
- Idempotency re-run: aborts at SE.1658 guard ✓
- `npm run build` → `✓ Compiled successfully in 12.1s` + `✓ Generating static pages (143/143) in 5.3s`

**Lesson surfaced**: when a parent plan flags "drift across 8+ files", audit first. A current-state map cost ~5 grep + 1 DB query and rerouted the work from "text-replacement-heavy refactor" to "1 targeted DB write". The wiki source's drift analysis was true at write time but stale by Workflow 5 sync time. Audit-first prevents spurious "I already fixed that" diffs.

→ jvto-web commits: `7800e48` (chore: ingest script), `6bd4011` (feat: content + schema)

---

## [2026-05-25] sync | wiki → jvto-web — Workstream C Guardian Archetype + Trust-Pillar Crew Mapping

**Source type**: Workflow 5 follow-up — third leg of the 2026-05-24 raw-folder ingest (Plan: `~/.claude/plans/modular-kindling-clock.md` §Workstream C). DB-driven content ingest, not schema. Shipped same day as Workstreams A + D (entry below) but as separate commit pair after owner mid-implementation correction on renderer capability.

**Patched in jvto-web (committed)**:
- **Workstream C** — `8eedb1a` + `6824b00`: prepended three framing sections via new ingest helper.
  - `/why-jvto/our-story` (row id=16): `+ guardian-archetype` at position 0 (Style B narrative dossier, 2 pull-quotes via GFM `>` blockquote). Source: [[content/copy-bank]] lines 93–99.
  - `/why-jvto/our-team` (row id=17): `+ guardian-mindset` + `+ trust-pillar-crew-mapping` at positions 0–1 (framing principle with Rendi crater-descent quote; 7-pillar mapping table + 5-archetype table, both via GFM pipe syntax). Source: [[people/crew-registry]] lines 129–163.
- **Mechanism**: new helper `scripts/ingest-workstream-c.mjs` (Prisma upsert; dry-run by default; `INGEST_CONFIRM=1` to apply; idempotency guard refuses double-prepend). Run with `node --env-file=.env.local`.
- **Block strategy**: single `markdown` block per section, GFM syntax. Renders via canonical `src/components/content/MarkdownRenderer.tsx` (react-markdown + remark-gfm). Branded blockquote (left-border `#9fce33`, italic, light-green bg) + branded table styling (Syne header, hover state). No new block types, no renderer changes.

**Mid-implementation correction**: original plan-mode locked constraint "MarkdownRenderer is custom, no GFM" was based on a subagent reading `src/components/website/MarkdownRenderer.tsx` (dead code, zero imports). Canonical renderer at `src/components/content/MarkdownRenderer.tsx` IS GFM-enabled. Owner re-approved revised approach via AskUserQuestion → ingested verbatim wiki markdown (cleaner than the originally-planned bold-paragraph + grid workaround).

**Verification**:
- DB SAFETY CHECK pass: dry-run → preview confirmed → `INGEST_CONFIRM=1` write → 2/2 rows updated cleanly
- Snapshot regen via `scripts/export-public-page-snapshots.mjs` → wrote 17 routes
- `npm run build` → `✓ Compiled successfully in 12.7s` + `✓ Generating static pages (143/143) in 4.2s`
- `git diff src/lib/publicContent/generated/dbPageSnapshots.json | grep '"id":'` → exactly 3 new section IDs added

**Out of pass (still open per modular-kindling-clock plan)**:
- Workstream B — EAV NLP sharpening across 8+ schema/Faqs files
- Stefan Loose ISBN/year contradiction — owner adjudication
- `reviewApiSnapshots.json` artifact stale (2026-05-08, trustpilot:47) — owner ingest tool

→ jvto-web commits: `8eedb1a` (chore: ingest script), `6824b00` (feat: content)

---

## [2026-05-25] sync | wiki → jvto-web — FOUNDER EAV + verify-jvto/legal continuity

**Source type**: Workflow 5 follow-up. Absorbs narrative + schema content from the 2026-05-24 raw-folder ingest into the live site. Two of four scoped workstreams shipped; two scoped + deferred. Plan: `~/.claude/plans/modular-kindling-clock.md`.

**Patched in jvto-web (committed)**:
- **Workstream A** — `f8ae382`'s parent + `6587e03`: `src/lib/schemas/entityGraph.ts` FOUNDER_SCHEMA — `jobTitle` array `['Founder', 'Active Tourist Police Officer']` → single string `'Active Tourist Police Officer, Ditpamobvit East Java'`; `alternateName` `'Mr. Sam'` → `['Mr. Sam', 'Bripka Agung Sambuko']`; new `description` field citing SPRIN POLPAR + SPRIN WAL-TRAVEL 2024 + Detik / Radar Jember press. Per [[content/aeo-claims]] §EAV Optimization Notes (lines 230–241) + [[content/brand-voice]] §E-E-A-T Framing (lines 129–142). Founder role preserved via `worksFor: { '@id': ORG_ID }` — no signal lost.
- **Workstream D** — `9c6e58b`: `src/app/(website)/verify-jvto/legal/page.tsx` — new "Operational Continuity" section between Legal Entity Card and SHA-256 Anchors. Two-column grid:
  - Left: Address Anchor — Ijen Bondowoso Homestay → PT continuity at Jl. Khairil Anwar No.102, Bondowoso since 2015; Booking.com 2015 (9.4/10) shipping anchor; Stefan Loose mention. Per [[credentials/legal-licenses]] §Address Continuity (lines 77–87).
  - Right (inset card): Audit Disclosure — legacy NIB `0220001393513` may appear in OSS records; canonical active is `1102230032918`. Legacy NIB NOT added to schema `hasCredential` or `taxID` per [[credentials/legal-licenses]] line 18/84 rule. Page-copy-only disclosure.

**Verification**: Both passes `npm run build` → `✓ Compiled` exit 0. Grep invariants:
- `jobTitle.*Founder` in `src/lib/schemas/` → 0 hits ✓
- `0220001393513` in `src/` → 1 hit (legal page only) ✓ — zero leak into schema files.

**Scoped + deferred (not in this pass)**:
- **Workstream B** (EAV NLP sharpening — health screening + legalName). Surface much bigger than plan estimated: ~20 files across schema builders, hardcoded TSX pages, components, FAQ data + DB-derived snapshot regen. Many "mandatory health" hits already cite BBKSDA SE.1658 (technically compliant with [[content/brand-voice]] voice-invariant). Strict EAV upgrade (add Dr. Irwandanu SIP citation per [[content/aeo-claims]] line 240) needs split execution per file class:
  - B.1: schema builders (1–2 hits, near-canonical, low risk)
  - B.2: hardcoded TSX pages — `verify-jvto/page.tsx:422,712` + `tour-from-{bali,surabaya}/page.tsx` + `tours-from-surabaya/page.tsx:521` + `travel-guide/page.tsx:423` (5 hits)
  - B.3: components — `SafetyOnToursPage.tsx`, `TermsPage.tsx`, `TourRequirements.tsx`, `IjenHealthCertFAQ.tsx`, `TravelGuideTeaser.tsx`, `TravelGuidePage.tsx` (6 hits, includes section headings → visual impact)
  - B.4: FAQ data + constants — `lib/faq-data.ts:88`, `constants.ts:149,182`, `data/knowledge.ts:143,175-176`, `data/faqs.ts:25`, `data.ts:393`
  - B.5: SKIP — `src/data_new.ts` (14 hits, looks legacy/duplicated), `src/lib/publicContent/generated/*.json` (auto-generated; source = DB content_pages.faq + narrative_claims, regen via `scripts/export-public-page-snapshots.mjs`)
  - `legalName` half = no-op; already canonical `'PT Java Volcano Rendezvous'` in all 4 sites (entityGraph, site-config, HomePage component, verify-jvto/page.tsx).
- **Workstream C** (Guardian Archetype + Trust-Pillar Crew Mapping on `/why-jvto/our-story` + `/why-jvto/our-team`). Phase-0 blocker resolved — snapshot script exists at `scripts/export-public-page-snapshots.mjs` and both routes are in scope (lines 30–31). Implementation path: DB row write to `content_pages.content.sections` → `node scripts/export-public-page-snapshots.mjs` → snapshot json regenerates → SSG picks up next build. Source copy verbatim in [[content/copy-bank]] §Guardian Archetype framing + [[people/crew-registry]] §Guardian Mindset / §Trust-Pillar Crew Mapping.

**Live drift (owner adjudication required, NOT in this plan's scope)**:
- `src/lib/schemas/entityGraph.ts:144–154` and `:259–269` currently publish Stefan Loose `isbn: '978-3-7701-7881-0'` + `datePublished: '2018-07-05'`. [[credentials/press-coverage]] flagged this as a do-not-publish contradiction pending physical scan verification (existing wiki: 2016 / 9783770167654). Recommend keeping current published values until owner has the book in hand; do not unilaterally roll back.

**Plan reference**: `~/.claude/plans/modular-kindling-clock.md`

---

## [2026-05-24] sync | wiki SSOT → jvto-web code

**Source type**: Workflow 5 sync pass. Triggered by user request "eksplore llm-wiki untuk dapat di update ke jvto web". Forensic mapping by 2 parallel Explore agents on llm-wiki SSOT + jvto-web claim sites; cross-reference surfaced drift in review counts, foundingDate, and dead duplicate review blocks.

**Drift patched in jvto-web (commit pending)**:
- `src/lib/jvtoReviews.ts` — already canonical (`reviewCount: 51`, verified 2026-05-09). Left as-is; this is now the SOLE hardcoded source for Trustpilot count.
- `src/lib/schemas/entityGraph.ts:35` — `foundingDate: '2016'` → `'2015'` (matches CLAUDE.md + wiki + Booking.com 2015 award).
- `src/lib/site-config.ts` — dead `socialProof`, `reputation`, `reviewPlatforms` blocks DELETED (no consumer in codebase per grep; AggregateRating already flows from `jvtoReviews.ts` via `entityGraph.ts:14`). Replaced with narrow `reviewLinks` (URLs only).
- `src/lib/tourFaqs.ts` — literal `"4.8 ★ across 47+ verified reviews"` → interpolated from `AGGREGATE_RATING.ratingValue` + `AGGREGATE_RATING.reviewCount`. Future wiki ingest now updates one file (`jvtoReviews.ts`) and propagates to all consumers.
- `src/app/(website)/why-jvto/page.tsx:266` — `foundingDate: "2016-01-01"` → `"2015-01-01"`.
- `src/app/(website)/travel-guide/page.tsx:361` — same fix.
- `src/lib/generateFaqSchema.ts:89` — same fix.
- `src/lib/schemas/buildToursHubSchemas.ts:122` — stale doc comment "canonical 47 reviews" → "values sourced from wiki SSOT".

**Verification**: `npm run build` → `✓ Compiled successfully` after each pass. Single-source grep `(reviewCount|count):\s*51\b` returns only `src/lib/jvtoReviews.ts`.

**Not patched (flagged for owner)**:
- `src/lib/publicContent/generated/reviewApiSnapshots.json` — generated artifact, dated 2026-05-08, still holds `"trustpilot": 47`. Should be regenerated by owner's ingest script (do not hand-edit).
- `src/app/(website)/why-jvto/page_ssot.tsx`, `page_old.tsx` — backup clutter files per CLAUDE.md "ignore unless owner asks".
- `site-config.ts` had `tripadvisorRating: 5.0` (wiki = 4.95) — block was deleted entirely (dead code), so no live drift remains.
- Bromo MAGMA Level II Waspada (wiki 2026-05-17) not surfaced on `/destinations/mount-bromo` — content design decision, out of sync scope.
- Crew count audit (wiki = 11) vs DB `crew_members` table — needs DB query, out of scope.

**Plan reference**: `~/.claude/plans/modular-kindling-clock.md`

---

## [2026-05-24] ingest | raw folder — 16 files, 7 source pages, GEO/AEO + Why JVTO architecture

**Source type**: Workflow 4 typed ingest. Profiles: seo-audit (Groups 1–2), web-clip (Groups 3–7).
**Skipped**: `JVTO SEO Audit — Full Site Review.md` (confirmed duplicate of [[sources/seo-audit-2026-05]]); `gemini-code-1779633053483.html` (dev artifact).

**Pages created (9)**:
- [[sources/geo-aeo-strategy-2026-05]] — 4-file GEO/AEO audit synthesis. Digital Trust Fortress 5-component model, AEO per-page targets table, TL;DR HTML + Organization JSON-LD + FAQPage code, confirmed #1 SERP rankings, llms.txt recommendation.
- [[sources/eav-ai-optimization-2026-05]] — 3-file EAV/AI audit synthesis. EAV entity framework (4 entities), 8-layer SSOT→JSON-LD map, NLP sharpening before/after (jobTitle: "Founder" → "Active Tourist Police Officer"), StartLocation as primary discriminator.
- [[sources/seo-ux-integration-2026-05]] — URL governance comparison table (MBA/GA/JVTO), SSOT→DOM SPOF integration, WCAG note, keyword cannibalization gaps, WAF/crawler conflict finding, off-page backlink opportunities.
- [[sources/why-jvto-trust-architecture]] — 4-file Why JVTO trust audit. Hub & spoke URL sitemap (6 URLs), Trust Asset Registry (LEG-001–PRESS-001), new facts: Stefan Loose ISBN/year contradiction, second NIB 0220001393513 flagged, Ijen Bondowoso Homestay → PT entity continuity, Guardian Archetype framing.
- [[sources/digital-trust-fortress-blueprint]] — Next.js full file tree, component registry (AuthorityShield/ForensicGallery/CrewCard/TrustNavigation), /api/verifiable-credentials endpoint, Costly Signals principle for police documents.
- [[sources/crew-strategy-integration-2026-05]] — 7-pillar crew mapping table, crew archetypes (Joyo/Yandi/Fredi/Gufron/Anjas), 4-zone team page structure, Guardian Mindset principle.
- [[sources/competitor-design-analysis-2026-05]] — MBA: Level 1-7 difficulty, 67% CAC reduction/50% RPB increase 2018–2020, Django+React, B-Corp. GA: REST API SSOT, `/trips/[name]/[id]/` ID persistence, looptail brand system.
- [[ops/geo-aeo-strategy]] — NEW ops page. GEO entity architecture, AEO universal rules + per-page targets, EAV principles, confirmed rankings, OTA/App Engine optimization.
- [[ops/why-jvto-architecture]] — NEW ops dev page. URL map with schema injection layers, component registry, data architecture (SSOT JSON), evidence asset structure, 6 trust pillars.

**Pages updated (11)**:
- [[credentials/legal-licenses]] — Added NIB 0220001393513 as historical/legacy with `[stale?]` flag; added Ijen Bondowoso Homestay address continuity note.
- [[credentials/press-coverage]] — Added Stefan Loose second ISBN (978-3-7701-7881-0, DuMont Reiseverlag) and 2018 year; full `> Contradiction` callout (existing wiki: 2016/9783770167654; raw docs: 2018/978-3-7701-7881-0).
- [[credentials/trust-signals]] — Stefan Loose row updated with ⚠ year flag + both ISBNs + link to press-coverage for full details.
- [[ops/seo-strategy]] — Added `## GEO/AEO Extension` section with confirmed #1 rankings, scale pattern, key action, source links.
- [[ops/competitors]] — Added Tier 4 global UX/design benchmarks (MBA + G Adventures) with applicable JVTO patterns table.
- [[content/aeo-claims]] — Added `## EAV Optimization Notes` section: NLP sharpening table (4 attributes), YMYL classification for Ijen C4 claims, updated source links.
- [[content/brand-voice]] — Added `## E-E-A-T Framing` section: 4-dimension table (Experience/Expertise/Authoritativeness/Trustworthiness), "Active Tourist Police Officer" > "Founder" principle.
- [[content/copy-bank]] — Added `## Why JVTO Hub Copy Angles` section: Guardian Archetype quotes, Trust Asset ID table (6 assets), Hub & Spoke URL reference (6 URLs).
- [[people/crew-registry]] — Added `## Guardian Mindset Framing` section + `## Trust-Pillar Crew Mapping` table (7 pillars → crew) + Key Crew Archetypes table (5 entries with DB IDs).
- [[people/agung-sambuko]] — Updated Stefan Loose note with both ISBN/year values + contradiction link; updated Schema `jobTitle` to "Active Tourist Police Officer" (EAV primary value); added Guardian Archetype section with copy-ready quotes.
- [[index]] — Added 7 source entries + 2 ops entries; total_pages 55→64.

**Contradictions flagged**:
- Stefan Loose year/ISBN: wiki says 2016/9783770167654; raw docs say 2018/978-3-7701-7881-0. Full callout in [[credentials/press-coverage]]. Do not publish either ISBN in copy until physical scan verified.
- NIB 0220001393513: possible legacy OSS record. Flagged `[stale?]` in [[credentials/legal-licenses]].

---

## [2026-05-24] ingest | 3D Route Viewer + GeoJSON route data — all 5 destinations

Pages created: [[sources/3d-route-viewer]] (new) — Mapbox 3D fly-through feature reference: viewer URLs for all 5 destinations, full route stats table (length/gain/elevation range/point count), tech stack (Next.js 16, Mapbox GL JS v3, @turf/turf, hand-rolled SVG ElevationChart), data provenance, component paths.

Pages updated (5 destinations): `route_viewer_url` frontmatter added + `3D viewer` row inserted in Trail Data table + `→ [[sources/3d-route-viewer]]` cross-reference appended to: [[destinations/kawah-ijen]], [[destinations/mount-bromo]], [[destinations/madakaripura]], [[destinations/papuma-beach]], [[destinations/tumpak-sewu]].

Pages updated (meta): [[index]] — source entry added, destination descriptions updated with viewer URLs, `total_pages: 50 → 51`, `last_updated: 2026-05-24`.

Data source: `F:/jvto-web/public/routes/index.json` + 5 GeoJSON files (same GPX origin as `raw/*.gpx`). Feature committed on `design/sam` branch (commit `650e70a`).

---

## [2026-05-19] ingest | Teori & Konsep Manajemen Komunikasi

Pages updated: [[sources/comm-management-theory]] (new), [[ops/canned-responses]] (new), [[ops/2026-05-14-whatsapp-operations-playbook]] (BANT + SLA cross-links added), [[index]] (2 entries added).
Key additions: BANT qualification framework adapted for JVTO (N/T/B/A components mapped), MECE chatbot menu design, SFC/FCR principle, SLA benchmarks (WA 2–5 min / email 2–4 hr), ISO 10002 FAQ tracking, GDPR/UU PDP data-request rule, 4-stage pre-booking funnel, 6-stage customer journey. New [[ops/canned-responses]] page: 16 ready-to-use scripts bilingual ID/EN covering Triage, Discovery, Proposal, Urgency/Closing, Post-Booking (H-7, H-1, post-tour review), and 4 objection-handling templates.

---

## [2026-05-18] ingest | Trustpilot full structured catalog — all 49 reviews

Pages updated: [[reviews/trustpilot-all-reviews]] (new), [[reviews/trustpilot-compilation]] (cross-ref added), [[index]] (entry added). Key additions: 49 reviews fully structured with reviewer name, country flag, date, stars, verbatim body, inferred package, guide tags, driver tags. Source: live firecrawl scrape across 3 pages. 2 reviews platform-side without text body not captured. Country breakdown: ID 24, SG 11, US 3, DE 3, GB 2, HK 2, MY 1, AU 1, TH 1, IN 1, PL 1.

---

## [2026-05-18] verify | Trustpilot live scrape — 4.8/51 confirmed

Pages updated: [[reviews/trustpilot-compilation]]. Key additions: live firecrawl scrape confirmed 4.8/51 unchanged. Added rating distribution (94% 5-star, 6% 4-star, 0% other). Added 13 new review excerpts from Jan–Sep 2025 and Jan–May 2026. Updated last_verified to 2026-05-18.

---

## [2026-05-18] health-check | Monthly

**Triggered**: Manual — "run monthly health check"

---

### On-Demand Checks

**Contradiction scan**: 1 contradiction resolved, 2 existing flags confirmed active.

- ✅ **RESOLVED** — `wiki/overview.md` §Packages: "11 from Surabaya" + "Treat 15 as canonical" was stale. Updated to 16 total (12 SUB + 4 Bali) per [[sources/sitemap-2026-05]] (packages-overview.md had already resolved this 2026-05-12). Contradiction note removed.
- ✅ **RESOLVED** — `wiki/overview.md` §Aggregate Rating: "verified 2026-04-19" — updated to 2026-05-18 after live Trustpilot verification.
- ⚠️ **ACTIVE** — `wiki/overview.md` §Trust Pillars line 3: CLAUDE.md says "mandatory Ijen health check" vs SSOT conditional framing. This contradiction predates this audit; flagged in CLAUDE.md §Core differentiators. Content-facing output files use the conditional framing correctly. No fix needed in the wiki page — it exists as documentation of the known gap.
- ⚠️ **ACTIVE** — `output/faq/bromo.md`, `output/aeo/bromo.md`, `output/website/destinations/mount-bromo.md`: Level II Waspada content flagged `[stale?]` — no active update source. Retained; editors to verify before publishing.

**Orphan detection**: 0 orphans across 50 pages ✓

**Stale claim flags**: All 50 wiki pages have `last_updated` 2026-05-11 to 2026-05-18 (max 7 days old). No 90-day stale flags triggered.

**Gap page identification**: Open Gaps in [[index]] — 2 active:
- `bromo-ijen-status-today` — blocked on replacement live PVMBG source
- `content/voice-invariants` — optional; live as section in [[content/brand-voice]] §voice-invariants

---

### Weekly Checks

**30-day stale sweep**: No pages exceed 30 days — all updated within 7 days ✓

**New orphan detection**: 0 orphans ✓ (run above)

**Index completeness**: wiki/ has 50 pages (excl. index, log, overview). All 50 listed in [[index]] ✓

**Log completeness**: All raw/ + Clippings/ files have corresponding ingest entries:
- GPX files (5): `[2026-05-11] ingest | GPX Trail Data` entry ✓
- `routes.csv` + `route_details.csv`: `[2026-05-18] ingest | route-data-csv` ✓
- All other raw/ + Clippings/ files: log entries confirmed ✓

---

### Monthly-Specific Checks

**Credential web-verification**:

| Credential | Method | Result | Action |
|---|---|---|---|
| Trustpilot rating | Playwright live check | **4.8 / 51 reviews** — unchanged from canonical | ✓ No change needed |
| Trustpilot count | Playwright live check | 51 — unchanged | ✓ No change needed |
| Detik article (Polpar) | WebFetch | Title + date confirmed in page metadata (2021-03-14) | ✓ Article live |
| NIB 1102230032918 (OSS) | WebFetch | OSS API endpoint returned 404 | ⚠️ Manual check needed |
| INDECON listing | WebFetch | 403 Forbidden | ⚠️ Manual check needed |
| ISIC Provider 259268 | WebFetch | Page live but provider listing truncated | ⚠️ Manual check needed (suggest Playwright) |

**Trustpilot new review sweep**: 51 reviews — no new reviews since last ingest (2026-05-09). No action needed.

**Gap page audit**: See Open Gaps above. All previously open gaps resolved except `bromo-ijen-status-today` (source-blocked) and `content/voice-invariants` (optional).

**Output staleness**: No output files with dates in filenames >90 days. All output dated 2026-05-12 to 2026-05-18 ✓

---

### Summary

| Check | Status |
|---|---|
| Contradictions | 2 resolved; 2 known active (documented) |
| Orphans | 0 ✓ |
| Stale pages | 0 (all within 7 days) ✓ |
| Index completeness | 50/50 ✓ |
| Log completeness | All raw files covered ✓ |
| Trustpilot live | 4.8/51 unchanged ✓ |
| NIB web-check | Cannot verify via web (OSS 404) — manual check needed |
| INDECON web-check | 403 — manual check needed |
| ISIC web-check | Incomplete — manual check recommended |
| New Trustpilot reviews | None since 2026-05-09 ✓ |
| Output staleness | 0 files >90 days ✓ |

**Pages updated by this health check**: [[overview]] (package count corrected 15→16, rating verification date updated)

---

## [2026-05-18] ingest | route-data-csv — 43-route segment library

**Source type**: ssot-update (CSV supplements db-export-2026-05)
**Raw files**: `raw/routes.csv` (43 routes, id 1–45 excl. 13+18) + `raw/route_details.csv` (217 activity rows, 42 of 43 routes have detail)

**Key findings**:
- 43 named day-segments covering all journey origins (SUB, Bali, Bromo, Ijen, Jember, Malang, Tumpak Sewu area)
- Each route maps to one day/leg of a multi-day package; canonical packages are assembled from 2–6 routes
- Route 8 (SUB-YOGYA) has no timed detail rows
- Routes 7, 8, 16, 30 appear to be optional add-ons not in any SSOT 16 canonical packages
- Schema.org `type` values in route_details (`TravelAction`/`TouristAttractionVisit`/`CheckInAction`) are ready for JSON-LD itinerary expansion

**Pages created (1)**:
- [[sources/route-data-csv]] — Full 43-route index, structure documentation, usage status table, relationship to db-export-2026-05

**Pages updated (2)**:
- [[index]] — New source entry; CSV open gap resolved; total_pages 49→50
- [[log]] — This entry

---

## [2026-05-18] ingest + schema | taman-safari-prigen-bromo-madakaripura-3d2n itinerary

**Source type**: implicit ssot-update (CSV supplements db-export-2026-05)
**Raw files used**: `raw/routes.csv` route 6 (SUB-SAFARI-BROMO, Day 1 detail) + `raw/route_details.csv` route_id=6 (timed activity breakdown) + `raw/routes.csv` route 20 (BROMO-MADAKARIPURA-SUB, Day 3 pattern)

**Itinerary structure confirmed**:
- Day 1: Surabaya → Taman Safari Prigen (safari adventure, ~2.5h) → Bromo area overnight (Night 1 = Joglo Kecombrang Bromo)
- Day 2: Bromo sunrise sequence (01:00-02:00 departure, Penanjakan, Sea of Sand, crater) → second overnight (Night 2 = Joglo Kecombrang Bromo)
- Day 3: Madakaripura Waterfall canyon trek → return to Surabaya
- Meals: B · — · — (Day 1), B (Day 2), B (Day 3). Lunch at Safari area = own expense.

**Pages updated (2)**:
- [[products/packages-itineraries]] — New `taman-safari-prigen-bromo-madakaripura-3d2n` section added between `bromo-2d1n` and `ijen-2d1n`; sourced from CSV routes
- [[products/packages-overview]] — Package 12 note updated: "itinerary not yet ingested" removed, links to itineraries + pricing pages added

**Schema regenerated (1)**:
- `output/schema/taman-safari-prigen-bromo-madakaripura-3d2n-schema.json` — Stub replaced with full TouristTrip (3-day itinerary detail) + FAQPage (5 Q&As). Receipt updated.
- **3 pricing corrections** (stub had wrong mid-tier values vs canonical):
  - 3 pax: 4,100,000 → **4,150,000**
  - 4–5 pax: 3,850,000 → **3,950,000**
  - 6–7 pax: 3,700,000 → **3,750,000**
  - 2 pax, 8-10 pax, 11+ pax: already correct

---

## [2026-05-18] schema | TouristAttraction + BreadcrumbList — all 5 destinations

**Profile**: schema (Workflow 5)

**Output files generated (10)**:
- `output/schema/ijen-crater-schema.json` + `.receipt.md`
- `output/schema/mount-bromo-schema.json` + `.receipt.md`
- `output/schema/tumpak-sewu-waterfall-schema.json` + `.receipt.md`
- `output/schema/madakaripura-waterfall-schema.json` + `.receipt.md`
- `output/schema/papuma-beach-schema.json` + `.receipt.md`

**Each file contains**: `[TouristAttraction, BreadcrumbList]` — two schema objects per destination page.

**Geo data source**: bbox center coordinates computed from GPX bounding boxes in each destination wiki page.

**Verification**: No reviewCount/ratingValue in TouristAttraction schemas (those belong on TouristTrip tour pages only). NIB `1102230032918` used as `provider.identifier` in all 5. All geo/locality values traced to destinations/*.md.

**Wiki page created (1)**:
- [[content/schema-templates]] — JSON-LD reference page (page-type → schema map, field rules, verification checklist). Fills the "to be created" gap flagged in [[sources/seo-audit-2026-05]].

**Pages updated (2)**:
- [[index]] — Added schema-templates to Content Production section; marked schema-templates gap as resolved; total_pages 48→49
- [[log]] — This entry

**FAQPage verification** (from this session): Existing TouristTrip schemas contain properly structured FAQPage arrays (Question/acceptedAnswer/Answer pattern, mainEntity array, minimum 4 Q&As per page) ✓

**Schema inventory after this session**:
- TouristTrip + FAQPage: 16/16 ✓
- Organization (homepage): 1/1 ✓
- TouristAttraction + BreadcrumbList: 5/5 ✓
- `taman-safari-prigen-bromo-madakaripura-3d2n` TouristTrip: stub (itinerary not yet ingested)
- BreadcrumbList for tour pages: included in TouristTrip schema files ✓

---

## [2026-05-18] cleanup | MAGMA removal + repo hygiene pass

**Trigger**: MAGMA feed permanently removed. Full repo cleanup to remove active workflow dependencies.

**Files changed (9)**:
- [[ops/ingestion-profiles]] — Removed `magma-report` profile (6 profiles remain: web-clip, pdf-doc, ssot-update, review-feed, press-clip, seo-audit)
- [[index]] — Removed `magma-report` from ingestion-profiles description; added 4 Open Gaps entries (schema-templates, bromo-ijen-status-today, CSV files)
- [[ops/seo-strategy]] — Replaced 2 MAGMA-as-source refs: `bromo-ijen-status-today` now noted as "needs replacement live source"
- [[sources/seo-audit-2026-05]] — Same replacement (1 ref)
- `output/faq/bromo.md` — Added top-level `[stale?]` warning for Level II Waspada data
- `output/aeo/bromo.md` — Added `[stale?]` markers on 2 status Q&A blocks
- `output/website/destinations/mount-bromo.md` — Converted alert section to conditional block; removed "Source: MAGMA Indonesia" attribution
- `.claude/settings.local.json` — Added 2 allowlist entries (committed separately)
- `output/website/tours/surabaya/ijen-2d1n.md` — BOM removal (committed separately)

**Skill updated (outside repo)**:
- `.claude/skills/jvto-verified-output/SKILL.md` — Volcano row now points to `destinations/*.md` instead of deleted `wiki/ops/volcano-status.md`

**Dead references confirmed resolved**:
- `[[ops/volcano-status]]` referenced in log entries below — that page was deleted in prior commit `a416d86`. Log entries are historical (append-only); dead wikilinks in log are acceptable.
- `magma-report` profile — removed from all active workflow docs

**Not changed (intentional)**:
- Schema JSON `"JVTO monitors MAGMA Indonesia / PVMBG"` — factual operational claim, NOT a workflow dependency. Kept.
- `output/INDEX.md` line 182 stale-resolved note — harmless historical marker. Kept.

**Raw files needs-review**:
- `raw/routes.csv` + `raw/route_details.csv` — unclassified; may overlap with db-export-2026-05. Added to Open Gaps.
- GPX files — already integrated inline in destination pages. No source pages required.

---

## [2026-05-18] output | bulk compilation — 4 profiles, all missing gaps filled

Profiles: website-copy, social, aeo, faq. Parallel 4-agent run. All files pass voice-invariant verification (0 violations).

**website-copy:**
- `output/website/destinations/mount-bromo.md` refreshed with Level II Waspada framing (1km exclusion zone, Penanjakan unaffected). Sources: mount-bromo, copy-bank, brand-voice, packages-overview, operational-facts.

**social (first output ever for this profile):**
- `output/social/batch-2026-05-18.md` — 10 posts, 14 caption units. Topics: C1–C9 differentiators (police, medical screening, reviews, Ijen, Bromo, pricing, founding story, private tours, Tumpak Sewu, Madakaripura). Platforms: Instagram + Twitter/X. Sources: brand-voice, copy-bank, trustpilot-compilation, agung-sambuko, police-integration, medical-screening.

**aeo (per-destination — first output for this sub-type):**
- `output/aeo/ijen.md` — 12 Q&A blocks. 4E Ijen conditional: PASS.
- `output/aeo/bromo.md` — 11 Q&A blocks. Level II Waspada reflected.
- `output/aeo/tumpak-sewu.md` — 10 Q&A blocks.
- `output/aeo/madakaripura.md` — 10 Q&A blocks.
- `output/aeo/papuma.md` — 10 Q&A blocks.
Sources: aeo-claims, faq-master, legal-licenses, trust-signals, destinations/*.

**faq:**
- `output/faq/papuma.md` new — 12 Q&As. ⚠ Pricing figures need verification vs packages-full-pricing.md before publishing.
- `output/faq/bromo.md` refreshed — 20 Q&As (was 53 words stale). Level II Waspada dedicated Q&As added. Sources: faq-master, mount-bromo, operational-facts, packages-overview, brand-voice.

Voice invariant verification: PASS across all 8 new/refreshed files (0 total violations).
Output INDEX updated. Missing Outputs section resolved for AEO per-destination and Social profile.

## [2026-05-17] fix | stale output files — Level II Waspada update

**Trigger**: Two output files flagged stale after MAGMA report ingest (2026-05-16) — crater-access copy pre-dated Level II restriction.

**Files updated (2)**:
- `output/faq/bromo.md` — Added Level II status banner; updated "Can I ride a horse to the Bromo crater rim?", "What is at the Bromo crater?", and "What happens if Mount Bromo closes for volcanic activity?" to reflect 1 km exclusion zone and active Plan-B.
- `output/website/destinations/mount-bromo.md` — Added `Alert Status Banner` section to data structure spec (conditional: Level II+); added crater restriction note to Crater Walk section; updated Closure & Plan B condition from manual flag to `alert_level >= 2`.

**Also committed**: `output/website/travel-guide/bromo-ijen-status-today.md` (generated in previous session, was untracked); deleted `llm-wiki/.obsidian/` artifact files (empty Obsidian default vault).

---

## [2026-05-17] output | bromo-ijen-status-today travel guide page

**Profile**: website-copy (Style B)
**Output file**: `output/website/travel-guide/bromo-ijen-status-today.md`
**SEO target**: keyword #7 "is bromo open today" / "bromo status" (500–2,000/mo)
**Sources drawn**: [[ops/volcano-status]], [[destinations/mount-bromo]], [[destinations/kawah-ijen]], [[content/brand-voice]], [[content/operational-facts]]

**Content**: Current status table (Bromo Level II Waspada, Ijen Level I Normal), per-zone access breakdown, 4-level alert reference, Plan-B and Travel Credit guidance, update cadence note, official MAGMA source link.

**Maintenance note**: Re-generate this file after each MAGMA report ingest. See [[ops/volcano-status]] Update Instructions.

Also deleted `llm-wiki/llm-wiki/` — empty Obsidian default vault (Welcome.md artifact, no JVTO content).

---

## [2026-05-17] ingest | SEO Audit 2026-05-17 + Schema Profile + Trust Signals Update

**Source type**: seo-audit (new Workflow 4 profile — see [[ops/ingestion-profiles]])
**Raw file**: `Uploads/c2bb0489-jvtoseoaudit20260517.md`
**Scope**: Full site SEO audit — technical, on-page, schema, keywords, competitors, content gaps, action plan

**Pages created (4)**:
- [[sources/seo-audit-2026-05]] — Source summary: critical findings, data discrepancies (D1–D5), schema requirements, quick-win references
- [[ops/seo-strategy]] — 15 keyword targets, 4 content silos with readiness map, title tag rewrites (10 pages), QW action tracker (14 items), 90-day targets
- [[ops/competitors]] — 3-tier competitor registry (OTAs + 3 dominant + 7 mid-tier + 9 EMD), JVTO differentiator map, monitoring protocol
- [[ops/redirect-map]] — 13 legacy → SSOT URL redirect table; subdomain decisions; implementation notes for dev

**Pages updated (6)**:
- [[credentials/trust-signals]] — Fixed stale Trustpilot count (47→51); added social media URL registry (Facebook, Instagram, Twitter, 8 platforms total); added Schema Canonical Values section; added seo-audit-2026-05 to sources
- [[content/brand-voice]] — Added Meta Description Formula section (3-part structure, examples, rules); added seo-audit-2026-05 to sources
- [[ops/compilation-profiles]] — Added `schema` profile (6th profile: generates JSON-LD, mandatory numeric verification step, 5 output types); added meta description formula cross-reference to website-copy profile
- [[ops/ingestion-profiles]] — Added `seo-audit` profile spec (extraction targets: keywords, competitors, schema, action items)
- [[index]] — Added 4 new pages (sources + 3 ops); updated ops section with all 7 profiles; total_pages 46→49
- [[log]] — This entry

**Data discrepancies resolved**:
- D1: `reviewCount: 47` in audit TouristTrip example → wiki canonical is 51 (trust-signals updated, schema profile warns against hardcoding)
- D2: Ambiguous `ratingValue: 4.9` → schema canonical values section establishes Trustpilot 4.8 as conservative cross-platform value
- D3: Package count 15 vs 16 → will resolve in favor of 16 (sitemap-confirmed) on next SSOT update
- D4: Placeholder INDECON URL → schema profile directs to legal-licenses for the verified URL

**Key insight**: Bromo Level II status (from Step 0) is the live data feed for Silo 3's `bromo-ijen-status-today` page — the audit identified this as a high-value opportunity and JVTO already has the source infrastructure for it.

---

## [2026-05-17] ingest | MAGMA Volcano Activity Reports — Bromo & Ijen (2026-05-16)

**Source type**: magma-report (new Workflow 4 profile — see [[ops/ingestion-profiles]])
**Raw files**: `Clippings/Laporan Aktivitas Gunung Api - Bromo, Sabtu - 16 Mei 2026...md` + `Clippings/Laporan Aktivitas Gunung Api - Ijen, Sabtu - 16 Mei 2026...md`
**Source**: MAGMA Indonesia (magma.esdm.go.id), PVMBG/ESDM government service

**Status summary**:
- **Gunung Bromo**: Level II Waspada — 1km crater exclusion zone, phreatic eruption risk, gas plume 50–600m. Seismicity: continuous tremor (0.5–1mm). Penanjakan and sea-of-sand approach unaffected.
- **Kawah Ijen**: Level I Normal — standard operations. Thin gas 50–100m. Shallow volcanic quakes + tremor (baseline hydrothermal). Health-screening coordination per SE.1658/KSA.9/2024 applies as usual.

**Pages created (1)**:
- [[ops/volcano-status]] — Live status tracker for both volcanoes; alert levels, exclusion zones, operational implications, update instructions

**Pages updated (5)**:
- [[destinations/mount-bromo]] — Added `## Current Status` section (Level II, 1km exclusion); updated sources + last_updated
- [[destinations/kawah-ijen]] — Added `## Current Status` section (Level I, standard ops); updated sources + last_updated
- [[content/operational-facts]] — Added `## Current Volcano Alert Levels` table; updated sources + last_updated
- [[ops/ingestion-profiles]] — Added `magma-report` and `seo-audit` profile specs
- [[index]] — Added volcano-status page to Ops section; ingestion-profiles updated to list 7 profiles; total_pages 45→46

**Output files flagged as stale (2)**:
- `output/website/destinations/mount-bromo.md` → stale (crater-access copy pre-dates Level II)
- `output/faq/bromo.md` → stale (crater-access FAQ pre-dates Level II 1km restriction)

---

## [2026-05-16] fix | G1 navigation gap resolved

**Trigger**: health check G1 flag — `products/packages-overview` had no in-body forward link to `products/packages-itineraries` (link to `packages-full-pricing` was already present at line 109).

**Pages updated (1)**:
- [[products/packages-overview]] — added "Day-by-day itineraries for all packages: see [[products/packages-itineraries]]" immediately after the existing full-pricing reference. Both detail pages now linked from the body, not just the footer.

**G1 status**: resolved ✅

---

## [2026-05-16] health-check | Monthly (1st run)

**Vault state**: 45 wiki pages · 16 raw files · first monthly run

---

### Weekly Checks (carried from 2nd weekly run)

All 8 weekly checks PASS — see [2026-05-16] health-check | Weekly (2nd run).

---

### Monthly Check 1 — Credential Web Verification

| Credential | Method | Result |
|---|---|---|
| **Trustpilot 4.8/51** | Fetched JVTO homepage widget | **4.8/5 · 51 reviews** — matches wiki canonical exactly ✅ |
| **Bripka Agung Sambuko Polpar** | Fetched Detik.com article (2021-03-14) | Article live, Bripka Agung Sambuko named as active Tourist Police officer, verbatim quotes present ✅ |
| **NIB 1102230032918 (OSS)** | PDF dokumen OSS resmi (`f:\S22\Download\NIB.pdf`, dicetak 11 Feb 2023) | **CONFIRMED** ✅ — Nama, alamat, tanggal terbit, dan KBLI semua match wiki canonical. |

**NIB verification detail** (sumber: PDF OSS resmi, ditandatangani elektronik BSrE-BSSN):

| Field | PDF | Wiki | ✓ |
|---|---|---|---|
| NIB | 1102230032918 | 1102230032918 | ✅ |
| Nama | PT JAVA VOLCANO RENDEZVOUS | PT Java Volcano Rendezvous | ✅ |
| Alamat | Jl. Khairil Anwar 102 A, Badean, Bondowoso 68214 | Jl. Khairil Anwar No.102 A, Badean, Bondowoso | ✅ |
| Terbit | 11 Februari 2023 | 2023-02-11 | ✅ |
| KBLI 79911 (Jasa Informasi Pariwisata) | NIB Terbit, Rendah | Tercatat | ✅ |
| KBLI 62019 (Pemrograman Komputer) | NIB Terbit, Rendah | Tercatat | ✅ |
| KBLI 79121 (Biro Perjalanan Wisata) | NIB Terbit + Sertifikat Standar, Menengah Rendah | Tercatat | ✅ |

> Minor observation: PDF OSS mencantumkan 3 KBLI; wiki mencatat 5 (+ 79120, 79921). KBLI tambahan mungkin dari registrasi terpisah — tidak ada konflik.

**Net result**: 3/3 verified ✅

---

### Monthly Check 2 — Trustpilot New Review Sweep

- **Wiki canonical**: 51 reviews, 4.8/5 (verified 2026-05-09, 7 days ago)
- **Live count (JVTO homepage widget)**: 51 reviews, 4.8/5
- **Delta**: 0 new reviews since last ingest
- **Threshold**: >2 new reviews required to flag for ingestion

**PASS** ✅ — no new reviews to ingest.

---

### Monthly Check 3 — Gap Page Audit

| Gap | Status |
|---|---|
| `credentials/medical-screening` | ✅ Created 2026-05-16 |
| `credentials/police-integration` | ✅ Created 2026-05-16 |
| `credentials/press-coverage` | ✅ Created 2026-05-16 |
| `content/voice-invariants` | ⏸ Intentionally deferred — canonical in [[content/brand-voice]] |

No unfilled gaps remain. **PASS** ✅

---

### Monthly Check 4 — Output Staleness (>90 days)

Phase 2 (2026-05-16) removed all date-based filenames from `output/`. Files now carry `output_date:` in frontmatter only.

| output_date value | File count | Age | Status |
|---|---:|---|---|
| `2026-05-16` | 13 files | 0 days | ✅ Current |
| `2026-05-12` | 46 files | 4 days | ✅ Current |

No output file exceeds 90 days. **PASS** ✅

---

### Summary

| Check | Result | Notes |
|---|---|---|
| All 8 weekly checks | ✅ PASS | Carried forward |
| Trustpilot web-check | ✅ PASS | 4.8/51 confirmed live |
| Polpar status web-check | ✅ PASS | Detik.com article live, name confirmed |
| NIB OSS web-check | ✅ PASS | PDF OSS resmi diverifikasi — semua data match |
| Trustpilot new review sweep | ✅ PASS | 0 new reviews (delta below threshold) |
| Gap page audit | ✅ PASS | All 3 credential gaps resolved |
| Output staleness (>90 days) | ✅ PASS | Newest: 0 days, oldest: 4 days |

**Semua checks PASS. Tidak ada action item outstanding.**

---

## [2026-05-16] health-check | Weekly (2nd run)

**Vault state**: 45 wiki pages · 16 raw files

### On-Demand Checks (carried from 3rd on-demand run)

| Check | Result |
|---|---|
| Contradiction scan | ✅ PASS |
| Orphan detection | ✅ PASS — zero true orphans |
| Stale claims (>90 days) | ✅ PASS |
| Gap page identification | ✅ PASS |

### Weekly Check 1 — 30-Day Stale Sweep

No `last_updated` date outside the 2026-05 range found across all 47 files. All pages between 2026-05-11 and 2026-05-16. **PASS** ✅

### Weekly Check 2 — New Orphan Detection

`git log --diff-filter=A` confirms zero new wiki pages created since the last log entry ([2026-05-16] health-check | On-Demand 3rd run). **PASS** ✅

### Weekly Check 3 — Index Completeness

`find wiki/ -name "*.md"` → 45 content pages (47 total - index.md - log.md). `comm -23` against index.md wikilinks → zero files missing from index. **PASS** ✅

### Weekly Check 4 — Log Completeness

16/16 raw files confirmed with log entries (slug grep against log.md). **PASS** ✅

### Summary

| Check | Result | Action |
|---|---|---|
| Contradiction scan | ✅ PASS | None |
| Orphan detection | ✅ PASS | None |
| Stale claims (>90 days) | ✅ PASS | None |
| Gap page identification | ✅ PASS | None |
| 30-day stale sweep | ✅ PASS | None |
| New orphan detection | ✅ PASS | None |
| Index completeness | ✅ PASS (45 pages) | None |
| Log completeness | ✅ PASS (16/16) | None |

**No pages modified. Vault is clean.**

---

## [2026-05-16] health-check | On-Demand (3rd run)

**Vault state**: 45 wiki pages · 16 raw files · session end-of-day check

| Check | Result | Notes |
|---|---|---|
| Contradiction scan | ✅ PASS | No new contradictions. Pre-existing blocks (founding date, package count, review count, mandatory-screening framing) all correctly documented. |
| Orphan detection | ✅ PASS | Zero true orphans. Low-count pages (llm-kb-tooling-guide=2, ops cluster=3 each) all confirmed linked from content pages. |
| Stale claims (>90 days) | ✅ PASS | All 47 files last_updated 2026-05-11 → 2026-05-16. Max age: 5 days. |
| Gap page identification | ✅ PASS | All 3 credential gaps resolved. `content/voice-invariants` remains deferred (intentional). No new gaps. |
| Index completeness | ✅ PASS | 47 files = 45 pages + index + log. `total_pages: 45` ✓ |
| Raw/log completeness | ✅ PASS | 16/16 raw files have log entries (confirmed from weekly check). |

**No pages modified. Vault is clean.**

---

## [2026-05-16] output | 9 output files refreshed — secondary wave

**Trigger**: user request to update all output files not yet updated.

**Triage result**: 55 files at 2026-05-12 audited. 9 had meaningful new content from 2026-05-16 wiki changes. 46 files (tour pages ×16, policy ×4, FAQ bromo/madakaripura/tumpak-sewu ×3, non-Ijen destinations ×4, misc) had no material source changes — left untouched.

**Files updated (9)**:

| File | What was added |
|---|---|
| `website/verify-jvto/hub.md` | Health Screening sub-section added (pointer to /travel-guide/ijen-health-screening); sources updated |
| `website/verify-jvto/legal.md` | Image column added to SHA-256 table (7 document image URLs: NIB, TDUP, HPWKI, SPRIN ×2, Press ×2); sources updated |
| `website/verify-jvto/history-artifacts.md` | Asset slug references replaced with live image URLs (Booking.com plaque + label, Stefan Loose page + crop + Mr. Sam photo); sources updated |
| `website/destinations/ijen-crater.md` | Health Screening schema updated: doctor reference now links to /travel-guide/ijen-health-screening; `credentials/medical-screening` added to sources |
| `website/why-jvto/our-story.md` | Asset slug references replaced with live image URLs (Booking.com, Stefan Loose, founder-with-guests); sources updated |
| `website/why-jvto/the-jvto-difference.md` | SPRIN document image URLs added inline; section 4 now links to /travel-guide/ijen-health-screening; sources updated |
| `website/travel-guide/police-escort-for-groups.md` | Police Escort Photos section added (3 image URLs: day/night escort, vehicle); sources updated |
| `aeo/why-jvto.md` | Sources updated to include credentials/police-integration, credentials/press-coverage, credentials/medical-screening |
| `faq/ijen.md` | Sources updated to include credentials/medical-screening |

**output/INDEX.md**: output_date updated for all 9 files (2026-05-12 → 2026-05-16).

---

## [2026-05-16] output | 4 stale output files refreshed

**Trigger**: user request after Phase 2 identified 4 stale candidates in INDEX.md.

**Files updated (4)**:

| File | What was added |
|---|---|
| `output/website/travel-guide/ijen-health-screening.md` | Partner facilities table (Klinik Bakti Husada, Puskesmas Licin, hotel session); digital system URL (health.mountijen.com); 6 screening photo URLs; sources updated to include `credentials/medical-screening` |
| `output/website/verify-jvto/police-safety.md` | Image URLs for SPRIN POLPAR + SPRIN WAL-TRAVEL (PNG/WebP); field operations photos section (5 images: 2 escort, vehicle, Geopark briefing, Baratha Hotel); sources updated to include `credentials/police-integration` |
| `output/website/verify-jvto/press-recognition.md` | Screenshot column added to press table (3 URLs); entity linking paragraph; historical recognition table expanded with 5 image URLs; sources updated to include `credentials/press-coverage` |
| `output/website/why-jvto/our-team.md` | Portrait URL added to all 11 crew members; KTA card URL added to 5 KTA-credentialed guides (Anjas, Taufik, Rendi, Kiki, Gufron); sources updated to include `sources/ssot-image-asset-map` |

**output/INDEX.md updated**: output_date 2026-05-12 → 2026-05-16 for all 4 files; stale candidates note resolved.

---

## [2026-05-16] ops | output/ Phase 2 — rename, frontmatter, INDEX.md

**Trigger**: user request (Phase 2 after Option B reorganisation).

**Changes**:

1. **58 files renamed** — date stripped from all filenames; redundant section prefix/suffix stripped; hub pages renamed to `hub.md`:
   - `aeo-YYYY-MM-DD-*` → `*` (2 files)
   - `faq-YYYY-MM-DD-*` → `*` (4 files)
   - `copy-YYYY-MM-DD-*` → `*` (52 files, with section prefix + origin suffix removed where folder already encodes that info)

2. **Frontmatter standardised** across all 59 non-archive files:
   - `generated:` → `output_date:` (8 files: all aeo/, faq/, landing pages)
   - `status: draft` added to all files that lacked it (59 files)

3. **`output/INDEX.md` created** — master map of all 59 output files → URL → output_date → status. Includes "Missing Outputs" section flagging: AEO per destination, social posts, slide decks, and 4 stale candidates (outputs pre-dating 2026-05-16 wiki updates to medical-screening, police-integration, press-coverage, crew-registry image assets).

**Net result**: output/ folder is now navigable by folder, searchable by URL slug, and status-trackable via frontmatter grep.

---

## [2026-05-16] ops | output/ folder reorganisation — incremental (Option B)

**Trigger**: user request after output folder analysis.

**What changed**: 60 output files moved from flat root into subfolders mirroring website structure. No files renamed, no content modified.

**New structure**:

```
output/
  _archive/   (2)  — legacy pre-convention files, superseded
  aeo/        (2)  — AEO Q&A block outputs
  faq/        (4)  — FAQ per destination
  website/    (7)  — sitewide & misc (homepage, landings, blog, contact, tours hub, isic)
    destinations/  (6)  — hub + 5 destination pages
    tours/
      surabaya/   (12)  — all 12 Surabaya tour pages
      bali/        (4)  — all 4 Bali tour pages
    travel-guide/  (9)  — hub + 8 travel guide sub-pages
    why-jvto/      (6)  — hub + 5 why-jvto sub-pages
    verify-jvto/   (5)  — hub + 4 verify-jvto sub-pages
    policy/        (4)  — hub + 3 policy pages
```

**Pain points identified but deferred** (Phase 2 optimizations):
- Tanggal di filename (akan dihapus batch berikutnya — tanggal ke frontmatter saja)
- `status` frontmatter field (`draft | reviewed | published | stale`) belum ditambahkan
- `output/INDEX.md` mapping file → URL → wiki sources → status belum dibuat
- Staleness check di Workflow 6 (flag output yang source wiki-nya sudah diupdate) belum diimplementasi

---

## [2026-05-16] health-check | Weekly

**Vault state**: 45 wiki pages · 16 raw files · last weekly: first run

---

### On-Demand Checks (carried from 2nd on-demand run, same session)

| Check | Result |
|---|---|
| Contradiction scan | ✅ PASS |
| Orphan detection | ✅ PASS — zero true orphans |
| Stale claims (>90 days) | ✅ PASS — oldest page: 2026-05-11 (5 days) |
| Gap page identification | ✅ PASS — all gaps resolved |

---

### Weekly Check 1 — 30-Day Stale Sweep

All 45 wiki pages have `last_updated` between 2026-05-11 and 2026-05-16. No page or its sourcing page exceeds the 30-day threshold. Canonical Trustpilot count (51 reviews, verified 2026-05-09) sourced from `sources/trustpilot-reviews-2026.md` (last_updated: 2026-05-11 — 5 days old).

**PASS** ✅

---

### Weekly Check 2 — New Orphan Detection

Pages created since the last log entry ([2026-05-16] fix | G1 navigation gap resolved):
- None — G1 fix was an edit to an existing page only.

Pages created earlier today, all confirmed with strong inbound links:

| Page | Inbound count (non-index/log) |
|---|---|
| [[sources/ssot-image-asset-map]] | 11 |
| [[credentials/press-coverage]] | 8 |
| [[credentials/medical-screening]] | 8 |
| [[credentials/police-integration]] | 8 |

**PASS** ✅

---

### Weekly Check 3 — Index Completeness

**Method**: `find wiki/ -name "*.md"` → 47 files. Excluding `index.md` and `log.md` → 45 content pages. `index.md` `total_pages: 45`. ✓

Cross-reference verified manually against index sections:
- Sources (13) · Destinations (5) · Products (3) · People (3) · Credentials (5) · Reviews (3) · Content (7) · Ops (5) · Root infrastructure (overview + index + log = 3)
- Total: 13+5+3+3+5+3+7+5+3 = **47 files = 45 pages + index + log** ✓

> Note: automated `comm` diff produced false positives — some pages are wikilinked twice in index.md (once in frontmatter `sources:` list, once in body), causing them to appear in "in index but not in wiki." Root-level pages (overview) lack a subfolder prefix and don't match the grep pattern. Both are tooling artefacts; no real gaps exist.

**PASS** ✅

---

### Weekly Check 4 — Log Completeness

16 raw files audited — all confirmed with log entries:

| Raw file | Log entry |
|---|---|
| `Tourist Police-Led Private Volcano Tours in East Java.md` | [2026-05-11] init ✓ |
| `JVTO_FINAL_CLEAN_SSOT.json` | [2026-05-11] ingest \| SSOT v6.0 ✓ |
| `Air_Terjun_Tumpak_Sewu.gpx` · `Gunung_Bromo.gpx` · `Kawah_Ijen_Volcano.gpx` · `Madakaripura_Waterfalls.gpx` · `Pantai_dan_Tanjung_Papuma.gpx` | [2026-05-11] ingest \| GPX Trail Data ✓ |
| `llm-kb-tooling-guide.md` | [2026-05-11] ingest \| LLM KB Tooling Guide ✓ |
| `JVTO_Policy_Pack_REVISED_v6_2026-01-26_3POLICIES_ONLY.md` | [2026-05-12] ingest \| JVTO Policy Pack ✓ |
| `JVTO_Travel_Guide_PUBLISHABLE_EN_2026-01-18.md` + `JVTO_Travel_Guide_SSOT_EN.json` | [2026-05-12] ingest \| JVTO Travel Guide EN ✓ |
| `db_export_raw.json` | [2026-05-12] ingest \| DB Export ✓ |
| `sitemap.xml` | [2026-05-12] ingest \| JVTO Website Sitemap ✓ |
| `JVTO SSOT Image Asset Map.md` · `JVTO SSOT Image Inventory.md` · `jvto_image_asset_map.json` | [2026-05-16] ingest \| JVTO Image Asset Map ✓ |

**PASS** ✅

---

### Summary

| Check | Result | Action taken |
|---|---|---|
| Contradiction scan | ✅ PASS | None |
| Orphan detection | ✅ PASS | None |
| Stale claims (>90 days) | ✅ PASS | None |
| Gap page identification | ✅ PASS | None |
| 30-day stale sweep | ✅ PASS | None |
| New orphan detection | ✅ PASS | None |
| Index completeness | ✅ PASS (45 pages, 47 files) | None |
| Log completeness | ✅ PASS (16/16 raw files) | None |

**No pages modified by this health check. Vault is clean.**

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

## [2026-05-26] ingest | JVTO Verification Dossier + Ijen Safety Protocol

Sources ingested: 2 files from raw/
- `JVTO_Verification_Dossier.pdf` (R060) — 14-page NotebookLM dossier, AI-generated (weight 8)
- `Operational Safety Management Protocol...md` (R061) — 7-section Ijen safety protocol, AI-generated (weight 8)

Pages created (2): sources/jvto-verification-dossier, sources/ijen-safety-protocol

Pages updated (3):
- credentials/legal-licenses — added AHU-0023020 (Company Registry number)
- destinations/kawah-ijen — added Emergency & Evacuation section (Lamborghini trolley, SAR protocol, Sengkan Gandrung braking zone, TWA Call Center)
- website/operational-facts — added TWA Call Center contact, Ijen Rijik cleanup volume (100-150kg/month) + Cemara Gunung planting

Manifests updated: raw-files-index (+2), ingest-status (+2), evidence-registry (+E017, E018), conflict-log (CONF-001 updated with dossier Stefan Loose "Year: 2018"), recommendation-log (+REC-010 Buleleng Hiace verification)

Key notes: Both files are AI-generated (NotebookLM, evidence weight 8). Most content corroborates existing wiki. New verifiable fact: AHU-0023020. Unverified item: "Buleleng Hiace Fatality" transit incident — needs Sam confirmation (REC-010).

---

## [2026-05-26] ingest | Ijen Safety Resource Mapping + Tourist Accidents

Sources ingested: 2 Excel files from raw/
- `Mount Ijen Safety and Support Resource Mapping.xlsx` (R058) — 5 safety categories, 14 source references
- `Tourist Accidents at Kawah Ijen and Surrounding Areas.xlsx` (R059) — 7 incidents (2015–2026), 4 fatalities

Pages created (2): sources/ijen-safety-resource-mapping, sources/ijen-tourist-accidents

Pages updated (3):
- destinations/kawah-ijen — added Safety Incidents & Restricted Zones section (Hutan Mati, 500m radius, red flags, incident summary table)
- credentials/medical-screening — added Incident Data section (50% of fatalities fitness-related → validates health screening)
- website/operational-facts — enhanced Ijen Closure with Ijen Rijik program name + March 2019 establishment date

Manifests updated: raw-files-index (+2), ingest-status (+2), evidence-registry (+E015, E016), recommendation-log (+REC-008, REC-009)

Key finding: 50% of Ijen fatalities (2/4) were fitness-related (heart attack, exhaustion) — the exact risk pattern BBKSDA health screening targets. Strongest evidence yet that screening is not bureaucratic theater.

New recommendations: REC-008 (dedicated safety-incidents wiki page), REC-009 (Silo 3 /travel-guide/ijen-safety-incidents URL — requires human approval due to named fatalities).

---

## [2026-05-11] init | Wiki Initialization

Seeded from: `jvto-web` `CLAUDE.md`, `DESIGN.md`, `docs/STRATEGIC_REFERENCE.md`, Clippings homepage clip.

Pages created (18): overview, index, log, destinations/kawah-ijen, destinations/mount-bromo, destinations/tumpak-sewu, destinations/madakaripura, reviews/trustpilot-compilation, reviews/review-patterns, products/packages-overview, people/agung-sambuko, people/dr-ahmad-irwandanu, credentials/legal-licenses, credentials/trust-signals, content/brand-voice, content/faq-master, content/aeo-claims, sources/jvto-homepage-clip.

Known gaps at init: individual guide/driver profiles, pricing details, competitor data, press mentions. Many gaps resolved by 2026-05-11 SSOT ingest above.

## [2026-06-01] consolidate | Website Context Master + Extended Trust Bundle v1

Pages updated:
- `wiki/website/website-context-master.md` (NEW) — Single implementation reference: working values table (review counts, credential IDs, pricing, contact), 10 business logic rules (Ijen health screening conditional, blue fire language, cancellation/Travel Credit, monthly closure, FOC tiers, vehicle allocation, room allocation, police escort conditional, booking confirmation, micro-customization), approved/forbidden wording, schema requirements per page type, trust signal matrix (C1–C9 × page section), 7 open implementation gaps.
- `output/website/trust-bundle/products.json` (NEW) — 22 packages with full pax-tier pricing, ijen_relevant flag, health_screening flag, destinations, URLs.
- `output/website/trust-bundle/policies.json` (NEW) — booking rules, cancellation (48h threshold/Travel Credit), inclusions/exclusions, vehicle allocation, FOC tiers, health screening protocol + conditional wording, forbidden wording inventory.
- `output/website/trust-bundle/destinations.json` (NEW) — 5 destinations: entity summaries, geo-coordinates, key facts, JVTO package lists, health screening flags, AEO block paths.
- `output/website/trust-bundle/people.json` (NEW) — Founder, medical officer, 14 crew with KTA status, portrait URLs, review counts, archetypes.
- `output/website/trust-bundle/operational.json` (NEW) — Temperatures, travel times, Ijen closure schedule, seasonal guide, 23 hotel partners by phase, room allocation rules.
- `output/website/trust-bundle/_manifest.json` (UPDATED) — Extended bundle section added.
- `output/website/trust-bundle/extended-bundle-receipt.md` (NEW) — Full verification receipt for all 5 JSON files.
- `bases/website-readiness.base` (NEW) — Obsidian Base dashboard: type-filtered (destination/product/person/credential/website/seo), `days_since_update` formula, stale flag, 4 views (all pages staleness order, stale-only, Ijen health pages, domain cards).
- `wiki/index.md` — Updated total_pages (95 → 96), registered new files in Website and Compiled Outputs sections.

Key additions: unified implementation reference for any LLM or developer building the JVTO website; complete structured JSON domain exports covering all wiki areas beyond the original Trust Bundle; active Obsidian readiness dashboard.

Drift found and flagged:
- `trust-signals.md §Schema Canonical Values` shows cross-platform reviewCount = 164 (stale; was 51+92+21=164). Live Review Platforms table in same file shows Google = 123 (verified 2026-05-26 API), making real total 195. See GAP-01 in website-context-master.md. **Action needed**: update §Schema Canonical Values in trust-signals.md; regenerate Organization schemas.
- `HANDOFF.md` line ~175 shows Google Maps: 4.90 / 92 reviews — stale. See GAP-01.

## [2026-05-28] compile | trust-bundle v0.1.0 — 9 claims, 0 errors, 0 warnings

## [2026-06-02] compile | trust-bundle v0.1.0 — 9 claims, 0 errors, 0 warnings

## [2026-06-07] integrate | Package Readiness Bundle consumer sync (jvto-web)
Pages updated: wiki/ops/transformation-map.md (package-readiness pipeline row + status anchor).
Key additions: jvto-web now consumes the clean Package Readiness Bundle v1.2 via a new
`scripts/sync-package-readiness.mjs` / `npm run sync:packages`, copying all 6 artifacts
(`_manifest`, `package-registry`, `package-pricing`, `package-itineraries`,
`booking-compatibility`, `gap-report`) to `src/data/package-readiness/`. Manifest-gated on
`clean === true` + `schema_version` "package-readiness/*" prefix + positive
`canonical_package_count` (no F1–F8 block on this manifest, unlike trust-bundle). Mirrors the
existing trust-bundle sync; producer artifacts unchanged. Runtime page/DB wiring deferred.
