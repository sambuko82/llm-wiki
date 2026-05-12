# JVTO Website Copy — All Sitemap Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate `output/copy-2026-05-12-[page].md` website copy files for all 53 URLs in `raw/sitemap.xml` using the website-copy compilation profile and verified JVTO wiki content only.

**Architecture:** Each task reads the relevant wiki source pages, generates website copy in Style B voice (Style A for policy/verify pages), writes to the standardized output filename, verifies no voice invariants are violated, and commits. No code — pure content generation. Three files already exist (homepage, surabaya-landing, bali-landing); 50 new files are created across 12 tasks.

**Tech Stack:** JVTO Wiki (wiki/) · website-copy compilation profile (wiki/ops/compilation-profiles.md) · Markdown output (output/) · git

---

## Already Complete — Skip

| URL | Output file |
|---|---|
| `/` | `output/copy-2026-05-12-homepage.md` ✓ |
| `/tours/from-surabaya` | `output/copy-2026-05-12-surabaya-landing.md` ✓ |
| `/tours/from-bali` | `output/copy-2026-05-12-bali-landing.md` ✓ |

Reference files (non-standard names, kept for reference):
- `output/kawah-ijen-page-copy.md` → superseded by Task 6
- `output/mount-bromo-page-copy.md` → superseded by Task 6

---

## Voice Invariants (apply to EVERY task)

**Forbidden phrases** — grep for these after every task; 0 hits required:
- `Blue Fire guaranteed`
- `100% Blue Fire`
- `mandatory health screening` (without BBKSDA qualifier)
- `JVTO provides police escort` (without conditional context)

**Required conditional language for Ijen pages:**
- ✅ "Blue Fire is a natural phenomenon subject to weather and gas activity."
- ✅ "Ijen access rules can require a recent local health certificate."
- ✅ "JVTO coordinates clinic workflow when access rules require it."

---

## File Map — 50 New Output Files

### Task 1 — Misc (3 files)
- `output/copy-2026-05-12-contact.md`
- `output/copy-2026-05-12-blog.md`
- `output/copy-2026-05-12-isic-student-package.md`

### Task 2 — Why JVTO section (6 files)
- `output/copy-2026-05-12-why-jvto.md`
- `output/copy-2026-05-12-why-jvto-the-jvto-difference.md`
- `output/copy-2026-05-12-why-jvto-reviews.md`
- `output/copy-2026-05-12-why-jvto-our-story.md`
- `output/copy-2026-05-12-why-jvto-our-team.md`
- `output/copy-2026-05-12-why-jvto-community-standards.md`

### Task 3 — Verify JVTO section (5 files)
- `output/copy-2026-05-12-verify-jvto.md`
- `output/copy-2026-05-12-verify-jvto-legal.md`
- `output/copy-2026-05-12-verify-jvto-press-recognition.md`
- `output/copy-2026-05-12-verify-jvto-history-artifacts.md`
- `output/copy-2026-05-12-verify-jvto-police-safety.md`

### Task 4 — Travel Guide section (9 files)
- `output/copy-2026-05-12-travel-guide.md`
- `output/copy-2026-05-12-travel-guide-faq.md`
- `output/copy-2026-05-12-travel-guide-safety-on-tours.md`
- `output/copy-2026-05-12-travel-guide-weather-and-closures.md`
- `output/copy-2026-05-12-travel-guide-packing-and-fitness.md`
- `output/copy-2026-05-12-travel-guide-booking-information.md`
- `output/copy-2026-05-12-travel-guide-best-time-to-visit.md`
- `output/copy-2026-05-12-travel-guide-police-escort-for-groups.md`
- `output/copy-2026-05-12-travel-guide-ijen-health-screening.md`

### Task 5 — Policy section (4 files)
- `output/copy-2026-05-12-policy.md`
- `output/copy-2026-05-12-policy-booking-payment-cancellation.md`
- `output/copy-2026-05-12-policy-inclusions-exclusions.md`
- `output/copy-2026-05-12-policy-privacy.md`

### Task 6 — Destinations section (6 files)
- `output/copy-2026-05-12-destinations.md`
- `output/copy-2026-05-12-destinations-mount-bromo.md`
- `output/copy-2026-05-12-destinations-ijen-crater.md`
- `output/copy-2026-05-12-destinations-madakaripura-waterfall.md`
- `output/copy-2026-05-12-destinations-tumpak-sewu-waterfall.md`
- `output/copy-2026-05-12-destinations-papuma-beach.md`

### Task 7 — Tours hub (1 file)
- `output/copy-2026-05-12-tours.md`

### Task 8 — Surabaya short tours (3 files)
- `output/copy-2026-05-12-tour-bromo-1d1n-surabaya.md`
- `output/copy-2026-05-12-tour-bromo-2d1n-surabaya.md`
- `output/copy-2026-05-12-tour-ijen-2d1n-surabaya.md`

