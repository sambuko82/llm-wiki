# JVTO Canned Responses — WA Pro CRM Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `canned_responses` table + API to the Laravel back-office so Inan can use shortcode templates in WA Pro CRM, and the webhook automatically sends an off-hours acknowledgment to new contacts outside 08:00–22:00 WIB.

**Architecture:** MySQL table stores 19 bilingual (ID/EN) templates keyed by shortcode. A thin Laravel API serves them to the CRM frontend. A single hook inserted at the top of the existing webhook handler handles off-hours auto-ack by querying the `t3` template from the same table.

**Tech Stack:** Laravel 10.x · PHPUnit · MySQL (`u1805424_jvto_clone`) · Carbon for timezone-aware time checks

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `database/migrations/xxxx_create_canned_responses_table.php` | CREATE | Table DDL |
| `app/Models/CannedResponse.php` | CREATE | Eloquent model, `findByCode()` scope |
| `database/seeders/CannedResponsesSeeder.php` | CREATE | 19 template records |
| `database/seeders/DatabaseSeeder.php` | MODIFY | Call `CannedResponsesSeeder` |
| `app/Http/Controllers/CannedResponseController.php` | CREATE | `index()` + `show()` actions |
| `routes/api.php` | MODIFY | 2 new GET routes |
| `app/Http/Controllers/WebhookController.php` | MODIFY | Off-hours hook (top of `handleIncoming`) |
| `tests/Feature/CannedResponseApiTest.php` | CREATE | API endpoint feature tests |
| `tests/Unit/WebhookHelperTest.php` | CREATE | `detectLanguage` + `isNewContact` unit tests |
| `tests/Feature/OffHoursAutoAckTest.php` | CREATE | Off-hours webhook integration test |

---

## Task 1 — Migration

**Files:**
- Create: `database/migrations/xxxx_create_canned_responses_table.php`

- [ ] **Step 1: Generate migration**

```bash
php artisan make:migration create_canned_responses_table
```

- [ ] **Step 2: Write migration content**

Open the generated file and replace its content:

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::create('canned_responses', function (Blueprint $table) {
            $table->id();
            $table->string('code', 20)->unique();
            $table->enum('stage', ['triage','discovery','proposal','urgency','post_booking','objection']);
            $table->enum('channel', ['wa','email','both']);
            $table->string('name_id', 100);
            $table->string('name_en', 100);
            $table->text('body_id');
            $table->text('body_en');
            $table->char('bant_component', 1)->nullable();
            $table->tinyInteger('is_auto')->default(0);
            $table->tinyInteger('is_active')->default(1);
            $table->smallInteger('sort_order')->default(0);
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('canned_responses');
    }
};
```

- [ ] **Step 3: Run migration**

```bash
php artisan migrate
```

Expected output contains: `create_canned_responses_table ... DONE`

- [ ] **Step 4: Verify table exists**

```bash
php artisan tinker --execute="Schema::hasTable('canned_responses') ? 'OK' : 'MISSING';"
```

Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add database/migrations/
git commit -m "feat: add canned_responses migration"
```

---

## Task 2 — Model

**Files:**
- Create: `app/Models/CannedResponse.php`

- [ ] **Step 1: Generate model**

```bash
php artisan make:model CannedResponse
```

- [ ] **Step 2: Write model**

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Builder;

class CannedResponse extends Model
{
    protected $fillable = [
        'code', 'stage', 'channel', 'name_id', 'name_en',
        'body_id', 'body_en', 'bant_component', 'is_auto',
        'is_active', 'sort_order',
    ];

    protected $casts = [
        'is_auto'   => 'boolean',
        'is_active' => 'boolean',
    ];

    public function scopeActive(Builder $query): Builder
    {
        return $query->where('is_active', 1);
    }

    public function scopeForStage(Builder $query, string $stage): Builder
    {
        return $query->where('stage', $stage);
    }

    public function scopeForChannel(Builder $query, string $channel): Builder
    {
        return $query->where('channel', $channel);
    }

    public static function findByCode(string $code): ?self
    {
        return static::where('code', $code)->where('is_active', 1)->first();
    }

    public function bodyFor(string $lang): string
    {
        return $lang === 'id' ? $this->body_id : $this->body_en;
    }
}
```

- [ ] **Step 3: Commit**

```bash
git add app/Models/CannedResponse.php
git commit -m "feat: add CannedResponse model"
```

---

## Task 3 — Seeder

**Files:**
- Create: `database/seeders/CannedResponsesSeeder.php`
- Modify: `database/seeders/DatabaseSeeder.php`

**Source for body_id / body_en text:** `wiki/ops/canned-responses.md` in the llm-wiki repo. Each section maps to one shortcode. Copy verbatim — templates contain `[PLACEHOLDER]` markers Inan fills before sending.

- [ ] **Step 1: Create seeder file**

```bash
php artisan make:seeder CannedResponsesSeeder
```

- [ ] **Step 2: Write seeder**

```php
<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\CannedResponse;

