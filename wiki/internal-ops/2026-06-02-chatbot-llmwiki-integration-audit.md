---
type: internal-ops
title: Chatbot-Web-JVTO ↔ LLM-Wiki — Integration Audit & Consolidation Plan
last_updated: 2026-06-02
sources: [chatbot-web-jvto-repo-snapshot-2026-06-02, whatsapp-rules-engine, whatsapp-canned-responses, whatsapp-operations-playbook, package-readiness-compiler-spec, whatsapp-reply-intelligence-compiler-spec, policy-source-ownership, trust-bundle-v1]
owner: wiki-llm
stale_after_days: 60
---

# Chatbot-Web-JVTO ↔ LLM-Wiki — Integration Audit & Consolidation Plan

> Audit dilakukan 2026-06-02 atas repo `D:\chatbot-web-jvto` (live admin UI + WhatsApp webhook + chat API) terhadap `llm-wiki` (canonical SSOT + compiled bundles). Tujuan: identifikasi korelasi, gap, dan urutan optimalisasi pengimplementasian.

---

## 1. Scope & Source of Audit

| Repo | Path | Snapshot |
|---|---|---|
| Chatbot consumer | `D:\chatbot-web-jvto` | git ref @2026-06-02, Next.js 16 + React 19 + Postgres 17 (host `31.97.223.43`) + Ollama (qwen2.5:latest) + OpenAI Assistants |
| Wiki producer | `E:\Users\JAVA VOLCANO\llm-wiki` | git ref @2026-06-02, 45 wiki/sources, 6 bundle indexes, 2 DONE compilers (trust + package), 8 Bases |

**Audit boundary:** read-only. No edits to chatbot code, DB, or runtime. No edits to canonical wiki. This doc is a planning artifact, not a change record.

---

## 2. Chatbot Architecture — What It Actually IS

### 2.1 Runtime stack (verified)

| Layer | Component | Evidence |
|---|---|---|
| HTTP framework | Next.js 16 (App Router) | `package.json` `next@^16.0.0`, `app/` routes |
| LLM A (cold inquiries) | OpenAI Assistants v1 API (threads + assistant_id) | `src/gptsClient.js` uses `openai.beta.threads` + `OPENAI_ASSISTANT_ID` env |
| LLM B (post-booking) | Local Ollama at `http://localhost:11434` with `qwen2.5:latest` | `src/chatbot.js` posts to `/api/chat`, model from settings |
| State store | Postgres @ `31.97.223.43:5432/chatbot_web` | `src/db.js` — tables: `conversations`, `settings`, `knowledge_entries` |
| Retrieval | BM25-lite (token overlap, title×2 + tags×2 + content×1, top-3) | `src/knowledgeRetrieval.js` |
| WhatsApp ingress | Webhook `POST /api/whatsapp/webhook` (auth via `secret` query or `x-api-key`) | `app/api/whatsapp/webhook/route.ts` |
| WhatsApp egress | `src/whatsappSender.js` (not yet read in detail) | imported by webhook route |
| Booking lookup | External REST `bookingApiClient.lookupByPhone(phone)` | `src/bookingApiClient.js` |
| Admin UI | React: ChatPanel, ConversationList, KnowledgeManager, SettingsSidebar | `components/*.tsx` |

### 2.2 State machine — `orderFlow.js`

**Funnel states (10 + 2 side):**

```
GREETING → TANYA_NAMA → TANYA_ORIGIN → TANYA_DURASI → PILIH_PAKET
  → TANYA_TANGGAL → TANYA_PAX → KONFIRMASI → TANYA_BAYAR → SELESAI

side: UBAH_KONFIRMASI (modify selection), HUMAN_HANDOFF
```

These are **slot-collection states**, not customer-journey states. Each state corresponds to one data point the bot needs (`customerName`, `origin`, `requestedDays`, `selectedPackage`, `tanggal`, `pax`, `metodeBayar`).

