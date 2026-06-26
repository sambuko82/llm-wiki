---
name: verified-content
description: Generate JVTO public-facing content (website copy, FAQ, AEO snippet, a query answer, or a claim) AND verify it in the same pass — every material claim must stay inside its evidence boundary, be backed by a cited wiki source, and use no stale/forbidden wording. Use when the user asks to "write/draft" copy, "answer this for the site", "draft a FAQ/AEO answer", "buat jawaban", "tulis copy", or whenever an output makes factual claims about JVTO's credentials, history, reviews, partners, or medical/safety rules. Replaces the manual post-generation check (Booking "same address", Stefan year/edition, Detik "at Ijen", stale review counts, "BBKSDA certified", universal medical mandate, ISIC over-claim) with an automatic claim ledger + pass/block verdict. Does NOT publish — hands back verified copy + the ledger.
---

# JVTO Verified Content

The recurring failure is not *writing* JVTO copy — it is a claim slipping past its
**evidence boundary** after the draft looks good: Booking framed as "the same address" /
continuity, Stefan given a year/edition, Detik pinned to Kawah Ijen, a stale review count
(Google 92 / Trustpilot 47), "BBKSDA certified JVTO", a universal "screening is mandatory"
rule, or ISIC asserted as a partner. Today a human re-checks every output against the
boundaries. This skill folds that check into generation: **draft → verify → report**, and
**blocks** any output whose claims are not bounded and source-backed.

It is the content-production analog of the bootstrap repo's `jvto-okf-verified-curation`
skill, but for `llm-wiki` (website copy / FAQ / AEO / query answers).

## Activation guard

Require `CLAUDE.md` mentioning JVTO / llm-wiki **AND** one of:
- User asks to write/answer something that makes a factual claim about JVTO: "write the
  hero copy", "draft a FAQ for X", "answer this for the site", "AEO snippet for Y",
  "buat jawaban tentang Z", "tulis copy untuk …".
- User asks to verify/check an existing draft's claims ("is this claim safe?", "cek klaim
  ini", "does this over-claim?").
- The Query workflow (CLAUDE.md §Workflow 2) is producing a filed answer that asserts a
  credential, review figure, history fact, partner, or medical/safety rule.

Do **not** activate for pure formatting, translation with no new claim, or non-JVTO text.

## Inputs
- The content request (topic, target page/route, audience, format: page | faq | aeo | answer | claim).
- Canonical sources (read, never invent): `wiki/credentials/trust-signals.md`,
  `wiki/credentials/legal-licenses.md`, `wiki/people/agung-sambuko.md`,
  `wiki/credentials/press-coverage.md`, `wiki/index.md` (to find the right page), and the
  manifest registries `raw/_manifest/{claim-registry,decision-registry,evidence-registry}.yml`.

## Step 1 — Generate (claim-tagged)
Draft the content from wiki sources only. As you write, tag every **material claim**
(credential, number, date, history, partner, medical/safety rule, review figure) with the
wiki source it came from, e.g. `[[credentials/trust-signals]]`. A claim with no wiki source
is not allowed to ship — either source it or cut it. Match the voice in
`wiki/website/brand-voice.md` (direct, evidence-led).

## Step 2 — Verify (the step that replaces manual checking)
Run `python scripts/verify_claims.py --stdin` on the **generated draft** (pipe the draft
text in). It returns the boundary/stale violations deterministically — rules live in
`scripts/claim_boundaries.yml`. **Scan the draft only, never the canonical sources**: pages
like `trust-signals.md` and `press-coverage.md` legitimately quote stale/superseded strings
(the `92`/`47` warning, the dropped Stefan ISBN) as historical notes, so grepping the
denylist over the sources would false-positive. Use the sources only for canonical lookups
(2b) and source-backing (2c). Then build the **claim ledger**. (2a documents what the script
enforces against the draft.)

**2a. Evidence-boundary denylist** (enforced by `verify_claims.py` on the draft) — fail if:
- **Stefan**: any `year / edition / 2016 / 2018 / 4th Edition / DuMont / 978-3-7701`, or
  Stefan tied to `Khairil Anwar / same address / address continuity / current office /
  legal succession`. Allowed: identifies "Agung" re Ijen Bondowoso Homestay + tour
  arrangements, `ISBN-13 9783770167654`, `p. 287`. (decision-registry DEC-001 / CONF-001.)
- **Booking / address**: `same address (where JVTO operates today) / address continuity /
  operational continuity / continuous operational presence`. Allowed: No.102 (homestay) vs
  No.102A (office) on the same street, **historical address context only, not legal succession**.
