---
type: strategy
title: JVTO Tooling Ecosystem — Comprehensive Mapping & Analysis
last_updated: 2026-05-27
sources: [system-mcp-inventory, system-skills-inventory, wiki/index, wiki/overview]
audience: founder (SAM)
status: living document
---

# JVTO Tooling Ecosystem — Comprehensive Mapping & Analysis

Analisis pemetaan menyeluruh atas tiga lapisan kapabilitas yang tersedia di sesi ini:
**(A)** MCP servers yang sudah connected (tools langsung jalan), **(B)** MCP servers yang masih perlu auth (siap dipasang), **(C)** Skills ecosystem (~155 skill resmi). Disilang-rujuk dengan keadaan wiki JVTO saat ini (92 pages, 16 packages live, 195 reviews konsolidasi, sprint terbuka dengan 7 open items).

---

## 1. EXECUTIVE DIAGNOSIS

### 1.1 Posisi sekarang (state)

JVTO punya **fondasi knowledge base sangat matang** (92 wiki pages, SSOT v6.0, backoffice DB 210 tables/63k rows, Trust Stack 24 proof items dengan SHA-256, 9 canonical claims C1–C9, voice invariants tegas). Output production sudah jalan: 16 tour pages live, 16 destination/policy/travel-guide pages, 23 schema JSON-LD, 14 crew bio pages.

**Yang masih bottleneck**: produksi konten masih manual (compile → tulis → publish). Wiki kaya, tapi belum terhubung otomatis ke kanal eksekusi (sosial media, email, WhatsApp, deploy).

### 1.2 Yang berubah hari ini (capability shift)

Sesi ini membuka akses ke ekosistem **>200 MCP tools** + **~155 skills**. Secara fungsional, ini menambah 4 layer kapabilitas baru di atas wiki:

| Layer | Sebelum | Sekarang |
|---|---|---|
| **Intelligence** (riset/data) | Manual web search | Ahrefs (rank tracker, GSC, brand radar), AllTrails, Hotel search, Wolfram |
| **Production** (asset/copy) | Manual writing | Canva MCP, Higgsfield image/video gen, brand-voice skills |
| **Distribution** (publish/send) | Manual copy-paste | Gmail/Calendar/Drive native, Vercel deploy, Canva post, (pending: Slack/Notion/Klaviyo/PayPal) |
| **Operations** (rutinitas) | Ad-hoc | Scheduled tasks + 35 small-business skills + artifacts dashboard |

### 1.3 Bottom line (1 kalimat)

Wiki JVTO sudah ready untuk dihubungkan ke **closed-loop content & ops engine**: dari source → wiki → asset gen (Canva/Higgsfield) → distribusi (Gmail/Vercel/social) → measurement (Ahrefs/reviews) → balik ke wiki. Yang hilang sekarang hanya **integrator/orchestrator layer** — bisa dibangun pakai scheduled-tasks + artifacts + 3-4 skill kunci tanpa coding tambahan.

---

## 2. PINPOINTS (peta detail per tool)

### 2.1 MCP Servers — Tier 1: SUDAH LIVE (langsung jalan)

| Server | Kategori | Tools utama | Status |
|---|---|---|---|
| **Gmail** (`11930f59`) | Inbox/Comms | create_draft, search_threads, list/create/delete/update label, get_thread, label_message/thread | LIVE |
| **Google Calendar** (`8842a316`) | Scheduling | create/update/delete_event, list_events, list_calendars, respond_to_event, suggest_time | LIVE |
| **Google Drive** (`8dbe492a`) | File storage | search_files, read_file_content, download_file_content, create_file, copy_file, get_file_metadata, list_recent_files | LIVE |
| **Ahrefs** (`10e6eb2f`) | SEO/Marketing intel | 90+ tools: rank-tracker, site-explorer, keywords-explorer, GSC integration, brand-radar (AI mention tracking), site-audit, social-media, web-analytics, render-data-table/chart/scorecard | LIVE |
| **AllTrails** (`0bfe5a34`) | Trail data | find_trails_near_location, find_trails_within_bounds, get_trail_details, get_trail_weather_overview, search_trails_by_name | LIVE |
| **Hotel Search** (`f9fb0bea`) | Hotel data | search_hotels, compare_hotels, hotel_details | LIVE |
| **Canva** (`986ad785`) | Design | 30+ tools: generate-design (AI + brand template), perform-editing-operations, export-design, list-brand-kits, create-folder, comment-on-design, copy-design, get-presenter-notes, merge-designs, resize-design, upload-asset-from-url | LIVE |
| **Higgsfield** (`f4bd937b`) | AI media gen | generate_image, generate_video, marketing_studio, personal_clipper (video clipping), virality_predictor, characters, presets | LIVE |
| **Vercel** (`21947402`) | Deploy/host | deploy_to_vercel, list_deployments, get_deployment_build_logs, get_runtime_logs, list_projects, check_domain_availability_and_price, search_vercel_documentation, toolbar threads | LIVE |
| **Wolfram** (`adc4f06f`) | Compute | WolframAlpha, WolframLanguageEvaluator, WolframContext | LIVE |
| **Claude in Chrome** | Browser auto | navigate, get_page_text, javascript_tool, read_console_messages, read_network_requests, file_upload, computer (mouse/keyboard), shortcuts | LIVE |
| **Desktop Commander** | OS control | start_process, interact_with_process, edit_block, read/write_file, list_directory, write_pdf, start_search | LIVE |
| **Windows-MCP** | Windows native | PowerShell, FileSystem, Clipboard, Screenshot, Click/Type/Scroll, Process/Registry, Notification, MultiEdit, Scrape | LIVE |
| **PDF Viewer** | PDF interactive | display_pdf, annotate, fill_form, sign, list_pdfs | LIVE |
| **MCP Registry** | Tool discovery | search_mcp_registry, suggest_connectors, list_connectors | LIVE |
| **Plugins/Skills** | Plugin discovery | list_plugins, search_plugins, suggest_plugin_install, list_skills, suggest_skills | LIVE |
| **Cowork** | Session UI | create_artifact, list_artifacts, update_artifact, request_cowork_directory | LIVE |
| **Scheduled Tasks** | Automation | create/update/list_scheduled_task | LIVE |
| **Session Info** | Session memory | list_sessions, read_transcript | LIVE |
| **Workspace** | Sandbox | bash, web_fetch | LIVE |
| **Medicare/NCD** (`21f6fb08`) | US healthcare | search_local/national_coverage, get_contractors, etc. | LIVE (TIDAK relevan untuk JVTO) |

### 2.2 MCP Servers — Tier 2: PERLU AUTH (siap dipasang)

