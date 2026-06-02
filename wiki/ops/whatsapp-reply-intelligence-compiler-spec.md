---
type: ops
title: WhatsApp Reply Intelligence Compiler — Implementation Spec
last_updated: 2026-06-02
sources: [whatsapp-operations-playbook, whatsapp-rules-engine, whatsapp-canned-responses, jvto-policy-pack-v6, policy-source-ownership, db-export-2026-05, wa-pro-crm-api]
owner: wiki-llm
stale_after_days: 120
---

# WhatsApp Reply Intelligence Compiler — Implementation Spec

Spec only. **No code in this phase.** Registered as wedge **P3** in -> [[ops/transformation-map]] (WhatsApp Reply Intelligence Bundle = Canonical Bundle 5 per -> [[ops/bundle-taxonomy]]). Implementation is a separate, later, explicitly-approved phase.

## 1. Purpose

WhatsApp is JVTO's primary customer touchpoint and the largest manual-labour surface in the business. The wiki already encodes the full operational model: -> [[whatsapp/operations-playbook]] (peta operasi, lima alur, pin points), -> [[whatsapp/rules-engine]] (7-step deterministic routing + intent taxonomy + action table + SLA + hard rules), and -> [[whatsapp/canned-responses]] (25+ bilingual templates per stage: Triage, Discovery, Proposal, Closing, Post-Booking, Objections). Trust Bundle proved the registry → validate → render → artifact pattern; Package Readiness proved the cross-source gap-report extension. This wedge applies both patterns to WhatsApp — but the deliverable is **(a) a deterministic reply-routing bundle** (channel × state × intent → action + pre-rendered template) **and (b) a gap report** flagging every coverage gap or contradiction between the three canonical wiki files and the policy/trust/package bundles they must obey.

The compiler answers: *given an inbound WhatsApp message classified to (channel, state, intent), which action fires, with what pre-rendered bilingual reply, citing which canonical claim/package/policy — and is the entire matrix consistent and complete?* It compiles a machine-readable reply-routing bundle **and** flags every missing route, ungrounded template, deprecated-wording violation, or bilingual-parity break.

It does **NOT** generate runtime AI replies. Runtime LLM classification + grounded reply generation belongs in the WA Pro CRM consumer (see §9). The compiler emits the *deterministic skeleton* the runtime LLM is constrained to: routing table, pre-rendered template slots, claim citations, policy guards.

It does NOT mutate canonical WhatsApp data. It reads canonical wiki, cross-checks against Trust Bundle / Package Readiness / Policy / FAQ outputs, and emits artifacts + a gap report.

## 2. Source Files

### Canonical (wiki — single source of truth)

| Role | File | Provides |
|---|---|---|
| Operations playbook | `wiki/whatsapp/operations-playbook.md` | 5 inbox/channel inventory, human roles (Inan/Sam/David/Dr Irwandanu/crew), pin points, brand-voice anchor |
| Rules engine | `wiki/whatsapp/rules-engine.md` | STEP 1–7 deterministic flow, intent taxonomy (per channel), master action table (channel × intent × confidence × risk → action), action definitions, time windows, SLA table, intent codes |
| Canned responses | `wiki/whatsapp/canned-responses.md` | 25+ bilingual templates (ID/EN), tagged `[WA]/[EMAIL]` + stage (T/D/P/U/PB/OB) + audience (Auto/Inan/Sam) + BANT codes; hard rules (no quote before 3 BANT locks; max 2 options at Proposal stage) |

### Reference bundles (already DONE — reused, not recompiled)