- **Detik**: `at Ijen / Kawah Ijen / patrolling the Ijen area / duties at Ijen` when Detik
  is the subject → must be **Bondowoso area** (the article is general Bondowoso tourist-police
  duty). Collective lines that group Detik with BBKSDA/Radar (genuinely Ijen) are OK.
- **Stale review counts**: Google `92`, Trustpilot `47` near their platform name.
- **Over-claims**: `BBKSDA certified (JVTO)`; ISIC as `partner / official provider listing`
  without direct provider evidence; medical screening stated as a universal JVTO rule
  (`mandatory and non-negotiable`, `No Valid QR = No Access`) instead of the conditional
  BBKSDA-rule wording; `certified / endorsed by` for any historical Reference.

**2b. Canonical-value assertion** — any figure/identifier in the draft must match
`trust-signals.md` / CLAUDE.md: Google **4.9 / 123**, Trustpilot **4.8 / 51**, TripAdvisor
**4.95 / 21**, total **195**; NIB **1102230032918**; office **No.102A**; PT **2016-01-01**;
TDUP **2023-02-11**; HPWKI **AHU-0001072.AH.01.07.TAHUN 2024**; Dr. Ahmad Irwandanu **SIP**.
A mismatch fails the draft.

**2c. Source-backing** — every material claim in the ledger maps to a wiki source page that
actually supports it. Unsourced or AI-only claim → fail.

**2d. Build/structure checks** — if the output lands in `output/`, run the relevant existing
guards: `python scripts/compile_trust.py --dry-run`, `python scripts/compile_packages.py
--dry-run --strict`, `python scripts/verify_output_index.py`. Any non-zero → fail.

> The denylist scans the **draft**, not the canonical sources. To audit a saved file later,
> `python scripts/verify_claims.py <path>`; to sweep the active public copy on demand,
> `python scripts/verify_claims.py --all` (an audit, not yet a blocking CI gate — see Tools).

## Step 3 — Verdict + ledger
Emit a compact ledger and a decision; **never return polished copy without it**:

```
# Verification — <title / route>
Decision: approved | approved_with_qualifiers | blocked
| # | Claim | Wiki source | Boundary check | Canonical | Status |
|---|-------|-------------|----------------|-----------|--------|
| 1 | …     | [[…]]       | pass           | match     | ok     |
Blocking issues: <none | list with the exact offending string + the bounded rewrite>
Qualifiers applied: <e.g. medical wording made conditional; Booking → historical context>
```
- `blocked` → show the offending strings and the bounded rewrite; do not hand over the copy
  as final.
- `approved_with_qualifiers` → ship with the narrower wording, list what was softened.
- `approved` → all claims bounded, sourced, canonical-matched, scripts green.

## Output contract
1. The generated content. 2. The verification ledger. 3. The block/qualify decision with
exact strings. 4. (If it touches `output/`) the index/log entries needed. No publish step —
hand off to `blog-publisher` / the normal commit flow only after `approved`.

## Tools
1. **`scripts/verify_claims.py` (BUILT — the key enabler).** Deterministic claim-boundary
   linter; rules + canonical values in `scripts/claim_boundaries.yml` (mirrors the locked
   SSOT: `decision-registry.yml` DEC-001, `trust-signals.md`, `CLAUDE.md`). Scans a draft via
   `--stdin`, named files, or `--all`; emits the ledger + non-zero exit on any
   boundary/stale violation. The llm-wiki analog of the bootstrap `validate_okf.py`
   boundary checks. Tests in `tests/test_verify_claims.py`.
   - **Follow-up (not yet done):** wiring `--all` into CI as a blocking gate needs a one-time
     baseline cleanup — a current `--all` run flags genuine pre-existing stale `Google 92`
     counts (e.g. `pages/why-jvto/reviews.md`, `verify-jvto/hub.md`) that must be corrected to
     `123` first. Until then `--all` is an on-demand audit, and the skill enforces on drafts.
2. **Existing, reuse as-is:** `scripts/compile_trust.py --dry-run`,
   `scripts/compile_packages.py --dry-run --strict`, `scripts/verify_output_index.py`, and
   the `raw/_manifest/*.yml` registries + `trust-signals.md` as the canonical SSOT.
3. **`Read`:** the canonical wiki sources for source-backing (Step 2c). `Grep` only as a quick
   manual cross-check — `verify_claims.py` is the source of truth for the denylist.
4. **`WebFetch` (optional, non-blocking):** live source-health for dynamic external claims
   (review counts, registry URLs). Per the OKF/source-health contract, a blocked/CAPTCHA/403
   read is a warning that retains the last observation — it must never invalidate a claim or
   block the draft; record the attempt only.
