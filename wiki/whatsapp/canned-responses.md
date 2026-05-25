---
type: ops
title: JVTO Canned Responses — WhatsApp & Email Scripts per Stage
last_updated: 2026-05-19
sources: [comm-management-theory, jvto-policy-pack-v6, jvto-travel-guide-en, ssot-v6]
companion: 2026-05-14-whatsapp-operations-playbook
---

# JVTO Canned Responses

> **Audiens**: Inan (staf operasional, daily use), Sam (review & closing), David (integrasi ke WA Pro CRM / chatbot).
> **Format**: Setiap template diberi tag: `[WA]` atau `[EMAIL]`, stage, komponen BANT jika relevan.
> **Bahasa**: Semua blok tersedia `[ID]` Bahasa Indonesia dan `[EN]` English. Pilih sesuai bahasa customer.
> **Rule**: Jangan kirim quotation sebelum 3 komponen terkunci: tanggal pasti + jumlah pax + preferensi hotel.
> **Max 2 opsi** di stage Proposal — tidak lebih.

Untuk konteks channel dan state machine lengkap → [[ops/2026-05-14-whatsapp-operations-playbook]]
Untuk teori di balik framework ini → [[sources/comm-management-theory]]

---

## STAGE 1 — TRIAGE (Automated Welcome)

*Otomatis. Kirim saat customer pertama kali menghubungi nomor JVTO dari nomor yang belum terdaftar di database. Target: dalam 2 menit.*

---

### T-1 · Welcome + MECE Menu `[WA]` `[Auto]` `[MECE]`

**[ID]**
```
Halo! Selamat datang di JVTO — Java Volcano Tour Operator. 🌋

Kami operator tur privat East Java yang didirikan oleh Bripka Agung Sambuko, anggota aktif Tourist Police.
Semua tur 100% privat — tidak ada grup gabungan.

Boleh kami tahu Anda butuh bantuan untuk apa?

[1] 🗺️ Tanya Paket Wisata (Ijen, Bromo, Tumpak Sewu, dll.)
[2] 📋 Status Booking Aktif (sudah booking, perlu info lanjutan)
[3] 🤝 Kemitraan / B2B (travel agent, reseller)

Balas dengan angka pilihannya ya!
```

**[EN]**
```
Hello! Welcome to JVTO — Java Volcano Tour Operator. 🌋

We're a private tour operator in East Java, founded by Bripka Agung Sambuko, an active Tourist Police officer.
Every tour is 100% private — no shared groups, ever.

How can we help you today?

[1] 🗺️ Tour Package Inquiry (Ijen, Bromo, Tumpak Sewu, etc.)
[2] 📋 Active Booking Status (already booked, need info or assistance)
[3] 🤝 Partnership / B2B (travel agent, reseller)

Just reply with the number of your choice!
```

---

### T-2 · After [1] Selected — Data Collection Prompt `[WA]` `[Auto or Inan]` `[BANT: N, T]`

*Kirim setelah customer pilih [1]. Kumpulkan 4 data dasar sebelum Inan terlibat.*

**[ID]**
```
Siap! Untuk kami carikan paket yang paling sesuai, boleh share info berikut:

1. 👤 Nama Anda
2. 🌋 Destinasi yang diminati: Kawah Ijen / Bromo / Tumpak Sewu / Madakaripura / kombinasi?
3. 📅 Tanggal rencana perjalanan (atau kisaran bulan)
4. 👥 Jumlah peserta

Tim kami akan membalas dalam jam kerja kami: 08:00–22:00 WIB (UTC+7).
```

**[EN]**
```
Great! To find the best package for you, could you share the following:

1. 👤 Your name
2. 🌋 Destination(s) of interest: Kawah Ijen / Bromo / Tumpak Sewu / Madakaripura / combination?
3. 📅 Planned travel date (or approximate month)
4. 👥 Number of travelers

Our team will reply during business hours: 08:00–22:00 WIB (UTC+7).
```

---

### T-3 · Off-Hours Auto-Acknowledgment `[WA]` `[Auto]`

*Kirim otomatis jika pesan masuk di luar 08:00–22:00 WIB.*

