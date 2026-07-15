# Output Index

*Master map of all output files → website URL → wiki sources → status.*
*Updated: 2026-05-25. Regenerate after any wiki update that changes source pages.*

**Status values**: `draft` — generated, not reviewed · `reviewed` — copy-checked · `published` — live on site · `stale` — source wiki updated since output was generated

---

## How to use

- Find any output file by website URL (Ctrl+F the URL slug)
- Check `status` before using in production — `draft` means unreviewed
- After a wiki update, compare `output_date` against wiki `last_updated`; flag as `stale` if output is older

## Machine-Readable Bundles

| File | Consumer target | Output date | Status | Key sources |
|---|---|---|---|---|
| `website/policy-bundle/policy-bundle.json` | policy_page, checkout, booking_portal, e_voucher, invoice, faq | 2026-07-15 | reviewed | cancellation-package-credit.yml, policy-source-ownership, packages-overview, faq-master |
| `website/policy-bundle/consumer-bundles.json` | website_checkout, booking_portal, e_voucher, invoice, policy_page, faq, customer_support | 2026-07-15 | reviewed | policy-bundle |
| `website/policy-bundle/decision-matrix.json` | cancellation rule engine (jvto-itinerary-core, backend) | 2026-07-15 | reviewed | cancellation-package-credit.yml |
| `website/policy-bundle/customer-copy.json` | policy_page, checkout, booking_portal, e_voucher, faq, customer_support | 2026-07-15 | reviewed | cancellation-package-credit.yml |
| `website/policy-bundle/deprecated-wording-report.json` | consumer-bundle wording validation | 2026-07-15 | reviewed | policy-source-ownership §deprecated |
| `website/policy-bundle/gap-report.json` | policy compiler health check | 2026-07-15 | reviewed | cancellation-package-credit.yml, policy-source-ownership, packages-overview, faq-master |
| `website/policy-bundle/_manifest.json` | sync/version gate | 2026-07-15 | reviewed | cancellation-package-credit.yml, policy-source-ownership, packages-overview, faq-master |
| `website/policy-bundle/JVTO_WEB_SYNC_HANDOFF.md` | jvto-web implementation handoff | 2026-07-15 | reviewed | policy-bundle manifest + consumer bundle |

---

## AEO Blocks

| File | Website target | Output date | Status | Key sources |
|---|---|---|---|---|
| `website/aeo/why-jvto.md` | `/why-jvto` (AEO overlay) | 2026-05-16 | reviewed | aeo-claims C1–C9, faq-master, legal-licenses, trust-signals |
| `website/aeo/policy-travel-guide.md` | `/policy` + `/travel-guide` (AEO overlay) | 2026-05-12 | reviewed | jvto-policy-pack-v6, jvto-travel-guide-en, faq-master |
| `website/aeo/ijen.md` | `/destinations/ijen-crater` (AEO overlay) | 2026-05-18 | reviewed | aeo-claims, faq-master, legal-licenses, trust-signals, kawah-ijen |
| `website/aeo/bromo.md` | `/destinations/mount-bromo` (AEO overlay) | 2026-05-18 | reviewed | aeo-claims, faq-master, legal-licenses, trust-signals, mount-bromo |
| `website/aeo/tumpak-sewu.md` | `/destinations/tumpak-sewu-waterfall` (AEO overlay) | 2026-05-18 | reviewed | aeo-claims, faq-master, legal-licenses, trust-signals, tumpak-sewu |
| `website/aeo/madakaripura.md` | `/destinations/madakaripura-waterfall` (AEO overlay) | 2026-05-18 | reviewed | aeo-claims, faq-master, legal-licenses, trust-signals, madakaripura |
| `website/aeo/papuma.md` | `/destinations/papuma-beach` (AEO overlay) | 2026-05-18 | reviewed | aeo-claims, faq-master, legal-licenses, trust-signals, papuma-beach |
| `website/aeo/bbksda-regulations-ijen.md` | `/travel-guide/bbksda-regulations-ijen` (AEO overlay) | 2026-05-25 | reviewed | kawah-ijen, medical-screening, bbksda-pelatihan-pemandu-2024, legal-licenses |
| `website/aeo/ijen-gas-mask-equipment.md` | `/travel-guide/ijen-gas-mask-equipment` (AEO overlay) | 2026-05-25 | reviewed | kawah-ijen, faq-master, packages-overview |
| `website/aeo/bbksda-regulations-bromo.md` | `/travel-guide/bbksda-regulations-bromo` (AEO overlay) | 2026-05-25 | reviewed | mount-bromo, faq-master, packages-overview |
---