| Server | Domain | Relevansi JVTO | Effort pasang |
|---|---|---|---|
| **PayPal** (`small-business`) | Payment | TINGGI — JVTO terima PayPal di sebagian bookings | OAuth, 2 menit |
| **QuickBooks** (`small-business`) | Accounting | TINGGI — bisa replace/komplemen backoffice finance | OAuth, 2 menit |
| **Stripe** (`small-business`) | Payment | SEDANG — kalau JVTO terima credit card | OAuth, 2 menit |
| **Square** (`small-business`) | POS/Payment | RENDAH — JVTO bukan POS-based | — |
| **Canva** (`small-business`) | Design (alt) | DUPLIKAT — sudah ada Canva di Tier 1 | skip |
| **DocuSign** (`small-business`) | E-signing | SEDANG — untuk MOU vendor/partner | OAuth |
| **Notion** (`productivity`) | Wiki alt | SEDANG — bisa cermin wiki untuk akses mobile | OAuth |
| **Atlassian** (`productivity`) | Confluence/Jira | RENDAH — overkill untuk size JVTO | — |
| **Microsoft 365** (`productivity`) | Office suite | RENDAH — JVTO sudah pakai Google | — |
| **ClickUp** (`productivity`) | Project mgmt | SEDANG — kalau mau tracking sprint formal | OAuth |
| **Linear** (`productivity`) | Issue tracker | SEDANG — kalau jvto-web pakai Linear | OAuth |
| **Monday** (`productivity`) | PM | RENDAH | — |
| **Slack** (`productivity`) | Team chat | SEDANG — kalau ada tim internal di Slack | OAuth |
| **Ahrefs** (`marketing` auth) | SEO | DUPLIKAT — Tier 1 Ahrefs sudah lebih lengkap | skip |
| **Klaviyo** (`marketing`) | Email marketing | TINGGI — bisa ganti/komplemen blast email manual | OAuth |
| **Supermetrics** (`marketing`) | Multi-channel data | SEDANG — kalau iklan FB/IG aktif | OAuth |
| **Apollo** (`sales`) | B2B prospecting | SEDANG — untuk outreach travel agent/MICE | OAuth |
| **Close** (`sales`) | CRM | RENDAH — JVTO punya backoffice CRM | — |
| **Outreach** (`sales`) | Sales engagement | RENDAH — JVTO inbound-driven | — |
| **Fireflies** (`product-management`) | Meeting transcript | SEDANG — record founder strategy calls | OAuth |
| **Amplitude** (`product-management`) | Product analytics | RENDAH — overkill untuk static site | — |
| **Pendo** (`product-management`) | Product analytics | RENDAH | — |
| **Figma** (`brand-voice`) | Design files | SEDANG — kalau jvto-web punya Figma | OAuth |
| **Intercom** (`customer-support`) | Help desk | RENDAH — WA adalah channel primer | — |
| **Guru** (`customer-support`) | KB | RENDAH — wiki sudah jadi KB | — |
| **Hex** (`data`) | Notebooks | RENDAH | — |
| **Datadog** (`engineering`) | Monitoring | RENDAH | — |
| **Prisma** | DB ORM | SEDANG — kalau jvto-web pakai Prisma | OAuth |

### 2.3 Skills — peta per domain

**`small-business` (35 skills) — paling cocok untuk profil JVTO**
Onboarding/router: `smb-onboard`, `smb-router`. Briefings: `business-pulse`, `monday-brief`, `friday-brief`, `quarterly-review`. Content/marketing: `content-strategy`, `run-campaign`, `canva-creator`, `sales-brief`. Finance: `cash-flow-snapshot`, `plan-payroll`, `close-month`, `month-end-prep`, `month-heads-up`, `tax-prep`, `tax-season-organizer`, `invoice-chase`. Pricing: `price-check`, `margin-analyzer`. Customer: `customer-pulse`, `customer-pulse-check`, `handle-complaint`, `ticket-deflector`. Leads: `lead-triage`, `call-list`. CRM: `crm-cleanup`, `crm-maintenance`. Contracts: `contract-review`, `review-contract`. HR: `job-post-builder`.

**`marketing` (8 skills) — direct fit**
`content-creation`, `draft-content`, `brand-review`, `email-sequence`, `campaign-plan`, `performance-report`, `competitive-brief`, `seo-audit`.

**`brand-voice` (3 skills) — direct fit (paling penting!)**
`discover-brand`, `enforce-voice`, `generate-guidelines`. Wiki sudah punya `website/brand-voice.md` + `aeo-claims.md` + `copy-bank.md` — bisa langsung dipakai sebagai source guidelines.

**`sales` (9 skills)** — relevansi sedang
`account-research`, `call-prep`, `pipeline-review`, `forecast`, `draft-outreach`, `daily-briefing`, `create-an-asset`, `competitive-intelligence`, `call-summary`.

**`anthropic-skills` (16 skills) — format helpers**
`docx`, `pptx`, `xlsx`, `pdf`, `canvas-design`, `frontend-design`, `theme-factory`, `brand-guidelines`, `seo-audit`, `campaign-plan`, `internal-comms`, `doc-coauthoring`, `mcp-builder`, `skill-creator`, `setup-cowork`, `consolidate-memory`.

**`ops` (9)**: `change-request`, `process-optimization`, `compliance-tracking`, `process-doc`, `vendor-review`, `status-report`, `runbook`, `risk-assessment`, `capacity-plan`.

**`product-management` (8)**: `brainstorm`/`product-brainstorming`, `competitive-brief`, `roadmap-update`, `metrics-review`, `write-spec`, `synthesize-research`, `stakeholder-update`, `sprint-planning`.

**`human-resources` (9)**: untuk recruit crew baru / formalisasi tim. `onboarding`, `comp-analysis`, `interview-prep`, `performance-review`, `org-planning`, `draft-offer`, `people-report`, `policy-lookup`, `recruiting-pipeline`.

**`design` (7)**: `ux-copy`, `user-research`, `research-synthesis`, `design-system`, `design-handoff`, `design-critique`, `accessibility-review` — relevan untuk jvto-web redesign sprint.

**`data` (10)**: `analyze`, `validate-data`, `build-dashboard`, `create-viz`, `sql-queries`, `statistical-analysis`, `write-query`, `data-context-extractor`, `data-visualization`, `explore-data` — bisa untuk backoffice DB.

**`engineering` (10)**: `system-design`, `testing-strategy`, `tech-debt`, `standup`, `incident-response`, `documentation`, `deploy-checklist`, `debug`, `code-review`, `architecture` — untuk jvto-web codebase.

**`customer-support` (5)**: `customer-research`, `customer-escalation`, `ticket-triage`, `kb-article`, `draft-response`.

**`finance` (8)**: `close-management`, `journal-entry-prep`, `reconciliation`, `audit-support`, `journal-entry`, `financial-statements`, `variance-analysis`, `sox-testing` — terlalu enterprise; pakai versi `small-business` saja.

**`productivity` (4)**: `start`, `memory-management`, `task-management`, `update`.

**`pdf-viewer` (4)**: `annotate`, `fill-form`, `sign`, `open`/`view-pdf`.

**`cowork-plugin-management` (2)**: `create-cowork-plugin`, `cowork-plugin-customizer` — bisa untuk packaging "JVTO Plugin" kalau mau distribute internal.

---

## 3. PAIN POINTS (apa yang sebenarnya menyakitkan untuk JVTO sekarang)

Pain points di-derive dari Current Sprint open items + struktur wiki + nature of tour operator ops.

### 3.1 Pain Point 1 — Content production masih labour-intensive

**Gejala**: Setiap kali ada update SSOT atau review baru, harus manual compile ke 5–15 wiki pages, lalu manual lagi ke website copy, lalu manual ke social post. Sprint catatan menyebut "Silo 2 depth expansion — Madakaripura + Tumpak Sewu + Papuma to 1,500+ words" sebagai blocker.

