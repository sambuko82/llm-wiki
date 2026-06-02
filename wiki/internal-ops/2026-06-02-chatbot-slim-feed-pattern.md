---
type: internal-ops
title: Chatbot ↔ LLM-Wiki — Slim Feed Pattern (Efficient Middle Ground)
last_updated: 2026-06-02
sources: [chatbot-web-jvto-repo-snapshot-2026-06-02, whatsapp-reply-intelligence-compiler-spec, package-readiness-compiler-spec, policy-source-ownership, trust-bundle-v1, 2026-06-02-chatbot-llmwiki-integration-audit]
owner: wiki-llm
stale_after_days: 60
supersedes_planning: 2026-06-02-chatbot-llmwiki-integration-audit §5 Phase 1/2/3 (those phases preserved as long-term ambition; this doc defines the slim near-term path)
---

# Slim Feed Pattern — Efficient Chatbot ↔ Wiki Integration

> Audit hari ini (`2026-06-02-chatbot-llmwiki-integration-audit.md`) menemukan 10 critical findings dan menulis 3-phase roadmap (~12 minggu). Doc ini menyaring temuan itu menjadi **pola minimal yang tetap menutup risiko utama**, dengan menghormati chatbot sebagai sistem produksi yang sudah berjalan.

## 1. Insight Pemicu

| Pertanyaan | Jawaban |
|---|---|
| Apa yang chatbot **benar-benar konsumsi** untuk tiap reply? | (a) FAQ knowledge text untuk grounding LLM, (b) `packages.js` `PACKAGES[]` array untuk funnel, (c) template strings dari `settings.templates.*` untuk auto-reply, (d) `settings.knowledge.faqBase` sebagai fallback |
| Apa yang chatbot **tidak konsumsi** dari P3 spec saya? | 33-state machine, 6-channel routing, bilingual templates (English-only by design), hard-rules JSON (funnel sudah punya guard sendiri), trust-attached/package-attached pre-rendered replies (chatbot pakai BM25 + LLM, bukan template injection) |
| Apa yang chatbot **butuh tapi tidak punya**? | (a) Authoritative claim text untuk verbatim citation, (b) Up-to-date pricing tanpa manual paste, (c) Deprecated-phrase enforcement, (d) Boot-time access ke compiled wiki output (bukan markdown text) |
| Apa **dead code** yang sudah teridentifikasi? | `src/systemPrompt.js` — zero imports across `src/`, `app/`, `components/`, `lib/`. Confirmed grep result: empty. Safe to delete. |

**Kesimpulan:** P3 compiler spec saya (12 output artifact) **overkill** untuk consumer yang sebenarnya. Yang dibutuhkan adalah **3 file output** yang slot langsung ke jalur konsumsi chatbot yang sudah ada.

---

## 2. The Slim Feed Pattern

```
LLM-WIKI (producer)              CHATBOT (consumer)
─────────────────                ─────────────────
compiled bundles                 existing runtime
(trust + package readiness)      (BM25 + funnel + dual LLM)
        │
        ▼
  [Slim Feed Compiler]
        │
        ▼
output/whatsapp/chatbot-feed/    ──pull──>  knowledge_entries (source='llm-wiki-feed')
  knowledge.jsonl                ──pull──>  src/packages.js (gitignored, regenerated)
  packages-data.json             ──pull──>  in-memory guardrails cache
  guardrails.json
  _manifest.json
```

**Nama pattern:** `Slim Feed Contract` — minimal producer→consumer contract antara 2 repo, satu kompiler kecil, satu sync route, tanpa breaking change ke runtime chatbot.

### Prinsip

1. **Reuse, don't rewrite.** Compiler **tidak compile ulang** trust-bundle/package-readiness — keduanya sudah DONE. Compiler hanya **reshape + slim** output yang sudah ada agar pas dengan shape konsumen.
2. **One compiler, one sync route, three artifacts.** Bukan 12 artifact, bukan 6 wedge. Satu.
3. **Consumer interface preserved.** `PACKAGES`, `filterPackages`, `buildPackageReply`, `getPriceForPax`, `formatPriceTiers` exports dari `packages.js` tetap. Hanya **isi `PACKAGES` array** yang di-generate.
4. **BM25 retrieval is fine.** Chatbot pakai token-overlap, jangan paksa vector embeddings. Knowledge feed di-shape untuk BM25 (title yang descriptive, tags yang ke-tokenize, content paragraf).
5. **Guardrails as data, not framework.** Forbidden phrases = JSON list + replacement suggestion. Cek di 1 function. Bukan rule engine.