class CannedResponsesSeeder extends Seeder
{
    public function run(): void
    {
        $templates = [
            // ── TRIAGE ───────────────────────────────────────────────────────
            [
                'code'    => 't1', 'stage' => 'triage', 'channel' => 'wa',
                'name_id' => 'Welcome + Menu MECE', 'name_en' => 'Welcome + MECE Menu',
                'bant_component' => null, 'is_auto' => 1, 'sort_order' => 10,
                'body_id' => "Halo! Selamat datang di JVTO — Java Volcano Tour Operator. 🌋\n\nKami operator tur privat East Java yang didirikan oleh Bripka Agung Sambuko, anggota aktif Tourist Police.\nSemua tur 100% privat — tidak ada grup gabungan.\n\nBoleh kami tahu Anda butuh bantuan untuk apa?\n\n[1] 🗺️ Tanya Paket Wisata (Ijen, Bromo, Tumpak Sewu, dll.)\n[2] 📋 Status Booking Aktif (sudah booking, perlu info lanjutan)\n[3] 🤝 Kemitraan / B2B (travel agent, reseller)\n\nBalas dengan angka pilihannya ya!",
                'body_en' => "Hello! Welcome to JVTO — Java Volcano Tour Operator. 🌋\n\nWe're a private tour operator in East Java, founded by Bripka Agung Sambuko, an active Tourist Police officer.\nEvery tour is 100% private — no shared groups, ever.\n\nHow can we help you today?\n\n[1] 🗺️ Tour Package Inquiry (Ijen, Bromo, Tumpak Sewu, etc.)\n[2] 📋 Active Booking Status (already booked, need info or assistance)\n[3] 🤝 Partnership / B2B (travel agent, reseller)\n\nJust reply with the number of your choice!",
            ],
            [
                'code'    => 't2', 'stage' => 'triage', 'channel' => 'wa',
                'name_id' => 'Kumpulkan Data Awal', 'name_en' => 'Data Collection Prompt',
                'bant_component' => 'N', 'is_auto' => 1, 'sort_order' => 20,
                'body_id' => "Siap! Untuk kami carikan paket yang paling sesuai, boleh share info berikut:\n\n1. 👤 Nama Anda\n2. 🌋 Destinasi yang diminati: Kawah Ijen / Bromo / Tumpak Sewu / Madakaripura / kombinasi?\n3. 📅 Tanggal rencana perjalanan (atau kisaran bulan)\n4. 👥 Jumlah peserta\n\nTim kami akan membalas dalam jam kerja kami: 08:00–22:00 WIB (UTC+7).",
                'body_en' => "Great! To find the best package for you, could you share the following:\n\n1. 👤 Your name\n2. 🌋 Destination(s) of interest: Kawah Ijen / Bromo / Tumpak Sewu / Madakaripura / combination?\n3. 📅 Planned travel date (or approximate month)\n4. 👥 Number of travelers\n\nOur team will reply during business hours: 08:00–22:00 WIB (UTC+7).",
            ],
            [
                'code'    => 't3', 'stage' => 'triage', 'channel' => 'wa',
                'name_id' => 'Auto-Ack di Luar Jam Kerja', 'name_en' => 'Off-hours Auto-Acknowledgment',
                'bant_component' => null, 'is_auto' => 1, 'sort_order' => 30,
                'body_id' => "Halo! Terima kasih sudah menghubungi JVTO. 🌋\n\nPesan Anda sudah kami terima. Tim kami akan membalas segera saat jam kerja dimulai: 08:00 WIB.\n\nSementara menunggu, Anda bisa melihat semua paket tur kami di:\n👉 javavolcano-touroperator.com\n\nSampai jumpa!",
                'body_en' => "Hello! Thank you for reaching out to JVTO. 🌋\n\nWe've received your message. Our team will reply as soon as business hours begin: 08:00 WIB (UTC+7).\n\nWhile you wait, you can browse all our tour packages at:\n👉 javavolcano-touroperator.com\n\nTalk soon!",
            ],
            // ── DISCOVERY ────────────────────────────────────────────────────
            [
                'code'    => 'd1', 'stage' => 'discovery', 'channel' => 'wa',
                'name_id' => 'Konfirmasi Kebutuhan + Timeline', 'name_en' => 'Confirm Need + Timeline',
                'bant_component' => 'N', 'is_auto' => 0, 'sort_order' => 40,
                'body_id' => "Halo [NAMA]! Saya Inan dari tim JVTO. 😊\n\nTerima kasih sudah tertarik dengan [DESTINASI]. Beberapa pertanyaan singkat supaya kami bisa buatkan penawaran yang tepat:\n\n1. Tanggalnya sudah pasti, atau masih tentatif?\n2. Ini untuk perjalanan pribadi, keluarga, atau kelompok wisata?\n3. Untuk paket Ijen — apakah Anda dan peserta lain dalam kondisi fisik yang fit untuk mendaki sekitar 1–2 jam malam hari? (Kami ada skrining medis opsional yang kami koordinasikan sebelumnya.)\n\nSatu pertanyaan lagi: apakah Anda yang akan mengkonfirmasi dan membayar booking ini, atau ada anggota tim/keluarga lain yang perlu dikonsultasikan dulu?",
                'body_en' => "Hello [NAME]! I'm Inan from the JVTO team. 😊\n\nThanks for your interest in [DESTINATION]. A few quick questions so we can put together the right proposal:\n\n1. Is your travel date confirmed, or still tentative?\n2. Is this a personal trip, family, or group tour?\n3. For Ijen packages — are you and your fellow travelers physically fit for approximately 1–2 hours of night hiking? (We coordinate a medical screening beforehand as standard.)\n\nOne more: will you be the one confirming and paying the booking, or does someone else in your group or family need to be consulted first?",
            ],
            [
                'code'    => 'd2', 'stage' => 'discovery', 'channel' => 'wa',
                'name_id' => 'Cek Tier Akomodasi (Budget Proxy)', 'name_en' => 'Budget Tier Check',
                'bant_component' => 'B', 'is_auto' => 0, 'sort_order' => 50,
                'body_id' => "Untuk akomodasi, JVTO bekerja sama dengan hotel-hotel di titik-titik singgah tur.\nApakah Anda lebih suka hotel bintang 3 (nyaman, praktis) atau bintang 4 ke atas (lebih luas dan premium)?\n\nIni akan mempengaruhi total harga paket — kami akan tampilkan keduanya di penawaran.",
                'body_en' => "For accommodation, JVTO works with hotels at each stop along the route.\nWould you prefer 3-star hotels (comfortable, practical) or 4-star and above (more spacious, premium quality)?\n\nThis affects the total package price — we'll show you both options in the proposal.",
            ],
            [
                'code'    => 'd3', 'stage' => 'discovery', 'channel' => 'wa',
                'name_id' => 'Checklist Kunci (Catatan Internal)', 'name_en' => 'Lock Checklist (Internal Note)',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 55,
                'body_id' => "INTERNAL — jangan kirim ke customer.\n\nChecklist sebelum buat quotation:\n[ ] Tanggal pasti terkunci\n[ ] Jumlah pax terkonfirmasi\n[ ] Preferensi hotel (standard / premium)\n[ ] Origin: Surabaya atau Bali?\n\nKalau belum semua, kembali ke d1 atau d2.",
                'body_en' => "INTERNAL — do not send to customer.\n\nChecklist before creating quotation:\n[ ] Confirmed departure date\n[ ] Confirmed pax count\n[ ] Hotel preference (standard / premium)\n[ ] Origin: Surabaya or Bali?\n\nIf not all confirmed, go back to d1 or d2.",
            ],
            [
                'code'    => 'd4', 'stage' => 'discovery', 'channel' => 'wa',
                'name_id' => 'Flag Cold Lead (Tanggal Tentatif)', 'name_en' => 'Cold Lead Flag',
                'bant_component' => 'T', 'is_auto' => 0, 'sort_order' => 60,
                'body_id' => "Oke, tidak masalah! Untuk perjalanan yang masih dalam perencanaan, kami sarankan Anda mulai dengan menjelajahi paket-paket kami di website:\n👉 javavolcano-touroperator.com\n\nKalau tanggalnya sudah lebih pasti, silakan hubungi kami lagi — kami siap bantu buatkan penawaran resmi.\nUntuk Ijen khususnya, kuota permit terbatas di musim ramai, jadi semakin cepat konfirmasi semakin aman. 😊",
                'body_en' => "No problem at all! For trips still in the planning phase, we'd suggest browsing our packages first:\n👉 javavolcano-touroperator.com\n\nOnce your dates are more confirmed, feel free to reach out — we'll put together a formal proposal.\nFor Ijen especially, permit slots fill up quickly during peak season, so earlier is always better. 😊",
            ],
            // ── PROPOSAL ─────────────────────────────────────────────────────
            [
                'code'    => 'p1', 'stage' => 'proposal', 'channel' => 'wa',
                'name_id' => 'Ringkasan Penawaran WA (Maks 2 Opsi)', 'name_en' => 'WA Proposal Summary',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 70,
                'body_id' => "Halo [NAMA]! Ini penawaran khusus untuk [JUMLAH PAX] orang, berangkat [TANGGAL]:\n\n━━━━━━━━━━━━━━━━━━━━\n🌋 *OPSI A — [NAMA PAKET STANDARD]*\nDurasi: [X hari Y malam]\nDestinasi: [IJEN / BROMO / DLL.]\nHotel: Bintang 3\nHarga: IDR [X.XXX.XXX]/orang (total IDR [Y.YYY.YYY])\n━━━━━━━━━━━━━━━━━━━━\n🌋 *OPSI B — [NAMA PAKET PREMIUM]*\nDurasi: [X hari Y malam]\nDestinasi: [sama]\nHotel: Bintang 4\nHarga: IDR [X.XXX.XXX]/orang (total IDR [Y.YYY.YYY])\n━━━━━━━━━━━━━━━━━━━━\n\n✅ *Sudah termasuk*: Transport AC privat, pengemudi + pemandu, tiket masuk semua lokasi, akomodasi + sarapan, masker gas & alat keselamatan Ijen, skrining medis Ijen, air minum harian, kaos JVTO.\n❌ *Tidak termasuk*: Penerbangan, tips, pengeluaran pribadi, asuransi perjalanan.\n\nPenawaran ini berlaku hingga *[TANGGAL + 48 JAM]*. \nSetelah itu harga dan ketersediaan perlu dikonfirmasi ulang.\n\nMau pilih Opsi A atau B? Atau ada pertanyaan dulu? 😊",
                'body_en' => "Hello [NAME]! Here's your private proposal for [PAX COUNT] traveler(s), departing [DATE]:\n\n━━━━━━━━━━━━━━━━━━━━\n🌋 *OPTION A — [STANDARD PACKAGE NAME]*\nDuration: [X days Y nights]\nDestinations: [Ijen / Bromo / etc.]\nHotels: 3-star\nPrice: IDR [X,XXX,XXX]/person (total IDR [Y,YYY,YYY])\n━━━━━━━━━━━━━━━━━━━━\n🌋 *OPTION B — [PREMIUM PACKAGE NAME]*\nDuration: [X days Y nights]\nDestinations: [same]\nHotels: 4-star\nPrice: IDR [X,XXX,XXX]/person (total IDR [Y,YYY,YYY])\n━━━━━━━━━━━━━━━━━━━━\n\n✅ *Included*: Private AC transport, driver + guide, all entrance fees & permits, accommodation + breakfast, Ijen gas masks & safety gear, Ijen medical screening, daily mineral water, JVTO travel T-shirt.\n❌ *Not included*: Flights, tips, personal expenses, travel insurance.\n\nThis offer is valid until *[DATE + 48 HOURS]*.\nAfter that, pricing and availability need to be reconfirmed.\n\nWhich option suits you — A or B? Or any questions first? 😊",
            ],
            [
                'code'    => 'p2', 'stage' => 'proposal', 'channel' => 'email',
                'name_id' => 'Template Quotation Email', 'name_en' => 'Email Quotation Template',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 80,
                'body_id' => "Subject: [JVTO] Penawaran Tur Privat — [NAMA PAKET] · [TANGGAL] · [X Pax]\n\nHalo [NAMA],\n\nTerima kasih sudah menghubungi Java Volcano Tour Operator (JVTO).\nBerikut penawaran resmi untuk perjalanan Anda:\n\nDETAIL PERJALANAN\n─────────────────\nPaket     : [NAMA PAKET]\nTanggal   : [TANGGAL KEBERANGKATAN]\nPeserta   : [X] orang\nOrigin    : [Surabaya / Bali]\nDurasi    : [X hari Y malam]\n\nHARGA\n─────────────────\nOpsi A (Hotel Bintang 3) : IDR [X.XXX.XXX]/orang · Total IDR [Y.YYY.YYY]\nOpsi B (Hotel Bintang 4) : IDR [X.XXX.XXX]/orang · Total IDR [Y.YYY.YYY]\n\nSUDAH TERMASUK\n─────────────────\n✓ Transport AC privat (MPV / Hiace sesuai jumlah peserta)\n✓ Pengemudi profesional + pemandu wisata berbahasa Inggris\n✓ Tiket masuk dan permit semua lokasi di itinerary\n✓ Akomodasi + sarapan setiap malam\n✓ Masker gas & trekking poles Ijen (untuk paket Ijen)\n✓ Koordinasi skrining medis Ijen (untuk paket Ijen)\n✓ Air minum harian\n✓ Kaos perjalanan JVTO (1 per peserta)\n\nBELUM TERMASUK\n─────────────────\n✗ Penerbangan internasional / domestik\n✗ Tips untuk pengemudi dan pemandu\n✗ Pengeluaran pribadi (snack, oleh-oleh, laundry)\n✗ Asuransi perjalanan\n\nCARA KONFIRMASI\n─────────────────\n1. Konfirmasi paket pilihan (Opsi A atau B) via email atau WhatsApp\n2. Kami kirimkan link pembayaran deposit (20% dari total)\n3. Setelah deposit diterima, E-Voucher resmi diterbitkan\n4. Akses My Booking Portal untuk detail lengkap perjalanan\n\nPenawaran ini berlaku hingga: [TANGGAL + 48 JAM]\n\n📱 +62 822-4478-8833 (08:00–22:00 WIB)\n📧 hello@javavolcano-touroperator.com\n\nSalam,\n[NAMA STAF]\nJava Volcano Tour Operator",
                'body_en' => "Subject: [JVTO] Private Tour Proposal — [PACKAGE NAME] · [DATE] · [X Pax]\n\nDear [NAME],\n\nThank you for reaching out to Java Volcano Tour Operator (JVTO).\nPlease find your private tour proposal below:\n\nTRIP DETAILS\n─────────────────\nPackage   : [PACKAGE NAME]\nDate      : [DEPARTURE DATE]\nTravelers : [X] people\nOrigin    : [Surabaya / Bali]\nDuration  : [X days Y nights]\n\nPRICING\n─────────────────\nOption A (3-star hotels) : IDR [X,XXX,XXX]/person · Total IDR [Y,YYY,YYY]\nOption B (4-star hotels) : IDR [X,XXX,XXX]/person · Total IDR [Y,YYY,YYY]\n\nINCLUDED\n─────────────────\n✓ Private air-conditioned transport (MPV / Hiace based on group size)\n✓ Professional driver + English-speaking escort guide\n✓ All entrance fees and permits for every listed location\n✓ Accommodation + breakfast every night\n✓ Gas masks & trekking poles at Ijen (for Ijen packages)\n✓ Ijen medical screening coordination (for Ijen packages)\n✓ Daily mineral water in vehicle\n✓ JVTO travel T-shirt (1 per participant)\n\nNOT INCLUDED\n─────────────────\n✗ International / domestic flights\n✗ Tips for driver and guide\n✗ Personal expenses (snacks, souvenirs, laundry)\n✗ Travel insurance (recommended)\n\nHOW TO CONFIRM\n─────────────────\n1. Confirm your preferred option (A or B) via email or WhatsApp\n2. We'll send a secure payment link for the deposit (20% of total)\n3. Once deposit is received, your Official E-Voucher (PDF) is issued\n4. Access the My Booking Portal for full trip details\n\nThis proposal is valid until: [DATE + 48 HOURS]\n\n📱 +62 822-4478-8833 (08:00–22:00 WIB / UTC+7)\n📧 hello@javavolcano-touroperator.com\n\nWarm regards,\n[STAFF NAME]\nJava Volcano Tour Operator",
            ],
            // ── URGENCY ───────────────────────────────────────────────────────
            [
                'code'    => 'u1', 'stage' => 'urgency', 'channel' => 'wa',
                'name_id' => 'Reminder 24 Jam Sebelum Penawaran Hangus', 'name_en' => '24h Validity Reminder',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 90,
                'body_id' => "Halo [NAMA]! 👋\n\nSekadar mengingatkan — penawaran tur privat untuk [TANGGAL] akan berakhir besok, [DEADLINE].\n\nUntuk paket Ijen, slot permit sangat terbatas di periode ini. Kami tidak bisa menjamin ketersediaan jika dikonfirmasi setelah deadline.\n\nJika Anda siap lanjut, cukup balas WA ini dan kami bantu proses depositnya. 😊",
                'body_en' => "Hello [NAME]! 👋\n\nJust a friendly reminder — your private tour proposal for [DATE] expires tomorrow, [DEADLINE].\n\nFor Ijen packages, permit slots are limited during this period. We can't guarantee availability after the deadline.\n\nIf you're ready to proceed, just reply here and we'll walk you through the deposit. 😊",
            ],
            [
                'code'    => 'u2', 'stage' => 'urgency', 'channel' => 'wa',
                'name_id' => 'Instruksi Pembayaran Deposit', 'name_en' => 'Payment Instructions',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 100,
                'body_id' => "Bagus! Mari kita amankan tanggal [TANGGAL] untuk [X] orang. 🎉\n\nDETAIL PEMBAYARAN DEPOSIT\n──────────────────────────\nPaket      : [NAMA PAKET] — Opsi [A/B]\nTotal Paket: IDR [TOTAL]\nDeposit DP : IDR [20% TOTAL] (20%)\n\nCara bayar paling cepat:\n👉 Kartu kredit/debit: Kami kirimkan link pembayaran aman (Midtrans/Stripe)\n   → Saldo dilunasi paling lambat 5 hari sebelum hari-H via kartu\n\nAtau via transfer bank:\n🏦 BRI — PT Java Volcano Rendezvous — 001301001779564\n🏦 BCA — PT Java Volcano Rendezvous — 1200944352\n   → Saldo dilunasi paling lambat 3 hari sebelum hari-H via transfer\n\n⚠️ Catatan penting: JVTO tidak pernah meminta nomor kartu, CVV, atau password perbankan via chat.\n\nSetelah deposit masuk, E-Voucher resmi akan diterbitkan dalam 1–2 jam kerja. ✅",
                'body_en' => "Excellent! Let's secure [DATE] for [X] traveler(s). 🎉\n\nDEPOSIT PAYMENT DETAILS\n──────────────────────────\nPackage    : [PACKAGE NAME] — Option [A/B]\nTotal      : IDR [TOTAL]\nDeposit    : IDR [20% TOTAL] (20%)\n\nFastest option:\n👉 Credit/debit card: We'll send you a secure payment link (Midtrans/Stripe)\n   → Balance due no later than 5 days before Day 1 via card\n\nOr bank transfer:\n🏦 BRI — PT Java Volcano Rendezvous — 001301001779564 — SWIFT: BRINIDJAXXX\n🏦 BCA — PT Java Volcano Rendezvous — 1200944352 — SWIFT: CENAIDJAXXX\n   → Balance due no later than 3 days before Day 1\n\n⚠️ Security note: JVTO will never ask for your full card number, CVV, or banking password via chat.\n\nOnce deposit is received, your Official E-Voucher (PDF) will be issued within 1–2 business hours. ✅",
            ],
            [
                'code'    => 'u3', 'stage' => 'urgency', 'channel' => 'wa',
                'name_id' => 'Konfirmasi E-Voucher (Post-DP)', 'name_en' => 'E-Voucher Confirmation',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 110,
                'body_id' => "✅ Deposit diterima! Booking Anda untuk [PAKET] tanggal [TANGGAL] sudah terkonfirmasi.\n\nE-Voucher resmi sedang kami proses — akan kami kirimkan ke email Anda dalam 1–2 jam kerja.\n\nSelanjutnya, Anda akan mendapat akses ke *My Booking Portal* untuk melihat detail lengkap: jadwal harian, hotel, info pickup, dan checklist persiapan.\n\nSelamat bersiap untuk petualangan Anda! 🌋",
                'body_en' => "✅ Deposit received! Your booking for [PACKAGE] on [DATE] is now confirmed.\n\nYour Official E-Voucher (PDF) is being prepared — we'll send it to your email within 1–2 business hours.\n\nYou'll also receive access to the *My Booking Portal*, where you can see your full itinerary, hotel details, pickup info, and a preparation checklist.\n\nWe're looking forward to your adventure! 🌋",
            ],
            // ── POST-BOOKING ─────────────────────────────────────────────────
            [
                'code'    => 'pb1', 'stage' => 'post_booking', 'channel' => 'wa',
                'name_id' => 'Pengingat H-7', 'name_en' => 'H-7 Reminder',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 120,
                'body_id' => "Halo [NAMA]! 🌋 Perjalanan Anda ke [DESTINASI] tinggal *7 hari lagi!*\n\nBeberapa hal untuk dipersiapkan:\n\n*PAKAIAN & PERLENGKAPAN*\n• Jaket tebal atau lapis-lapis (Ijen: 10–15°C · Bromo: 5–15°C malam hari)\n• Sepatu hiking dengan grip yang baik\n• Celana panjang, lengan panjang\n• Senter kepala (headlamp) — opsional tapi disarankan\n• ⚠️ Jangan pakai perhiasan perak ke Ijen — gas sulfur merusak permanen\n\n*PICKUP*\nKonfirmasi jam dan lokasi pickup Anda ada di E-Voucher. Pengemudi akan menghubungi Anda H-1.\n\nAda pertanyaan? Balas WA ini kapan saja (08:00–22:00 WIB). 😊",
                'body_en' => "Hello [NAME]! 🌋 Your trip to [DESTINATION] is *7 days away!*\n\nHere's a quick preparation checklist:\n\n*CLOTHING & GEAR*\n• Warm layers — thermal or multiple layers (Ijen: 10–15°C · Bromo: 5–15°C at night)\n• Hiking shoes with good grip\n• Long trousers and long sleeves\n• Headlamp — optional but recommended\n• ⚠️ No silver jewelry at Ijen — sulfur gases tarnish silver permanently\n\n*PICKUP*\nYour confirmed pickup time and location are on your E-Voucher. Your driver will contact you the day before.\n\nAny questions? Reply here anytime (08:00–22:00 WIB / UTC+7). 😊",
            ],
            [
                'code'    => 'pb2', 'stage' => 'post_booking', 'channel' => 'wa',
                'name_id' => 'Detail Pengemudi H-1', 'name_en' => 'H-1 Driver Details',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 130,
                'body_id' => "Halo [NAMA]! Besok hari petualangannya! 🌋\n\nIni detail penjemputan Anda:\n\n🚗 *Pengemudi*: [NAMA PENGEMUDI]\n📱 *WhatsApp*: [NOMOR WA PENGEMUDI]\n🕐 *Jam pickup*: [JAM] WIB\n📍 *Lokasi*: [TITIK PICKUP]\n\nTidur cukup malam ini — perjalanan dimulai dini hari! 😊\nKalau ada apa-apa, hubungi WA ini atau langsung [NAMA PENGEMUDI].",
                'body_en' => "Hello [NAME]! Tomorrow's the big day! 🌋\n\nHere are your pickup details:\n\n🚗 *Driver*: [DRIVER NAME]\n📱 *WhatsApp*: [DRIVER WA NUMBER]\n🕐 *Pickup time*: [TIME] WIB (UTC+7)\n📍 *Location*: [PICKUP POINT]\n\nGet some rest tonight — the journey starts early! 😊\nFor anything urgent, contact this number or reach [DRIVER NAME] directly.",
            ],
            [
                'code'    => 'pb3', 'stage' => 'post_booking', 'channel' => 'wa',
                'name_id' => 'Permintaan Review Post-Tour', 'name_en' => 'Post-Tour Review Request',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 140,
                'body_id' => "Halo [NAMA]! Semoga perjalanan ke [DESTINASI] berkesan. 🌋\n\nKami di JVTO sangat menghargai pendapat Anda. Jika Anda punya 2 menit, ulasan jujur Anda sangat membantu kami dan calon wisatawan lainnya:\n\n⭐ Trustpilot: https://www.trustpilot.com/review/javavolcano-touroperator.com\n⭐ Google: [LINK GOOGLE REVIEW JVTO]\n\nKalau ada hal yang kurang memuaskan, tolong sampaikan langsung ke kami sebelum menulis ulasan.\n\nTerima kasih sudah memilih JVTO! 🙏",
                'body_en' => "Hello [NAME]! We hope your trip to [DESTINATION] was everything you hoped for. 🌋\n\nAt JVTO, your honest feedback means the world to us — and helps future travelers make their decision.\nIf you have 2 minutes, we'd really appreciate a review:\n\n⭐ Trustpilot: https://www.trustpilot.com/review/javavolcano-touroperator.com\n⭐ Google: [JVTO GOOGLE REVIEW LINK]\n\nIf anything didn't meet your expectations, please let us know directly before posting.\n\nThank you for choosing JVTO! 🙏",
            ],
            // ── OBJECTION HANDLERS ───────────────────────────────────────────
            [
                'code'    => 'ob1', 'stage' => 'objection', 'channel' => 'wa',
                'name_id' => '"Berapa harga pastinya?"', 'name_en' => '"What\'s the exact price?"',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 150,
                'body_id' => "Harga kami dihitung berdasarkan jumlah peserta dan tanggal keberangkatan.\n\nUntuk penawaran yang akurat, boleh konfirmasi:\n• Tanggal pasti atau kisaran tanggal\n• Jumlah peserta\n\nSetelah itu kami berikan harga per orang langsung — tidak ada biaya tersembunyi, semua sudah termasuk transport, hotel, tiket, pemandu, dan sarapan.",
                'body_en' => "Our pricing is calculated based on your group size and travel dates.\n\nFor an accurate quote, could you confirm:\n• Your preferred date (or date range)\n• Number of travelers\n\nOnce we have those, we'll give you the exact per-person price — no hidden costs, everything included (transport, hotel, tickets, guide, breakfast).",
            ],
            [
                'code'    => 'ob2', 'stage' => 'objection', 'channel' => 'wa',
                'name_id' => '"Apa bedanya JVTO?"', 'name_en' => '"What makes JVTO different?"',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 160,
                'body_id' => "Ada 3 hal yang membedakan JVTO:\n\n1. *Didirikan Tourist Police aktif* — Bapak Sam (Bripka Agung Sambuko) adalah anggota aktif Tourist Police East Java. Tidak ada operator Ijen/Bromo lain yang punya latar belakang ini.\n\n2. *100% privat* — Setiap booking mendapat kendaraan, pengemudi, dan pemandu sendiri. Kami tidak pernah menggabungkan grup berbeda dalam satu tur.\n\n3. *Skrining medis Ijen* — Perawat datang ke hotel Anda malam sebelum pendakian. Ini standar BBKSDA, bukan formalitas — dan kami yang koordinasikan, termasuk dalam harga.\n\nLisensi kami bisa diverifikasi: NIB 1102230032918 · TDUP · HPWKI · BBKSDA · POLPAR.",
                'body_en' => "Three things set JVTO apart:\n\n1. *Founded by an active Tourist Police officer* — Mr. Sam (Bripka Agung Sambuko) is an active Tourist Police officer in East Java. No other Ijen/Bromo operator has this background.\n\n2. *100% private tours* — Every booking gets its own vehicle, driver, and guide. We never mix different groups into a single tour.\n\n3. *Ijen medical screening* — A nurse visits your hotel the evening before the hike. This is a BBKSDA requirement, not a formality — and we coordinate it, included in the price.\n\nOur licenses are publicly verifiable: NIB 1102230032918 · TDUP · HPWKI · BBKSDA · POLPAR.",
            ],
            [
                'code'    => 'ob3', 'stage' => 'objection', 'channel' => 'wa',
                'name_id' => '"Apakah ada refund jika Ijen tutup?"', 'name_en' => '"Refund if Ijen is closed?"',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 170,
                'body_id' => "Kebijakan JVTO untuk penutupan Ijen:\n\nJika Ijen tutup karena kondisi alam atau kebijakan BBKSDA, kami akan:\n• Tawarkan rute alternatif yang aman\n• Atau tawarkan penjadwalan ulang ke tanggal lain (gratis, satu kali)\n• Jika elemen utama tidak bisa diganti → Travel Credit senilai komponen yang tidak bisa dijalankan\n\nTravel Credit tidak kadaluarsa dan bisa ditransfer ke orang lain.\nRefund tunai tidak tersedia untuk pembatalan inisiatif tamu.",
                'body_en' => "JVTO's policy for Ijen closures:\n\nIf Ijen closes due to volcanic conditions or BBKSDA regulation, we will:\n• Offer a safe alternative route\n• Or offer a free reschedule to another available date\n• If the main element can't be replaced → Travel Credit for the affected components\n\nTravel Credit has no expiry and is transferable to another person.\nCash refunds are not available for guest-initiated cancellations.",
            ],
            [
                'code'    => 'ob4', 'stage' => 'objection', 'channel' => 'wa',
                'name_id' => '"Bisa request jadwal khusus?"', 'name_en' => '"Can we request custom schedule?"',
                'bant_component' => null, 'is_auto' => 0, 'sort_order' => 180,
                'body_id' => "Kami menerima micro-customization dalam batas tertentu:\n\n✅ Bisa: Ganti kamar (twin bed vs double), upgrade hotel, tambah aktivitas opsional di lokasi\n✅ Bisa: Sesuaikan waktu pickup sesuai penerbangan/kereta Anda\n❌ Tidak bisa: Ubah urutan destinasi utama atau durasi paket secara signifikan\n❌ Tidak bisa: Sewa kendaraan saja tanpa paket lengkap\n\nKalau ada kebutuhan spesifik, sampaikan saja — kami usahakan dalam batas operasional kami.",
                'body_en' => "We do accommodate micro-customizations within certain limits:\n\n✅ Yes: Room type change (twin vs double bed), hotel upgrades, optional on-site activities\n✅ Yes: Adjust pickup time to fit your flight or train schedule\n❌ No: Changing the main destination sequence or significantly altering package duration\n❌ No: Vehicle-only or transport-only services\n\nIf you have a specific need, just let us know — we'll do our best within our operational model.",
            ],
        ];

        foreach ($templates as $data) {
            CannedResponse::updateOrCreate(
                ['code' => $data['code']],
                array_merge($data, ['is_active' => 1])
            );
        }
    }
}
```

- [ ] **Step 3: Register seeder in DatabaseSeeder**

In `database/seeders/DatabaseSeeder.php`, add inside `run()`:
```php
$this->call(CannedResponsesSeeder::class);
```

- [ ] **Step 4: Write the seeder test**

Create `tests/Feature/CannedResponseSeederTest.php`:

```php
<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
use App\Models\CannedResponse;