**Bukti di wiki**: `wiki/ops/compilation-profiles.md` ada (Workflow 5), tapi eksekusinya manual. Tidak ada otomasi yang tarik dari `wiki/destinations/madakaripura.md` → render ke `output/website/pages/destinations/madakaripura-waterfall.md` + `output/website/aeo/madakaripura.md` + post Instagram.

**Dampak**: Kecepatan publish lambat. AEO/SEO opportunity hilang ketika 5 destinasi belum punya konten >1,500 kata.

### 3.2 Pain Point 2 — SEO data tidak dilihat secara live

**Gejala**: `seo-audit-2026-05.md` mencatat "Ahrefs data unavailable — volumes estimated". Sekarang Ahrefs MCP live dengan rank tracker, GSC integration, brand radar (AI mention tracking), site explorer.

**Bukti di wiki**: 15 keyword targets di `seo/seo-strategy.md` tanpa volume real-time. `seo/competitors.md` tier 1-4 tanpa monitoring otomatis.

**Dampak**: Strategi SEO blind. Tidak tahu ranking drift, AI mention share, atau competitor movement.

### 3.3 Pain Point 3 — Reviews 195 total, monitoring manual

**Gejala**: Google Maps 123 + Trustpilot 51 + TripAdvisor 21 = 195 reviews, dikonsolidasikan secara batch (`google-maps-reviews-api-2026.md` di-export sekali). Tidak ada alarm kalau ada review bintang ≤3 baru.

**Bukti**: `reviews/google-tripadvisor-2026.md` is point-in-time snapshot. Open issue: homepage masih show "92 on Google Maps" sementara realita 123.

**Dampak**: Trust signal stale, response time terhadap negative review tidak terjamin, ada urgent fix di sprint.

### 3.4 Pain Point 4 — WhatsApp ops sudah documented tapi belum executable

**Gejala**: `whatsapp/operations-playbook.md` + `rules-engine.md` + `canned-responses.md` ada lengkap (bilingual, BANT-tagged, 7-step pipeline). Tapi runtime-nya belum jalan — masih konsep + reference API doc (`wa-pro-crm-api.md`).

**Dampak**: 5,547 conversations historis di backoffice. Tanpa runtime engine, classification + auto-reply masih manual.

### 3.5 Pain Point 5 — Backoffice DB punya truth, tapi tidak ada dashboard

**Gejala**: 210 tables, 63k rows di MariaDB Hostinger, sudah di-extract jadi CSV + wiki summaries. Tapi data view = file markdown statis. Tidak ada way untuk owner buka dashboard "revenue this month vs last" tanpa minta Claude tarik.

**Dampak**: Decision-making tertunda — perlu request data setiap kali.

### 3.6 Pain Point 6 — Asset generation manual, hilang konsistensi brand

**Gejala**: Social post (`output/social/batch-2026-05-18.md`) ditulis manual. Brand voice di `wiki/website/brand-voice.md` tegas (Style A vs Style B, voice invariants — "blue fire guaranteed" terlarang, "mandatory health screening" tanpa qualifier terlarang). Tapi nothing enforces this saat asset baru di-create.

**Dampak**: Risiko brand drift, terutama kalau ada tangan ketiga (vendor, partner) yang bikin konten JVTO.

### 3.7 Pain Point 7 — Deploy ke jvto-web masih manual

**Gejala**: Output dihasilkan di `output/website/`, tapi pipeline ke production (jvto-web Next.js codebase) belum otomatis. Open issue: "Duplicate TouristTrip in tour page JSON-LD" + "robots.txt Cloudflare conflict" — harus turun tangan ke codebase.

**Dampak**: Hak veto teknis ada di tangan dev, friction antara wiki SSOT dan live site.

### 3.8 Pain Point 8 — Custom tour quoting masih spreadsheet

**Gejala**: `finance/custom-tour-builder.md` adalah template manual COGS + 25% markup. Setiap inquiry custom (lewat WA atau email) → buka rate cards JSON → kalkulasi manual.

**Dampak**: Founder/staff time tersedot, response time lambat, salah hitung mungkin.

### 3.9 Pain Point 9 — Crew/vendor management tidak ada single pane

**Gejala**: 14 crew + 23 hotels + 6 vehicle types + 27 activities tersebar di rate cards, crew registry, hotel registry. Tidak ada view "siapa available minggu depan, sebelum upgrade jadi engagement".

**Dampak**: Scheduling conflict mungkin tertutup sampai terjadi.

### 3.10 Pain Point 10 — Founder bottleneck (single point of decision)

**Gejala**: Mr. Sam multitasking — Tourist Police active duty + tour operator + content reviewer + final approver. Tidak ada autonomous loop yang bisa jalan tanpa dia.

**Dampak**: Scaling capped.

---

## 4. FIT WITH THE PROJECT (mapping tool/skill → JVTO use case)

Format: **JVTO use case** | **Tool/Skill yang paling cocok** | **Wiki page yang di-touch** | **Tingkat fit**.

### 4.1 Content Production & SEO

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Expand Silo 2 destinasi (Madakaripura/Tumpak Sewu/Papuma to 1,500+ words) | `marketing:content-creation` + `brand-voice:enforce-voice` + Ahrefs MCP (keywords + competitor pages by traffic) | `destinations/*` + `output/website/pages/destinations/*` | **TINGGI** |
| Audit SEO live (volumes real, rank, AI mention) | Ahrefs MCP: `keywords-explorer-overview`, `rank-tracker-overview`, `brand-radar-mentions-overview`, `site-audit-issues` | `seo/seo-strategy.md` + `seo/competitors.md` | **TINGGI** |
| Fix homepage stale review count (92→123) | Manual edit jvto-web + `cowork:create_artifact` review monitor | `wiki/index.md`, `reviews/google-tripadvisor-2026.md` | **TINGGI** |
| Deduplicate TouristTrip in tour page JSON-LD | `engineering:debug` + Vercel MCP (read build logs) + Desktop Commander (edit jvto-web) | `website/schema-templates.md` + 16 tour schema files | **SEDANG** |
| Generate AEO Q&A snippets per destination | `anthropic-skills:doc-coauthoring` + wiki source pages | `output/website/aeo/*` | **TINGGI** |
| Generate FAQ pages | `marketing:draft-content` + `brand-voice:enforce-voice` | `website/faq-master.md` + `output/website/faq/*` | **TINGGI** |
| Schema JSON-LD generation per tour | Skill: `anthropic-skills:doc-coauthoring` + wiki templates | `website/schema-templates.md` + `output/website/schema/*` | **TINGGI** |
| GEO/AEO compliance check (llms.txt, sameAs cross-press) | `marketing:seo-audit` + Ahrefs site-audit | `seo/geo-aeo-strategy.md` | **TINGGI** |