**[ID]**
```
Halo! Terima kasih sudah menghubungi JVTO. 🌋

Pesan Anda sudah kami terima. Tim kami akan membalas segera saat jam kerja dimulai: 08:00 WIB.

Sementara menunggu, Anda bisa melihat semua paket tur kami di:
👉 javavolcano-touroperator.com

Sampai jumpa!
```

**[EN]**
```
Hello! Thank you for reaching out to JVTO. 🌋

We've received your message. Our team will reply as soon as business hours begin: 08:00 WIB (UTC+7).

While you wait, you can browse all our tour packages at:
👉 javavolcano-touroperator.com

Talk soon!
```

---

## STAGE 2 — DISCOVERY (BANT Qualification — Inan / Human Agent)

*Human-handled. Tujuan: kunci tanggal pasti, jumlah pax, preferensi hotel sebelum membuat quotation. Jangan quote sebelum ketiganya terkunci.*

---

### D-1 · Confirm Need + Timeline `[WA]` `[Inan]` `[BANT: N, T]`

*Gunakan setelah data awal dari T-2 diterima. Gali lebih dalam tentang kebutuhan dan kepastian tanggal.*

**[ID]**
```
Halo [NAMA]! Saya Inan dari tim JVTO. 😊

Terima kasih sudah tertarik dengan [DESTINASI]. Beberapa pertanyaan singkat supaya kami bisa buatkan penawaran yang tepat:

1. Tanggalnya sudah pasti, atau masih tentatif?
2. Ini untuk perjalanan pribadi, keluarga, atau kelompok wisata?
3. Untuk paket Ijen — apakah Anda dan peserta lain dalam kondisi fisik yang fit untuk mendaki sekitar 1–2 jam malam hari? (Kami ada skrining medis opsional yang kami koordinasikan sebelumnya.)

Satu pertanyaan lagi: apakah Anda yang akan mengkonfirmasi dan membayar booking ini, atau ada anggota tim/keluarga lain yang perlu dikonsultasikan dulu?
```

**[EN]**
```
Hello [NAME]! I'm Inan from the JVTO team. 😊

Thanks for your interest in [DESTINATION]. A few quick questions so we can put together the right proposal:

1. Is your travel date confirmed, or still tentative?
2. Is this a personal trip, family, or group tour?
3. For Ijen packages — are you and your fellow travelers physically fit for approximately 1–2 hours of night hiking? (We coordinate a medical screening beforehand as standard.)

One more: will you be the one confirming and paying the booking, or does someone else in your group or family need to be consulted first?
```

---

### D-2 · Budget Tier Check (Subtle) `[WA]` `[Inan]` `[BANT: B]`

*Gunakan setelah D-1 terjawab. Jangan tanya "berapa budget Anda?" — ganti dengan preferensi hotel.*

**[ID]**
```
Untuk akomodasi, JVTO bekerja sama dengan hotel-hotel di titik-titik singgah tur.
Apakah Anda lebih suka hotel bintang 3 (nyaman, praktis) atau bintang 4 ke atas (lebih luas dan premium)?

Ini akan mempengaruhi total harga paket — kami akan tampilkan keduanya di penawaran.
```

**[EN]**
```
For accommodation, JVTO works with hotels at each stop along the route.
Would you prefer 3-star hotels (comfortable, practical) or 4-star and above (more spacious, premium quality)?

This affects the total package price — we'll show you both options in the proposal.
```

---

### D-3 · Lock Confirmation (Before Quoting) `[WA]` `[Inan]`

*Internal checklist Inan. Kirim pesan ini hanya jika ketiga komponen sudah terkunci.*

**Checklist internal (jangan kirim ke customer):**
- [ ] Tanggal pasti terkunci
- [ ] Jumlah pax terkonfirmasi
- [ ] Preferensi hotel (standard / premium) terkonfirmasi
- [ ] Origin: Surabaya atau Bali?

Kalau belum semua, kembali ke D-1 atau D-2. **Jangan buat quotation sebelum checklist ini selesai.**

---

### D-4 · Cold Lead Flag — Timeline Tentatif `[WA]` `[Inan]` `[BANT: T]`

*Gunakan jika customer jawab "masih tentatif" atau perjalanan >3 bulan ke depan.*