| Role | File | Provides |
|---|---|---|
| Trust Bundle | `output/website/trust-bundle/claims.json` | 9 canonical claims with `claim_id`, `canonical_text` — single source for "Tourist Police-led / 100% private / NIB 1102230032918 / founded 2015 / medical screening" wording |
| Trust Bundle ext | `output/website/trust-bundle/{people,policies,destinations}.json` | Dr Ahmad Irwandanu screening protocol, booking/cancellation rules, destination facts |
| Package Readiness | `output/products/package-readiness/{package-registry,package-pricing,package-itineraries,booking-compatibility}.json` | 16 canonical packages, pax-tier pricing, day-by-day itineraries, instant_book/whatsapp_assisted flags |
| Policy ownership | `wiki/ops/policy-source-ownership.md` | Canonical owner per policy block, **§deprecated-wording** (blue-fire-guaranteed / helmet-included-Madakaripura / police-escort-default / 50%-fee / cash-refund / Trip.com-booking — forbidden phrases) |
| FAQ master | `wiki/website/faq-master.md` + `output/website/faq/*.md` | Authoritative FAQ wording per destination + topic |
| Brand voice | `wiki/website/brand-voice.md` | Tone rules (direct, evidence-led; no overpromise; "estimate" for timing) |

### Reference snapshots (for cross-check, not auto-edit)

| Role | File | Provides |
|---|---|---|
| WA Pro CRM API | `wiki/sources/wa-pro-crm-api.md` | Webhook shape (`number_key`, `from`, `body`, `type`, `media_url`, `timestamp`), available actions, rate limits |
| DB snapshot | `wiki/sources/db-export-2026-05.md` | `bookings.customer_phone`, `klook_bookings.guest_phone`, `wa_messages`, `wa_conversations`, `wa_drafts` table contracts (used in STEP 3 lookup + STEP 7 logging) |
| Communication theory | `wiki/sources/comm-management-theory.md` | BANT framework, MECE rule, stage definitions — referenced by canned-responses |

Canonical wiki is the source of truth. Trust Bundle / Package Readiness / Policy are **reuse contracts** — divergence becomes a gap-report finding (`WA-08`, `WA-15`), never an auto-edit of either side.

## 3. Canonical Channel × State × Intent Matrix

**Canonical inbox count: 3** (customer, b2b_partner, internal_ops) per rules-engine STEP 2.

**Canonical channel count: 6** (jvto_inquiry, jvto_post_booking, jvto_returning, klook, window, vendor_crew) per rules-engine STEP 3–4.

**Canonical state count (encode in compiler):**
- `klook` → 6 states (booked, pre_tour, d_day, in_tour, post_tour, archive)
- `jvto_post_booking` → 7 states (pre_tour_prep, pre_tour_active, d_day, in_tour, post_tour, review_window, archive)
- `jvto_inquiry` → 5 states (cold, qualified, quoted, negotiating, lost) + 1 transition (→ jvto_post_booking on DP)
- `jvto_returning` → reuses inquiry states with `returning` flag
- `window` → 5 states (b2b_inquiry, b2b_quoted, b2b_confirmed, b2b_in_execution, b2b_reconciliation)
- `vendor_crew` → 5 states (dispatch_sent, confirmed, briefed, executing, done)

**Total canonical (channel, state) pairs: 33** (assert in compiler).

**Canonical action vocabulary (encode in compiler):** `auto_ack`, `auto_reply`, `auto_reply_db_grounded`, `auto_reply_redirect_klook`, `draft_for_inan`, `draft_for_inan_b2b`, `escalate_inan`, `escalate_inan_urgent`, `escalate_sam`, `escalate_sam_urgent`, `escalate_inan_or_sam`, `alert_inan_urgent`, `alert_inan_and_sam_urgent`, `auto_log_confirm`. **14 actions, closed set.**

**Canonical template stages:** T (Triage 1–3), D (Discovery 1–4), P (Proposal 1–2), U (Urgency/Closing 1–3), PB (Post-Booking 1–3), OB (Objection 1–4). **6 stages, ~19 base templates × 2 languages = 38 template blocks.**

## 4. Output Path

```
output/whatsapp/reply-intelligence/
```

Per the `output/<domain>/<bundle>/` convention in -> [[ops/transformation-map]]. No `compiled/`. No `data/`. Output domain `whatsapp/` already reserved in transformation-map (FUTURE → now P3 active).

## 5. Output Files