## FAQ Pages

| File | Website target | Output date | Status | Key sources |
|---|---|---|---|---|
| `website/faq/ijen.md` | `/travel-guide/faq` (Ijen section) | 2026-05-16 | reviewed | faq-master, kawah-ijen, dr-ahmad-irwandanu, packages-overview |
| `website/faq/bromo.md` | `/travel-guide/faq` (Bromo section) | 2026-05-18 | reviewed | faq-master, mount-bromo, operational-facts, packages-overview |
| `website/faq/tumpak-sewu.md` | `/travel-guide/faq` (Tumpak Sewu section) | 2026-05-12 | reviewed | faq-master, tumpak-sewu, packages-overview |
| `website/faq/madakaripura.md` | `/travel-guide/faq` (Madakaripura section) | 2026-05-12 | reviewed | faq-master, madakaripura, packages-overview |
| `website/faq/papuma.md` | `/travel-guide/faq` (Papuma section) | 2026-05-25 | reviewed | faq-master, papuma-beach, packages-overview, brand-voice |
| `website/faq/bbksda-regulations-ijen.md` | `/travel-guide/faq` (Ijen regulations) | 2026-05-25 | reviewed | kawah-ijen, medical-screening, bbksda-pelatihan-pemandu-2024, legal-licenses |
| `website/faq/ijen-gas-mask-equipment.md` | `/travel-guide/faq` (Gas masks) | 2026-05-25 | reviewed | kawah-ijen, faq-master, packages-overview |
| `website/faq/bbksda-regulations-bromo.md` | `/travel-guide/faq` (Bromo regulations) | 2026-05-25 | reviewed | mount-bromo, faq-master, packages-overview |
---

## Website — Sitewide

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/homepage.md` | `/` | 2026-05-25 | reviewed |
| `website/pages/surabaya-landing.md` | `/tours` (Surabaya angle) | 2026-05-25 | reviewed |
| `website/pages/bali-landing.md` | `/tours` (Bali angle) | 2026-05-25 | reviewed |
| `website/pages/tours.md` | `/tours` | 2026-05-25 | reviewed |
| `website/pages/isic-student-package.md` | `/isic/student-package` | 2026-05-12 | reviewed |
| `website/pages/blog.md` | `/blog` | 2026-05-12 | reviewed |
| `website/pages/contact.md` | `/contact` | 2026-05-12 | reviewed |

---

## Website — Markets

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/markets/taiwan.md` | `/markets/taiwan` | 2026-06-11 | reviewed |

---

## Website — Destinations

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/destinations/hub.md` | `/destinations` | 2026-05-12 | reviewed |
| `website/pages/destinations/ijen-crater.md` | `/destinations/ijen-crater` | 2026-05-16 | reviewed |
| `website/pages/destinations/mount-bromo.md` | `/destinations/mount-bromo` | 2026-05-18 | reviewed |
| `website/pages/destinations/tumpak-sewu-waterfall.md` | `/destinations/tumpak-sewu-waterfall` | 2026-05-12 | reviewed |
| `website/pages/destinations/madakaripura-waterfall.md` | `/destinations/madakaripura-waterfall` | 2026-05-12 | reviewed |
| `website/pages/destinations/papuma-beach.md` | `/destinations/papuma-beach` | 2026-05-12 | reviewed |

---

## Website — Tours (Surabaya origin, 12 packages)

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/tours/surabaya/bromo-1d1n.md` | `/tours/from-surabaya/bromo-1d1n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/bromo-2d1n.md` | `/tours/from-surabaya/bromo-2d1n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-2d1n.md` | `/tours/from-surabaya/ijen-2d1n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-bromo-madakaripura-3d2n.md` | `/tours/from-surabaya/ijen-bromo-madakaripura-3d2n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/bromo-madakaripura-ijen-3d2n.md` | `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-4d3n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-bromo-madakaripura-4d3n.md` | `/tours/from-surabaya/ijen-bromo-madakaripura-4d3n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/tumpak-sewu-bromo-ijen-4d3n.md` | `/tours/from-surabaya/tumpak-sewu-bromo-ijen-4d3n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-5d4n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-bromo-madakaripura-malang-5d4n.md` | `/tours/from-surabaya/ijen-bromo-madakaripura-malang-5d4n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n.md` | `/tours/from-surabaya/ijen-papuma-tumpak-sewu-bromo-malang-6d5n` | 2026-05-12 | reviewed |
| `website/pages/tours/surabaya/taman-safari-prigen-bromo-madakaripura-3d2n.md` | `/tours/from-surabaya/taman-safari-prigen-bromo-madakaripura-3d2n` | 2026-05-12 | reviewed |