### Task 9 — Surabaya 3D2N tours (3 files)
- `output/copy-2026-05-12-tour-bromo-madakaripura-ijen-3d2n-surabaya.md`
- `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-3d2n-surabaya.md`
- `output/copy-2026-05-12-tour-taman-safari-prigen-bromo-madakaripura-3d2n-surabaya.md`

### Task 10 — Surabaya 4D3N tours (3 files)
- `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-4d3n-surabaya.md`
- `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-4d3n-surabaya.md`
- `output/copy-2026-05-12-tour-tumpak-sewu-bromo-ijen-4d3n-surabaya.md`

### Task 11 — Surabaya 5D4N+ tours (3 files)
- `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-malang-5d4n-surabaya.md`
- `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-5d4n-surabaya.md`
- `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-malang-6d5n-surabaya.md`

### Task 12 — Bali tours (4 files)
- `output/copy-2026-05-12-tour-bromo-ijen-3d2n-bali.md`
- `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-3d2n-bali.md`
- `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-4d3n-bali.md`
- `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-5d4n-bali.md`

---

## Standard Frontmatter Template

Every output file starts with:

```markdown
---
profile: website-copy
page: /[url-path]
output_date: 2026-05-12
sources: [list of wiki pages read]
voice: Style B  (or: Style A for policy/verify pages)
---
```

---

## Standard Tour Page Template

All 16 individual tour pages follow this structure:

```
# [Tour Name]
## Hero (1 punchy sentence + 1 credibility sentence)
## At a Glance (table: origin, duration, destinations, group type, health screening)
## Day-by-Day Itinerary (sourced from wiki/products/packages-itineraries)
## What's Included / Excluded (sourced from wiki/sources/jvto-policy-pack-v6 §inclusions)
## Pricing (per-person IDR table from wiki/products/packages-full-pricing)
## Health Screening Note (Ijen packages only — use conditional language)
## CTAs (Book + Verify JVTO)
```

---

## Task 1: Misc Pages — Contact, Blog, ISIC

**Wiki sources to read:**
- `wiki/overview.md` (contact info: Jl. Khairil Anwar No.102A, Bondowoso, +62 822 4478 8833)
- `wiki/credentials/legal-licenses.md` (ISIC Provider 259268)
- `wiki/products/packages-full-pricing.md` (student package pricing)
- `wiki/content/brand-voice.md` (voice)

- [ ] **Step 1: Read sources**

Read: `wiki/overview.md`, `wiki/credentials/legal-licenses.md`, `wiki/products/packages-full-pricing.md`

- [ ] **Step 2: Write `output/copy-2026-05-12-contact.md`**

Sections:
- Hero: direct statement of how to reach JVTO (WhatsApp primary CTA)
- Contact methods: WhatsApp (+62 822 4478 8833), Email (hello@javavolcano-touroperator.com)
- Office: Jl. Khairil Anwar No.102A, Bondowoso, East Java 68214
- Hours: per `wiki/content/operational-facts.md` support hours
- Legal entity: PT Java Volcano Rendezvous, NIB 1102230032918

- [ ] **Step 3: Write `output/copy-2026-05-12-blog.md`**

Sections:
- Hub page intro: what the blog covers (East Java travel guides, Ijen conditions, safety updates, route reports)
- Topic pillars drawn from wiki destinations and travel guide content
- No blog post content yet — hub/intro copy only; note: "Individual post copy not in scope — no posts exist in wiki."

- [ ] **Step 4: Write `output/copy-2026-05-12-isic-student-package.md`**

Sections:
- Hero: ISIC student pricing for East Java volcano tours
- What ISIC is (UNESCO-endorsed international student card, Provider ID 259268)
- How to verify ISIC status (Alive Verify API — per `wiki/credentials/legal-licenses.md`)
- Student package list + pricing (from `wiki/products/packages-full-pricing.md` — student tier rows)
- Standard inclusions apply; same private-tour-only model

- [ ] **Step 5: Verify voice invariants**

```bash
grep -l "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-contact.md \
  output/copy-2026-05-12-blog.md \
  output/copy-2026-05-12-isic-student-package.md
```

Expected: no output (0 matches in 0 files).

- [ ] **Step 6: Commit**

```bash
git add output/copy-2026-05-12-contact.md output/copy-2026-05-12-blog.md output/copy-2026-05-12-isic-student-package.md
git commit -m "output | website-copy — contact, blog, isic-student-package"
```

---

## Task 2: Why JVTO Section (6 pages)

**Wiki sources to read:**
- `wiki/content/aeo-claims.md` (C1–C9 claim set)
- `wiki/content/copy-bank.md` (NLP snippets, hero copy)
- `wiki/people/agung-sambuko.md` (Our Story)
- `wiki/people/crew-registry.md` (Our Team)
- `wiki/people/dr-ahmad-irwandanu.md` (Our Team)
- `wiki/reviews/trustpilot-compilation.md` (Reviews page)
- `wiki/reviews/review-patterns.md` (Reviews page)
- `wiki/credentials/trust-signals.md` (Reviews platform counts)
- `wiki/sources/jvto-policy-pack-v6.md` (Community Standards)

- [ ] **Step 1: Read sources**