### 2.3 Knowledge surface — three separate sources of "truth"

| Source | Where | Format | Owner | Sync to llm-wiki |
|---|---|---|---|---|
| **Hardcoded JS packages** | `src/packages.js` | TypeScript array of 16 objects with `id, name, from, to, days, nights, slug, priceTiers[]` | Dev (manual) | ❌ NONE — drift risk |
| **settings.json `knowledge.faqBase`** | `settings.json` lines 32–86 + DB `settings` row | Single text blob (English only) | Manual via Settings UI | ❌ NONE — duplicate of wiki/website/faq-master |
| **`knowledge_entries` table** | Postgres + warmed cache | Per-entry: `id, title, content, domain, tags, source, last_updated` with `source ∈ {'llm-wiki', 'manual'}` | Mixed | ✅ PARTIAL via `POST /api/knowledge/sync` |
| **OpenAI Assistant knowledge** | OpenAI cloud (assistant_id) | Whatever was uploaded to assistant config | Opaque | ❌ INVISIBLE — cannot audit |
| **settings.json `templates.*`** | `settings.json` lines 14–30 + DB | Hardcoded English strings per state (`welcomeMessage`, `TANYA_NAMA`, `TANYA_ORIGIN`, `HUMAN_HANDOFF`, `nudges.*`) | Manual | ❌ NONE — duplicates wiki/whatsapp/canned-responses |
| **`src/systemPrompt.js BASE`** | Hardcoded JS | Brand voice rules + FAQ summary | Dev | ❌ NONE — duplicates wiki/website/brand-voice |

### 2.4 Existing llm-wiki integration — `POST /api/knowledge/sync`

```
clone/pull git@github.com:${LLMWIKI_REPO}.git via LLMWIKI_DEPLOY_KEY (base64)
  → walk wiki/{destinations,products,people,credentials,website,whatsapp}/**/*.md
  → BLACKLIST: wiki/whatsapp/rules-engine.md, operations-playbook.md,
               website/{aeo-claims,copy-bank,query-hero-claim,schema-templates}.md
  → parse frontmatter (title, aliases as tags)
  → upsertMany(entries, source='llm-wiki')
```

**Important:** sync pulls **raw markdown content as text**, not compiled bundles. The chatbot does not currently consume `output/website/trust-bundle/*.json` or `output/products/package-readiness/*.json`.

---

## 3. Correlation Matrix — llm-wiki ↔ Chatbot

| llm-wiki canonical / output | Chatbot consumer | Sync mechanism | Drift risk |
|---|---|---|---|
| `wiki/products/packages-overview.md` + `packages-full-pricing.md` | `src/packages.js` (16 hardcoded) | Manual paste | **HIGH** — slug match verified ✓ but price tiers separate code path |
| `output/products/package-readiness/package-registry.json` | NONE | Not consumed | **HIGH** — canonical price source ignored |
| `output/products/package-readiness/package-pricing.json` | NONE | Not consumed | **HIGH** — pax-tier pricing duplicated in `packages.js` |
| `output/website/trust-bundle/claims.json` | NONE (text only via FAQ blob) | Not consumed structurally | **MEDIUM** — chatbot mentions Tourist Police, NIB, screening without citing claim_id |
| `output/website/trust-bundle/policies.json` | NONE | Not consumed | **MEDIUM** — booking/cancellation rules duplicated in `faqBase` |
| `output/website/trust-bundle/people.json` (Dr Irwandanu, founder) | NONE | Not consumed | **LOW** — referenced as text in faqBase |
| `wiki/website/faq-master.md` + `output/website/faq/*.md` | `settings.knowledge.faqBase` (manually maintained text) | Manual | **HIGH** — drift since both are wordy and hand-edited |
| `wiki/website/brand-voice.md` | `src/systemPrompt.js BASE` constant | Hardcoded | **MEDIUM** — rules largely consistent ("never guarantee Blue Fire", "100% private", "20% deposit") but version-locked at dev time |
| `wiki/whatsapp/canned-responses.md` (25+ bilingual templates) | `settings.templates.*` (English-only single strings) | None | **HIGH** — chatbot has 8 template slots; wiki has 19 templates × 2 lang = 38 blocks |
| `wiki/whatsapp/rules-engine.md` (channels, states, intents, action table) | Chatbot's `orderFlow.js` (10 funnel states) | None | **STRUCTURAL** — different abstraction levels, not directly comparable but complementary |
| `wiki/whatsapp/operations-playbook.md` | None | BLACKLISTED in sync | **N/A** — explicitly excluded |
| `wiki/ops/policy-source-ownership.md` §deprecated-wording | None enforced | None | **HIGH** — runtime can emit deprecated phrases ("Blue Fire guaranteed" partially hedged but "police escort", "50% admin fee" not blocked) |
| `wiki/sources/wa-pro-crm-api.md` (webhook contract) | `app/api/whatsapp/webhook/route.ts` | Indirect (dev coded to match) | **MEDIUM** — webhook schema implemented but `number_key`-based inbox routing (rules-engine STEP 2) NOT implemented |
| `wiki/people/crew-registry.md` | `bookingData.guides[]`, `drivers[]` (when guest matched) | Indirect via bookingApi | **LOW** — runtime data from booking system |

