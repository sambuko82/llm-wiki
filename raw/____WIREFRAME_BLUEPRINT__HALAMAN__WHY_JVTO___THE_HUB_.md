🗺️ WIREFRAME BLUEPRINT: HALAMAN "WHY JVTO" (THE HUB)

File Path: /src/app/why-jvto/page.tsx
Konsep Visual Utama: Dark Mode Authority (Biru Dongker/Slate/Oranye), Glassmorphism Cards, Estetika Forensik Bersih.
Sumber Data: Di-render secara dinamis dari /content/why-jvto-ssot.json via SSOTRenderer.tsx.

⚙️ LAYER 0: INJEKSI SEO & SCHEMA (INVISIBLE LAYER)

Berjalan di latar belakang untuk optimasi E-E-A-T.

Di /src/app/layout.tsx (Global): <JsonLdInjector /> menyuntikkan Schema Level 1 & 2 (TravelAgency, Organization, PostalAddress).

Di /src/app/why-jvto/layout.tsx (Hub Layout): <JsonLdInjector /> menyuntikkan Schema Level 3 & 4 (ItemList untuk pilar kepercayaan, Person untuk Otoritas Polisi, dan MedicalBusiness untuk Skrining).

🌐 GLOBAL NAVIGATION

Komponen: <StickyHeader /> (Konsisten & Responsif)

+-----------------------------------------------------------------------------+
| [ LOGO JVTO ]     Safety | History | Legal | Reviews | Health   [ BOOK NOW ]|
+-----------------------------------------------------------------------------+


⬇ Transisi Scroll: Pengantar Tesis Utama ⬇

🛡️ CORE THESIS (HERO SECTION)

Tujuan: Mengunci perhatian pengguna dengan diferensiator terkuat JVTO (Kepemimpinan Polisi & Kepastian Operasional).
Data: why-jvto-ssot.json (hero_subhead, h1)

+-----------------------------------------------------------------------------+
|  [Background: Gambar gelap/elegan operasi lapangan JVTO dengan efek kabut]  |
|                                                                             |
|  [ Lencana: 🔒 SHA-256 Verified Digital Trust Fortress ]                    |
|                                                                             |
|  H1: OPERATIONAL CERTAINTY IN THE RING OF FIRE                              |
|                                                                             |
|  P:  Dalam lanskap vulkanik Jawa Timur yang penuh ketidakpastian, JVTO      |
|      menjual kepastian operasional. Dibangun di atas disiplin kepolisian,   |
|      bukti yang terdokumentasi, dan eksekusi lokal—bukan sekadar janji.     |
|                                                                             |
|  [ Tombol Primer: How to Book & Pay ]   [ Tombol Sekunder: Explore Proof ]  |
+-----------------------------------------------------------------------------+


⬇ Visual Cue: Panah ke bawah "The Pillars of Trust" ⬇

🚓 SECTION 1: AUTHORITY SHIELD (POLICE-LED)

Komponen: <AuthorityShield />
Tujuan: Membangun kredibilitas instan berbasis otoritas negara (The "Nuclear Option").
Data: SSOTRenderer memanggil entitas Agung Sambuko & Ditpamobvit.

+-----------------------------------------------------------------------------+
|  [ Ikon: 🛡️ Perisai Polisi Emas/Oranye ]                                      |
|  H2: State-Sanctioned Security & Police Command                             |
|  P: Operasional kami dipimpin oleh Perwira Polisi Pariwisata Aktif.         |
|                                                                             |
|  [ Grid 2 Kolom - Glassmorphism Card ]                                      |
|  +-------------------------+ +--------------------------------------------+ |
|  | [Foto: Mr. Sam berseragam]| | "Protection Beyond Business"               | |
|  | Lencana: Active Duty      | | • Pengawalan & Patroli Resmi               | |
|  | Ditpamobvit Officer       | | • Akses Intelijen Vulkanik Real-time       | |
|  +-------------------------+ +--------------------------------------------+ |
|                                                                             |
|  🔗 [Tombol Rute]: "View Forensic Police Proof (SPRIN & Detik.com) ➔"       |
|     Target Navigasi: `/src/app/why-jvto/proof/police/page.tsx`              |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Otoritas yang kuat lahir dari sejarah yang panjang..." ⬇