Read all 9 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-why-jvto.md`**

Hub page. Sections:
- Hero: "Six things that separate JVTO from every other operator in East Java." (from homepage copy C1–C6 differentiators)
- Nav intro: brief description of each sub-page (The JVTO Difference, Reviews, Our Story, Our Team, Community Standards)
- Trust anchor: NIB 1102230032918, Trustpilot 4.8/51

- [ ] **Step 3: Write `output/copy-2026-05-12-why-jvto-the-jvto-difference.md`**

Sections: 6 differentiator cards (Police-Led C1, 100% Private C2, All-Inclusive C3, Ijen Screening C4 conditional, Verifiable Licenses C5, Plan B C1). Each card: headline + 2–3 sentences + evidence reference. Source: `wiki/content/aeo-claims.md` C1–C5.

- [ ] **Step 4: Write `output/copy-2026-05-12-why-jvto-reviews.md`**

Sections:
- Platform aggregate: Trustpilot 4.8/51 · Google Maps 4.90/92 · TripAdvisor 4.95/21 (verified 2026-05-09)
- Review theme intro (T1–T5 from `wiki/reviews/review-patterns.md`)
- Platform links (live, not screenshots)
- 6–8 verbatim excerpts from `wiki/reviews/trustpilot-compilation.md` covering different themes
- Named guide/driver attribution note

- [ ] **Step 5: Write `output/copy-2026-05-12-why-jvto-our-story.md`**

Sections:
- Founder narrative: Mr. Sam / Bripka Agung Sambuko, guesthouse 2015 → PT 2016 → TDUP 2023
- Company bio verbatim block (from `wiki/content/copy-bank.md` §company-bio)
- Why private-only model: safety gaps observed first-hand
- Evidence chain: Booking.com 2015 (9.4/10), Stefan Loose 2016 p.287
Source: `wiki/people/agung-sambuko.md`

- [ ] **Step 6: Write `output/copy-2026-05-12-why-jvto-our-team.md`**

Sections:
- Team registry intro: 11 members (7 guides + 4 drivers), KTA-credentialed 2024, HPWKI training
- Mr. Sam (founder / Tourist Police officer)
- Dr. Ahmad Irwandanu (medical officer, SIP verifiable)
- Guide profiles (from `wiki/people/crew-registry.md`): Anjas, Taufik, Rendi, Gufron, Kiki — name, languages, routes, review mention count
- Driver profiles
Source: `wiki/people/crew-registry.md`, `wiki/people/agung-sambuko.md`, `wiki/people/dr-ahmad-irwandanu.md`

- [ ] **Step 7: Write `output/copy-2026-05-12-why-jvto-community-standards.md`**

Sections:
- What community standards means for JVTO: written rules before booking
- "Read the Rulebook Before You Book" — links to policy section
- Sulfur miner etiquette (from `wiki/destinations/kawah-ijen.md` §sulfur-mining)
- Local Boys policy (INDECON membership from `wiki/credentials/trust-signals.md`)
- No-tipping policy if documented, no invented content if not
Source: `wiki/sources/jvto-policy-pack-v6.md`, `wiki/credentials/trust-signals.md`

- [ ] **Step 8: Verify voice invariants**

```bash
grep -l "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-why-jvto*.md
```

Expected: no output.

- [ ] **Step 9: Commit**

```bash
git add output/copy-2026-05-12-why-jvto*.md
git commit -m "output | website-copy — why-jvto section (6 pages)"
```

---

## Task 3: Verify JVTO Section (5 pages)

**Voice:** Style A (dossier — these are credential/proof pages).

**Wiki sources to read:**
- `wiki/credentials/legal-licenses.md` (all license details + SHA-256 anchors)
- `wiki/credentials/trust-signals.md` (press table, historical)
- `wiki/people/agung-sambuko.md` (police-safety + history)
- `wiki/sources/detik-polpar-2021.md`
- `wiki/sources/radar-jember-polpar-geopark-2021.md`
- `wiki/sources/radar-jember-bau-menyengat-2021.md`
- `wiki/sources/bbksda-pelatihan-pemandu-2024.md`

- [ ] **Step 1: Read sources**

Read all 7 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-verify-jvto.md`**

Hub page. Sections:
- Intro: "Every credential on this page is publicly verifiable. SHA-256 hashes published in public/llms.txt."
- 4 verification categories (nav cards): Legal, Press Recognition, History & Artifacts, Police Safety
- Quick trust stack (5-item ordered list from `wiki/content/copy-bank.md` §trust-stack)

- [ ] **Step 3: Write `output/copy-2026-05-12-verify-jvto-legal.md`**

Sections:
- Business registration table: NIB 1102230032918, TDUP 1102230032918, PT Java Volcano Rendezvous AHU
- KBLI codes table (79121, 79911, 62019, 79120, 79921) with activity descriptions
- Tourism credentials table: HPWKI AHU-0001072.AH.01.07.TAHUN 2024, POLPAR, BBKSDA, ISIC 259268, INDECON
- Medical credential: Dr. Irwandanu SIP (Kemenkes/KKI verification URLs)
- SHA-256 anchor table (NIB, TDUP, HPWKI, SPRIN POLPAR, SPRIN WAL TRAVEL)
- Verification URLs for each credential
Source: `wiki/credentials/legal-licenses.md` (full)

