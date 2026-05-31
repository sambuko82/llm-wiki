---
type: source
title: Tango Workflow — JVTO Website Booking Flow
last_updated: 2026-05-31
sources: [packages-overview, faq-master, ssot-v6]
owner: wiki-llm
stale_after_days: 90
pages_updated: [wiki/index, wiki/ops/policy-source-ownership, wiki/products/packages-overview, wiki/website/booking-platform-analysis, wiki/website/faq-master]
---

# Tango Workflow — JVTO Website Booking Flow

**Source type**: Tango workflow tool — screenshot PDF, 4 pages, 18 steps
**Creator**: Agung Sambuko
**Date recorded**: 2026-05-31
**Raw file**: `raw/a28a3c50-ecd0-43e6-9ebd-4d34f0aa1713.pdf` (R065, 3.3 MB, image-based)
**Analysis page**: -> [[website/booking-platform-analysis]]

---

## What This Source Is

Tango is a workflow documentation tool that records step-by-step screen captures as a sharable PDF. This PDF shows Agung Sambuko walking through the **JVTO website self-checkout flow** — the "Instant Book" path a guest can take directly on javavolcano-touroperator.com without WhatsApp contact first.

**Key distinction**: This is the website **self-checkout flow** (Instant Book), not the WhatsApp-assisted booking flow described in [[products/packages-overview]] §booking-flow. Both paths exist; this source documents the one that is often invisible in wiki coverage.

---

## Workflow Summary (5 Phases, 18 Steps)

### Phase 1: Package Discovery / Listing (Steps 1–2)

Guest lands on package listing. Origin, difficulty, and private/group filter visible. Selects package.

### Phase 2: Package Detail + Date & Traveler Selection (Steps 3–6)

Package detail page. Guest inputs:
- Departure date (Day 1)
- Traveler count (pax tier)
- Clicks "DONE" to confirm selection → price quote shown

**Price captured**: IDR 3,350,000 (package: likely `ijen-bromo-madakaripura-3d2n`, pax tier unconfirmed)

### Phase 3: Add-On / Transport Modal (Steps 7–10)

"INSTANT BOOK" button triggers checkout. Add-on transport modal appears:
- "Transport to Medewi…" option visible (Bali coastal extension)
- Guest selects / skips, clicks "CONTINUE"

### Phase 4: Trip Confirmation + Contact Details (Steps 11–13)

- "TRIP CONFIGURATION…" — special requests / dietary / mobility inputs
- Google auth (sign in with Google to autofill contact)
- "REVIEW & PAY →" — summary before payment

### Phase 5: Review, Payment & Order Summary (Steps 14–18)

- Payment details entry (card, billing address)
- Terms & Conditions checkbox (Step 15) — **CRITICAL**: must display JVTO Travel Credit cancellation terms
- "PAY IDR 3.350.000" button (Step 16)
- Currency/country region selector (🇮🇩 IDR)
- Order Summary / e-Voucher issuance (Step 18)

**Expected post-payment**: E-voucher emailed + WhatsApp contact to +62 822 4478 8833 for pick-up confirmation.

---

## Critical Gaps Identified

1. **Price Anomaly** — IDR 3,350,000 displayed vs SSOT reference (IDR 3,570,000 for 2 pax or IDR 6,300,000 solo for `ijen-bromo-madakaripura-3d2n`). Commission rebate, promotional discount, or different pax tier? Needs Sam verification.

2. **Add-On Alignment** — "Transport to Medewi" upsell not in [[products/packages-overview]] §inclusions/exclusions. Need to confirm what JVTO website upsells are authorised.

3. **Health Screening Missing** — No step in the checkout flow collects health screening data or confirms BBKSDA/Dr. Irwandanu coordination. Required for all Ijen routes. Presumably collected post-booking via WhatsApp — confirm.

4. **Terms Checkbox Content** — Step 15 terms must display JVTO Travel Credit policy (100% credit ≥48h notice, forfeited <48h). Needs UI audit to verify correct policy text is shown.

5. **wiki/products/packages-overview §booking-flow is stale** — Describes WhatsApp-only flow (6 steps starting with "Inquiry via WhatsApp"). Self-checkout / Instant Book path exists and is not documented there. Gap to flag.

---

## Relation to Existing Wiki

| Page | Relation |
|------|---------|
| [[products/packages-overview]] | Self-checkout flow is parallel to, not replacing, WA-assisted flow. §booking-flow needs "Instant Book path" added. |
| [[website/faq-master]] Q15 | Booking flow FAQ describes WA path; should reference Instant Book alternative. |
| [[website/faq-master]] Q16 | Payment via secure checkout — aligns with this flow. |
| [[website/faq-master]] Q17 | Cancellation / Travel Credit — must match Step 15 terms text. |
| [[website/booking-platform-analysis]] | Full 18-step analysis with step-by-step table. This source page is the lightweight reference. |
