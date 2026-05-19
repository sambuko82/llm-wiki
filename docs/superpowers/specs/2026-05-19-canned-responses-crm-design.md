# Spec: JVTO Canned Responses — WA Pro CRM Integration + Off-Hours Auto-Ack

**Date:** 2026-05-19
**Status:** Approved — ready for implementation
**Implementor:** David (IT / WA Pro CRM)
**Source templates:** [[wiki/ops/canned-responses]] (19 scripts, bilingual ID/EN)

---

## Problem

Inan handles all WhatsApp manually without pre-written templates. Discovery, Proposal, and Urgency stages are done ad-hoc — inconsistent quality, high mental load, no SLA tracking. Off-hours messages from European leads (arriving 02:00–06:00 WIB) receive no acknowledgment until morning.

## Solution

Two components:

1. **Quick Reply System** — `canned_responses` table + Laravel API. Inan types `/t1` etc. in WA Pro CRM chat window → template populates in message composer. 19 templates across 6 stages.
2. **Off-Hours Auto-Ack** — Single webhook hook. When new/unknown customer contacts outside 08:00–22:00 WIB → system auto-sends T-3 acknowledgment template.

---

## Component 1: Quick Reply System

### Database

**Table: `canned_responses`** — add to `u1805424_jvto_clone` MySQL database.

```sql
CREATE TABLE canned_responses (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  code            VARCHAR(20)  NOT NULL UNIQUE,
  stage           ENUM('triage','discovery','proposal','urgency','post_booking','objection') NOT NULL,
  channel         ENUM('wa','email','both') NOT NULL,
  name_id         VARCHAR(100) NOT NULL,
  name_en         VARCHAR(100) NOT NULL,
  body_id         TEXT NOT NULL,
  body_en         TEXT NOT NULL,
  bant_component  CHAR(1)      NULL,       -- 'N','T','B','A' or NULL
  is_auto         TINYINT(1)   DEFAULT 0,  -- 1 = system-sent, 0 = human-sent
  is_active       TINYINT(1)   DEFAULT 1,
  sort_order      SMALLINT     DEFAULT 0,
  created_at      TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Seeder

**File:** `database/seeders/CannedResponsesSeeder.php`

Populate from `wiki/ops/canned-responses.md`. Full shortcode registry:

| code | stage | channel | name_en | bant | is_auto |
|------|-------|---------|---------|------|---------|
| `t1` | triage | wa | Welcome + MECE Menu | — | 1 |
| `t2` | triage | wa | Data Collection Prompt | N,T | 1 |
| `t3` | triage | wa | Off-hours Auto-Ack | — | 1 |
| `d1` | discovery | wa | Confirm Need + Timeline | N,T | 0 |
| `d2` | discovery | wa | Budget Tier Check | B | 0 |
| `d3` | discovery | wa | Lock Checklist (internal note) | — | 0 |
| `d4` | discovery | wa | Cold Lead Flag | T | 0 |
| `p1` | proposal | wa | WA Proposal Summary | — | 0 |
| `p2` | proposal | email | Email Quotation Template | — | 0 |
| `u1` | urgency | wa | 24h Validity Reminder | — | 0 |
| `u2` | urgency | wa | Payment Instructions | — | 0 |
| `u3` | urgency | wa | E-Voucher Confirmation | — | 0 |
| `pb1` | post_booking | wa | H-7 Reminder | — | 0 |
| `pb2` | post_booking | wa | H-1 Driver Details | — | 0 |
| `pb3` | post_booking | wa | Post-Tour Review Request | — | 0 |
| `ob1` | objection | wa | "Berapa harga?" handler | — | 0 |
| `ob2` | objection | wa | "Bedanya JVTO?" handler | — | 0 |
| `ob3` | objection | wa | "Refund jika Ijen tutup?" handler | — | 0 |
| `ob4` | objection | wa | "Request jadwal khusus?" handler | — | 0 |

**Total: 19 records.** Each record has full `body_id` and `body_en` from `wiki/ops/canned-responses.md`.

### API Endpoints

Add to Laravel back-office (`new-backoffice.javavolcano-touroperator.com`):

```php
// routes/api.php
Route::get('/canned-responses', [CannedResponseController::class, 'index']);
Route::get('/canned-responses/{code}', [CannedResponseController::class, 'show']);
```

**`GET /api/canned-responses`**
Query params (all optional):
- `?stage=triage` — filter by stage
- `?channel=wa` — filter by channel
- `?code=t1` — filter by code
- `?lang=id|en` — return `body` field in specified language (default: return both `body_id` + `body_en`)

Response:
```json
[
  {
    "code": "t1",
    "stage": "triage",
    "channel": "wa",
    "name": "Welcome + MECE Menu",
    "body_id": "...",
    "body_en": "...",
    "bant_component": null,
    "is_auto": true
  }
]
```

**`GET /api/canned-responses/{code}?lang=en`**
Returns single template. `body` field contains the requested language version.

### CRM UI Integration

In WA Pro CRM chat window (David implements):
- Agent types `/` in message composer → dropdown opens showing all `is_active=1` templates
- Dropdown filterable by typing shortcode (e.g., `/t` shows all triage templates)
- Selecting template → composer shows both `body_id` and `body_en`; Inan picks the right language tab before sending
- Optional future upgrade: auto-detect language from first customer message + store in conversation record

---

## Component 2: Off-Hours Auto-Ack

### Hook Location

Insert into existing webhook handler **before** the existing routing logic:

**File:** `app/Http/Controllers/WebhookController.php` (or equivalent in David's codebase)

```php
public function handleIncoming(Request $request)
{
    $payload = $request->all();
    
    // --- OFF-HOURS AUTO-ACK HOOK ---
    if ($this->isNewContact($payload['from']) && $payload['inbox'] === 'customer') {
        $jakartaHour = Carbon::now('Asia/Jakarta')->hour;
        if ($jakartaHour < 8 || $jakartaHour >= 22) {
            $lang     = $this->detectLanguage($payload['body']); // 'id' or 'en'
            $template = CannedResponse::where('code', 't3')->first();
            $body     = $lang === 'id' ? $template->body_id : $template->body_en;
            
            $this->sendWAMessage($payload['from'], $body);
            $this->logAutoAck($payload['from'], $jakartaHour);
            return response()->json(['status' => 'auto_ack_sent']);
        }
    }
    // --- END HOOK ---
    
    // ... existing routing logic continues unchanged
}
```

### Language Detection

Simple keyword check — no ML/NLP required:

```php
private function detectLanguage(string $text): string
{
    $idKeywords = ['halo', 'selamat', 'apa', 'saya', 'boleh', 'mau', 
                   'bisa', 'ingin', 'paket', 'berapa', 'tolong', 'hai'];
    $lower = strtolower($text);
    foreach ($idKeywords as $word) {
        if (str_contains($lower, $word)) {
            return 'id';
        }
    }
    return 'en'; // default English
}
```

### `isNewContact` Check

```php
private function isNewContact(string $phone): bool
{
    // Returns true if phone not in any known customer/partner tables.
    // David: verify exact table + column names against u1805424_jvto_clone schema.
    // Baseline check — expand as needed:
    return !DB::table('bookings')->where('customer_phone', $phone)->exists()
        && !DB::table('klook_bookings')->where('guest_phone', $phone)->exists();
    // Add window_contacts / other partner tables if they exist in the DB.
}
```

---

## Data Flow

```
WA message received (webhook)
    │
    ├─[new contact + off-hours]──→ send T-3 auto-ack → log → return
    │
    └─[business hours / known contact]──→ existing routing (channel detection, state machine)
    