| File | Content |
|---|---|
| `inbox-router.json` | `number_key → inbox` mapping (3 records); unknown-number-key handler config (log + alert) — STEP 2 of rules-engine in machine form |
| `channel-router.json` | Customer inbox channel detection ordered rules (STEP 3): lookup priority + DB query template + fallback `jvto_inquiry`; reference to `bookings.customer_phone`, `klook_bookings.guest_phone` field names from DB snapshot |
| `state-machine.json` | Per channel: `states[]` with `state_id`, `entry_condition`, `exit_transition` (e.g. `jvto_inquiry.negotiating` + DP received → `jvto_post_booking.pre_tour_prep`); 33 (channel, state) pairs total |
| `intents.json` | Intent taxonomy per channel: `intent_id`, `channel`, `state_scope[]`, `description`, `examples[]`, `default_risk_level`; derived from rules-engine "Intent Taxonomy" section |
| `routing.json` | Master action table: per `(channel, intent_pattern, confidence_threshold, risk_level)` → `action_id`; fallback `confidence < 0.5 → escalate_inan`; mirrors rules-engine STEP 6 |
| `actions.json` | Action vocabulary: per `action_id` → `outbound` (bool), `requires_template_id` (nullable), `requires_db_grounding` (bool), `notification_target[]` (telegram_inan / telegram_sam / both / none), `notification_priority` (normal / urgent / alarm), `default_sla_p50_minutes`, `default_sla_p95_minutes` |
| `templates.json` | Canned responses normalised: per `template_id` (e.g. `T-1`, `D-2`, `P-1`, `OB-3`) → `stage`, `audience` (Auto / Inan / Sam), `channel_applicability[]`, `bant_tags[]`, `delivery_modes[]` (WA / EMAIL), `body.id`, `body.en`, `slot_variables[]` (e.g. `{customer_name}`, `{pax_count}`, `{package_slug}`, `{total_idr}`), `hard_rule_refs[]` (e.g. requires 3-BANT-lock for `P-1`) |
| `package-attached-replies.json` | Pre-rendered template × package matrix: for templates with `{package_*}` slots (P-1, U-2, PB-1, PB-2, OB-1), one record per (template_id × package_id) with slots resolved from `package-registry.json` + `package-pricing.json` + `package-itineraries.json`; bilingual; ~19 × 16 = up to 304 rows, but only relevant template/package combos rendered |
| `trust-attached-replies.json` | Templates with claim citations: for any template containing protected claim wording (Tourist Police / 100% private / founded 2015 / NIB / screening), one record per (template_id × claim_id) linking to `trust-bundle/claims.json` for the canonical text + source proof_ids; ensures runtime never paraphrases a claim |
| `sla-matrix.json` | (channel, state) × (business_hours / off_hours) → `frt_p50_minutes`, `frt_p95_minutes`, derived from rules-engine "SLA per state" table |
| `hard-rules.json` | Pre-send guards: `no_quote_before_bant_lock`, `max_two_proposal_options`, `no_deprecated_wording`, `conditional_health_screening_only`, `madakaripura_helmet_not_included`, `bali_origin_ferry_included`, `redirect_klook_for_change_or_refund`; per rule → `rule_id`, `applies_to_actions[]`, `applies_to_stages[]`, `block_or_warn` |
| `gap-report.json` | All findings: `{rule_id, severity, target_type, target_id, field, message, suggested_fix}`. Primary deliverable. |
| `_manifest.json` | Compile metadata: source file hashes, canonical counts asserted (3 inboxes, 6 channels, 33 states, 14 actions, 19 templates, 38 bilingual blocks), counts emitted per file, rule pass/fail summary, reuse-bundle versions consumed (trust-bundle@1.0, package-readiness@1.2), generated-by, schema_version. Mirrors trust-bundle and package-readiness `_manifest.json` shapes. |

## 6. Validation Rules

Each rule has an ID (`WA-01`…`WA-16`), a severity (`error` blocks a clean compile under `--strict`; `warn` reports only), and writes findings to `gap-report.json`. Modeled on Trust Bundle's F1–F8 and Package Readiness PKG-01–12.