### 4.2 Visual & Multimedia Asset Production

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Social media batch (IG/FB/X/LinkedIn) per minggu | Canva MCP `generate-design` + Higgsfield `marketing_studio` + Skill `small-business:canva-creator` + brand kit | `output/social/*` + `wiki/website/brand-voice.md` | **TINGGI** |
| Hero image per destinasi (consistent style) | Higgsfield `generate_image` + reference: `sources/ssot-image-asset-map.md` (54 live images) | `wiki/destinations/*` + image asset map | **TINGGI** |
| Video clip (sunrise Bromo, blue fire Ijen, dll) | Higgsfield `generate_video` + `personal_clipper_create` | `wiki/destinations/*` + GPX waypoints | **SEDANG-TINGGI** |
| Brochure PDF custom tour | Canva `generate-design-structured` + `anthropic-skills:pdf` | `output/marketing/*` | **TINGGI** |
| Crew bio cards untuk team page | Canva brand template + 14 crew portraits | `output/website/pages/team/*` | **TINGGI** |
| Tour itinerary 1-pager PDF | Canva + `anthropic-skills:pdf` | `products/packages-itineraries.md` | **TINGGI** |
| Virality predictor untuk post sebelum publish | Higgsfield `virality_predictor` | sosial batches | **SEDANG** |

### 4.3 Customer Comms & Reviews

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Monitor 195 reviews + alert kalau ≤3★ baru | `cowork:create_artifact` (dashboard) + Ahrefs brand-radar + scheduled-tasks (daily) | `reviews/google-tripadvisor-2026.md` | **TINGGI** |
| Draft reply ke review baru (bilingual, on-brand) | `small-business:ticket-deflector` + `brand-voice:enforce-voice` | `whatsapp/canned-responses.md` | **TINGGI** |
| Customer sentiment monthly digest | `small-business:customer-pulse` + scheduled-task monthly | `reviews/review-patterns.md` | **TINGGI** |
| Handle complaint end-to-end | `small-business:handle-complaint` + WA Pro CRM API | `whatsapp/rules-engine.md` | **SEDANG** (perlu runtime WA) |
| KB article dari resolved complaints | `customer-support:kb-article` | `website/faq-master.md` | **SEDANG** |

### 4.4 Finance & Pricing

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Custom tour quote otomatis dari WA inquiry | Custom flow: parse inquiry → rate cards JSON → `anthropic-skills:xlsx` quote generator | `finance/custom-tour-builder.md` + `finance/rate-cards.md` | **TINGGI** |
| Margin analysis per package | `small-business:margin-analyzer` + `finance/profit-analysis.md` | `finance/package-costs.md` + `finance/profit-analysis.md` | **TINGGI** |
| Pricing scenario (raise 5%/10%) | `small-business:price-check` | `products/packages-full-pricing.md` | **TINGGI** |
| Cash flow 30/60/90 day forecast | `small-business:cash-flow-snapshot` (needs PayPal/QB auth) | `finance/profit-analysis.md` | **SEDANG** (perlu auth) |
| Invoice chase (overdue PayPal) | `small-business:invoice-chase` (needs PayPal auth) | — | **SEDANG** (perlu auth) |
| Tax prep / quarterly estimated | `small-business:tax-prep` / `tax-season-organizer` (needs QB auth) | — | **SEDANG** (perlu auth) |

### 4.5 Operations & Backoffice

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Backoffice DB → live dashboard (revenue, bookings, pax) | `cowork:create_artifact` + custom SQL via Desktop Commander | `sources/backoffice-*.md` | **TINGGI** |
| Crew/vendor availability tracker | `cowork:create_artifact` + crew_registry + bookings data | `people/crew-registry.md` + `sources/backoffice-staff.md` | **TINGGI** |
| Monday brief (cash, sales, pipeline, week ahead) | `small-business:monday-brief` + scheduled-task | `internal-ops/*` (new) | **TINGGI** |
| Friday brief (revenue vs prior week) | `small-business:friday-brief` + scheduled-task | `internal-ops/*` (new) | **TINGGI** |
| Business pulse (one-page snapshot) | `small-business:business-pulse` | `internal-ops/*` (new) | **TINGGI** |
| Quarterly review narrative | `small-business:quarterly-review` | `internal-ops/*` (new) | **SEDANG** |
| Vendor review (hotel rates per phase) | `operations:vendor-review` + Hotel Search MCP | `website/hotels.md` + `sources/backoffice-vendors.md` | **TINGGI** |

### 4.6 Trail/Destination Enrichment

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Validate JVTO GPX tracks vs AllTrails public data | AllTrails MCP: `search_trails_by_name` + `get_trail_details` per destinasi | `destinations/*` + 5 GPX files | **TINGGI** |
| Weather overview per destinasi (sebelum batch booking) | AllTrails `get_trail_weather_overview` + scheduled-tasks (daily) | `website/operational-facts.md` | **SEDANG-TINGGI** |
| Madakaripura "tallest in Java" reconciliation (DQ-002) | Wolfram Alpha (height verification) + AllTrails details | `destinations/madakaripura.md` | **TINGGI** |
| Hotel competitive benchmark | Hotel Search `compare_hotels` di Bondowoso/Probolinggo/Banyuwangi | `website/hotels.md` | **TINGGI** |
| Sunrise/sunset time per destinasi per tanggal | Wolfram Alpha | content `travel-guide/*` | **TINGGI** |
| Elevation profile per tour route (untuk AEO snippet) | Wolfram + GPX data | `output/website/pages/destinations/*` | **TINGGI** |

### 4.7 jvto-web Development

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Deploy preview lalu production | Vercel MCP: `deploy_to_vercel`, `get_deployment_build_logs` | `seo/why-jvto-architecture.md` | **TINGGI** |
| Custom domain check / SSL audit | Vercel `check_domain_availability_and_price` + browser tools | — | **SEDANG** |
| Page text scrape + verify live vs SSOT | Chrome MCP `navigate` + `get_page_text` | wiki SSOT comparison | **TINGGI** |
| robots.txt Cloudflare conflict debug | Chrome + Vercel build logs + `engineering:debug` | open sprint issue | **TINGGI** |
| Frontend redesign mockup | `anthropic-skills:frontend-design` + `design:design-handoff` + Higgsfield | `sources/digital-trust-fortress-blueprint.md` | **TINGGI** |
| 301 redirect map deploy | Vercel + `seo/redirect-map.md` | `seo/redirect-map.md` | **TINGGI** |
| Schema dedup (TouristTrip) | Desktop Commander + `engineering:debug` | `output/website/schema/*` | **TINGGI** |

### 4.8 Marketing Campaign (multi-channel)

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Run end-to-end campaign | `small-business:run-campaign` (sales analysis → brief → Canva → posts) | `output/marketing/*` | **TINGGI** |
| Email newsletter (existing customers) | `marketing:email-sequence` + Klaviyo (perlu auth) | `output/marketing/*` | **SEDANG** |
| Content calendar 30 hari | `marketing:campaign-plan` + `small-business:content-strategy` | `output/marketing/*` | **TINGGI** |
| Geographic landing pages (Singapore/Malaysia) | `marketing:content-creation` + Ahrefs keyword-explorer per country | open sprint item | **TINGGI** |
| Brand review draft sebelum publish | `marketing:brand-review` or `brand-voice:enforce-voice` | `website/brand-voice.md` | **TINGGI** |
| Performance report monthly | `marketing:performance-report` + Ahrefs web-analytics + Google Search Console (via Ahrefs `gsc-*`) | `output/marketing/*` | **TINGGI** |
| Competitor monitoring tier 1-4 | `marketing:competitive-brief` + Ahrefs `rank-tracker-competitors-*` | `seo/competitors.md` | **TINGGI** |