Inan opens WA Pro CRM chat
    │
    ├─ types "/" in composer
    │       └──→ GET /api/canned-responses → dropdown
    │
    └─ selects template → body populates → Inan edits [NAMA], [TANGGAL] placeholders → send
```

---

## What Stays Human

- **Discovery (d1–d4):** BANT qualification requires judgment — Inan reads context, selects appropriate template, fills placeholders.
- **Proposal (p1–p2):** Pricing requires Sam approval and real-time availability check from `packages-full-pricing`. Inan fetches price, fills `[TOTAL]` placeholder manually.
- **Urgency/Closing (u2):** Payment instruction sent by Inan after Sam/Inan confirms which option customer chose.

---

## Placeholders Convention

Templates contain `[PLACEHOLDER]` markers in UPPERCASE that Inan fills before sending:

Common placeholders: `[NAMA]`, `[TANGGAL]`, `[X PAX]`, `[DESTINASI]`, `[TOTAL]`, `[20% TOTAL]`, `[DEADLINE]`, `[OPSI A/B]`, `[NAMA PENGEMUDI]`, `[NOMOR WA PENGEMUDI]`, `[JAM]`

David can optionally auto-populate from `bookings` table where data is available (e.g., post-booking templates pb1/pb2 know the customer name and tour date).

---

## Verification Checklist

1. `php artisan migrate` runs without error — `canned_responses` table created
2. `php artisan db:seed --class=CannedResponsesSeeder` → 19 rows inserted, all with non-empty `body_id` + `body_en`
3. `GET /api/canned-responses?stage=triage` → returns 3 records (t1, t2, t3)
4. `GET /api/canned-responses/t3?lang=en` → returns T-3 EN text
5. Send WA message to JVTO number at 23:00 WIB from unknown number → T-3 EN auto-reply received within 2 minutes
6. Send WA message at 23:00 WIB from known booking number → no auto-ack (existing flow continues)
7. Send "halo" from unknown number at 23:00 WIB → T-3 **ID** variant received
8. Send "hello" from unknown number at 23:00 WIB → T-3 **EN** variant received
9. CRM chat window: type `/t` → dropdown shows triage templates; select t1 → body populates composer

---

## Files to Create (David's back-office repo)

| File | Action |
|------|--------|
| `database/migrations/xxxx_create_canned_responses_table.php` | CREATE |
| `database/seeders/CannedResponsesSeeder.php` | CREATE |
| `app/Models/CannedResponse.php` | CREATE |
| `app/Http/Controllers/CannedResponseController.php` | CREATE |
| `routes/api.php` | UPDATE — add 2 routes |
| `app/Http/Controllers/WebhookController.php` | UPDATE — add off-hours hook |

---

## Source References

- Template content: `wiki/ops/canned-responses.md` (19 templates, all verbatim)
- Framework theory: `wiki/sources/comm-management-theory.md`
- WA Pro CRM context: `wiki/ops/2026-05-14-whatsapp-operations-playbook.md` §2.2, §6 Flow A
- Business hours: `wiki/content/operational-facts.md` §customer-support (08:00–22:00 WIB)