**[ID]**
```
Oke, tidak masalah! Untuk perjalanan yang masih dalam perencanaan, kami sarankan Anda mulai dengan menjelajahi paket-paket kami di website:
👉 javavolcano-touroperator.com

Kalau tanggalnya sudah lebih pasti, silakan hubungi kami lagi — kami siap bantu buatkan penawaran resmi.
Untuk Ijen khususnya, kuota permit terbatas di musim ramai, jadi semakin cepat konfirmasi semakin aman. 😊
```

**[EN]**
```
No problem at all! For trips still in the planning phase, we'd suggest browsing our packages first:
👉 javavolcano-touroperator.com

Once your dates are more confirmed, feel free to reach out — we'll put together a formal proposal.
For Ijen especially, permit slots fill up quickly during peak season, so earlier is always better. 😊
```

---

## STAGE 3 — PROPOSAL (Max 2 opsi — Inan / Sam)

*Kirim setelah Discovery selesai dan ketiga komponen terkunci. Max 2 opsi variasi. Lebih dari 2 = jangan dikirim.*

---

### P-1 · WA Proposal Summary `[WA]` `[Inan]` `[Max 2 opsi]`

*Ringkasan pendek via WA. Lampirkan atau follow-up dengan PDF itinerary lengkap.*

**[ID]**
```
Halo [NAMA]! Ini penawaran khusus untuk [JUMLAH PAX] orang, berangkat [TANGGAL]:

━━━━━━━━━━━━━━━━━━━━
🌋 *OPSI A — [NAMA PAKET STANDARD]*
Durasi: [X hari Y malam]
Destinasi: [Ijen / Bromo / dll.]
Hotel: Bintang 3
Harga: IDR [X.XXX.XXX]/orang (total IDR [Y.YYY.YYY])
━━━━━━━━━━━━━━━━━━━━
🌋 *OPSI B — [NAMA PAKET PREMIUM]*
Durasi: [X hari Y malam]
Destinasi: [sama]
Hotel: Bintang 4
Harga: IDR [X.XXX.XXX]/orang (total IDR [Y.YYY.YYY])
━━━━━━━━━━━━━━━━━━━━

✅ *Sudah termasuk*: Transport AC privat, pengemudi + pemandu, tiket masuk semua lokasi, akomodasi + sarapan, masker gas & alat keselamatan Ijen, skrining medis Ijen, air minum harian, kaos JVTO.
❌ *Tidak termasuk*: Penerbangan, tips, pengeluaran pribadi, asuransi perjalanan.

Penawaran ini berlaku hingga *[TANGGAL + 48 JAM]*. 
Setelah itu harga dan ketersediaan perlu dikonfirmasi ulang.

Mau pilih Opsi A atau B? Atau ada pertanyaan dulu? 😊
```

**[EN]**
```
Hello [NAME]! Here's your private proposal for [PAX COUNT] traveler(s), departing [DATE]:

━━━━━━━━━━━━━━━━━━━━
🌋 *OPTION A — [STANDARD PACKAGE NAME]*
Duration: [X days Y nights]
Destinations: [Ijen / Bromo / etc.]
Hotels: 3-star
Price: IDR [X,XXX,XXX]/person (total IDR [Y,YYY,YYY])
━━━━━━━━━━━━━━━━━━━━
🌋 *OPTION B — [PREMIUM PACKAGE NAME]*
Duration: [X days Y nights]
Destinations: [same]
Hotels: 4-star
Price: IDR [X,XXX,XXX]/person (total IDR [Y,YYY,YYY])
━━━━━━━━━━━━━━━━━━━━

✅ *Included*: Private AC transport, driver + guide, all entrance fees & permits, accommodation + breakfast, Ijen gas masks & safety gear, Ijen medical screening, daily mineral water, JVTO travel T-shirt.
❌ *Not included*: Flights, tips, personal expenses, travel insurance.

This offer is valid until *[DATE + 48 HOURS]*.
After that, pricing and availability need to be reconfirmed.

Which option suits you — A or B? Or any questions first? 😊
```

---

### P-2 · Email Quotation Template `[EMAIL]` `[Inan / Sam]`