**Chatbot → llm-wiki reverse flow (telemetry):** currently NONE. All conversation logs in `conversations.messages` JSONB stay in chatbot DB. No path back to inform wiki/whatsapp/canned-responses gaps, intent taxonomy refinement, or opportunity-register.

---

## 4. Critical Findings (ranked by severity × probability × business impact)

### CR-01 — Pricing drift between `packages.js` and canonical wiki
**Severity:** HIGH
**Evidence:** `src/packages.js` lines 1–80 hardcode `priceTiers[]` per package; `output/products/package-readiness/package-pricing.json` is the canonical compiled source; no automated check.
**Business risk:** quoted price diverges from website/checkout/finance rate-card → trust break with customer mid-conversation, refund disputes, brand damage.
**Probability of drift:** HIGH within 6 months (pricing reviewed quarterly per [Assumption] standard SMB cycle).

### CR-02 — Deprecated wording NOT enforced at runtime
**Severity:** HIGH
**Evidence:** `policy-source-ownership.md` §deprecated lists forbidden phrases (Blue Fire guaranteed, helmet-included for Madakaripura, police-escort-default, 50% admin fee, cash-refund, Trip.com booking). Chatbot's `systemPrompt.js BASE` covers 2 of 6 ("Never guarantee Blue Fire visibility"; deposit at 20% implied). Other 4 not blocked.
**Business risk:** legal/policy violation in customer-facing reply that contradicts published policy. WhatsApp text becomes evidence in disputes.
**Probability:** LOW per message, HIGH cumulatively over 1000s of replies.

### CR-03 — Bilingual gap — chatbot English-only despite WA serving ID customers
**Severity:** HIGH
**Evidence:** `systemPrompt.js BASE` line 3: "Always respond in English." `settings.templates.*` are all English. `whatsapp-webhook` filters: `nonIndonesiaFilterEnabled` — currently set to process non-Indonesia + whitelist. But `canned-responses.md` ships 38 bilingual blocks (ID + EN). Indonesian customer messaging Sam direct will get an English bot reply.
**Business risk:** Indonesian customer perceives bot as foreign, escalation rate higher, conversion lost.
**Probability:** depends on `whitelist` content + filter setting.

### CR-04 — Three sources of "knowledge" with no precedence rule
**Severity:** HIGH
**Evidence:**
1. `settings.knowledge.faqBase` (fallback when retrieval returns nothing)
2. `knowledge_entries` table top-3 via BM25 (primary when message has tokens)
3. OpenAI Assistant baked-in knowledge (when `llm=gpts` and no bookingData)