### 4.9 Knowledge Base Maintenance

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Workflow 1 (Ingest source baru) | `brand-voice:discover-brand` (Drive search) + wiki workflow | `wiki/sources/*` | **TINGGI** |
| Workflow 3 (Lint - contradictions, orphans) | Custom analysis pakai Grep/Glob + skills | `wiki/log.md` | **TINGGI** |
| Workflow 6 (Health check tiered) | Scheduled-task weekly/monthly + `cowork:create_artifact` health dashboard | `wiki/ops/health-checks.md` | **TINGGI** |
| Memory consolidation | `anthropic-skills:consolidate-memory` + `productivity:memory-management` | `CLAUDE.md` | **SEDANG** |
| Source discovery (web clip baru di Drive) | Gmail search (forwarded clips) + Drive search | `wiki/sources/*` | **TINGGI** |

### 4.10 Internal Comms & Ops (kalau JVTO punya tim internal)

| Use case JVTO | Tool/Skill | Wiki pages | Fit |
|---|---|---|---|
| Crew onboarding doc baru | `human-resources:onboarding` + `small-business:job-post-builder` | `people/*` | **SEDANG** |
| SOP / runbook crew | `operations:runbook` + `operations:process-doc` | `internal-ops/*` (new) | **TINGGI** |
| Vendor MOU/contract review | `small-business:contract-review` + DocuSign (perlu auth) | — | **SEDANG** |
| Calendar meetings (Gmail/Calendar already live) | Calendar MCP `suggest_time` + `create_event` | — | **TINGGI** |
| Internal newsletter / status report | `internal-comms` skill | `internal-ops/*` (new) | **SEDANG** |

---

## 5. CREATIVE SOLUTIONS (cara kombinasi tools jadi sistem)

Bagian ini berisi 12 solusi konkret. Setiap solusi: **input → flow → output → tools yang dipakai → impact**.

### Solution 1 — "Live Wiki Dashboard" (artifact persistent)

**Premis**: Owner butuh single pane untuk: hari ini pesanan baru berapa, review baru, cash position, sprint items urgent, schema health.

**Flow**:
1. `cowork:create_artifact` bikin HTML satu file.
2. Inside artifact: `window.cowork.callMcpTool('mcp__8dbe492a-cdf9-443b-a115-9a22b7ff6aab__list_recent_files')` baca recent Drive activity.
3. `callMcpTool('Ahrefs rank-tracker-overview')` ambil 15 keyword rank harian.
4. `callMcpTool('Gmail search_threads', { q: 'newer_than:1d (review OR booking)' })` count incoming.
5. Cache di artifact, refresh on demand pakai Reload button.
6. Optional: `window.cowork.runScheduledTask(taskId)` trigger Monday brief.

**Output**: Live dashboard, persist across sessions, refresh saat dibuka.

**Tools**: Cowork artifact + Drive + Gmail + Ahrefs + Scheduled-tasks.

**Impact**: Founder cek bisnis dalam 30 detik tiap pagi. **Eliminates Pain Points #5, #10.**

### Solution 2 — "Content Compilation Auto-Pipeline" (closed loop)

**Premis**: Open issue "Silo 2 depth expansion" stuck karena manual. Bikin pipeline: wiki source → AEO snippet + FAQ + landing copy + Instagram caption — semua dari satu trigger.

**Flow**:
1. Pilih destinasi (misal Madakaripura).
2. Read: `wiki/destinations/madakaripura.md` + `wiki/credentials/*` + `wiki/website/brand-voice.md` + relevant review excerpts.
3. Ahrefs `keywords-explorer-overview` untuk keyword cluster "madakaripura waterfall".
4. Ahrefs `serp-overview` untuk top 10 SERP.
5. `marketing:content-creation` generate 1,500+ words landing copy.
6. `brand-voice:enforce-voice` lint terhadap voice invariants ("tallest waterfall" — flag ke DQ-002).
7. Generate AEO Q&A block + FAQPage schema.
8. `anthropic-skills:doc-coauthoring` finalize markdown.
9. Save to `output/website/pages/destinations/madakaripura-waterfall.md` + `output/website/aeo/madakaripura.md`.
10. Higgsfield `generate_image` 3 hero variants.
11. Canva `generate-design-structured` 5 IG carousel slides.
12. Save assets to Drive folder per destinasi.

**Output**: Per destinasi: landing copy + AEO + FAQ + 3 hero images + 5 IG slides — semua on-brand, compliance voice invariants.

**Tools**: Ahrefs + marketing skill + brand-voice + docx/doc-coauthoring + Higgsfield + Canva + Drive.

**Impact**: 5 destinasi × ~2 jam → 1 sesi tools. Silo 2 unlocked. **Eliminates Pain Points #1, #6.**

### Solution 3 — "Review Alarm + Reply Composer" (scheduled task)

**Premis**: 195 reviews, manual monitoring. Mau auto-alert kalau ada ≤3★ baru atau review mention nama crew tertentu.

**Flow**:
1. `scheduled-tasks` daily 8am: scrape Google Maps (Chrome MCP + page nav) + Trustpilot + TripAdvisor.
2. Diff vs last known state (stored in Drive).
3. Kalau ada review baru ≤3★ atau mention crew: drafts reply pakai `small-business:ticket-deflector` + `brand-voice:enforce-voice`.
4. Save draft ke Gmail draft (label "JVTO/Review-Reply-Pending").
5. Notify owner.
6. Update `reviews/review-patterns.md` weekly compile.

**Output**: Owner buka Gmail draft → 1 click approve → post reply.

**Tools**: Chrome + scheduled-tasks + small-business skills + brand-voice + Gmail + Drive.

**Impact**: Response time ≤24h tanpa effort harian. **Eliminates Pain Point #3.**

### Solution 4 — "Custom Tour Quote in 60 Seconds"

**Premis**: WA inquiry custom → manual COGS + markup → kirim. Lambat dan error-prone.

**Flow**:
1. Owner forward WA inquiry ke Gmail dengan label "JVTO/Custom-Quote".
2. Scheduled-task hourly: scan label, parse inquiry (departure city, destinations, days, pax, hotel preference).
3. Load `raw/FINANCE/rate_cards/*.json` (5 rate cards).
4. Kalkulasi COGS (crew, vehicle, accommodation, activities, other).
5. Apply 25% markup default.
6. Generate quote PDF via Canva or `anthropic-skills:pdf`.
7. Upload PDF to Drive folder per customer.
8. Draft Gmail reply dengan PDF attached.
9. Owner approve & send.

**Output**: Quote ready dalam ~5 menit instead of 30 menit.

**Tools**: Gmail + Scheduled-tasks + rate cards JSON + Canva/pdf + Drive.

**Impact**: Faster funnel. **Eliminates Pain Point #8.**

### Solution 5 — "Brand Voice Enforcement Gate"

**Premis**: `wiki/website/brand-voice.md` punya voice invariants (forbidden phrases). Mau enforce di setiap output baru.