---

## Website — Tours (Bali origin, 4 packages)

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/tours/bali/bromo-ijen-3d2n.md` | `/tours/from-bali/bromo-ijen-3d2n` | 2026-05-12 | reviewed |
| `website/pages/tours/bali/ijen-bromo-madakaripura-3d2n.md` | `/tours/from-bali/ijen-bromo-madakaripura-3d2n` | 2026-05-12 | reviewed |
| `website/pages/tours/bali/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-4d3n` | 2026-05-12 | reviewed |
| `website/pages/tours/bali/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `/tours/from-bali/ijen-papuma-tumpak-sewu-bromo-5d4n` | 2026-05-12 | reviewed |

---

## Website — Travel Guide

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/travel-guide/hub.md` | `/travel-guide` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/best-time-to-visit.md` | `/travel-guide/best-time-to-visit` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/booking-information.md` | `/travel-guide/booking-information` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/faq.md` | `/travel-guide/faq` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/ijen-health-screening.md` | `/travel-guide/ijen-health-screening` | 2026-05-16 | reviewed |
| `website/pages/travel-guide/packing-and-fitness.md` | `/travel-guide/packing-and-fitness` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/police-escort-for-groups.md` | `/travel-guide/police-escort-for-groups` | 2026-05-16 | reviewed |
| `website/pages/travel-guide/safety-on-tours.md` | `/travel-guide/safety-on-tours` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/weather-and-closures.md` | `/travel-guide/weather-and-closures` | 2026-05-12 | reviewed |
| `website/pages/travel-guide/bromo-vs-ijen-comparison.md` | `/travel-guide/bromo-vs-ijen-comparison` | 2026-05-25 | reviewed |
| `website/pages/travel-guide/what-to-pack-bromo-ijen.md` | `/travel-guide/what-to-pack-bromo-ijen` | 2026-05-25 | reviewed |
| `website/pages/travel-guide/private-vs-shared-tour-comparison.md` | `/travel-guide/private-vs-shared-tour-comparison` | 2026-05-25 | reviewed |
| `website/pages/travel-guide/bromo-ijen-itinerary-guide.md` | `/travel-guide/bromo-ijen-itinerary-guide` | 2026-05-25 | reviewed |
| `website/pages/travel-guide/surabaya-vs-bali-starting-point.md` | `/travel-guide/surabaya-vs-bali-starting-point` | 2026-05-25 | reviewed |
| `website/pages/travel-guide/bbksda-regulations-ijen.md` | `/travel-guide/bbksda-regulations-ijen` | 2026-05-25 | draft |
| `website/pages/travel-guide/bbksda-regulations-bromo.md` | `/travel-guide/bbksda-regulations-bromo` | 2026-05-25 | draft |
| `website/pages/travel-guide/ijen-gas-mask-equipment.md` | `/travel-guide/ijen-gas-mask-equipment` | 2026-05-25 | draft |
| `website/pages/travel-guide/permit-requirements-east-java.md` | `/travel-guide/permit-requirements-east-java` | 2026-05-25 | draft |
| `website/pages/travel-guide/sulfur-mining-cultural-guide.md` | `/travel-guide/sulfur-mining-cultural-guide` | 2026-05-25 | draft |
---

## Website — Why JVTO

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/why-jvto/hub.md` | `/why-jvto` | 2026-05-12 | reviewed |
| `website/pages/why-jvto/community-standards.md` | `/why-jvto/community-standards` | 2026-05-12 | reviewed |
| `website/pages/why-jvto/our-story.md` | `/why-jvto/our-story` | 2026-05-25 | reviewed |
| `website/pages/why-jvto/our-team.md` | `/why-jvto/our-team` | 2026-05-25 | reviewed |
| `website/pages/why-jvto/reviews.md` | `/why-jvto/reviews` | 2026-05-25 | reviewed |
| `website/pages/why-jvto/the-jvto-difference.md` | `/why-jvto/the-jvto-difference` | 2026-05-25 | reviewed |
| `website/pages/why-jvto/2026-05-27-all-inclusive-narrative-page.md` | `/why-jvto/all-inclusive` | 2026-05-27 | draft |
| `website/pages/why-jvto/2026-05-27-lifetime-travel-credit-page.md` | `/why-jvto/lifetime-travel-credit` | 2026-05-27 | draft |