class CannedResponseSeederTest extends TestCase
{
    use RefreshDatabase;

    public function test_seeder_inserts_19_records(): void
    {
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
        $this->assertSame(19, CannedResponse::count());
    }

    public function test_all_records_have_non_empty_bodies(): void
    {
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
        $empty = CannedResponse::where('body_id', '')->orWhere('body_en', '')->count();
        $this->assertSame(0, $empty);
    }

    public function test_t3_record_exists_and_is_auto(): void
    {
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
        $t3 = CannedResponse::where('code', 't3')->first();
        $this->assertNotNull($t3);
        $this->assertTrue((bool)$t3->is_auto);
        $this->assertStringContainsString('08:00 WIB', $t3->body_en);
    }

    public function test_expected_codes_exist(): void
    {
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
        $expected = ['t1','t2','t3','d1','d2','d3','d4','p1','p2',
                     'u1','u2','u3','pb1','pb2','pb3','ob1','ob2','ob3','ob4'];
        foreach ($expected as $code) {
            $this->assertNotNull(
                CannedResponse::where('code', $code)->first(),
                "Missing canned response: {$code}"
            );
        }
    }
}
```

- [ ] **Step 5: Run seeder test (expect fail — no seeder yet written to DB)**

```bash
php artisan test tests/Feature/CannedResponseSeederTest.php
```

Expected: FAIL (table exists but 0 records)

- [ ] **Step 6: Run seeder**

```bash
php artisan db:seed --class=CannedResponsesSeeder
```

Expected output: no errors

- [ ] **Step 7: Run seeder test again (expect pass)**

```bash
php artisan test tests/Feature/CannedResponseSeederTest.php
```

Expected: 4 tests PASS

- [ ] **Step 8: Commit**

```bash
git add database/seeders/ tests/Feature/CannedResponseSeederTest.php
git commit -m "feat: add CannedResponsesSeeder with 19 bilingual templates"
```

---

## Task 4 — API Controller + Routes

**Files:**
- Create: `app/Http/Controllers/CannedResponseController.php`
- Modify: `routes/api.php`
- Create: `tests/Feature/CannedResponseApiTest.php`

- [ ] **Step 1: Write failing API feature tests**

Create `tests/Feature/CannedResponseApiTest.php`:

```php
<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class CannedResponseApiTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
    }

    public function test_index_returns_all_active_templates(): void
    {
        $response = $this->getJson('/api/canned-responses');
        $response->assertOk()
                 ->assertJsonCount(19)
                 ->assertJsonStructure([['code','stage','channel','name_id','name_en','body_id','body_en','bant_component','is_auto']]);
    }

    public function test_index_filters_by_stage(): void
    {
        $response = $this->getJson('/api/canned-responses?stage=triage');
        $response->assertOk()->assertJsonCount(3);
        foreach ($response->json() as $item) {
            $this->assertSame('triage', $item['stage']);
        }
    }

    public function test_index_filters_by_channel(): void
    {
        $response = $this->getJson('/api/canned-responses?channel=email');
        $response->assertOk();
        foreach ($response->json() as $item) {
            $this->assertContains($item['channel'], ['email', 'both']);
        }
    }

    public function test_show_returns_single_template(): void
    {
        $response = $this->getJson('/api/canned-responses/t3');
        $response->assertOk()
                 ->assertJsonFragment(['code' => 't3'])
                 ->assertJsonStructure(['code','stage','channel','name_id','name_en','body_id','body_en']);
    }

    public function test_show_with_lang_en_returns_body_field(): void
    {
        $response = $this->getJson('/api/canned-responses/t3?lang=en');
        $response->assertOk()
                 ->assertJsonFragment(['code' => 't3'])
                 ->assertJsonStructure(['code','body']);
        $this->assertStringContainsString('08:00 WIB', $response->json('body'));
    }

    public function test_show_with_lang_id_returns_id_body(): void
    {
        $response = $this->getJson('/api/canned-responses/t3?lang=id');
        $response->assertOk();
        $this->assertStringContainsString('08:00 WIB', $response->json('body'));
        $this->assertStringContainsString('Terima kasih', $response->json('body'));
    }

    public function test_show_returns_404_for_unknown_code(): void
    {
        $this->getJson('/api/canned-responses/zzz')->assertNotFound();
    }

    public function test_inactive_template_excluded_from_index(): void
    {
        \App\Models\CannedResponse::where('code', 't1')->update(['is_active' => 0]);
        $response = $this->getJson('/api/canned-responses');
        $codes = array_column($response->json(), 'code');
        $this->assertNotContains('t1', $codes);
    }
}
```

- [ ] **Step 2: Run tests — expect fail (routes don't exist yet)**

```bash
php artisan test tests/Feature/CannedResponseApiTest.php
```

Expected: FAIL — `404` for all endpoints

- [ ] **Step 3: Create controller**

```bash
php artisan make:controller CannedResponseController
```

Write `app/Http/Controllers/CannedResponseController.php`:

```php
<?php