🏛️ SECTION 2: TIMELINE TWIN (PROVEN HISTORY)

Komponen: <TimelineTwin />
Tujuan: Mematahkan keraguan tentang "operator musiman" dengan bukti fisik lintas dekade.
Data: SSOTRenderer memanggil entitas historical-recognition.

+-----------------------------------------------------------------------------+
|  H2: Decades of Verifiable Truth (Time-on-Market)                           |
|                                                                             |
|  [ Garis Waktu Vertikal Interaktif ]                                        |
|                                                                             |
|  ⏳ 2015 ━━━ [ Gambar: Plakat Booking.com & Label Pengiriman Asli ]         |
|               "Fondasi awal kami sebagai Ijen Bondowoso Homestay."          |
|                                                                             |
|  ⏳ 2018 ━━━ [ Gambar: Scan Halaman Buku Stefan Loose - Hal 287 ]           |
|               "Diakui oleh buku panduan paling ketat dari Jerman."          |
|                                                                             |
|  🔗 [Tombol Rute]: "Inspect Time-Proof Artifacts ➔"                         |
|     Target Navigasi: `/src/app/why-jvto/proof/history/page.tsx`             |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Sejarah ini dipayungi oleh entitas korporat yang legal..." ⬇

⚖️ SECTION 3: FORTRESS CARD (LEGAL HQ)

Komponen: <FortressCard />
Tujuan: Menunjukkan akuntabilitas korporat, entitas PT, dan kehadiran fisik.
Data: SSOTRenderer memanggil entitas legal-entity & NIB.

+-----------------------------------------------------------------------------+
|  H2: Corporate Accountability & Legal Infrastructure                        |
|                                                                             |
|  [ 3 Kolom Kartu Solid / Elegan ]                                           |
|  +--------------------+ +--------------------+ +--------------------------+ |
|  | 🏢 Physical Office | | 📄 NIB Registry    | | 📄 TDUP License          | |
|  | Jl. Khairil Anwar  | | No: 1102230032918  | | KBLI 79120               | |
|  | Bondowoso HQ       | | Verified via OSS   | | PT Java Volcano Rend.    | |
|  +--------------------+ +--------------------+ +--------------------------+ |
|                                                                             |
|  🔗 [Tombol Rute]: "View Cryptographic Legal Documents ➔"                   |
|     Target Navigasi: `/src/app/why-jvto/proof/legal/page.tsx`               |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Keamanan legal & struktural ini menghasilkan ulasan nyata..." ⬇

⭐ SECTION 4: TRIANGULATION GRID (REVIEWS)

Komponen: <TriangulationGrid />
Tujuan: Membangun Social Proof lintas platform (TripAdvisor, Trustpilot, Google).
Data: SSOTRenderer memanggil ulasan yang terikat pada Kru (Gufron, Rendi).

+-----------------------------------------------------------------------------+
|  H2: The Personality Economy (Guest Voices)                                 |
|  P: Kami menolak ulasan palsu. Ini adalah suara dari platform independen.   |
|                                                                             |
|  [ Layout Masonry Grid untuk Ulasan ]                                       |
|  +-------------------------+ +-------------------------+                    |
|  | ★★★★★ (Trustpilot)      | | ★★★★★ (TripAdvisor)     |                    |
|  | 📸 Gufron (Guide)       | | ⛑️ Rendi (Guide)        |                    |
|  | "He chooses good spots  | | "Held our hands down    |                    |
|  | for photos..."          | | the steep crater."      |                    |
|  | - Nina Nguyen           | | - Wing Shan Lui         |                    |
|  +-------------------------+ +-------------------------+                    |
|                                                                             |
|  🔗 [Tombol Rute]: "Analyze Multi-Platform Reviews ➔"                       |
|     Target Navigasi: `/src/app/why-jvto/reviews/page.tsx`                   |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Dan semua tur ini diwajibkan melewati gerbang keselamatan kami..." ⬇