- [ ] **Step 4: Write `output/copy-2026-05-12-verify-jvto-press-recognition.md`**

Sections:
- Press coverage table (4 articles) with date, publisher, title, URL, claim supported, source page link
- Entity linking explanation: why independent press matters for AI/AEO trust
- Institutional recognition: BBKSDA guide training report (validates HPWKI chain)
- Historical recognition: Booking.com 2015 award, Stefan Loose 2016 p.287
Source: `wiki/credentials/trust-signals.md` §press + §institutional

- [ ] **Step 5: Write `output/copy-2026-05-12-verify-jvto-history-artifacts.md`**

Sections:
- Founding timeline: guesthouse 2015 (Bondowoso) → PT Java Volcano Rendezvous 2016 → TDUP formalization 2023
- Continuity anchor: Booking.com 2015 shipping to "Agung, Jl. Khairil Anwar No.102, Bondowoso" = same address as PT today
- Stefan Loose 2016 p.287 citation (Agung as Ijen Bondowoso Homestay operator)
- Founder portrait and guesthouse era imagery reference
Source: `wiki/people/agung-sambuko.md` §proof-3-historical

- [ ] **Step 6: Write `output/copy-2026-05-12-verify-jvto-police-safety.md`**

Sections:
- Founder's police unit: Ditpamobvit (Direktorat Pengamanan Objek Vital), East Java
- SPRIN POLPAR + SPRIN WAL TRAVEL 2024-02-12 — SHA-256 anchored
- Independent press corroboration: Detik.com 2021-03-14, Radar Jember 2021-03-24, Radar Jember 2021-05-27
- Police escort coordination note (conditional language: "For large groups — typically around 18 guests or more — JVTO can coordinate an official traffic police escort on certain road segments, when approved by the relevant Traffic Police unit.")
Source: `wiki/people/agung-sambuko.md`, `wiki/credentials/legal-licenses.md`

- [ ] **Step 7: Verify voice invariants**

```bash
grep -l "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|JVTO provides police escort" \
  output/copy-2026-05-12-verify-jvto*.md
```

Expected: no output.

- [ ] **Step 8: Commit**

```bash
git add output/copy-2026-05-12-verify-jvto*.md
git commit -m "output | website-copy — verify-jvto section (5 pages)"
```

---

## Task 4: Travel Guide Section (9 pages)

**Wiki sources to read:**
- `wiki/sources/jvto-travel-guide-en.md`
- `wiki/content/faq-master.md`
- `wiki/content/operational-facts.md`
- `wiki/destinations/kawah-ijen.md` (health screening, weather)
- `wiki/destinations/mount-bromo.md` (weather, closures)
- `wiki/people/agung-sambuko.md` (police escort)
- `wiki/sources/jvto-policy-pack-v6.md` (booking information)

- [ ] **Step 1: Read sources**

Read all 7 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-travel-guide.md`**

Hub page. Sections: intro + 8 nav cards (one per sub-page) with one-line description each.

- [ ] **Step 3: Write `output/copy-2026-05-12-travel-guide-faq.md`**

Draw from `wiki/content/faq-master.md`. Sections:
- General FAQ (booking, cancellation, private tours)
- Ijen FAQ (health screening conditional, Blue Fire conditional)
- Bromo FAQ
- Madakaripura FAQ
- Packing / Fitness FAQ
Format: H3 question + 2–5 sentence answer. Note: existing faq output files (faq-2026-05-12-*.md) exist — cross-reference but use faq-master as canonical source; this page is website-copy format.

- [ ] **Step 4: Write `output/copy-2026-05-12-travel-guide-safety-on-tours.md`**

Sections: risk-aware planning (C1), emergency handling on tours, Plan B framework, safety briefings (from review patterns T4), BBKSDA guide training (SAR/PPGD from bbksda-pelatihan-pemandu-2024).

- [ ] **Step 5: Write `output/copy-2026-05-12-travel-guide-weather-and-closures.md`**

Sections:
- Bromo closure SOP (Plan B framework from `wiki/destinations/mount-bromo.md`)
- Ijen gas/weather conditions affecting Blue Fire (conditional language)
- Best and worst months per destination (from `wiki/content/operational-facts.md`)
- Kasada festival closure note for Bromo if documented

- [ ] **Step 6: Write `output/copy-2026-05-12-travel-guide-packing-and-fitness.md`**

Sections: fitness levels per destination (from `wiki/sources/jvto-travel-guide-en.md`), packing lists (layers for cold, waterproofs for Madakaripura/Tumpak Sewu), silver jewelry warning for Ijen (sulfur reacts — from travel guide source).

- [ ] **Step 7: Write `output/copy-2026-05-12-travel-guide-booking-information.md`**

Sections: payment steps, My Booking Portal, bank transfer details, FOC scheme (from `wiki/sources/jvto-policy-pack-v6.md` + `wiki/sources/jvto-travel-guide-en.md`).

- [ ] **Step 8: Write `output/copy-2026-05-12-travel-guide-best-time-to-visit.md`**

Sections: dry season (Apr–Oct) vs wet season, per-destination recommendations, month-by-month guide. Source: `wiki/content/operational-facts.md`, destination pages. Note: this page was updated 2026-05-12 on live site — treat as high-priority accuracy page.

- [ ] **Step 9: Write `output/copy-2026-05-12-travel-guide-police-escort-for-groups.md`**

Sections:
- What police escort is (Ditpamobvit Traffic Police coordination)
- Who qualifies (typically 18+ guests — conditional: "when approved by relevant Traffic Police unit")
- How it works operationally
- How to request
Source: `wiki/people/agung-sambuko.md`, `wiki/credentials/legal-licenses.md`, `wiki/content/brand-voice.md` §approved-police-escort

- [ ] **Step 10: Write `output/copy-2026-05-12-travel-guide-ijen-health-screening.md`**

Sections:
- What it is: BBKSDA SE.1658/KSA.9/2024 — when crater conditions require it
- The process: pre-hike clinic visit, Dr. Ahmad Irwandanu SIP, what's checked
- Who coordinates: JVTO coordinates clinic workflow when access rules require it
- What happens if not fit to hike: policy per `wiki/content/faq-master.md`
- Verification: Dr. Irwandanu SIP at satusehat.kemkes.go.id/sdmk
Voice: all conditional language per `wiki/content/brand-voice.md` §voice-invariants.

- [ ] **Step 11: Verify voice invariants**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|JVTO provides police escort" \
  output/copy-2026-05-12-travel-guide*.md
```