---

## 3. Compiler Spec — `scripts/compile_chatbot_feed.py`

### 3.1 Inputs (semua sudah ada, tidak ada wiki canonical baru)

| Input | Path | Reused from |
|---|---|---|
| Claims | `output/website/trust-bundle/claims.json` | Trust Bundle v1 |
| Policies | `output/website/trust-bundle/policies.json` | Trust Bundle v1 |
| People | `output/website/trust-bundle/people.json` | Trust Bundle ext |
| Destinations | `output/website/trust-bundle/destinations.json` | Trust Bundle ext |
| FAQ | `output/website/trust-bundle/faq.json` + `output/website/faq/*.md` | Trust Bundle + Website Logic |
| Operational | `output/website/trust-bundle/operational.json` | Trust Bundle ext |
| Package registry | `output/products/package-readiness/package-registry.json` | Package Readiness v1.2 |
| Package pricing | `output/products/package-readiness/package-pricing.json` | Package Readiness v1.2 |
| Booking compatibility | `output/products/package-readiness/booking-compatibility.json` | Package Readiness v1.2 |
| Deprecated wording | `wiki/ops/policy-source-ownership.md` §deprecated-wording | Policy SSOT |

**Catatan:** compiler ini tidak baca `wiki/whatsapp/*.md`. Itu untuk P3 lengkap nanti. Sekarang chatbot tidak butuh routing/templates/states dari wiki — chatbot punya yang sendiri yang sudah work.

### 3.2 Outputs (3 file + manifest)

```
output/whatsapp/chatbot-feed/
├── knowledge.jsonl           (~80 KB) — flat knowledge for BM25 ingestion
├── packages-data.json        (~24 KB) — pure data, drops into packages.js refactor
├── guardrails.json           (~4 KB)  — forbidden phrases + replacement hints
└── _manifest.json
```

#### `knowledge.jsonl` (one JSON object per line)

Shape compatible langsung dengan `knowledgeStore.upsertMany(entries, 'llm-wiki-feed')`:

```jsonl
{"id":"trust-claim-C1","title":"Safety-Led Operations","content":"Volcano travel is unpredictable, so JVTO focuses on operational certainty: disciplined decisions, clear safety boundaries, and realistic expectations.","domain":"credentials","tags":["claim_id:C1","trust","safety","verified"],"verbatim_lock":true}
{"id":"trust-claim-C2","title":"Police-Led Founding","content":"Founder Agung Sambuko is an active Tourist Police officer (Ditpamobvit)...","domain":"credentials","tags":["claim_id:C2","tourist-police","founder","verified"],"verbatim_lock":true}
{"id":"trust-policy-deposit","title":"Booking Deposit Policy","content":"20% deposit confirms booking; balance due 3 days before Day 1 via Bank Transfer/Wise...","domain":"website","tags":["policy","booking","deposit"],"verbatim_lock":true}
{"id":"trust-people-dr-irwandanu","title":"Medical Officer — Dr Ahmad Irwandanu","content":"Licensed physician...","domain":"people","tags":["doctor","screening","ijen"],"verbatim_lock":true}
{"id":"trust-dest-ijen","title":"Kawah Ijen — Key Facts","content":"...","domain":"destinations","tags":["ijen","destination"],"verbatim_lock":true}
{"id":"package-bromo-1d1n","title":"1-Day Bromo Midnight Experience — Quick Facts","content":"Surabaya → Bromo same-day, ~16-hour tour, IDR pricing tiered 1M–1.55M/pax...","domain":"products","tags":["package","slug:tours/from-surabaya/bromo-1d1n","surabaya","bromo","1d1n"],"verbatim_lock":false}
```

Notes:
- `verbatim_lock: true` → renderer must boost retrieval score AND instruct LLM "use this text exactly, do not paraphrase"
- `claim_id:Cx` di tags → enables future audit "did this reply cite C2?"
- `slug:tours/...` di tags → links knowledge ke package routing
- Domain mirrors chatbot's existing `DOMAIN_ORDER`: `destinations, products, people, credentials, website, whatsapp, general`