*Untuk customer yang prefer email atau request itinerary formal. Lampirkan PDF itinerary.*

**[ID] Subject:** `[JVTO] Penawaran Tur Privat — [NAMA PAKET] · [TANGGAL] · [X Pax]`

```
Halo [NAMA],

Terima kasih sudah menghubungi Java Volcano Tour Operator (JVTO).
Berikut penawaran resmi untuk perjalanan Anda:

DETAIL PERJALANAN
─────────────────
Paket     : [NAMA PAKET]
Tanggal   : [TANGGAL KEBERANGKATAN]
Peserta   : [X] orang
Origin    : [Surabaya / Bali]
Durasi    : [X hari Y malam]

HARGA
─────────────────
Opsi A (Hotel Bintang 3) : IDR [X.XXX.XXX]/orang · Total IDR [Y.YYY.YYY]
Opsi B (Hotel Bintang 4) : IDR [X.XXX.XXX]/orang · Total IDR [Y.YYY.YYY]

SUDAH TERMASUK
─────────────────
✓ Transport AC privat (MPV / Hiace sesuai jumlah peserta)
✓ Pengemudi profesional + pemandu wisata berbahasa Inggris
✓ Tiket masuk dan permit semua lokasi di itinerary
✓ Akomodasi + sarapan setiap malam
✓ Masker gas & trekking poles Ijen (untuk paket Ijen)
✓ Koordinasi skrining medis Ijen (untuk paket Ijen)
✓ Air minum harian
✓ Kaos perjalanan JVTO (1 per peserta)

BELUM TERMASUK
─────────────────
✗ Penerbangan internasional / domestik
✗ Tips untuk pengemudi dan pemandu
✗ Pengeluaran pribadi (snack, oleh-oleh, laundry)
✗ Asuransi perjalanan

CARA KONFIRMASI
─────────────────
1. Konfirmasi paket pilihan (Opsi A atau B) via email atau WhatsApp
2. Kami kirimkan link pembayaran deposit (20% dari total)
3. Setelah deposit diterima, E-Voucher resmi diterbitkan
4. Akses My Booking Portal untuk detail lengkap perjalanan

Penawaran ini berlaku hingga: [TANGGAL + 48 JAM]

Untuk pertanyaan, balas email ini atau hubungi WhatsApp kami:
📱 +62 822-4478-8833 (08:00–22:00 WIB)
📧 hello@javavolcano-touroperator.com

Salam,
[NAMA STAF]
Java Volcano Tour Operator
javavolcano-touroperator.com
```

**[EN] Subject:** `[JVTO] Private Tour Proposal — [PACKAGE NAME] · [DATE] · [X Pax]`

```
Dear [NAME],

Thank you for reaching out to Java Volcano Tour Operator (JVTO).
Please find your private tour proposal below:

TRIP DETAILS
─────────────────
Package   : [PACKAGE NAME]
Date      : [DEPARTURE DATE]
Travelers : [X] people
Origin    : [Surabaya / Bali]
Duration  : [X days Y nights]

PRICING
─────────────────
Option A (3-star hotels) : IDR [X,XXX,XXX]/person · Total IDR [Y,YYY,YYY]
Option B (4-star hotels) : IDR [X,XXX,XXX]/person · Total IDR [Y,YYY,YYY]

INCLUDED
─────────────────
✓ Private air-conditioned transport (MPV / Hiace based on group size)
✓ Professional driver + English-speaking escort guide
✓ All entrance fees and permits for every listed location
✓ Accommodation + breakfast every night
✓ Gas masks & trekking poles at Ijen (for Ijen packages)
✓ Ijen medical screening coordination (for Ijen packages)
✓ Daily mineral water in vehicle
✓ JVTO travel T-shirt (1 per participant)

NOT INCLUDED
─────────────────
✗ International / domestic flights
✗ Tips for driver and guide
✗ Personal expenses (snacks, souvenirs, laundry)
✗ Travel insurance (recommended — JVTO does not sell it)

HOW TO CONFIRM
─────────────────
1. Confirm your preferred option (A or B) via email or WhatsApp
2. We'll send a secure payment link for the deposit (20% of total)
3. Once deposit is received, your Official E-Voucher (PDF) is issued
4. Access the My Booking Portal for full trip details

This proposal is valid until: [DATE + 48 HOURS]

Questions? Reply to this email or reach us on WhatsApp:
📱 +62 822-4478-8833 (08:00–22:00 WIB / UTC+7)
📧 hello@javavolcano-touroperator.com

Warm regards,
[STAFF NAME]
Java Volcano Tour Operator
javavolcano-touroperator.com
```