namespace App\Http\Controllers;

use App\Models\CannedResponse;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class CannedResponseController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $query = CannedResponse::active()->orderBy('sort_order');

        if ($request->filled('stage'))   $query->forStage($request->stage);
        if ($request->filled('channel')) $query->forChannel($request->channel);
        if ($request->filled('code'))    $query->where('code', $request->code);

        return response()->json($query->get());
    }

    public function show(Request $request, string $code): JsonResponse
    {
        $template = CannedResponse::findByCode($code);

        if (!$template) {
            return response()->json(['error' => 'Template not found'], 404);
        }

        if ($request->filled('lang')) {
            $data = $template->toArray();
            $data['body'] = $template->bodyFor($request->lang);
            unset($data['body_id'], $data['body_en']);
            return response()->json($data);
        }

        return response()->json($template);
    }
}
```

- [ ] **Step 4: Add routes**

In `routes/api.php`, add:

```php
use App\Http\Controllers\CannedResponseController;

Route::get('/canned-responses', [CannedResponseController::class, 'index']);
Route::get('/canned-responses/{code}', [CannedResponseController::class, 'show']);
```

- [ ] **Step 5: Run tests — expect pass**

```bash
php artisan test tests/Feature/CannedResponseApiTest.php
```

Expected: 8 tests PASS

- [ ] **Step 6: Smoke test via curl**

```bash
curl -s "http://localhost/api/canned-responses?stage=triage" | python -m json.tool | head -20
```

Expected: JSON array with 3 triage templates (t1, t2, t3)

- [ ] **Step 7: Commit**

```bash
git add app/Http/Controllers/CannedResponseController.php routes/api.php tests/Feature/CannedResponseApiTest.php
git commit -m "feat: add canned responses API (index + show endpoints)"
```

---

## Task 5 — Webhook Helpers (`detectLanguage` + `isNewContact`)

**Files:**
- Modify: `app/Http/Controllers/WebhookController.php`
- Create: `tests/Unit/WebhookHelperTest.php`

- [ ] **Step 1: Write unit tests for helpers**

Create `tests/Unit/WebhookHelperTest.php`:

```php
<?php