#### `packages-data.json` (drop-in for refactored `packages.js`)

```json
{
  "compiled_at": "2026-06-02T...",
  "source_versions": { "package-readiness": "1.2" },
  "packages": [
    {
      "id": 73,
      "name": "1 Day Bromo Midnight Experience",
      "from": "Surabaya", "to": "Surabaya",
      "days": 1, "nights": 1,
      "startFrom": 1000000,
      "slug": "tours/from-surabaya/bromo-1d1n",
      "physicality": "moderate",
      "keyExperiences": ["Bromo Sunrise Tour"],
      "highlights": [...],
      "priceTiers": [
        { "name": "11+ Pax", "minPax": 11, "maxPax": 0, "pricePerPerson": 1000000 },
        ...
      ]
    },
    ... 15 more packages
  ]
}
```

Shape **identik** dengan `src/packages.js` current `PACKAGES` array. Generated dari `package-registry.json` (slug, origin, destinations) + `package-pricing.json` (priceTiers) + `package-itineraries.json` (highlights, keyExperiences) + `booking-compatibility.json` (physicality estimation).

#### `guardrails.json`

```json
{
  "compiled_at": "2026-06-02T...",
  "source": "wiki/ops/policy-source-ownership.md §deprecated-wording",
  "forbidden_phrases": [
    {
      "id": "F-BLUE-FIRE-GUARANTEE",
      "pattern_regex": "(?i)blue\\s*fire\\s+(?:is\\s+)?(?:guaranteed|certain|sure|will\\s+(?:be\\s+)?(?:visible|appear))",
      "severity": "block",
      "replacement_hint": "Blue Fire is a natural phenomenon — visibility depends on weather, volcanic activity, and authority clearance. Even without it, the sunrise and crater lake are spectacular.",
      "context_required": "blue fire"
    },
    {
      "id": "F-MADAKARIPURA-HELMET",
      "pattern_regex": "(?i)helmet\\s+(?:is\\s+)?included.*madakaripura|madakaripura.*helmet\\s+(?:is\\s+)?included",
      "severity": "block",
      "replacement_hint": "At Madakaripura, helmets are provided by the local site management — not part of JVTO inclusions.",
      "context_required": "madakaripura"
    },
    {
      "id": "F-POLICE-ESCORT-DEFAULT",
      "pattern_regex": "(?i)police\\s+escort\\s+(?:is\\s+)?(?:included|default|standard)",
      "severity": "block",
      "replacement_hint": "Tourist Police support is available where regulations require, not on every tour by default.",
      "context_required": null
    },
    {
      "id": "F-50PCT-FEE",
      "pattern_regex": "(?i)50\\s*%\\s*(?:admin|cancellation)\\s*fee",
      "severity": "block",
      "replacement_hint": "Cancellation: see policy — refund schedule depends on notice period before Day 1.",
      "context_required": null
    },
    {
      "id": "F-CASH-REFUND",
      "pattern_regex": "(?i)cash\\s+refund",
      "severity": "block",
      "replacement_hint": "Refunds are processed via the original payment method (Bank Transfer/Wise).",
      "context_required": null
    },
    {
      "id": "F-TRIPDOTCOM",
      "pattern_regex": "(?i)trip\\.com|booking\\s+via\\s+trip",
      "severity": "block",
      "replacement_hint": "Booking is via our website self-checkout or WhatsApp-assisted — not Trip.com.",
      "context_required": null
    }
  ],
  "escalation_triggers": [
    { "id": "E-LEGAL-CONCERN", "pattern_regex": "(?i)\\b(lawyer|legal\\s+action|sue|police\\s+report)\\b", "action": "escalate_sam_urgent" },
    { "id": "E-EMERGENCY", "pattern_regex": "(?i)\\b(emergency|accident|injured|hospital|ambulance)\\b", "action": "alert_inan_and_sam_urgent" }
  ]
}
```

`context_required` mencegah false positives — "Blue Fire" sebagai topik OK, "Blue Fire guaranteed" tidak OK.

### 3.3 Validation (4 rules, bukan 16)