| ID | Severity | Rule |
|---|---|---|
| WA-01 | error | **Inbox/channel inventory complete** — 3 inboxes + 6 channels enumerated; every inbox routes to ≥1 channel; unknown `number_key` handler defined (log + alert Inan, never silent drop) |
| WA-02 | error | **State coverage** — every channel has ≥1 state; every state has `entry_condition` + `exit_transition` (or terminal); 33 total (channel, state) pairs asserted; `jvto_inquiry.negotiating + DP` transition to `jvto_post_booking.pre_tour_prep` present |
| WA-03 | error | **Intent taxonomy complete** — every intent has channel binding + ≥1 state_scope; every intent in rules-engine STEP 6 action table is defined in STEP "Intent Taxonomy"; no orphan intent (defined but never routed) |
| WA-04 | error | **Action vocabulary closed** — every action referenced in `routing.json` exists in `actions.json` (14 canonical); no freeform action strings; fallback `confidence < 0.5 → escalate_inan` present |
| WA-05 | error | **Bilingual parity** — every template has both `body.id` (Bahasa Indonesia) and `body.en` (English) non-empty; same slot_variables present in both; no untranslated placeholder leftover |
| WA-06 | error | **Template tagging complete** — every template has `stage` (T/D/P/U/PB/OB), `audience` (Auto/Inan/Sam), `delivery_modes` (≥1 of WA/EMAIL); BANT tags optional but if present must use canonical codes {B,A,N,T} |
| WA-07 | error | **Price citation** — any template `body` containing an IDR amount or pricing language ("per pax", "total") must have `slot_variable` resolving from `package-pricing.json` — no hard-coded prices in template bodies; per JVTO solo-pricing-rule (`website-context-master.md` §3.11) any pricing reply for 1 pax requires explicit upcharge wording |
| WA-08 | error | **Claim grounding** — any template containing protected wording {Tourist Police, 100% private, founded 2015, PT Java Volcano Rendezvous, NIB 1102230032918, TDUP, BBKSDA, medical screening by Dr Ahmad Irwandanu} must cite a `claim_id` from `trust-bundle/claims.json` and use that claim's `canonical_text` verbatim |
| WA-09 | error | **Deprecated wording absent** — per -> [[ops/policy-source-ownership]] §deprecated-wording, none of {"Blue Fire guaranteed", "helmet included" (for Madakaripura), "police escort default", "50% admin fee", "cash refund", "Trip.com booking", "WA-only booking" implied as required} appears in any template body or routing description, in either language |
| WA-10 | error | **Pre-quote gate enforced** — every template with `stage: P` (Proposal) carries `hard_rule_refs: [no_quote_before_bant_lock]`; runtime guard config in `hard-rules.json` asserts the 3 components (date locked + pax count + hotel preference) must all be true on `wa_conversations` before P-stage templates fire |
| WA-11 | error | **Max 2 options at Proposal** — no P-stage template body offers >2 options; `hard-rules.json` `max_two_proposal_options` guard configured |
| WA-12 | error | **Conditional health-screening wording** — every template/routing description mentioning Ijen health screening uses conditional wording ("where BBKSDA rules require" / "for guests over [age]" / "as part of our included safety protocol") matching `trust-bundle/policies.json` and `wiki/people/dr-ahmad-irwandanu.md`; never "universally mandatory" or "police-mandated" |
| WA-13 | error | **SLA coverage** — every (channel, state) pair has FRT P50 + P95 in `sla-matrix.json`, split by business_hours / off_hours; SLAs match rules-engine "SLA per state" table or document override with reason |
| WA-14 | error | **Off-hours coverage** — every customer-inbox channel (`jvto_inquiry`, `jvto_post_booking`, `jvto_returning`, `klook`) has an off-hours `auto_ack` template assigned (T-3 or channel-specific variant); off-hours window per rules-engine "Time Windows" section |
| WA-15 | error | **Package reference integrity** — every `package_slug` slot value in `package-attached-replies.json` exists in `output/products/package-readiness/package-registry.json`; every `total_idr` value matches a `pax_tier` in `package-pricing.json`; Bali-origin packages render with ferry-included wording per package booking-compatibility |
| WA-16 | error | **Escalation routing complete** — every `escalate_*` and `alert_*` action specifies `notification_target` (telegram_inan / telegram_sam / both) and `notification_priority` (normal / urgent / alarm); `vendor_crew.emergency` intent maps to `alert_inan_and_sam_urgent`; no escalation action has empty target |