namespace Tests\Unit;

use Tests\TestCase;
use App\Http\Controllers\WebhookController;
use Illuminate\Support\Facades\DB;

class WebhookHelperTest extends TestCase
{
    private WebhookController $ctrl;

    protected function setUp(): void
    {
        parent::setUp();
        $this->ctrl = new WebhookController();
    }

    // ── detectLanguage ────────────────────────────────────────────────────

    public function test_detect_language_returns_id_for_halo(): void
    {
        $this->assertSame('id', $this->invokeDetect('halo ada tour ijen?'));
    }

    public function test_detect_language_returns_id_for_saya(): void
    {
        $this->assertSame('id', $this->invokeDetect('saya mau tanya paket'));
    }

    public function test_detect_language_returns_en_for_english(): void
    {
        $this->assertSame('en', $this->invokeDetect('hello i want to book a tour'));
    }

    public function test_detect_language_defaults_en_for_unknown(): void
    {
        $this->assertSame('en', $this->invokeDetect(''));
    }

    public function test_detect_language_case_insensitive(): void
    {
        $this->assertSame('id', $this->invokeDetect('HALO SAYA MAU TANYA'));
    }

    // ── isNewContact ──────────────────────────────────────────────────────

    public function test_is_new_contact_returns_true_for_unknown_phone(): void
    {
        // No rows in bookings or klook_bookings
        $this->assertTrue($this->invokeIsNew('+6281234567890'));
    }