---

## STAGE 4 — URGENCY & CLOSING (Inan / Sam)

---

### U-1 · Price Validity Reminder (24-Hour Auto-Follow-Up) `[WA]` `[Auto or Inan]`

*Kirim 24 jam sebelum masa berlaku penawaran habis, jika customer belum konfirmasi.*

**[ID]**
```
Halo [NAMA]! 👋

Sekadar mengingatkan — penawaran tur privat untuk [TANGGAL] akan berakhir besok, [DEADLINE].

Untuk paket Ijen, slot permit sangat terbatas di periode ini. Kami tidak bisa menjamin ketersediaan jika dikonfirmasi setelah deadline.

Jika Anda siap lanjut, cukup balas WA ini dan kami bantu proses depositnya. 😊
```

**[EN]**
```
Hello [NAME]! 👋

Just a friendly reminder — your private tour proposal for [DATE] expires tomorrow, [DEADLINE].

For Ijen packages, permit slots are limited during this period. We can't guarantee availability after the deadline.

If you're ready to proceed, just reply here and we'll walk you through the deposit. 😊
```

---

### U-2 · Deposit / Payment Instructions `[WA]` `[Inan]` `[Setelah customer konfirmasi opsi]`

**[ID]**
```
Bagus! Mari kita amankan tanggal [TANGGAL] untuk [X] orang. 🎉

DETAIL PEMBAYARAN DEPOSIT
──────────────────────────
Paket      : [NAMA PAKET] — Opsi [A/B]
Total Paket: IDR [TOTAL]
Deposit DP : IDR [20% TOTAL] (20%)

Cara bayar paling cepat:
👉 Kartu kredit/debit: Kami kirimkan link pembayaran aman (Midtrans/Stripe)
   → Saldo dilunasi paling lambat 5 hari sebelum hari-H via kartu

Atau via transfer bank:
🏦 BRI — PT Java Volcano Rendezvous — 001301001779564
🏦 BCA — PT Java Volcano Rendezvous — 1200944352
   → Saldo dilunasi paling lambat 3 hari sebelum hari-H via transfer

⚠️ Catatan penting: JVTO tidak pernah meminta nomor kartu, CVV, atau password perbankan via chat.
Kalau ada link atau nomor rekening berbeda dari di atas, tolong verifikasi dulu.

Setelah deposit masuk, E-Voucher resmi akan diterbitkan dalam 1–2 jam kerja. ✅
```

**[EN]**
```
Excellent! Let's secure [DATE] for [X] traveler(s). 🎉

DEPOSIT PAYMENT DETAILS
──────────────────────────
Package    : [PACKAGE NAME] — Option [A/B]
Total      : IDR [TOTAL]
Deposit    : IDR [20% TOTAL] (20%)

Fastest option:
👉 Credit/debit card: We'll send you a secure payment link (Midtrans/Stripe)
   → Balance due no later than 5 days before Day 1 via card

Or bank transfer:
🏦 BRI — PT Java Volcano Rendezvous — 001301001779564 — SWIFT: BRINIDJAXXX
🏦 BCA — PT Java Volcano Rendezvous — 1200944352 — SWIFT: CENAIDJAXXX
   → Balance due no later than 3 days before Day 1

⚠️ Security note: JVTO will never ask for your full card number, CVV, or banking password via chat.
If you receive a different account number or link, please verify through our official WhatsApp first.

Once deposit is received, your Official E-Voucher (PDF) will be issued within 1–2 business hours. ✅
```

---

### U-3 · E-Voucher Confirmation (Post-DP) `[WA]` `[Auto or Inan]`