Additional warn-only rules:

| ID | Severity | Rule |
|---|---|---|
| WA-W1 | warn | **Template coverage per stage** — every stage (T/D/P/U/PB/OB) has ≥1 template; warn if any stage has <2 templates (insufficient variation) |
| WA-W2 | warn | **State-without-template** — every (channel, state) pair has ≥1 reachable template via routing.json; flag dead states |
| WA-W3 | warn | **High-confidence auto_reply paths** — flag any routing row with `auto_reply` action but template not in `trust-attached-replies.json` or `package-attached-replies.json` (i.e. ungrounded auto-send) |
| WA-W4 | warn | **Forbidden-phrase scan** — extend WA-09 to scan rules-engine examples + intent descriptions, not just template bodies |
| WA-W5 | warn | **Source freshness** — flag if any of the 3 canonical files exceeds `stale_after_days` (60) from frontmatter |

## 7. Compiler Architecture

Mirror `scripts/compile_trust.py` and `scripts/compile_packages.py` structure for consistency (do not reuse their registries):

```
scripts/compile_whatsapp.py        (NOT BUILT — implementation phase)
├── loaders        parse the 3 canonical WhatsApp markdown files →
│                  in-memory routing model
│                  (markdown table parsers for rules-engine STEPs 2–6
│                   and SLA tables; section parser for canned-responses
│                   templates including ID/EN block extraction; YAML
│                   frontmatter reader for freshness; bundle readers for
│                   trust-bundle/, package-readiness/ as reference sets)
├── enricher       cross-join templates × packages → package-attached-replies;
│                  cross-join templates × claims → trust-attached-replies;
│                  derive state-machine transitions; resolve template
│                  slot_variables to source bundles; attach hard_rule_refs
├── validators     WA-01…WA-16 + WA-W1…WA-W5 → findings list
│                  (each yields gap-report rows)
├── renderers      emit the 11 artifact JSONs + _manifest.json
└── CLI orchestrator
    --dry-run      run loaders+validators, print gap-report summary, write nothing
    --strict       exit non-zero if any `error`-severity finding remains
    --verbose      print each violation with file:line where possible
    (default)      atomic write of all 12 outputs to output/whatsapp/reply-intelligence/
```

Write semantics: atomic (temp + rename), all-or-nothing, same as trust and package compilers. `--dry-run` is the safe default for the first real run — it surfaces the gap report without producing artifacts.

Module reuse decision: **new** `scripts/whatsapp_compiler/{loader,enricher,validator,renderer}.py` package (mirror `scripts/compiler/` and `scripts/package_compiler/`). Do not extend trust or package compiler modules — domain models differ (claim/decision vs package vs channel/state/intent).

Reuse-bundle versions are pinned in `_manifest.json` (`trust-bundle@1.0`, `package-readiness@1.2`). If a pinned bundle version is missing or has changed since last compile, error and refuse to write (forces explicit re-pin).

## 8. Non-Goals (this phase)