**Flow**:
1. Skill `brand-voice:generate-guidelines` once: ingest `wiki/website/brand-voice.md` + `aeo-claims.md` + `copy-bank.md` + `sources/jvto-homepage-clip.md` → produce structured guidelines JSON di `wiki/website/brand-voice-machine.md`.
2. Untuk setiap content generation, call `brand-voice:enforce-voice` sebagai final check.
3. Flag jika ada "blue fire guaranteed", "100% blue fire", "mandatory health screening" (tanpa qualifier), price format non-IDR, dll.
4. Output dengan flag = blokir publish, owner review.

**Output**: Zero brand drift, semua output via gate.

**Tools**: brand-voice ecosystem.

**Impact**: Hilangkan risiko reputational. **Eliminates Pain Point #6.**

### Solution 6 — "SEO Live Cockpit" (Ahrefs powered)

**Premis**: 15 keyword targets, 4 tier competitors, tapi blind tanpa Ahrefs.

**Flow**:
1. `cowork:create_artifact` bikin SEO cockpit HTML.
2. Inside: panggil Ahrefs `rank-tracker-overview`, `gsc-keywords`, `keywords-explorer-overview` (untuk 15 keywords), `site-explorer-organic-competitors`, `brand-radar-mentions-overview` (AI mention share).
3. Chart per keyword: ranking trend 30 days.
4. Tabel competitor delta: tier 1-4 movement.
5. AI mention share JVTO vs competitors (brand radar).
6. Site audit issues count.
7. Refresh button: re-pull semua data.

**Output**: One page, all SEO data, refresh on click.

**Tools**: Ahrefs MCP + Cowork artifact.

**Impact**: Strategy SEO data-driven, bukan estimasi. **Eliminates Pain Point #2.**

### Solution 7 — "WA Runtime Bridge" (semi-otomatis)

**Premis**: WA playbook + rules-engine + canned-responses sudah lengkap, tapi belum jalan. Tanpa coding penuh, bisa bikin semi-otomatis dulu.

**Flow**:
1. WA Pro CRM webhook → forward ke Gmail (existing setup).
2. Scheduled-task setiap 15 menit: scan Gmail label "JVTO/WA-Inbound".
3. Per message: classify intent (Triage/Discovery/Proposal/Closing/Post-booking) pakai `customer-support:ticket-triage`.
4. Match canned response dari `wiki/whatsapp/canned-responses.md`.
5. Draft reply (bilingual ID/EN sesuai sender).
6. Run brand-voice gate.
7. Save draft ke Gmail draft + WA Pro CRM (manual paste atau API kalau ada send).
8. Owner approve.

**Output**: Klasifikasi otomatis + draft ready, owner approve.

**Tools**: Gmail + scheduled-tasks + customer-support skills + brand-voice + WA Pro CRM API.

**Impact**: Tiered automation tanpa rewrite WA stack. **Eliminates Pain Point #4 partial.**

### Solution 8 — "Destination Enrichment via AllTrails + Wolfram"

**Premis**: 5 destinasi punya GPX, tapi belum di-enrich dengan public trail data + sunrise/sunset/weather.

**Flow**:
1. Per destinasi: AllTrails `search_trails_by_name` ("Kawah Ijen", dll).
2. `get_trail_details` ambil distance, elevation gain, difficulty rating, photos.
3. `get_trail_weather_overview` 7-day forecast.
4. Wolfram: compute sunrise/sunset per destinasi per tanggal-tanggal kunci (musim peak).
5. Wolfram: elevation profile dari GPX.
6. Compile ke `wiki/destinations/*.md` + `output/website/pages/destinations/*.md`.
7. Madakaripura "tallest in Java" — Wolfram check terhadap data publik, resolve DQ-002.

**Output**: Tiap destinasi: enriched landing copy + verified facts + weather widget data.

**Tools**: AllTrails + Wolfram + wiki workflow.

**Impact**: Konten lebih kaya, resolve open data quality items. **Addresses Pain Points #1, sprint items.**

### Solution 9 — "Vercel Deploy Loop"

**Premis**: Output di-generate di wiki, tapi deploy ke jvto-web manual + ada bug schema dedup + robots conflict.

**Flow**:
1. Generate output di `output/website/*`.
2. Desktop Commander: sync ke jvto-web codebase (Next.js content folder).
3. Vercel MCP: `deploy_to_vercel` preview.
4. Chrome MCP: navigate preview URL, `get_page_text`, verify SSOT match.
5. If errors: Vercel `get_deployment_build_logs` + `engineering:debug`.
6. Approve preview → promote ke production.
7. Post-deploy: schema validator via Chrome (paste URL ke Google Rich Results Test).

**Output**: Deploy 1-click dari wiki → live.

**Tools**: Desktop Commander + Vercel + Chrome + engineering skills.

**Impact**: SSOT-to-live latency dari hari → menit. **Eliminates Pain Point #7.**

### Solution 10 — "Crew & Vendor Availability Pane"

**Premis**: 14 crew + 23 hotels tersebar di registry markdown + backoffice DB.

**Flow**:
1. `cowork:create_artifact` bikin availability dashboard.
2. Query backoffice DB (via Desktop Commander running MySQL client atau export refresh) untuk bookings 14 hari ke depan.
3. Cross-ref dengan `people/crew-registry.md` + `website/hotels.md`.
4. Tampilkan grid: hari × crew → engaged/available.
5. Tampilkan hotel allocation per phase.
6. Alert kalau ada double-book.

**Output**: Owner buka pane sebelum confirm new booking.

**Tools**: Cowork artifact + Desktop Commander + backoffice DB + wiki.

**Impact**: Scheduling conflict tertangkap di muka. **Eliminates Pain Point #9.**

### Solution 11 — "Higgsfield-Powered Marketing Studio" (untuk JVTO)

**Premis**: JVTO punya 54 live images di SSOT, tapi sosial media content tidak konsisten + butuh video.

**Flow**:
1. Tiap minggu: `small-business:content-strategy` → brief 3-5 post.
2. Per post: Higgsfield `generate_image` style "guardian/forensic/police-led" sesuai brand.
3. Higgsfield `generate_video` 15-detik clip (Bromo sunrise / Ijen blue fire / waterfall / crew action).
4. Higgsfield `virality_predictor` score sebelum publish.
5. `small-business:canva-creator` finalize template + caption + schedule via HubSpot (kalau ada) atau drafts ke Drive.
6. Save asset map update ke `sources/ssot-image-asset-map.md`.

**Output**: Weekly content batch, on-brand, with virality score.

**Tools**: Higgsfield + Canva + small-business + content-strategy + Drive.

**Impact**: Marketing output 3-5x. **Addresses Pain Points #1, #6.**

### Solution 12 — "Founder Time Recoup System"

**Premis**: Mr. Sam bottleneck. Mau kurangi load 20-30%.

**Flow**:
1. Scheduled tasks: Monday brief 7am (`small-business:monday-brief`), Friday brief 5pm (`small-business:friday-brief`), Month heads-up tanggal 25 (`small-business:month-heads-up`).
2. Calendar integration: setiap meeting baru di Calendar → auto-prep brief pakai `sales:call-prep` + Drive search account history.
3. Inbox triage: scheduled-task 3x sehari scan Gmail, classify urgent vs routine, batch routine ke "Later" label.
4. Custom tour quote auto-draft (Solution 4).
5. Review reply auto-draft (Solution 3).
6. Weekly sprint review: `productivity:update` + `productivity:task-management` tarik dari `wiki/log.md` + open items dari CLAUDE.md.
7. Approval queue dashboard: artifact yang list semua yang nunggu Sam (draft email, quote pending, content publish, vendor MOU).