**[ID]**
```
✅ Deposit diterima! Booking Anda untuk [PAKET] tanggal [TANGGAL] sudah terkonfirmasi.

E-Voucher resmi sedang kami proses — akan kami kirimkan ke email Anda dalam 1–2 jam kerja.

Selanjutnya, Anda akan mendapat akses ke *My Booking Portal* untuk melihat detail lengkap: jadwal harian, hotel, info pickup, dan checklist persiapan.

Selamat bersiap untuk petualangan Anda! 🌋
```

**[EN]**
```
✅ Deposit received! Your booking for [PACKAGE] on [DATE] is now confirmed.

Your Official E-Voucher (PDF) is being prepared — we'll send it to your email within 1–2 business hours.

You'll also receive access to the *My Booking Portal*, where you can see your full itinerary, hotel details, pickup info, and a preparation checklist.

We're looking forward to your adventure! 🌋
```

---

## POST-BOOKING — Pre-Departure & Post-Tour

---

### PB-1 · H-7 Reminder `[WA]` `[Auto atau Inan]`

*Kirim 7 hari sebelum keberangkatan.*

**[ID]**
```
Halo [NAMA]! 🌋 Perjalanan Anda ke [DESTINASI] tinggal *7 hari lagi!*

Beberapa hal untuk dipersiapkan:

*PAKAIAN & PERLENGKAPAN*
[Untuk Ijen / Bromo:]
• Jaket tebal atau lapis-lapis (Ijen: 10–15°C · Bromo: 5–15°C malam hari)
• Sepatu hiking dengan grip yang baik
• Celana panjang, lengan panjang
• Senter kepala (headlamp) — opsional tapi disarankan
• ⚠️ Jangan pakai perhiasan perak ke Ijen — gas sulfur merusak permanen

[Untuk Tumpak Sewu / Madakaripura:]
• Pakaian yang bisa basah & sepatu sandal grip
• Kantong plastik / dry bag untuk HP dan barang berharga
• Baju ganti

*PICKUP*
Konfirmasi jam dan lokasi pickup Anda ada di E-Voucher. Pengemudi akan menghubungi Anda H-1.

Ada pertanyaan? Balas WA ini kapan saja (08:00–22:00 WIB). 😊
```

**[EN]**
```
Hello [NAME]! 🌋 Your trip to [DESTINATION] is *7 days away!*

Here's a quick preparation checklist:

*CLOTHING & GEAR*
[For Ijen / Bromo:]
• Warm layers — thermal or multiple layers (Ijen: 10–15°C · Bromo: 5–15°C at night)
• Hiking shoes with good grip
• Long trousers and long sleeves
• Headlamp — optional but recommended
• ⚠️ No silver jewelry at Ijen — sulfur gases tarnish silver permanently

[For Tumpak Sewu / Madakaripura:]
• Clothes and shoes that can get wet
• Waterproof bag / dry bag for phone and valuables
• Change of clothes

*PICKUP*
Your confirmed pickup time and location are on your E-Voucher. Your driver will contact you the day before.

Any questions? Reply here anytime (08:00–22:00 WIB / UTC+7). 😊
```

---

### PB-2 · H-1 Driver Details `[WA]` `[Inan]`

*Kirim 1 hari sebelum keberangkatan.*

**[ID]**
```
Halo [NAMA]! Besok hari petualangannya! 🌋

Ini detail penjemputan Anda:

🚗 *Pengemudi*: [NAMA PENGEMUDI]
📱 *WhatsApp*: [NOMOR WA PENGEMUDI]
🕐 *Jam pickup*: [JAM] WIB
📍 *Lokasi*: [TITIK PICKUP — hotel/bandara/stasiun]

[Jika ada skrining medis Ijen:]
🏥 Perawat skrining akan datang ke hotel Anda malam ini sekitar jam [JAM]. Mohon pastikan semua peserta ada di hotel.

Tidur cukup malam ini — perjalanan dimulai dini hari! 😊
Kalau ada apa-apa, hubungi WA ini atau langsung [NAMA PENGEMUDI].
```