| ID | Severity | Rule |
|---|---|---|
| FEED-01 | error | Setiap claim di `claims.json` muncul di `knowledge.jsonl` dengan `verbatim_lock: true` |
| FEED-02 | error | Setiap package di `package-registry.json` muncul di `packages-data.json` dengan slug + pricing tier match exact |
| FEED-03 | error | Setiap forbidden_phrase punya `id`, `pattern_regex` yang valid, `replacement_hint` non-empty |
| FEED-04 | warn | `_manifest.json` pin trust-bundle version + package-readiness version; refuse re-emit if upstream version berbeda dari last successful |

### 3.4 Effort estimate

| Komponen | Effort |
|---|---|
| Compiler (loader + 3 renderer + validator + CLI) | 8–10 jam |
| Test corpus + happy path E2E | 4 jam |
| Documentation (README in `output/whatsapp/chatbot-feed/`) | 1 jam |
| **Total compiler side** | **~13–15 jam** |

---

## 4. Chatbot Integration — 3 Pull Points

### 4.1 Pull Point #1: knowledge.jsonl → DB

Extend `app/api/knowledge/sync/route.ts`. Tambah blok setelah existing wiki sync:

```ts
// After existing wiki .md sync (line ~120 of route.ts)
const feedDir = path.join(SYNC_DIR, 'output/whatsapp/chatbot-feed')
if (fs.existsSync(feedDir)) {
  const jsonlPath = path.join(feedDir, 'knowledge.jsonl')
  if (fs.existsSync(jsonlPath)) {
    const lines = fs.readFileSync(jsonlPath, 'utf8').split('\n').filter(Boolean)
    const feedEntries = lines.map(line => {
      const r = JSON.parse(line)
      return {
        id: r.id,
        title: r.title,
        content: r.content,
        domain: r.domain,
        tags: r.tags,
        verbatimLock: r.verbatim_lock,
        lastUpdated: new Date().toISOString(),
      }
    })
    await knowledgeStore.upsertMany(feedEntries, 'llm-wiki-feed')
  }
}
```

**Effort:** 2 jam. Reuse existing `upsertMany` mechanic.

### 4.2 Pull Point #2: packages-data.json → src/packages.js

**Option C (recommended) — minimal touch refactor:**

1. Move data out of `src/packages.js` ke `src/packages-data.json` (gitignored)
2. `src/packages.js` becomes:

```js
// src/packages.js — functions only; data injected at boot
const fs = require('fs');
const path = require('path');

let PACKAGES = [];
try {
  const dataPath = path.join(__dirname, 'packages-data.json');
  const raw = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
  PACKAGES = raw.packages || [];
  console.log(`[packages] Loaded ${PACKAGES.length} packages from feed v${raw.source_versions?.['package-readiness']}`);
} catch (e) {
  console.error('[packages] Failed to load packages-data.json — using empty list. Run sync.', e.message);
}

function filterPackages(criteria) { /* unchanged */ }
function buildPackageReply(pkgList) { /* unchanged */ }
function getPriceForPax(pkg, pax) { /* unchanged */ }
function formatPriceTiers(pkg) { /* unchanged */ }

module.exports = { PACKAGES, filterPackages, buildPackageReply, getPriceForPax, formatPriceTiers };
```

3. Sync route extended to copy `chatbot-feed/packages-data.json` → `src/packages-data.json` after pulling repo
4. `.gitignore` adds `src/packages-data.json`
5. Boot reads file once, functions unchanged

**Effort:** 3 jam (refactor + sync wire-up + verification). Zero breaking change to callers (orderFlow unchanged).

### 4.3 Pull Point #3: guardrails.json → outbound filter

Tambah `src/guardrails.js`:

```js
let _cache = null;

async function load() {
  // Read from sync directory after sync; cache in memory
  // ...
}

function check(message) {
  // Returns { blocked: false } or { blocked: true, replacement_hint, rule_id }
}

function checkEscalation(message) {
  // Returns null or { action, rule_id }
}

module.exports = { load, check, checkEscalation };
```

Wire in `src/chatbot.js` `callLLM()`:

```js
const guardrails = require('./guardrails');

// After receiving LLM response, before returning to caller
async function callLLM(...args) {
  // ... existing ollama call
  const answer = res.data?.message?.content?.trim() || "";

  // NEW: guardrail filter
  const check = guardrails.check(answer);
  if (check.blocked) {
    console.warn(`[guardrails] Blocked: ${check.rule_id}`);
    return check.replacement_hint + nudge;
  }
  return answer + nudge;
}
```