**Output**: Sam buka 1 artifact pagi hari → lihat semua queue → batch-approve.

**Tools**: Scheduled-tasks + Gmail + Calendar + Drive + small-business skills + productivity skills + cowork artifact.

**Impact**: Decision throughput naik tanpa burnout. **Eliminates Pain Point #10.**

---

## 6. IMPLEMENTATION PRIORITIES (urutan eksekusi, by effort × impact)

Saya susun dalam **3 wave**. Setiap wave: tujuan, deliverables, tools dipakai, dependency, estimasi waktu, risiko.

### WAVE 1 — Quick Wins (0–7 hari, no auth needed)

Semua pakai tool yang sudah LIVE. Output langsung dipakai untuk close current sprint items.

| # | Action | Tools | Wiki impact | Sprint item closed | Estimasi | Impact |
|---|---|---|---|---|---|---|
| 1.1 | Fix homepage stale review count (92→123) | Manual + Chrome verify | `wiki/index.md`, `reviews/google-tripadvisor-2026.md` | YES (urgent) | 30 min | HIGH |
| 1.2 | Build "Live Wiki Dashboard" artifact (Solution 1, lite version) | Cowork artifact + Drive + Gmail | new `internal-ops/*` | — | 2 jam | HIGH |
| 1.3 | Build "SEO Live Cockpit" artifact (Solution 6) | Cowork artifact + Ahrefs | `seo/seo-strategy.md` enrichment | YES (SEO blindness) | 3 jam | HIGH |
| 1.4 | Resolve DQ-002 (Madakaripura "tallest") via Wolfram | Wolfram + wiki update | `destinations/madakaripura.md` | YES (DQ-002) | 30 min | MED |
| 1.5 | Generate machine-readable brand voice guidelines | `brand-voice:generate-guidelines` | `wiki/website/brand-voice-machine.md` (new) | — | 1 jam | HIGH (prereq others) |
| 1.6 | Schema dedup TouristTrip + verify live | Desktop Commander + Vercel + Chrome | `output/website/schema/*` | YES (dedup) | 2 jam | HIGH |
| 1.7 | Run `discover-brand` skill across Drive | brand-voice + Drive | `wiki/sources/*` updates | — | 1 jam | MED |
| 1.8 | Daily review alarm scheduled task (Solution 3, draft mode) | Scheduled-tasks + Chrome + Gmail | `reviews/review-patterns.md` | — | 2 jam | HIGH |

**Total Wave 1**: ~12 jam kerja terdistribusi 1 minggu. **Output**: 4 closed sprint items + 2 dashboard live + voice gate ready.

### WAVE 2 — System Building (1–4 minggu, sebagian perlu auth)

Bangun pipeline yang nge-loop. Beberapa butuh OAuth (PayPal/QuickBooks/Notion/Slack — owner pasang 5 menit per pcs).

| # | Action | Tools | Wiki impact | Dependency | Estimasi | Impact |
|---|---|---|---|---|---|---|
| 2.1 | Auth PayPal + QuickBooks + (optional) Klaviyo | small-business connectors | new `finance/cash-flow-live.md` | owner action | 15 min auth | HIGH |
| 2.2 | Cash flow + invoice chase setup (Solution 4 prep) | small-business skills + connectors | `finance/*` | 2.1 | 3 jam | HIGH |
| 2.3 | Content compilation pipeline (Solution 2) — Madakaripura first | Ahrefs + marketing skills + brand-voice + Canva + Higgsfield | `destinations/*` + `output/website/*` | 1.5 | 4 jam pilot | HIGH |
| 2.4 | Apply Solution 2 ke Tumpak Sewu + Papuma | same as 2.3 | — | 2.3 | 6 jam (2 destinasi) | HIGH |
| 2.5 | AllTrails + Wolfram destination enrichment (Solution 8) | AllTrails + Wolfram + wiki | `destinations/*` | — | 3 jam | MED-HIGH |
| 2.6 | Vercel deploy loop (Solution 9) | Vercel + Desktop Commander + Chrome | `output/website/*` → jvto-web | — | 4 jam | HIGH |
| 2.7 | Custom tour quote pipeline pilot (Solution 4) | Gmail + scheduled-tasks + rate cards + pdf | `finance/custom-tour-builder.md` runtime | — | 4 jam | HIGH |
| 2.8 | Weekly Monday + Friday briefs scheduled | scheduled-tasks + small-business skills | `internal-ops/*` | 2.1 | 1 jam setup | HIGH |
| 2.9 | Brand voice enforcement gate integrated in all content pipelines | brand-voice | wiki/website governance | 1.5 | 2 jam | HIGH |
| 2.10 | Geographic landing pages (Singapore/Malaysia) | marketing + Ahrefs per-country | `output/website/pages/markets/*` | 2.3 pipeline | 6 jam | MED-HIGH |

**Total Wave 2**: ~33 jam kerja distribusi 4 minggu. **Output**: 3 destinasi published depth content, deploy loop, finance live, founder briefs running.

### WAVE 3 — Scale & Polish (1–3 bulan, optional auth)

Bangun yang nice-to-have, automasi tingkat lanjut, formalisasi internal ops.

| # | Action | Tools | Wiki impact | Estimasi | Impact |
|---|---|---|---|---|---|
| 3.1 | WA runtime bridge semi-otomatis (Solution 7) | Gmail + scheduled + WA API + skills | `whatsapp/*` runtime | 1 minggu | HIGH |
| 3.2 | Crew & vendor availability dashboard (Solution 10) | artifact + Desktop Commander + DB | `people/*` + `website/hotels.md` | 1 minggu | MED |
| 3.3 | Higgsfield Marketing Studio weekly (Solution 11) | Higgsfield + Canva + content-strategy + scheduled | `output/social/*` + image asset map | ongoing | HIGH |
| 3.4 | Founder Time Recoup System (Solution 12) | scheduled + Gmail/Cal + skills + artifact | `CLAUDE.md` + `TASKS.md` | 2 minggu | HIGH |
| 3.5 | Notion mirror (mobile access ke wiki) | Notion auth + sync script | wiki cross-mirror | 3 hari | MED |
| 3.6 | Fireflies integration untuk founder strategy calls | Fireflies auth + Drive | `wiki/sources/*` | 1 minggu | MED |
| 3.7 | Klaviyo email sequence: onboarding + post-tour + win-back | Klaviyo auth + marketing skills | new `marketing/*` | 2 minggu | MED-HIGH |
| 3.8 | Apollo + sales-skills untuk B2B travel agent outreach | Apollo auth + sales skills | new `marketing/b2b/*` | 2 minggu | MED |
| 3.9 | DocuSign untuk vendor MOU + crew contracts | DocuSign auth + contract-review skill | new `internal-ops/contracts/*` | 1 minggu | MED |
| 3.10 | Quarterly review automation | small-business + scheduled + artifact | `internal-ops/qbr-*` | 3 hari | MED |
| 3.11 | Tax prep packet (estimated quarterly + 1099 prep) | small-business:tax-prep + QB + PayPal | new `finance/tax-*` | 1 minggu | MED |
| 3.12 | Bromo-Ijen status today page (Silo 3 SEO) | needs PVMBG live source → Chrome scrape + scheduled | open sprint item | 2 minggu | MED-HIGH |