**[EN]**
```
Hello [NAME]! Tomorrow's the big day! 🌋

Here are your pickup details:

🚗 *Driver*: [DRIVER NAME]
📱 *WhatsApp*: [DRIVER WA NUMBER]
🕐 *Pickup time*: [TIME] WIB (UTC+7)
📍 *Location*: [PICKUP POINT — hotel/airport/station]

[If Ijen medical screening is included:]
🏥 The medical screening nurse will visit your hotel tonight around [TIME]. Please make sure all travelers are available at the hotel.

Get some rest tonight — the journey starts early! 😊
For anything urgent, contact this number or reach [DRIVER NAME] directly.
```

---

### PB-3 · Post-Tour Review Request `[WA]` `[Auto]` `[24 jam setelah tour selesai]`

*Kirim otomatis 24 jam setelah tanggal terakhir tur.*

**[ID]**
```
Halo [NAMA]! Semoga perjalanan ke [DESTINASI] berkesan. 🌋

Kami di JVTO sangat menghargai pendapat Anda. Jika Anda punya 2 menit, ulasan jujur Anda sangat membantu kami dan calon wisatawan lainnya:

⭐ Trustpilot: https://www.trustpilot.com/review/javavolcano-touroperator.com
⭐ Google: [Link Google Review JVTO]

Kalau ada hal yang kurang memuaskan, tolong sampaikan langsung ke kami sebelum menulis ulasan — kami ingin menyelesaikannya terlebih dahulu.

Terima kasih sudah memilih JVTO. Semoga bisa bertemu lagi di petualangan berikutnya! 🙏
```

**[EN]**
```
Hello [NAME]! We hope your trip to [DESTINATION] was everything you hoped for. 🌋

At JVTO, your honest feedback means the world to us — and helps future travelers make their decision.
If you have 2 minutes, we'd really appreciate a review:

⭐ Trustpilot: https://www.trustpilot.com/review/javavolcano-touroperator.com
⭐ Google: [JVTO Google Review Link]

If anything didn't meet your expectations, please let us know directly before posting — we'd love the chance to make it right first.

Thank you for choosing JVTO. Hope to see you again on your next East Java adventure! 🙏
```

---

## HANDLING COMMON OBJECTIONS

*Scripts singkat untuk pertanyaan yang sering muncul. Mengikuti SFC/FCR principle: jawab lengkap sekali.*

---

### OB-1 · "Berapa harga pastinya?" (sebelum tanggal terkunci) `[WA]` `[Inan]`

**[ID]**
```
Harga kami dihitung berdasarkan jumlah peserta dan tanggal keberangkatan.

Untuk penawaran yang akurat, boleh konfirmasi:
• Tanggal pasti atau kisaran tanggal
• Jumlah peserta

Setelah itu kami berikan harga per orang langsung — tidak ada biaya tersembunyi, semua sudah termasuk transport, hotel, tiket, pemandu, dan sarapan.
```

**[EN]**
```
Our pricing is calculated based on your group size and travel dates.

For an accurate quote, could you confirm:
• Your preferred date (or date range)
• Number of travelers

Once we have those, we'll give you the exact per-person price — no hidden costs, everything included (transport, hotel, tickets, guide, breakfast).
```

---

### OB-2 · "Apa bedanya JVTO dengan operator lain?" `[WA]` `[Inan]`

**[ID]**
```
Ada 3 hal yang membedakan JVTO:

1. *Didirikan Tourist Police aktif* — Bapak Sam (Bripka Agung Sambuko) adalah anggota aktif Tourist Police East Java. Tidak ada operator Ijen/Bromo lain yang punya latar belakang ini.

2. *100% privat* — Setiap booking mendapat kendaraan, pengemudi, dan pemandu sendiri. Kami tidak pernah menggabungkan grup berbeda dalam satu tur.

3. *Skrining medis Ijen* — Perawat datang ke hotel Anda malam sebelum pendakian. Ini standar BBKSDA, bukan formalitas — dan kami yang koordinasikan, termasuk dalam harga.

Lisensi kami bisa diverifikasi: NIB 1102230032918 · TDUP · HPWKI · BBKSDA · POLPAR.
```