And in `chatWithBot()` for inbound escalation:

```js
const escal = guardrails.checkEscalation(message);
if (escal) {
  setHumanHandoff(userId);
  // ... existing handoff flow
}
```

**Effort:** 4 jam.

### 4.4 Dead code cleanup

Delete `src/systemPrompt.js` (zero imports confirmed). **Effort:** 5 minutes.

### 4.5 Chatbot integration total

| Task | Effort |
|---|---|
| Pull #1 knowledge.jsonl ingestion | 2 h |
| Pull #2 packages refactor + sync | 3 h |
| Pull #3 guardrails module + wire-in | 4 h |
| Dead code delete + test | 1 h |
| Manual E2E test (10 messages) | 2 h |
| **Total chatbot side** | **~12 h** |

---

## 5. Total Effort vs Earlier Plan

| Approach | Wiki effort | Chatbot effort | Calendar time | Risk closed |
|---|---|---|---|---|
| **Slim Feed (this doc)** | 13–15 h | ~12 h | **~1 week solo** | CR-01 ✓, CR-02 ✓, CR-04 (knowledge precedence) ✓, CR-09 ✓ |
| Earlier Phase 1 (audit doc) | 0 h | ~25 h | 1–2 weeks | Same risks closed, plus CR-03 (bilingual heuristic) |
| Earlier Phase 1+2 | 34–46 h (P3 spec) | ~40 h | 8–10 weeks | All 10 CRs |
| Earlier full plan (Phases 1+2+3) | ~50 h | ~80 h | 3 months | All + feedback loop |

**Slim Feed menutup 4 dari 10 CR dengan ~25 jam total (vs 130 jam untuk full plan).** Sisa CR (bilingual, OpenAI Assistant opacity, number_key routing, telemetry, DB credential) tetap real risks tapi tidak block deployment dan bisa ditangani kemudian saat ada business trigger.

---

## 6. What Slim Feed Does NOT Address (And That's OK For Now)

| CR | Reason to defer |
|---|---|
| CR-03 Bilingual gap | Chatbot saat ini melayani audience yang chat-nya didominasi English (whitelist mode + filter non-Indonesia). Bilingual = future business trigger, bukan urgent fix. |
| CR-05 OpenAI Assistant opacity | Gpts path runs separately; sebelum chatbot beralih ke local-only atau Assistant migration, biarkan. Audit log Assistant outputs untuk monitoring. |
| CR-06 DB credential in repo | Security hygiene — sebaiknya jalan paralel sebagai task terpisah (rotate + `.env` only), bukan bagian wiki integration. |
| CR-07 number_key inbox routing | Hanya relevan kalau JVTO punya >1 nomor WA aktif sekarang. Konfirmasi dulu — kalau iya, baru build inbox-router (subset dari full P3 spec). |
| CR-08 Telemetry feedback | Nice-to-have. Bisa diship terpisah sebagai nightly cronjob — tidak butuh dependency apapun. |
| CR-10 Blacklist correct anyway | Tidak perlu diubah — blacklist intentional. |

---

## 7. New Shared Flow (visualized)

```
[wiki canonical]                  [chatbot runtime]
     │                                   │
     ▼                                   │
  trust-bundle                           │
  package-readiness   (existing,         │
  policy-source-       DONE)             │
   ownership                             │
     │                                   │
     ▼                                   │
[Slim Feed Compiler] (NEW, ~14 h)        │
     │                                   │
     ▼                                   │
output/whatsapp/                         │
  chatbot-feed/                          │
    knowledge.jsonl ──────sync route─────┼──> knowledge_entries (boost ×3)
    packages-data.json ──sync route──────┼──> src/packages-data.json
    guardrails.json ─────sync route──────┼──> guardrails cache
     │                                   │
     ▼                                   ▼
  _manifest.json                  [existing runtime]
  (version pin)                   - orderFlow.js (10 states)
                                  - BM25 retrieval
                                  - Ollama + OpenAI dual path
                                  - whatsappSender
                                  - bookingApiClient

       (optional Phase 2 — only when business need triggers)
       ────────────────────────────────────────────────────
       full P3 spec → output/whatsapp/reply-intelligence/
       12 artifacts: routing, intents, states, templates...
```