    public function test_is_new_contact_returns_false_for_known_booking(): void
    {
        DB::table('bookings')->insert(['customer_phone' => '+6281234567890']);
        $this->assertFalse($this->invokeIsNew('+6281234567890'));
    }

    // ── Helpers ───────────────────────────────────────────────────────────

    private function invokeDetect(string $text): string
    {
        $ref = new \ReflectionMethod(WebhookController::class, 'detectLanguage');
        $ref->setAccessible(true);
        return $ref->invoke($this->ctrl, $text);
    }

    private function invokeIsNew(string $phone): bool
    {
        $ref = new \ReflectionMethod(WebhookController::class, 'isNewContact');
        $ref->setAccessible(true);
        return $ref->invoke($this->ctrl, $phone);
    }
}
```

- [ ] **Step 2: Run tests — expect fail (methods don't exist)**

```bash
php artisan test tests/Unit/WebhookHelperTest.php
```

Expected: FAIL — method not found

- [ ] **Step 3: Add helper methods to WebhookController**

Add these two private methods to `app/Http/Controllers/WebhookController.php`:

```php
use Illuminate\Support\Facades\DB;

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
    return 'en';
}

private function isNewContact(string $phone): bool
{
    // Verify exact column names match u1805424_jvto_clone schema.
    return !DB::table('bookings')->where('customer_phone', $phone)->exists()
        && !DB::table('klook_bookings')->where('guest_phone', $phone)->exists();
}
```

- [ ] **Step 4: Run tests — expect pass**

```bash
php artisan test tests/Unit/WebhookHelperTest.php
```

Expected: 7 tests PASS

- [ ] **Step 5: Commit**

```bash
git add app/Http/Controllers/WebhookController.php tests/Unit/WebhookHelperTest.php
git commit -m "feat: add detectLanguage + isNewContact helpers to WebhookController"
```

---

## Task 6 — Off-Hours Auto-Ack Hook

**Files:**
- Modify: `app/Http/Controllers/WebhookController.php`
- Create: `tests/Feature/OffHoursAutoAckTest.php`

- [ ] **Step 1: Write failing feature test**

Create `tests/Feature/OffHoursAutoAckTest.php`:

```php
<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
use Carbon\Carbon;
use Illuminate\Support\Facades\Http;  // or your WA send mock

class OffHoursAutoAckTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        $this->seed(\Database\Seeders\CannedResponsesSeeder::class);
    }

    public function test_off_hours_new_contact_receives_t3_ack(): void
    {
        Carbon::setTestNow(Carbon::parse('2026-05-19 23:00:00', 'Asia/Jakarta'));

        // Mock sendWAMessage so no real WA call is made
        $this->mock(\App\Services\WaProCrmService::class, function ($mock) {
            $mock->shouldReceive('send')->once()->withArgs(function ($phone, $body) {
                return $phone === '+6281999888777'
                    && str_contains($body, 'javavolcano-touroperator.com');
            });
        });

        $response = $this->postJson('/webhook/wa-incoming', [
            'from'      => '+6281999888777',
            'inbox'     => 'customer',
            'body'      => 'hello i want to book ijen tour',
            'type'      => 'conversation',
            'timestamp' => now()->timestamp,
        ]);

        $response->assertOk()
                 ->assertJson(['status' => 'auto_ack_sent']);
    }

    public function test_off_hours_known_contact_skips_ack(): void
    {
        Carbon::setTestNow(Carbon::parse('2026-05-19 23:00:00', 'Asia/Jakarta'));
        \Illuminate\Support\Facades\DB::table('bookings')
            ->insert(['customer_phone' => '+6281999000111']);

        $this->mock(\App\Services\WaProCrmService::class, function ($mock) {
            $mock->shouldNotReceive('send');
        });

        // Should fall through to existing routing — just confirm no auto_ack_sent
        $response = $this->postJson('/webhook/wa-incoming', [
            'from'      => '+6281999000111',
            'inbox'     => 'customer',
            'body'      => 'hello',
            'type'      => 'conversation',
            'timestamp' => now()->timestamp,
        ]);

        $response->assertJson(fn($j) => !$j->has('status') || $j->where('status', '!=', 'auto_ack_sent'));
    }

    public function test_business_hours_new_contact_skips_ack(): void
    {
        Carbon::setTestNow(Carbon::parse('2026-05-19 10:00:00', 'Asia/Jakarta'));

        $this->mock(\App\Services\WaProCrmService::class, function ($mock) {
            $mock->shouldNotReceive('send');
        });

        $response = $this->postJson('/webhook/wa-incoming', [
            'from'      => '+6281888777666',
            'inbox'     => 'customer',
            'body'      => 'hello',
            'type'      => 'conversation',
            'timestamp' => now()->timestamp,
        ]);

        // Should NOT return auto_ack_sent
        $body = $response->json();
        $this->assertNotSame('auto_ack_sent', $body['status'] ?? null);
    }

    public function test_off_hours_indonesian_message_sends_id_variant(): void
    {
        Carbon::setTestNow(Carbon::parse('2026-05-19 23:00:00', 'Asia/Jakarta'));

        $this->mock(\App\Services\WaProCrmService::class, function ($mock) {
            $mock->shouldReceive('send')->once()->withArgs(function ($phone, $body) {
                return str_contains($body, 'Terima kasih');  // ID variant
            });
        });

        $this->postJson('/webhook/wa-incoming', [
            'from'      => '+6281777666555',
            'inbox'     => 'customer',
            'body'      => 'halo saya mau tanya paket ijen',
            'type'      => 'conversation',
            'timestamp' => now()->timestamp,
        ]);
    }

    protected function tearDown(): void
    {
        Carbon::setTestNow();  // reset Carbon mock
        parent::tearDown();
    }
}
```

> **Note:** The test mocks `WaProCrmService`. If David's existing webhook uses a different class for sending WA messages, replace `\App\Services\WaProCrmService::class` with the actual service/client class name and `send` with the actual method. Do not change the test logic.

- [ ] **Step 2: Run tests — expect fail**

```bash
php artisan test tests/Feature/OffHoursAutoAckTest.php
```

Expected: FAIL — hook not implemented

- [ ] **Step 3: Insert off-hours hook into WebhookController**

In `handleIncoming()`, add at the very top of the method body **before** any existing logic:

```php
use App\Models\CannedResponse;
use Carbon\Carbon;