- Do **not** implement `scripts/compile_whatsapp.py` or any code.
- Do **not** generate any JSON or create `output/whatsapp/reply-intelligence/`.
- Do **not** generate runtime AI replies. The compiler emits deterministic skeletons only; runtime LLM grounded-generation belongs in the WA Pro CRM consumer (see §9).
- Do **not** auto-create or auto-edit canned response templates. Missing templates surface as `WA-W1` warnings; humans author the fill.
- Do **not** modify `wiki/whatsapp/{operations-playbook,rules-engine,canned-responses}.md`. Compiler is read-only on canonical wiki.
- Do **not** touch Trust Bundle, Package Readiness, or their registries.
- Do **not** edit `raw/_manifest/decision-registry.yml` or any registry.
- Do **not** touch WA Pro CRM, webhook endpoints, `wa_messages`, `wa_conversations`, `wa_drafts`, or DB schema.
- Do **not** touch jvto-web.
- Do **not** integrate with Telegram (notification destination) — `notification_target` is a config string only; transport setup is consumer-side.
- Do **not** pre-fix gaps in canonical wiki to make validation pass — compiler's job is to *report*; fixes are a later, separate decision.

## 9. Next Implementation Phase

After this spec is confirmed:

1. **Build `scripts/compile_whatsapp.py`** — loaders + model first, TDD per the trust + package precedent (unit tests for each parser + each WA rule, E2E happy-path + strict-fail + reuse-bundle-version-mismatch fail). Pin `trust-bundle@1.0` and `package-readiness@1.2` as required inputs.
2. **First `--dry-run` against real wiki** — produce `gap-report.json`; triage findings with Sam. Expected real gaps based on current canonical files:
   - WA-13: SLA table in rules-engine covers ~9 (channel, state) rows; remaining 24 pairs need explicit SLA or documented inheritance rule.
   - WA-15: package_slug references in templates currently human-readable ("Bromo Ijen 3D2N") not canonical slug — slot extraction will surface mismatches.
   - WA-W1: stages with <2 templates likely include Discovery and Objections variants for B2B / vendor_crew channels.
   - WA-08: claim-citation linking is currently implicit in canned-responses — explicit `claim_id` references must be added (or the compiler infers, with `warn`).
3. **Resolve gaps in canonical wiki** (separate task; ordered by gap-report severity), then re-run without `--dry-run` to emit the first real WhatsApp Reply Intelligence bundle.
4. **Register consumers** (downstream of bundle emission, not part of this wedge):
   - WA Pro CRM webhook handler reads `inbox-router.json` + `channel-router.json` + `state-machine.json` + `routing.json` to perform STEP 1–4 deterministically (no LLM call).
   - Runtime LLM classifier (Haiku 4.5 per rules-engine STEP 5) receives `intents.json` taxonomy as system prompt constraint; outputs JSON conforming to `intents.json` schema.
   - Runtime LLM reply generator receives the matched `template_id` from `routing.json` + the pre-rendered version from `package-attached-replies.json` or `trust-attached-replies.json` and is constrained to fill `slot_variables` only (no freeform claim assertions; WA-08 guarantee enforced at compile time).
   - Pre-send guard reads `hard-rules.json` and blocks any outbound violating `no_quote_before_bant_lock`, `max_two_proposal_options`, `no_deprecated_wording`, `conditional_health_screening_only`, etc.
   - Telegram routing reads `actions.json` `notification_target` + `notification_priority`.
5. **Wire SLA monitoring** — `sla-matrix.json` feeds a separate dashboard (Bases or external) tracking real FRT against P50/P95 per (channel, state); not part of this wedge.

Implementation does not begin until explicitly approved.

## 10. Wedge Boundary (for Sam approval)

| In scope (this wedge) | Out of scope (later wedges or consumers) |
|---|---|
| Spec + compiler + 12 output artifacts + gap report | Runtime AI classification + reply generation |
| Validate canonical wiki against trust + package + policy bundles | Edit canonical wiki to close gaps |
| Define deterministic routing for STEP 1–7 of rules-engine | Implement webhook handler / Telegram bridge / WA Pro CRM integration |
| Cross-bundle reference resolution (package × template, claim × template) | Build the WhatsApp dashboard UI / Bases visualisation |
| Hard-rules config emission | Enforce hard-rules at runtime (consumer responsibility) |
| Pin trust-bundle@1.0 + package-readiness@1.2 reuse contract | Upgrade reuse-bundle versions when they ship new majors |

The gap-report from the first `--dry-run` is the natural decision point for what canonical wiki cleanup is needed before consumer integration begins.