No canonical precedence. Same fact (e.g. "deposit 20%") may exist in all three with potentially different wording.
**Business risk:** inconsistent answers across consecutive conversations; impossible to audit which source emitted what.

### CR-05 — OpenAI Assistant knowledge is OPAQUE
**Severity:** MEDIUM
**Evidence:** `gptsClient.js` calls `openai.beta.threads.runs` against `OPENAI_ASSISTANT_ID` — content of that Assistant (system prompt, attached files, tools) is configured in OpenAI dashboard, not in repo.
**Business risk:** brand-voice + claim integrity invisible to wiki audit; cannot validate against trust-bundle/claims.json.
**Probability:** ongoing — every cold inquiry uses this path.

### CR-06 — Hardcoded DB credentials in `src/db.js`
**Severity:** HIGH (security)
**Evidence:** `src/db.js` line 6–11: `password: process.env.DB_PASSWORD || 'SuksesL@ncarRezek1'` — password fallback in plaintext, committed to repo.
**Business risk:** repo compromise = production DB credential leak. Standard issue but worth flagging.
**Out of scope** for this audit but logged.

### CR-07 — Webhook `number_key`-based routing not implemented
**Severity:** MEDIUM (architectural)
**Evidence:** `wiki/whatsapp/rules-engine.md` STEP 2 routes by `number_key` to inbox (customer / b2b_partner / internal_ops). Chatbot webhook reads `data.from` only — treats every inbound as same inbox. B2B (Window Travel) and vendor/crew messages would go through same funnel as customer inquiry.
**Business risk:** B2B partner gets consumer welcome message; vendor confirm reply treated as new lead.

### CR-08 — No telemetry feedback to llm-wiki
**Severity:** MEDIUM
**Evidence:** `conversations.messages` JSONB captures everything but never exports to wiki. Real customer language patterns, intent classification accuracy, state-leak rates, HUMAN_HANDOFF triggers — none fed back to `wiki/whatsapp/rules-engine.md` intent taxonomy or `wiki/sources/`.
**Business risk:** wiki canonical drifts away from production reality over months.

### CR-09 — Sync route pulls **raw markdown content**, not compiled JSON
**Severity:** MEDIUM
**Evidence:** `app/api/knowledge/sync/route.ts` reads `wiki/<domain>/*.md` and dumps `body` (raw markdown) into `knowledge_entries.content`. The chatbot's BM25 retrieval treats this as text. Compiled bundles (`output/website/trust-bundle/*.json` with `claim_id` + `canonical_text`) are NOT consumed — they are the LLM-friendliest format precisely for grounding.
**Business risk:** runtime LLM paraphrases canonical claims rather than quoting them verbatim → WA-08 violation pattern at scale.