public function handleIncoming(Request $request)
{
    $payload = $request->all();

    // ── OFF-HOURS AUTO-ACK HOOK ──────────────────────────────────────────
    if (
        isset($payload['from'], $payload['inbox'], $payload['body'])
        && $payload['inbox'] === 'customer'
        && $this->isNewContact($payload['from'])
    ) {
        $jakartaHour = Carbon::now('Asia/Jakarta')->hour;
        if ($jakartaHour < 8 || $jakartaHour >= 22) {
            $lang     = $this->detectLanguage($payload['body']);
            $template = CannedResponse::findByCode('t3');

            if ($template) {
                $body = $template->bodyFor($lang);
                $this->sendWAMessage($payload['from'], $body);
                $this->logAutoAck($payload['from'], $jakartaHour, $lang);
            }

            return response()->json(['status' => 'auto_ack_sent']);
        }
    }
    // ── END OFF-HOURS HOOK ───────────────────────────────────────────────

    // ... existing handleIncoming logic continues unchanged below ...
```

Also add `logAutoAck` private method:

```php
private function logAutoAck(string $phone, int $hour, string $lang): void
{
    \Illuminate\Support\Facades\Log::info('wa_auto_ack_sent', [
        'phone' => $phone,
        'hour'  => $hour,
        'lang'  => $lang,
    ]);
}
```

- [ ] **Step 4: Run tests — expect pass**

```bash
php artisan test tests/Feature/OffHoursAutoAckTest.php
```

Expected: 4 tests PASS

- [ ] **Step 5: Run full test suite**

```bash
php artisan test
```

Expected: All tests PASS (no regressions in existing tests)

- [ ] **Step 6: Commit**

```bash
git add app/Http/Controllers/WebhookController.php tests/Feature/OffHoursAutoAckTest.php
git commit -m "feat: add off-hours auto-ack webhook hook using t3 template"
```

---

## Task 7 — CRM UI: Shortcode Dropdown

This task is a frontend integration. Steps describe behavior — David implements using the existing WA Pro CRM UI framework (likely Blade + JS or Vue).

**Files:** David's existing CRM chat window component (exact file depends on David's frontend structure)

- [ ] **Step 1: Add API call for template list**

In the chat window JavaScript, on component mount, fetch:
```
GET /api/canned-responses
```
Store result in a local variable `cannedResponses` (array).

- [ ] **Step 2: Detect `/` keystroke in message composer**

In the message input `keyup` or `input` handler:
```javascript
if (inputValue.startsWith('/')) {
  const query = inputValue.slice(1).toLowerCase(); // e.g. "t" from "/t"
  filteredTemplates = cannedResponses.filter(t =>
    t.code.startsWith(query) || t.name_en.toLowerCase().includes(query)
  );
  showDropdown(filteredTemplates);
} else {
  hideDropdown();
}
```

- [ ] **Step 3: Render dropdown**

Each dropdown item shows: `[code] — name_en`. Example: `t1 — Welcome + MECE Menu`

- [ ] **Step 4: On template select — show bilingual tabs**

When Inan clicks a template, replace the composer content with a two-tab view:
- Tab ID: `body_id` text
- Tab EN: `body_en` text

Inan selects the tab for the customer's language, edits `[PLACEHOLDER]` fields, then sends.

- [ ] **Step 5: Manual test**

1. Open WA Pro CRM chat for any conversation
2. Click into message composer, type `/t`
3. Verify dropdown shows: `t1 — Welcome + MECE Menu`, `t2 — Data Collection Prompt`, `t3 — Off-hours Auto-Acknowledgment`
4. Click `t1` → verify both language tabs appear in composer
5. Select EN tab → verify Welcome + MECE Menu English text is in composer
6. Clear, type `/ob` → verify 4 objection templates appear

- [ ] **Step 6: Commit**

```bash
git add [frontend files modified]
git commit -m "feat: add shortcode dropdown in WA Pro CRM chat composer"
```

---

## Task 8 — End-to-End Verification

Mirrors the spec verification checklist. Run after all tasks complete.

- [ ] **Verify 1: Migration + seeder**
```bash
php artisan migrate:fresh --seed
php artisan tinker --execute="echo App\Models\CannedResponse::count();"
```
Expected: `19`

- [ ] **Verify 2: API triage filter**
```bash
curl -s "http://localhost/api/canned-responses?stage=triage" | python -m json.tool
```
Expected: array of 3 (t1, t2, t3)

- [ ] **Verify 3: Single template with lang**
```bash
curl -s "http://localhost/api/canned-responses/t3?lang=en"
```
Expected: JSON with `body` containing `javavolcano-touroperator.com`

- [ ] **Verify 4: Full test suite green**
```bash
php artisan test
```
Expected: All PASS

- [ ] **Verify 5: Live off-hours test (staging)**
Send a WA message from an unregistered number to the JVTO test number at any time outside 08:00–22:00 WIB. Confirm T-3 auto-reply arrives within 2 minutes in the correct language.

- [ ] **Verify 6: Known-contact pass-through**
Send a WA message from a number that exists in `bookings.customer_phone`. Confirm no auto-ack — existing flow handles it.

---

## Self-Review Notes

**Spec coverage check:**
- ✅ DB schema → Task 1
- ✅ Model with `findByCode()` + `bodyFor()` → Task 2
- ✅ All 19 templates seeded with full body text → Task 3
- ✅ `GET /api/canned-responses` (index + filters) → Task 4
- ✅ `GET /api/canned-responses/{code}?lang=` → Task 4
- ✅ `detectLanguage` (default EN, keyword-based) → Task 5
- ✅ `isNewContact` (bookings + klook check) → Task 5
- ✅ Off-hours hook with lang detection → Task 6
- ✅ `logAutoAck` → Task 6
- ✅ CRM UI dropdown → Task 7
- ✅ Full verification → Task 8

**Type consistency:**
- `CannedResponse::findByCode(string $code): ?self` — used in Task 2, called in Task 6 ✅
- `$template->bodyFor(string $lang): string` — defined in Task 2, used in Tasks 4 + 6 ✅
- `detectLanguage` / `isNewContact` — defined in Task 5, called in Task 6 ✅
- `WaProCrmService::send` mock in Task 6 tests — David must confirm actual service class name ⚠️