**Total Wave 3**: 2-3 bulan distribusi. Optional, ditarik sesuai mau prioritas mana yang dijalankan.

---

## 7. PROJECTED OUTCOMES (kalau Wave 1+2 dieksekusi penuh)

| Metric | Sekarang | Target Q3 2026 (post Wave 2) |
|---|---|---|
| Tour pages with 1,500+ words depth | 2 (Ijen, Bromo) | 5 (semua destinasi) |
| Open sprint items | 7 | 1-2 (sisanya yang butuh external data) |
| Time from review → reply | ad-hoc, mungkin hari/minggu | ≤24 jam (alarm + draft) |
| Time from WA inquiry → custom quote | ~30 min | ~5 min |
| SEO data visibility | estimasi manual | real-time Ahrefs cockpit |
| Founder time on routine ops | high | -20-30% (briefs + dashboards) |
| Brand drift risk pada output baru | medium-high | low (gate enforce) |
| Schema/structured data health | issues open | clean, validated |
| Content production cadence (post/asset) | irregular | weekly batch |

---

## 8. RISK & DEPENDENCIES (apa yang bisa rusak)

| Risiko | Likelihood | Dampak | Mitigasi |
|---|---|---|---|
| Ahrefs subscription kena rate limit | RENDAH | SEDANG | check `subscription-info-limits-and-usage` early, batch calls |
| OAuth ke PayPal/QB gagal (compliance) | RENDAH | TINGGI | fallback ke CSV upload (skills support) |
| Higgsfield credit habis | SEDANG | SEDANG | check `balance` tool periodically, fallback ke Canva-only |
| Canva brand kit belum di-setup | SEDANG | SEDANG | run `list-brand-kits` early, setup di Wave 1 step 1.7 |
| Backoffice DB connection lost | RENDAH | TINGGI | refresh export periodically per `internal-ops/backoffice-extraction.md` |
| Schema generation rusak SEO live | RENDAH | TINGGI | preview deploy via Vercel + Chrome verify sebelum production |
| Voice gate false positive blokir publish | SEDANG | RENDAH | manual override path + log flag history |
| WA Pro CRM API breaking change | RENDAH | SEDANG | playbook doc keep current, version pin |
| Higgsfield image style off-brand | SEDANG | SEDANG | tight prompt library + virality_predictor pre-check |
| Vercel deploy gagal di production | RENDAH | TINGGI | preview wajib + rollback procedure |

---

## 9. WHAT NOT TO DO (anti-pattern bagi JVTO)

Berdasarkan profile bisnis JVTO (B2C tour ops, founder-led, lean team, Bondowoso based, no in-house dev):

1. **Jangan pakai full SaaS sales stack** (Outreach + Close + Apollo + Salesforce). JVTO inbound-driven, demand-pull. Apollo cukup kalau mau B2B partner outreach saja.
2. **Jangan pakai product analytics tier** (Amplitude/Pendo/Hex). Static site dengan ~tens of thousands traffic doesn't warrant ini. GSC + Ahrefs cukup.
3. **Jangan pakai support stack** (Intercom/Guru). WA = channel utama. Build WA runtime saja.
4. **Jangan migrasi wiki ke Notion full** — wiki sebagai filesystem + git lebih portable + reversible. Notion mirror OK untuk mobile access tapi jangan jadi source of truth.
5. **Jangan auto-publish konten tanpa brand voice gate**. Wiki voice invariants tegas; satu post yang lolos "blue fire guaranteed" bisa merusak C4 (medical screening) credibility.
6. **Jangan generate AI image yang ngaku photo** — JVTO punya 54 real images. Higgsfield untuk style illustration / banner only, bukan untuk "foto" crew atau "foto" destinasi yang akan dianggap real. Trust architecture rusak.
7. **Jangan deploy schema baru tanpa Rich Results Test pass**. Open sprint item TouristTrip dedup bukti penting.
8. **Jangan over-engineer scheduling**. Cron-style cukup; jangan pasang ClickUp/Linear kalau task system markdown wiki (`TASKS.md` per CLAUDE.md productivity skill) sudah cukup.
9. **Jangan ekspos PII WhatsApp 5,547 conversations**. Existing wiki sudah anonymize; pertahankan.
10. **Jangan rebuild wiki di skill ecosystem**. Wiki sudah punya struktur kuat. Skills sebagai accelerator workflow, bukan sebagai replacement.

---

## 10. SINGKAT — REKOMENDASI 1 PARAGRAF

**Wave 1 minggu ini** (12 jam): Fix homepage stale + dashboard live + SEO cockpit + brand voice gate + schema dedup. **Wave 2 4 minggu** (33 jam): Auth PayPal+QB, content pipeline Madakaripura/Tumpak Sewu/Papuma full depth, Vercel deploy loop, custom tour quote runtime, Monday/Friday briefs auto. **Hindari**: full sales/support/product-analytics stacks. Wave 3 ditarik sesuai bandwidth — yang highest impact di sana adalah WA runtime bridge (Solution 7) dan Founder Time Recoup (Solution 12).

---

## Appendix A — File Index (semua tool/skill mention dalam dokumen ini)

**MCP servers cited**: Gmail, Calendar, Drive, Ahrefs, AllTrails, Hotel Search, Canva, Higgsfield, Vercel, Wolfram, Chrome, Desktop Commander, Windows-MCP, PDF Viewer, MCP Registry, Plugins, Skills, Cowork, Scheduled-tasks, Workspace bash/web_fetch, Session Info, PayPal (auth), QuickBooks (auth), Stripe (auth), Klaviyo (auth), Apollo (auth), Slack (auth), Notion (auth), Fireflies (auth), DocuSign (auth), Figma (auth), ClickUp (auth), Linear (auth), Prisma.

**Skills cited**: `small-business:*` (35), `marketing:content-creation/draft-content/brand-review/email-sequence/campaign-plan/performance-report/competitive-brief/seo-audit`, `brand-voice:discover-brand/enforce-voice/generate-guidelines`, `sales:account-research/call-prep/competitive-intelligence`, `product-management:brainstorm/competitive-brief/metrics-review/write-spec/synthesize-research/stakeholder-update/sprint-planning`, `ops:vendor-review/runbook/process-doc/risk-assessment`, `human-resources:onboarding`, `customer-support:ticket-triage/kb-article/customer-research`, `engineering:debug`, `design:design-handoff`, `productivity:memory-management/task-management/update`, `anthropic-skills:docx/pptx/xlsx/pdf/doc-coauthoring/frontend-design/canvas-design/brand-guidelines/seo-audit/consolidate-memory`.

**Wiki pages cited**: index, overview, log, ops/*, sources/*, destinations/*, products/*, people/*, credentials/*, reviews/*, website/*, seo/*, whatsapp/*, finance/*, internal-ops/*.

---

*Document end. Status: draft for owner review. Next action: pilih Wave 1 items yang mau dieksekusi hari ini.*