---

## Website — Verify JVTO

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/verify-jvto/hub.md` | `/verify-jvto` | 2026-05-16 | reviewed |
| `website/pages/verify-jvto/legal.md` | `/verify-jvto/legal` | 2026-05-16 | reviewed |
| `website/pages/verify-jvto/history-artifacts.md` | `/verify-jvto/history-artifacts` | 2026-05-16 | reviewed |
| `website/pages/verify-jvto/police-safety.md` | `/verify-jvto/police-safety` | 2026-05-16 | reviewed |
| `website/pages/verify-jvto/press-recognition.md` | `/verify-jvto/press-recognition` | 2026-05-16 | reviewed |

---

## Website — Policy

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/policy/hub.md` | `/policy` | 2026-05-12 | reviewed |
| `website/pages/policy/booking-payment-cancellation.md` | `/policy/booking-payment-cancellation` | 2026-05-12 | reviewed |
| `website/pages/policy/inclusions-exclusions.md` | `/policy/inclusions-exclusions` | 2026-05-12 | reviewed |
| `website/pages/policy/privacy.md` | `/policy/privacy` | 2026-05-12 | reviewed |

---

## Website — Team

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/team.md` | `/team` | 2026-05-25 | reviewed |
| `website/pages/team/agung-sambuko.md` | `/team/agung-sambuko` | 2026-05-25 | reviewed |
| `website/pages/team/anjas.md` | `/team/anjas` | 2026-05-25 | reviewed |
| `website/pages/team/taufik.md` | `/team/taufik` | 2026-05-25 | reviewed |
| `website/pages/team/rendi.md` | `/team/rendi` | 2026-05-25 | reviewed |
| `website/pages/team/kiki.md` | `/team/kiki` | 2026-05-25 | reviewed |
| `website/pages/team/gufron.md` | `/team/gufron` | 2026-05-25 | reviewed |
| `website/pages/team/fauzi.md` | `/team/fauzi` | 2026-05-25 | reviewed |
| `website/pages/team/boy.md` | `/team/boy` | 2026-05-25 | reviewed |
| `website/pages/team/yandi.md` | `/team/yandi` | 2026-05-25 | reviewed |
| `website/pages/team/fredi.md` | `/team/fredi` | 2026-05-25 | reviewed |
| `website/pages/team/holili.md` | `/team/holili` | 2026-05-25 | reviewed |
| `website/pages/team/joyo.md` | `/team/joyo` | 2026-05-25 | reviewed |
| `website/pages/team/yusuf.md` | `/team/yusuf` | 2026-05-25 | reviewed |
| `website/pages/team/dika.md` | `/team/dika` | 2026-05-25 | reviewed |
| `website/pages/team/pras.md` | `/team/pras` | 2026-05-25 | reviewed |

---

## Website — Tours (Student packages, 6)

| File | URL | Output date | Status |
|---|---|---|---|
| `website/pages/tours/student/bromo-ijen-3d2n.md` | `/tours/student-package/bromo-ijen-3d2n` | 2026-05-25 | reviewed |
| `website/pages/tours/student/bromo-ijen-3d2n-to-bali.md` | `/tours/student-package/bromo-ijen-3d2n-to-bali` | 2026-05-25 | reviewed |
| `website/pages/tours/student/ijen-bromo-3d2n-bali.md` | `/tours/student-package/ijen-bromo-3d2n` | 2026-05-25 | reviewed |
| `website/pages/tours/student/ijen-bromo-madakaripura-night-market-4d3n.md` | `/tours/student-package/ijen-bromo-madakaripura-night-market-4d3n` | 2026-05-25 | reviewed |
| `website/pages/tours/student/ijen-papuma-tumpak-sewu-bromo-4d3n.md` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-4d3n` | 2026-05-25 | reviewed |
| `website/pages/tours/student/ijen-papuma-tumpak-sewu-bromo-5d4n.md` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-5d4n` | 2026-05-25 | reviewed |

---

## JSON-LD Schema — Student Packages (6)

| File | URL | Output date | Status |
|---|---|---|---|
| `website/schema/student-bromo-ijen-3d2n-schema.json` | `/tours/student-package/bromo-ijen-3d2n` | 2026-05-26 | draft |
| `website/schema/student-bromo-ijen-3d2n-to-bali-schema.json` | `/tours/student-package/bromo-ijen-3d2n-to-bali` | 2026-05-26 | draft |
| `website/schema/student-ijen-bromo-3d2n-bali-schema.json` | `/tours/student-package/ijen-bromo-3d2n` | 2026-05-26 | draft |
| `website/schema/student-ijen-bromo-madakaripura-night-market-4d3n-schema.json` | `/tours/student-package/ijen-bromo-madakaripura-night-market-4d3n` | 2026-05-26 | draft |
| `website/schema/student-ijen-papuma-tumpak-sewu-bromo-4d3n-schema.json` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-4d3n` | 2026-05-26 | draft |
| `website/schema/student-ijen-papuma-tumpak-sewu-bromo-5d4n-schema.json` | `/tours/student-package/ijen-papuma-tumpak-sewu-bromo-5d4n` | 2026-05-26 | draft |