### CR-10 — Blacklist excludes operational truth
**Severity:** LOW
**Evidence:** Blacklist intentionally excludes `whatsapp/rules-engine.md` + `operations-playbook.md` (they're operational, not customer-facing). Correct decision. But this means chatbot has zero visibility into its own intended routing logic. Consumer of P3 wedge (compiled `routing.json` + `actions.json`) would close this without re-introducing operational markdown.

---

## 5. Consolidation Roadmap

### Principle

**llm-wiki is canonical. Chatbot is consumer.** Every fact, claim, price, template, and policy in chatbot runtime must derive from a compiled bundle output, with version pinning and refresh path. Manual entries persist only in `knowledge_entries.source='manual'` and are explicitly second-class.

### Phase 1 — Quick wins (1–2 weeks, no compiler dependency)

| # | Action | Effort | ROI |
|---|---|---|---|
| 1.1 | Extend sync route to pull `output/website/trust-bundle/claims.json` + `policies.json` + `people.json` + `destinations.json`; render each as a high-precedence `knowledge_entries` row with `source='llm-wiki-trust'` and `tags=[claim_id, domain]` | 4–6 h | Closes CR-04 partial; chatbot retrieves claim canonical_text verbatim |
| 1.2 | Add deprecated-wording outbound filter: read `policy-source-ownership.md` §deprecated, build forbidden-phrase regex, applied in `chatbot.js` `callLLM()` post-process — replace match with safe phrasing OR escalate | 3–4 h | Closes CR-02 |
| 1.3 | Add slug + price validator: build-time script `scripts/validate-packages-vs-wiki.js` reads `output/products/package-readiness/package-pricing.json` + `package-registry.json`, asserts every `packages.js` package exists and `priceTiers[]` matches `pax_tiers[]`; CI gate or pre-commit | 3 h | Closes CR-01 |
| 1.4 | Enable bilingual mode: detect customer language from `data.text` (basic heuristic: contains `aku|saya|halo|terima kasih` → ID), switch `systemPrompt` "Always respond in English" line to mirror customer language | 4 h | Closes CR-03 partial; structural fix in Phase 2 |
| 1.5 | Document precedence rule in `chatbot.js` and `faqPrompt.js`: trust-bundle > knowledge_entries (llm-wiki-source) > knowledge_entries (manual) > settings.knowledge.faqBase fallback. Add comment + log line per retrieval. | 2 h | Closes CR-04 |

**Phase 1 deliverable:** chatbot runtime no longer paraphrases claims, no longer emits deprecated wording, no longer ships pricing that drifts from wiki. Bilingual baseline.

### Phase 2 — P3 WhatsApp Reply Intelligence wedge integration (4–6 weeks)

**Prerequisite:** P3 compiler spec'd (DONE 2026-06-02 per `wiki/ops/whatsapp-reply-intelligence-compiler-spec.md`); implementation per §9 of that spec.

| # | Action | Effort | ROI |
|---|---|---|---|
| 2.1 | After P3 compiler emits `output/whatsapp/reply-intelligence/`, extend chatbot sync route to pull bundle JSONs; cache in new table `wa_routing_bundle` (per-bundle version pinned) | 6 h | Foundation for 2.2–2.6 |
| 2.2 | Replace `settings.templates.*` with consumption from `output/whatsapp/reply-intelligence/templates.json` (bilingual, tagged, with slot variables) | 6–8 h | Closes CR-03 fully + canned-responses parity |
| 2.3 | Replace hardcoded `src/packages.js` with runtime read of `output/products/package-readiness/package-registry.json` + `package-pricing.json`; preserve `packages.js` exports interface so `orderFlow.js` doesn't break | 8 h | Closes CR-01 fully; manual-paste workflow ends |
| 2.4 | Implement `number_key` routing per `inbox-router.json` — webhook reads number key, maps to inbox (customer / b2b / internal); routes B2B + vendor_crew inbound to dedicated state machine OR escalation | 8–12 h | Closes CR-07 |
| 2.5 | Implement claim citation: when LLM retrieves a `trust-bundle/claims.json` entry, prepend `canonical_text` verbatim before LLM is allowed to paraphrase; runtime constrains LLM to fill `slot_variables` only | 6–8 h | Closes CR-05 partial (local LLM); CR-09 fully |
| 2.6 | Hard-rules runtime guard: read `hard-rules.json`, enforce `no_quote_before_bant_lock` (block Proposal-stage replies if order_data lacks date + pax + hotel preference); enforce `max_two_proposal_options` | 4–6 h | Closes CR-02 deep; matches canned-responses §Rule |

**Phase 2 deliverable:** chatbot becomes a thin runtime over compiled bundles. Any wiki update flows to runtime after re-compile + sync.

### Phase 3 — Feedback loop (after Phase 2 stable)

| # | Action | Effort | ROI |
|---|---|---|---|
| 3.1 | Nightly export: `conversations.messages` + `state` + `orderData` + `intent_classified` (if added) → JSONL → `raw/_inbox/whatsapp-telemetry-YYYY-MM.jsonl` → triggers intake-gate (Workflow 7) | 8 h | Closes CR-08; feeds opportunity-register |
| 3.2 | Intent-taxonomy refinement: classifier confidence + customer language samples → diff against `wiki/whatsapp/rules-engine.md` "Intent Taxonomy" section → gap-report fed to `raw/_manifest/recommendation-log.md` | 4 h | Wiki canonical learns from runtime |
| 3.3 | Migrate OpenAI Assistant prompt to bundle-driven: assistant config = `claims.json` + `templates.json` + intent definitions; version-pinned reuse contract identical to local LLM path | 8 h | Closes CR-05 fully |
| 3.4 | SLA monitoring: log FRT per (channel, state); dashboard reads `sla-matrix.json` for target; alert on P95 breach | 6 h | Operational visibility for Sam |

**Phase 3 deliverable:** wiki ↔ chatbot becomes bidirectional. Wiki ships canonical; chatbot ships reality.

---

## 6. Sequencing Decision

Two valid sequences. Both reach the same Phase 2 endpoint.

**Option A — Quick wins first (recommended):**
```
Phase 1 (1–2 wk)  →  P3 compiler build (4–6 wk per spec §9)  →  Phase 2 (4–6 wk)  →  Phase 3
```
- Pros: immediate runtime fixes (CR-01, CR-02, CR-03); buys time for compiler build
- Cons: some Phase 1 work (knowledge sync extension) gets superseded in Phase 2

**Option B — Wedge first:**
```
P3 compiler build (4–6 wk)  →  Phase 1+2 merged (6–8 wk)  →  Phase 3
```
- Pros: no superseded work; cleaner architecture
- Cons: 4–6 weeks of continued deprecated-wording risk + bilingual gap

**Saya rekomendasikan Option A** karena CR-01 (pricing drift) dan CR-02 (deprecated wording) adalah business risks yang materiil dan murah ditambal sekarang. Phase 1 throwaway cost = ~6 jam yang akan di-supersede di Phase 2.

---

## 7. Risk Register

| Risk | Mitigation |
|---|---|
| Phase 1.1 trust-bundle ingestion floods `knowledge_entries` with structured JSON that BM25 indexer can't tokenize well | Render JSON → markdown-style summary at sync time; preserve `claim_id` as tag |
| Phase 1.2 deprecated-wording filter false-positives on legitimate use ("Blue Fire" as topic vs guarantee) | Use context-aware regex (require "guaranteed/certain/sure" near "Blue Fire"); test corpus from existing conversations |
| Phase 2.3 runtime read of bundles introduces latency | Warm-cache at boot (already pattern for `settings` + `knowledge`); reload on sync route POST |
| Phase 2.5 verbatim claim insertion makes replies stiff | Allow LLM to wrap canonical_text in conversational frame ("To answer your question: [claim]") — claim text immutable, prefix/suffix free |
| Phase 3.1 telemetry export contains PII (customer phone, names) | Strip phone numbers before export; preserve only intent + state + language; mask names |
| Postgres credential in `db.js` exposed (CR-06) | Out of scope for this audit but should be rotated + `.env` only — separate sec task |
| OpenAI Assistant version drift (CR-05) | Phase 3.3 migrates away from Assistant API; until then, log assistant_id + asst_config_hash per response |

---

## 8. Out of Scope (this doc)

- Building the P3 WhatsApp Reply Intelligence Compiler — see `wiki/ops/whatsapp-reply-intelligence-compiler-spec.md`.
- Modifying chatbot code (this is an audit + plan; implementation requires Sam approval).
- DB credential rotation, hosting hardening, OpenAI billing review.
- Replacing Postgres with anything else.
- jvto-web (separate consumer of trust-bundle).
- Building the "JVTO Knowledge Kitchen" dashboard (see earlier review — premature).

---

## 9. Decision Points for Sam

1. **Approve Option A sequencing?** Quick wins this week + P3 compiler in parallel build (4–6 weeks), or wait for P3 first?
2. **CR-06 (DB credential in repo)** — when to rotate? Affects every redeploy.
3. **CR-05 (OpenAI Assistant opacity)** — keep gpts path for cold inquiries, or accelerate Phase 3.3 to remove it? Cost: OpenAI Assistants run is paid per message; local LLM is free but slower.
4. **CR-07 (number_key inbox routing)** — does JVTO have >1 active WhatsApp number now, or is this future-state? If future-state, defer to Phase 2.4; if current, accelerate.
5. **Bilingual scope** — Phase 1.4 quick heuristic, or jump to Phase 2.2 full template bilingual via `templates.json`? Quick heuristic risk: misclassifies mixed-language messages.

---

## 10. Implementation Order — Concrete Tasks

If Option A approved, here is the literal first-week list:

| Day | Task | File touched (chatbot) | Files read (llm-wiki) |
|---|---|---|---|
| 1 | Extend sync route to pull trust-bundle JSON | `app/api/knowledge/sync/route.ts` | `output/website/trust-bundle/claims.json`, `policies.json`, `people.json`, `destinations.json` |
| 1 | Add ingestion mapping: each claim → 1 knowledge_entry with `source='llm-wiki-trust'` | `src/knowledgeStore.js`, sync route | trust-bundle |
| 2 | Add boost in retrieval: `source='llm-wiki-trust'` entries get score × 3 | `src/knowledgeRetrieval.js` | n/a |
| 2 | Add precedence comment + log in `faqPrompt.js` | `src/faqPrompt.js` | n/a |
| 3 | Read `policy-source-ownership.md` §deprecated, write phrase list to constant | `src/deprecatedPhrases.js` (new) | `wiki/ops/policy-source-ownership.md` |
| 3 | Add `filterDeprecated(reply)` post-process in `chatbot.js` `callLLM()` | `src/chatbot.js` | n/a |
| 4 | Write `scripts/validate-packages-vs-wiki.js` | `scripts/validate-packages-vs-wiki.js` (new) | `output/products/package-readiness/*.json` |
| 4 | Add npm script `validate:packages` + CI/pre-commit hook | `package.json` | n/a |
| 5 | Language detection function + branch in `systemPrompt.js`/`faqPrompt.js` | `src/languageDetect.js` (new), `src/faqPrompt.js`, `src/systemPrompt.js` | n/a |
| 5 | Test corpus: 20 messages mix ID/EN, verify branching | `tests/` (new if absent) | n/a |

**Total Phase 1 effort:** ~5 dev days solo, ~25–30 hours.

---

## 11. Verification Plan

Each phase ships with measurable acceptance:

| Phase | Metric | Target |
|---|---|---|
| 1.1 | % LLM replies citing `claim_id` from trust-bundle | ≥40% within 2 weeks |
| 1.2 | Count of deprecated phrases emitted (log-based) | 0 within 1 week post-deploy |
| 1.3 | `packages.js` ↔ `package-pricing.json` mismatch count | 0 (CI-enforced) |
| 1.4 | Indonesian customers receiving ID replies | ≥90% (sample audit) |
| 2.x | Compiler output bundle versions pinned in `wa_routing_bundle` | 100% |
| 3.x | Wiki gap-report findings sourced from runtime telemetry | ≥5 per month |

---

## 12. Cross-References

- `wiki/ops/whatsapp-reply-intelligence-compiler-spec.md` — P3 compiler spec (this doc's runtime prerequisite for Phase 2)
- `wiki/ops/package-readiness-compiler-spec.md` — Phase 2.3 source
- `wiki/ops/policy-source-ownership.md` — Phase 1.2 source
- `wiki/ops/transformation-map.md` — overall pipeline status
- `wiki/whatsapp/operations-playbook.md` — operational context for CR-07
- `output/website/trust-bundle/_manifest.json` — version pinning reference for Phase 1.1