🏥 SECTION 5: HEALTH FLOW (IJEN SCREENING)

Komponen: <HealthFlow />
Tujuan: Mengilustrasikan ketegasan protokol medis prakondisi (The Hard Stop).
Data: SSOTRenderer memanggil health_protocol & dr. Ahmad Irwandanu.

+-----------------------------------------------------------------------------+
|  H2: Mandatory Biological Proof (Ijen Health Screening)                     |
|                                                                             |
|  [ Flowchart Visual Dinamis (Langkah 1 -> 2 -> 3) ]                         |
|                                                                             |
|  [1. Vitals Check] ➔ [2. Doctor Validation] ➔ [3. Digital Certificate]    |
|   (SpO2, BP, HR)      (dr. Ahmad Irwandanu)      (QR Code Clearance)        |
|                                                                             |
|  🚨 [ Alert Box Merah ]: THE "HARD STOP" POLICY                             |
|  "Jika tamu dinilai 'Unfit', pendakian dibatalkan seketika. Kami memilih    |
|  kehilangan pendapatan daripada mengorbankan nyawa Anda."                   |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Semua infrastruktur ini memberi Anda nilai nyata (Value)..." ⬇

🎒 SECTION 6: VALUE LIST (TANGIBLE VALUE)

Komponen: <ValueList />
Tujuan: Daftar manfaat spesifik, nyata, dan bukan sekadar kata-kata marketing kosong.
Data: SSOTRenderer memanggil operational_logic.

+-----------------------------------------------------------------------------+
|  H2: The JVTO Tangible Difference                                           |
|                                                                             |
|  [ Daftar Ceklis dengan Ikon Kustom / High-Fidelity ]                       |
|  ✔️ Eksklusivitas Privat (100% tanpa tamu campuran/strangers).              |
|  ✔️ Perlengkapan Keselamatan Kelas Industri (Masker gas standar tambang).   |
|  ✔️ Eksekusi "Plan B" Terjamin (Jika aktivitas vulkanik meningkat).         |
|  ✔️ Redundansi Kru (Supir khusus fokus mengemudi + Pemandu khusus fokus     |
|     menjaga Anda).                                                          |
+-----------------------------------------------------------------------------+


⬇ Alur Logika: "Kami didukung oleh ekosistem global yang memvalidasi operasi kami..." ⬇

🤝 SECTION 7: PARTNER LOGOS (PARTNERS)

Komponen: <PartnerLogos />
Tujuan: Afiliasi dengan otoritas eksternal untuk validasi fairness dan sustainability.
Data: SSOTRenderer memanggil partner_network.

+-----------------------------------------------------------------------------+
|  H2: Verified by the Ecosystem                                              |
|                                                                             |
|  [ Baris Logo Flexbox - Berubah dari Grayscale ke Warna saat di-hover ]     |
|                                                                             |
|  [ Logo ISIC ]    (Tooltip: International Student Pricing Verified)         |
|  [ Logo HPWKI ]   (Tooltip: Official Ijen Volcanic Safety Association)      |
|  [ Logo INDECON ] (Tooltip: Indonesian Ecotourism Network Member)           |
+-----------------------------------------------------------------------------+


🏁 GLOBAL FOOTER & FINAL CTA

Tujuan: Konversi setelah kepercayaan terbangun.

+-----------------------------------------------------------------------------+
|  H2: Ready for Operational Certainty?                                       |
|                                                                             |
|  [ Tombol Besar: Secure Your Expedition (Book Now) ]                        |
|  [ Tautan Teks: Consult via WhatsApp with Mr. Sam's Team ]                  |
|                                                                             |
|  [Footer Links]: Privacy Policy | Terms of Service | Contact                |
|  Microcopy: © 2026 PT Java Volcano Rendezvous. A Verified Entity.           |
+-----------------------------------------------------------------------------+