Expected: 0 matches.

- [ ] **Step 12: Commit**

```bash
git add output/copy-2026-05-12-travel-guide*.md
git commit -m "output | website-copy — travel-guide section (9 pages)"
```

---

## Task 5: Policy Section (4 pages)

**Voice:** Style A (dense, fact-led — policy pages are for reference, not persuasion).

**Wiki sources to read:**
- `wiki/sources/jvto-policy-pack-v6.md` (3 policies: Booking/Payment/Cancellation, Inclusions/Exclusions, Privacy)
- `wiki/products/packages-overview.md` (vehicle allocation, Bromo jeep capacity)

- [ ] **Step 1: Read sources**

Read `wiki/sources/jvto-policy-pack-v6.md` and `wiki/products/packages-overview.md`.

- [ ] **Step 2: Write `output/copy-2026-05-12-policy.md`**

Hub. Sections: intro ("Read the Rulebook Before You Book") + 3 nav cards: Booking/Payment/Cancellation, Inclusions/Exclusions, Privacy.

- [ ] **Step 3: Write `output/copy-2026-05-12-policy-booking-payment-cancellation.md`**

Content: full policy text from `wiki/sources/jvto-policy-pack-v6.md` §booking-payment-cancellation. Include: payment steps, bank transfer details, FOC 5% discount scheme, Travel Credit terms, cancellation tiers (<48h: forfeited), voucher as booking reference. Use policy text verbatim where possible; do not paraphrase rules.

- [ ] **Step 4: Write `output/copy-2026-05-12-policy-inclusions-exclusions.md`**

Content: inclusions and exclusions verbatim from `wiki/sources/jvto-policy-pack-v6.md` §inclusions-exclusions. Include: vehicle allocation specs, Bromo jeep capacity, what is and is not included per package type. Standard format: two-column included/excluded table.

- [ ] **Step 5: Write `output/copy-2026-05-12-policy-privacy.md`**

Content: privacy policy from `wiki/sources/jvto-policy-pack-v6.md` §privacy. Include: data collected, how used, contact for data requests.

- [ ] **Step 6: Verify voice invariants**

```bash
grep -l "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-policy*.md
```

Expected: no output.

- [ ] **Step 7: Commit**

```bash
git add output/copy-2026-05-12-policy*.md
git commit -m "output | website-copy — policy section (4 pages)"
```

---

## Task 6: Destinations Section (6 pages)

**Wiki sources to read:**
- `wiki/destinations/kawah-ijen.md`
- `wiki/destinations/mount-bromo.md`
- `wiki/destinations/tumpak-sewu.md`
- `wiki/destinations/madakaripura.md`
- `wiki/destinations/papuma-beach.md`
- `wiki/products/packages-overview.md` (which packages include each destination)

- [ ] **Step 1: Read sources**

