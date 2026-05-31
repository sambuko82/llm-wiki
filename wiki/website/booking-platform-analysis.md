---
type: website
title: Trip.com Booking Platform Workflow Analysis
last_updated: 2026-05-31
sources: [tango-workflow-trip-com, faq-master, packages-overview]
creator: Agung Sambuko
---

# Trip.com Booking Workflow Analysis

**Tango workflow reference**: Book Java Volcano Tour on Trip.com (18 steps, created May 31, 2026 by Agung Sambuko)
**Price point captured**: IDR 3,350,000 (likely 2 pax, `ijen-bromo-madakaripura-3d2n`)

---

## Workflow Summary (18 Steps)

### Phase 1: Package Selection (Steps 1–6)

| Step | Action | Wiki Parallel | Notes |
|------|--------|---------|-------|
| 1 | Click "FROM SURABAYA…" | [[products/packages-overview]] origin selector | Selects Surabaya as starting point |
| 2 | Click "moderate" | Package difficulty filter | Moderate = Ijen + Bromo routes (not Tumpak Sewu) |
| 3 | Click "Private Expedition" | 100% private guarantee | Trip.com label for JVTO private-only guarantee |
| 4 | Type "2026-06-25" (date) | Booking inquiry → package confirmation | Date of Day 1 |
| 5 | Click "1 Travelers" | Pax tier selector | 1 pax solo, or "1 Travelers" = 1 person (solo pricing applies) |
| 6 | Click "DONE" | Summary screen | Confirms package, date, pax, picks up cost quote |

**Implied package**: `ijen-bromo-madakaripura-3d2n` (3D2N, Ijen-relevant, solo tier → IDR 6,300,000 from SSOT, but Trip.com displays IDR 3,350,000 after discount — needs Sam verification)

---

### Phase 2: Add-ons / Enhancements (Steps 7–11)

| Step | Action | Wiki Parallel | Notes |
|------|--------|---------|-------|
| 7 | Click "INSTANT BOOK" | [[products/packages-overview]] §booking-flow step 4 | Triggers Trip.com payment flow (skips JVTO WhatsApp inquiry) |
| 8 | Click "Enhance Your Trip…" | Upsell / optional add-ons | Trip.com offers extras |
| 9 | Check "Transport to Medewi…" | Optional add-on | Medewi is a Bali coastal town; suggests Bali extension |
| 10 | Click "CONTINUE" | Advance to payment block | Confirms selected add-ons |

**Risk**: Upsells may not align with JVTO standard inclusions → verify with Sam.

---

### Phase 3: Trip Configuration & Review (Steps 11–14)

| Step | Action | Wiki Parallel | Notes |
|------|--------|---------|-------|
| 11 | Click "TRIP CONFIGURATION…" | Pre-trip guide + special requests | Guest inputs any special dietary/mobility needs |
| 12 | Click "Google" | Google sign-in (auth shortcut) | Guest logs in via Google to autofill contact details |
| 13 | Click "REVIEW & PAY →" | [[products/packages-overview]] step 4 (payment) | Summary + total before charging |
| 14 | Click "REVIEW & PAYMENT…" | Payment details entry | Card entry, billing address, Trip.com terms accept |

---

### Phase 4: Terms & Payment (Steps 15–16)

| Step | Action | Wiki Parallel | Notes |
|------|--------|---------|-------|
| 15 | Check "I agree to Terms & Conditions and Cancellation Policy" | [[sources/ssot-v6]] §7_1, Q3 link to policy | **CRITICAL**: Trip.com terms may differ from JVTO Travel Credit system ([[website/faq-master]] Q17). Verify Trip.com cancellation policy. |
| 16 | Click "PAY IDR 3.350.000" | Deposit charged (20% or full per close-dep rule) | **Price needs reconciliation**: SSOT says IDR 3,570,000/person (2 pax) or IDR 6,300,000 (solo). IDR 3,350,000 suggests discount or different package tier. |

---

### Phase 5: Post-Payment Checkout (Steps 17–18)

| Step | Action | Wiki Parallel | Notes |
|------|--------|---------|-------|
| 17 | Click "🇮🇩…" (currency/country) | Payment method region selector | Confirms Indonesia IDR as billing currency |
| 18 | Click "Order Summary…" | E-Voucher issuance | Final confirmation; Trip.com emails booking ref + e-voucher trigger to JVTO |

**Expected outcome**: E-Voucher emailed + WhatsApp contact to +62 822 4478 8833 for pick-up + itinerary confirmation.

---

## Key Correlations & Gaps

### Flow Alignment ✓

- **Package selection** (Steps 1–6) → **JVTO inquiry** (faq Q15 step 1): dates, origin, group size confirmed
- **Payment** (Step 16) → **JVTO booking step 4**: deposit via secure checkout
- **Terms acceptance** (Step 15) → **JVTO policy**: legal terms [[sources/ssot-v6]] §7_1
- **E-Voucher** (Step 18) → **JVTO step 5**: full trip details + pre-trip guide

### Critical Gaps ⚠

1. **Cancellation Policy Mismatch** (Step 15)
   - **JVTO**: Travel Credit (Q17: 100% ≥48h, forfeited <48h)
   - **Trip.com**: Standard OTA policy (may differ)
   - **Action**: Verify Trip.com terms against JVTO's — may need whitelabel caveat

2. **Price Anomaly** (Step 16)
   - **Displayed**: IDR 3,350,000
   - **SSOT reference**: IDR 3,570,000 (2 pax) or IDR 6,300,000 (solo)
   - **Action**: Clarify whether Trip.com applies commission rebate or promotional discount

3. **Add-on Alignment** (Step 9: Medewi transport)
   - Not in JVTO standard inclusions
   - **Action**: Audit Trip.com upsells against [[products/packages-overview]] §inclusions

4. **Health Screening Missing** (Ijen routes)
   - BBKSDA-required for Ijen ([[website/faq-master]] Q6, [[destinations/kawah-ijen]])
   - Trip.com workflow does not mention screening or Dr. Irwandanu coordination
   - **Action**: Confirm whether health screening is post-booking or Trip.com upsell

---

## Owner Tasks

**For Sam** (Agung Sambuko):
- [ ] Verify IDR 3,350,000 pricing for the captured Tango workflow
- [ ] Audit all Trip.com upsells against standard inclusions
- [ ] Confirm cancellation policy alignment (Travel Credit vs Trip.com terms)
- [ ] Verify health screening collection method for Ijen routes
- [ ] Test full e2e flow (Trip.com → e-voucher → WhatsApp handoff → pick-up)

---

### Trust Anchors

-> [[website/faq-master]] (Q15: booking flow, Q16: payments, Q17: cancellation) | -> [[products/packages-overview]] (booking-flow, payment-rules, inclusions) | -> [[destinations/kawah-ijen]] (health-screening requirement) | -> [[credentials/trust-signals]] | -> [[people/dr-ahmad-irwandanu]] (screening protocol)