Verification receipt: `website/schema/student-schemas.receipt.md`

---

## Developer Handoff

| File | Purpose | Output date |
|---|---|---|
| `website/HANDOFF.md` | Complete route → output → schema map for developer integration | 2026-05-25 |

---

## Archive (legacy — superseded)

| File | Superseded by | Note |
|---|---|---|
| `_archive/kawah-ijen-page-copy.md` | `website/pages/destinations/ijen-crater.md` | Pre-convention, 2026-05-11 |
| `_archive/mount-bromo-page-copy.md` | `website/pages/destinations/mount-bromo.md` | Pre-convention, 2026-05-11 |

---

## Social Media Posts

| File | Topics | Output date | Status |
|---|---|---|---|
| `social/batch-2026-05-18.md` | C1–C9 differentiators: police, medical screening, reviews, Ijen, Bromo, pricing, founding story, private tours, Tumpak Sewu, Madakaripura | 2026-05-18 | reviewed |

---

## Blog Posts

| File | URL | Output date | Status |
|---|---|---|---|
| `website/blog/2026-05-27-why-not-unlicensed-ijen-operator.md` | `/blog/why-not-unlicensed-ijen-operator` | 2026-05-27 | published |
| `website/blog/2026-06-11-ijen-medical-checkup-requirement.md` | `/blog/2026-06-11-ijen-medical-checkup-requirement` | 2026-06-11 | published |
| `website/blog/2026-06-11-kawah-ijen-guide.md` | `/blog/2026-06-11-kawah-ijen-guide` | 2026-06-11 | published |

---

## Missing Outputs (no file yet)

Outputs not yet generated for these website pages / content formats:

| Target | Notes |
|---|---|
| ~~AEO blocks — per destination~~ | **Resolved 2026-05-18** → `aeo/ijen.md`, `aeo/bromo.md`, `aeo/tumpak-sewu.md`, `aeo/madakaripura.md`, `aeo/papuma.md` |
| ~~Social media posts~~ | **Resolved 2026-05-18** → `social/batch-2026-05-18.md` (10 posts, 14 caption units) |
| Slide decks | Format type not yet produced (Workflow 5 `slide-deck` profile) |
| ~~`faq/papuma.md` pricing~~ | **Verified 2026-05-25** vs packages-full-pricing.md ✓ |

> ~~**Stale candidates** (resolved 2026-05-16)~~: All 4 previously stale files refreshed.
> ~~**Stale candidates** (resolved 2026-05-18)~~: `faq/bromo.md`, `website/destinations/mount-bromo.md` refreshed with Level II Waspada content.