**Pattern characteristics:**
- One-way pull (chatbot pulls from wiki output)
- Version-pinned reuse (manifest tracks upstream bundle versions)
- Drop-in shape (no chatbot interface changes — `PACKAGES`, retrieval entries, filter middleware)
- Backwards compatible (existing manual `source='manual'` entries preserved; feed is additional source with high BM25 boost)
- Reversible (sync failure = chatbot falls back to in-DB cached previous feed + `settings.knowledge.faqBase`)

---

## 8. P3 Spec Status After This Doc

The `wiki/ops/whatsapp-reply-intelligence-compiler-spec.md` saya tulis sebelumnya **tetap valid sebagai aspirasi**. Slim Feed adalah **subset minimal** dari P3:

| P3 artifact | Slim Feed equivalent | Defer status |
|---|---|---|
| `inbox-router.json` | — | Defer (CR-07 trigger needed) |
| `channel-router.json` | — | Defer |
| `state-machine.json` | — | Chatbot has its own |
| `intents.json` | — | Defer |
| `routing.json` | — | Defer |
| `actions.json` | — | Defer |
| `templates.json` | — | Defer (CR-03 bilingual trigger) |
| `package-attached-replies.json` | `packages-data.json` (slim) | **Slim ships** |
| `trust-attached-replies.json` | `knowledge.jsonl` with `verbatim_lock` | **Slim ships (different shape)** |
| `sla-matrix.json` | — | Defer |
| `hard-rules.json` | `guardrails.json` (slim) | **Slim ships (forbidden phrases only)** |
| `gap-report.json` | Optional — `_manifest.json` carries validation summary | Defer detailed gap report |

**Recommendation:** treat Slim Feed sebagai **Phase 0** dari P3 implementation. Saat business butuh 6-channel routing atau bilingual templates, kembali ke P3 spec untuk artifact yang tersisa.

Update register di `wiki/ops/transformation-map.md`:

```
| Bundle | Status | Priority |
| WhatsApp Reply Intelligence (Slim Feed) | NEXT (P3-A) | P3 — slim subset |
| WhatsApp Reply Intelligence (Full P3) | FUTURE (P3-B) | when business triggers |
```

---

## 9. Decision Points for Sam (Trimmed)

1. **Build Slim Feed compiler this week?** ~14 jam wiki side + ~12 jam chatbot side = ~3 day-job total.
2. **Confirm dead code delete `src/systemPrompt.js`** — saya verified zero imports; safe.
3. **Confirm refactor strategy untuk `packages.js`** — Option C (data JSON + functions) recommended; alternative Option B = generate whole .js file (faster bootstrap, less clean).
4. **`.gitignore` `src/packages-data.json`?** Yes (it's generated artifact). Chatbot repo will need this line added.
5. **First sync source-of-truth bundle versions?** Pin trust-bundle@1.0 + package-readiness@1.2 (current). Refuse to re-emit if upstream changes minor without explicit acknowledgement.

---

## 10. Next Concrete Step

If Sam approves:

1. **Wiki side (day 1–2):**
   - Build `scripts/compile_chatbot_feed.py` reading 6 inputs above
   - Emit 3 outputs + manifest to `output/whatsapp/chatbot-feed/`
   - Run `--dry-run` against current trust-bundle + package-readiness; review knowledge.jsonl + packages-data.json sample
   - Register slim wedge in `wiki/ops/transformation-map.md`

2. **Chatbot side (day 3–4):**
   - Branch `feature/slim-feed-integration`
   - Refactor `src/packages.js` to read `packages-data.json`
   - Extend `app/api/knowledge/sync/route.ts` for 3 new pull points
   - Add `src/guardrails.js` + wire-in
   - Delete `src/systemPrompt.js`
   - Test against staging WA webhook (10-message corpus)

3. **Verification (day 5):**
   - Compare BM25 retrieval results before/after feed ingestion (manual diff)
   - Trigger 5 forbidden phrases → confirm guardrail blocks
   - Trigger price quote → confirm sourced from feed not hardcoded
   - Confirm `wiki/log.md` entry: `## [2026-06-XX] feature | Slim Feed shipped`