**[EN]**
```
Three things set JVTO apart:

1. *Founded by an active Tourist Police officer* — Mr. Sam (Bripka Agung Sambuko) is an active Tourist Police officer in East Java. No other Ijen/Bromo operator has this background.

2. *100% private tours* — Every booking gets its own vehicle, driver, and guide. We never mix different groups into a single tour.

3. *Ijen medical screening* — A nurse visits your hotel the evening before the hike. This is a BBKSDA requirement, not a formality — and we coordinate it, included in the price.

Our licenses are publicly verifiable: NIB 1102230032918 · TDUP · HPWKI · BBKSDA · POLPAR.
```

---

### OB-3 · "Apakah ada refund jika Ijen tutup?" `[WA]` `[Inan]`

**[ID]**
```
Kebijakan JVTO untuk penutupan Ijen:

Jika Ijen tutup karena kondisi alam atau kebijakan BBKSDA, kami akan:
• Tawarkan rute alternatif yang aman (mis. Air Terjun Jagir atau lokasi lain di area Banyuwangi)
• Atau tawarkan penjadwalan ulang ke tanggal lain (gratis, satu kali, tersedia slot)
• Jika elemen utama tidak bisa diganti → Travel Credit senilai komponen yang tidak bisa dijalankan

Travel Credit tidak kadaluarsa dan bisa ditransfer ke orang lain.
Refund tunai tidak tersedia untuk pembatalan inisiatif tamu, kecuali ada ketentuan hukum yang berlaku.
```

**[EN]**
```
JVTO's policy for Ijen closures:

If Ijen closes due to volcanic conditions or BBKSDA regulation, we will:
• Offer a safe alternative route (e.g., Jagir Waterfall or another Banyuwangi-area location)
• Or offer a free reschedule to another available date
• If the main element can't be replaced → Travel Credit for the affected components

Travel Credit has no expiry and is transferable to another person.
Cash refunds are not available for guest-initiated cancellations, except where required by applicable law.
```

---

### OB-4 · "Apakah bisa request jadwal khusus?" `[WA]` `[Inan]`

**[ID]**
```
Kami menerima micro-customization dalam batas tertentu:

✅ Bisa: Ganti kamar (twin bed vs double), upgrade hotel, tambah aktivitas opsional di lokasi (mis. berkuda di Bromo)
✅ Bisa: Sesuaikan waktu pickup sesuai penerbangan/kereta Anda
❌ Tidak bisa: Ubah urutan destinasi utama atau durasi paket secara signifikan
❌ Tidak bisa: Sewa kendaraan saja tanpa paket lengkap

Kalau ada kebutuhan spesifik, sampaikan saja — kami usahakan dalam batas operasional kami.
```

**[EN]**
```
We do accommodate micro-customizations within certain limits:

✅ Yes: Room type change (twin vs double bed), hotel upgrades, optional on-site activities (e.g., horse riding at Bromo)
✅ Yes: Adjust pickup time to fit your flight or train schedule
❌ No: Changing the main destination sequence or significantly altering the package duration
❌ No: Vehicle-only or transport-only services (we operate end-to-end packages)

If you have a specific need, just let us know — we'll do our best within our operational model.
```

---

## USAGE NOTES

- **Harga**: Jangan masukkan angka harga di template — selalu ambil dari -> [[products/packages-full-pricing]] untuk pax tier yang sesuai sebelum kirim.
- **Silver warning**: Selalu sertakan di H-7 reminder untuk paket Ijen. Sumber: -> [[sources/jvto-travel-guide-en]] §packing.
- **Ijen first Friday**: Cek jadwal penutupan rutin (setiap Jumat pertama bulan) sebelum konfirmasi tanggal. Sumber: -> [[website/operational-facts]] §ijen-closure.
- **Pickup timing**: Day 1 latest pickup 16:00 WIB. Last-day flight jangan sebelum 18:00 WIB (20:00 WIB lebih aman). Sumber: -> [[website/operational-facts]] §arrival-departure.
- **GDPR rule**: Jangan minta data paspor, kondisi medis, atau ukuran sepatu sebelum DP diterima. Sumber: -> [[sources/comm-management-theory]] §GDPR.
- **Authority check**: Jika customer bilang "saya perlu konsultasikan dulu" → set follow-up reminder 48 jam, jangan push. Sumber: BANT-A.