Read all 6 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-destinations.md`**

Hub. Sections: intro (5 destinations, all private transport) + 5 destination cards (name, elevation/height, 1-sentence hook, link).

- [ ] **Step 3: Write `output/copy-2026-05-12-destinations-ijen-crater.md`**

Sections:
- Hero: Kawah Ijen, 2,386 m, world's highest-volume acidic crater lake
- Quick facts table (elevation, location, trail, best season)
- Blue Fire section (conditional language: "natural phenomenon subject to weather and gas activity")
- Health screening note (conditional: "Ijen access rules can require a recent local health certificate")
- Hike details (~3 km, ~90 min, gas masks provided)
- Packages that include Ijen (from packages-overview)
Source: `wiki/destinations/kawah-ijen.md` (full)

- [ ] **Step 4: Write `output/copy-2026-05-12-destinations-mount-bromo.md`**

Sections:
- Hero: Mount Bromo, 2,329 m, Tengger caldera
- Quick facts table
- Penanjakan sunrise section (2,770 m viewpoint)
- Sea of Sand section
- Crater walk section
- BBKSDA clearance + 4WD jeep included
- Plan B framework
- Packages that include Bromo
Source: `wiki/destinations/mount-bromo.md` (full)

- [ ] **Step 5: Write `output/copy-2026-05-12-destinations-madakaripura-waterfall.md`**

Sections:
- Hero: tallest waterfall in Java, Probolinggo Regency
- Quick facts (main curtain drop ~100 m, total height ~200 m per wiki/destinations/madakaripura.md §height-resolution)
- The approach (wading through stream, fully wet, helmet from local site management)
- Gajah Mada historical context if in wiki
- Packages that include Madakaripura
Source: `wiki/destinations/madakaripura.md`

- [ ] **Step 6: Write `output/copy-2026-05-12-destinations-tumpak-sewu-waterfall.md`**

Sections:
- Hero: curtain waterfall ~120 m, Lumajang Regency
- Two vantage points: rim (all visitors) vs canyon descent (optional)
- Safety note (helmet from local site management, wet conditions)
- Packages that include Tumpak Sewu
Source: `wiki/destinations/tumpak-sewu.md`

- [ ] **Step 7: Write `output/copy-2026-05-12-destinations-papuma-beach.md`**

Sections:
- Hero: white-sand beach + cape headland (~86 m), Jember
- What to expect (beach, headland views, coastal break in longer tours)
- Packages that include Papuma Beach
Source: `wiki/destinations/papuma-beach.md`

- [ ] **Step 8: Verify voice invariants**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-destinations*.md
```

Expected: 0 matches.

- [ ] **Step 9: Commit**

```bash
git add output/copy-2026-05-12-destinations*.md
git commit -m "output | website-copy — destinations section (6 pages)"
```

---

## Task 7: Tours Hub (1 page)

**Wiki sources to read:**
- `wiki/products/packages-overview.md`
- `wiki/content/copy-bank.md`

- [ ] **Step 1: Read sources**

Read `wiki/products/packages-overview.md` and `wiki/content/copy-bank.md`.

- [ ] **Step 2: Write `output/copy-2026-05-12-tours.md`**

Sections:
- Hero: "16 private tours. From Surabaya or Bali. 1 to 6 days."
- What all tours share: 100% private, all-inclusive, police-led operator
- Origin selector: From Surabaya (12 packages) vs From Bali (4 packages)
- Duration overview table (1D1N to 6D5N, what's covered per tier)
- ISIC note (student pricing available)
- CTAs: Browse Surabaya tours / Browse Bali tours

- [ ] **Step 3: Verify**

```bash
grep -n "Blue Fire guaranteed\|mandatory health screening\|provides police escort" output/copy-2026-05-12-tours.md
```

Expected: 0 matches.

- [ ] **Step 4: Commit**

```bash
git add output/copy-2026-05-12-tours.md
git commit -m "output | website-copy — tours hub"
```

---

## Task 8: Surabaya Short Tours (3 pages)

**Wiki sources to read:**
- `wiki/products/packages-full-pricing.md` (bromo-1d1n, bromo-2d1n, ijen-2d1n pricing)
- `wiki/products/packages-itineraries.md` (day-by-day for these 3 packages)
- `wiki/destinations/kawah-ijen.md` (for ijen-2d1n)
- `wiki/destinations/mount-bromo.md` (for bromo-1d1n, bromo-2d1n)

- [ ] **Step 1: Read sources**

Read all 4 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-tour-bromo-1d1n-surabaya.md`**

Use Standard Tour Page Template. Specific content:
- Hero: "1 Day Bromo Midnight Experience from Surabaya"
- At a glance: 1D1N, no Ijen (no health screening section), Bromo only
- Day 1: midnight departure from Surabaya → Penanjakan sunrise → Sea of Sand → Pura Luhur Poten → return
- Pricing: from packages-full-pricing bromo-1d1n rows (IDR/person by pax tier)
- No health screening section (ijen_relevant: no)

- [ ] **Step 3: Write `output/copy-2026-05-12-tour-bromo-2d1n-surabaya.md`**

Use Standard Tour Page Template. Specific content:
- Hero: "2 Day Bromo Sunrise Adventure from Surabaya"
- At a glance: 2D1N, Bromo, overnight Cemoro Lawang
- Day 1 + Day 2 from packages-itineraries
- Pricing: bromo-2d1n rows
- No health screening section

- [ ] **Step 4: Write `output/copy-2026-05-12-tour-ijen-2d1n-surabaya.md`**

Use Standard Tour Page Template. Specific content:
- Hero: "2 Day Ijen Blue Fire Expedition from Surabaya"
- At a glance: 2D1N, Ijen only, health screening coordination when rules apply
- Day 1 + Day 2 from packages-itineraries
- Pricing: ijen-2d1n rows
- Health screening section: conditional language, Dr. Irwandanu SIP

- [ ] **Step 5: Verify voice invariants**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-tour-bromo-1d1n-surabaya.md \
  output/copy-2026-05-12-tour-bromo-2d1n-surabaya.md \
  output/copy-2026-05-12-tour-ijen-2d1n-surabaya.md
```

Expected: 0 matches.

- [ ] **Step 6: Commit**

```bash
git add output/copy-2026-05-12-tour-bromo-1d1n-surabaya.md output/copy-2026-05-12-tour-bromo-2d1n-surabaya.md output/copy-2026-05-12-tour-ijen-2d1n-surabaya.md
git commit -m "output | website-copy — surabaya short tours (3D)"
```

---

## Task 9: Surabaya 3D2N Tours (3 pages)

**Wiki sources to read:**
- `wiki/products/packages-full-pricing.md` (bromo-madakaripura-ijen-3d2n, ijen-bromo-madakaripura-3d2n, taman-safari-prigen-bromo-madakaripura-3d2n pricing)
- `wiki/products/packages-itineraries.md`
- `wiki/destinations/kawah-ijen.md`, `wiki/destinations/mount-bromo.md`, `wiki/destinations/madakaripura.md`

- [ ] **Step 1: Read sources**

Read all 5 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-tour-bromo-madakaripura-ijen-3d2n-surabaya.md`**

Use Standard Tour Page Template:
- Hero: "3 Day Bromo, Madakaripura & Ijen Overland from Surabaya to Bali"
- Direction: Surabaya → Bromo → Madakaripura → Ijen → Bali (one-way overland)
- Note: "This tour ends in Bali — confirm onward travel from Bali before booking."
- 3-day itinerary from packages-itineraries
- Pricing from packages-full-pricing
- Health screening section (Ijen day — conditional)

- [ ] **Step 3: Write `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-3d2n-surabaya.md`**

Use Standard Tour Page Template:
- Hero: "3 Day Ijen, Bromo & Madakaripura Waterfall Discovery from Surabaya"
- Direction: Surabaya → Ijen → Bromo → Madakaripura → Surabaya (round trip)
- 3-day itinerary
- Pricing
- Health screening section (Ijen day — conditional)

- [ ] **Step 4: Write `output/copy-2026-05-12-tour-taman-safari-prigen-bromo-madakaripura-3d2n-surabaya.md`**

Use Standard Tour Page Template:
- Hero: "3 Day Taman Safari Prigen, Bromo & Madakaripura from Surabaya"
- Note: "Taman Safari Prigen is a wildlife and safari park in Prigen, East Java (near Pasuruan)."
- No Ijen — no health screening section
- Pricing from packages-full-pricing (if taman-safari rows exist; if not: note "Pricing not yet in wiki — confirm with JVTO directly")
- Source note: confirmed via sitemap 2026-05-12; full pricing/itinerary pending wiki update

- [ ] **Step 5: Verify voice invariants**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-tour-*-3d2n-surabaya.md
```

Expected: 0 matches.

- [ ] **Step 6: Commit**

```bash
git add output/copy-2026-05-12-tour-*-3d2n-surabaya.md
git commit -m "output | website-copy — surabaya 3d2n tours"
```

---

## Task 10: Surabaya 4D3N Tours (3 pages)

**Wiki sources to read:**
- `wiki/products/packages-full-pricing.md` (4D3N rows)
- `wiki/products/packages-itineraries.md`
- `wiki/destinations/kawah-ijen.md`, `wiki/destinations/mount-bromo.md`, `wiki/destinations/tumpak-sewu.md`, `wiki/destinations/papuma-beach.md`

- [ ] **Step 1: Read sources**

Read all 6 wiki pages listed above.

- [ ] **Step 2: Write `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-4d3n-surabaya.md`**

4-day itinerary: Ijen → Papuma Beach → Tumpak Sewu → Bromo. Health screening section (Ijen). Pricing table.

- [ ] **Step 3: Write `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-4d3n-surabaya.md`**

4-day itinerary: Ijen → Bromo → Madakaripura. Health screening (Ijen). Pricing table.

- [ ] **Step 4: Write `output/copy-2026-05-12-tour-tumpak-sewu-bromo-ijen-4d3n-surabaya.md`**

4-day itinerary: Tumpak Sewu → Bromo → Ijen → Bali (one-way overland, ends in Bali). Note: "This tour ends in Bali." Health screening (Ijen). Pricing table.

- [ ] **Step 5: Verify and commit**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-tour-*-4d3n-surabaya.md
git add output/copy-2026-05-12-tour-*-4d3n-surabaya.md
git commit -m "output | website-copy — surabaya 4d3n tours"
```

---

## Task 11: Surabaya 5D4N+ Tours (3 pages)

**Wiki sources to read:**
- `wiki/products/packages-full-pricing.md` (5D4N, 6D5N rows)
- `wiki/products/packages-itineraries.md`
- All 5 destination pages

- [ ] **Step 1: Read sources**

Read `wiki/products/packages-full-pricing.md`, `wiki/products/packages-itineraries.md`, and the 5 destination pages.

- [ ] **Step 2: Write `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-malang-5d4n-surabaya.md`**

5-day: Ijen → Bromo → Madakaripura → Malang City. Note Malang city day briefly (Mount Bromo wiki may have Malang context). Health screening (Ijen). Pricing.

- [ ] **Step 3: Write `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-5d4n-surabaya.md`**

5-day: Ijen → Papuma → Tumpak Sewu → Bromo. Health screening (Ijen). Pricing.

- [ ] **Step 4: Write `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-malang-6d5n-surabaya.md`**

6-day (longest package): Ijen → Papuma → Tumpak Sewu → Bromo → Malang. Health screening (Ijen). Pricing. Hero: "The Full East Java Circuit."

- [ ] **Step 5: Verify and commit**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|provides police escort" \
  output/copy-2026-05-12-tour-ijen-*-5d4n-surabaya.md \
  output/copy-2026-05-12-tour-ijen-*-6d5n-surabaya.md
git add output/copy-2026-05-12-tour-ijen-*-5d4n-surabaya.md output/copy-2026-05-12-tour-ijen-*-6d5n-surabaya.md output/copy-2026-05-12-tour-ijen-bromo-madakaripura-malang-5d4n-surabaya.md
git commit -m "output | website-copy — surabaya 5d4n+ tours"
```

---

## Task 12: Bali Tours (4 pages)

**Wiki sources to read:**
- `wiki/products/packages-full-pricing.md` (bali/ rows)
- `wiki/products/packages-itineraries.md`
- `wiki/destinations/kawah-ijen.md`, `wiki/destinations/mount-bromo.md`, `wiki/destinations/madakaripura.md`, `wiki/destinations/tumpak-sewu.md`, `wiki/destinations/papuma-beach.md`

- [ ] **Step 1: Read sources**

Read pricing, itineraries, and all relevant destination pages.

- [ ] **Step 2: Write `output/copy-2026-05-12-tour-bromo-ijen-3d2n-bali.md`**

Bali → Bromo → Ijen → Surabaya (ends in Surabaya). Note: "This tour ends in Surabaya — confirm onward travel." Health screening (Ijen). Pricing (priority 0.7 — Bali origin).

- [ ] **Step 3: Write `output/copy-2026-05-12-tour-ijen-bromo-madakaripura-3d2n-bali.md`**

Bali → Ijen → Bromo → Madakaripura → Surabaya. Note: ends in Surabaya. Health screening (Ijen). Pricing.

- [ ] **Step 4: Write `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-4d3n-bali.md`**

Bali → Ijen → Papuma → Tumpak Sewu → Bromo → Surabaya. Note: ends in Surabaya. Health screening (Ijen). Pricing.

- [ ] **Step 5: Write `output/copy-2026-05-12-tour-ijen-papuma-tumpak-sewu-bromo-5d4n-bali.md`**

5-day extended version of the 4D3N. Bali → Ijen → Papuma → Tumpak Sewu → Bromo → Surabaya. Note: ends in Surabaya. Health screening (Ijen). Pricing.

- [ ] **Step 6: Verify voice invariants**

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening\|JVTO provides police escort" \
  output/copy-2026-05-12-tour-*-bali.md
```

Expected: 0 matches.

- [ ] **Step 7: Final commit**

```bash
git add output/copy-2026-05-12-tour-*-bali.md
git commit -m "output | website-copy — bali tours (4 pages)"
```

---

## Verification — Full Inventory Check

After all 12 tasks, verify all 50 new files exist:

```bash
ls output/copy-2026-05-12-*.md | wc -l
```

Expected: ≥53 files (50 new + 3 pre-existing).

```bash
grep -rn "Blue Fire guaranteed\|100% Blue Fire\|mandatory health screening" output/copy-2026-05-12-*.md
```

Expected: 0 matches across all files.

---

## Self-Review

**Spec coverage:**
- All 53 sitemap URLs mapped to output files ✓
- 3 pre-existing files noted as skip ✓
- 50 new files across 12 tasks ✓
- Voice invariants enforced with grep checks in every task ✓
- Standard tour template defined ✓
- Each task lists exact wiki source pages to read ✓
- Taman Safari Prigen pricing gap noted (not in wiki yet) ✓

**No placeholders:** All tasks specify exact sections, exact wiki sources, exact filenames, exact git commands. The only conditional is the Taman Safari pricing gap (explicitly documented as known gap).

**Type consistency:** All output filenames follow `copy-2026-05-12-[slug].md` convention. All tour pages use the Standard Tour Page Template. Health screening conditional language referenced consistently.
