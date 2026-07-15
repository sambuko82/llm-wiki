---
type: ops
title: Policy Source Ownership — Canonical Map
last_updated: 2026-07-15
sources: [jvto-policy-pack-v6, tango-workflow-jvto-website-booking]
owner: wiki-llm
stale_after_days: 120
---

# Policy Source Ownership — Canonical Map

A single operating map defining which wiki file is **canonical** for each JVTO policy domain, which files support it, where it is consumed, and the constraints that keep policy wording consistent. Use this before editing any policy text: update the canonical source first, then let derived FAQ/copy follow.

## Ownership Table

| Policy Domain | Canonical Source | Supporting Sources | Consumers | Notes |
|---|---|---|---|---|
| Booking Paths | products/packages-overview.md | website/booking-platform-analysis.md, sources/tango-workflow-jvto-website-booking.md | website_checkout, booking_portal, faq, policy_page | **Website-only booking.** JVTO accepts bookings exclusively through the official website checkout under a valid JVTO Booking ID. WhatsApp/email are support channels only — they never create, confirm, modify, cancel, or transfer a booking. |
| Payment Rules | products/packages-overview.md | website/faq-master.md | checkout, invoice, FAQ | 20% deposit standard; close-departure (Day 1 within 14 days) may require full payment |
| Cancellation / Package Credit | policies/cancellation-package-credit.yml | products/packages-overview.md, website/faq-master.md | website_checkout, booking_portal, policy_page, booking_confirmation, e_voucher, invoice, customer_support, faq | **Canonical logic lives in the YAML** (compiler reads it directly). Full voluntary ≥48h → Lifetime Package Credit (no cash); full <48h → forfeited. **Partial passenger cancellation** (booking continues): ≥48h → 100% cash refund of cancelled pax price, <48h → 50%, after Day 1 → 0%. Package Credit: no expiry, no cash value, same package/pax/price locked, one transfer, no split. Flight disruption → 50% Recovery Fee (once). |
| Inclusions / Exclusions | products/packages-overview.md | website/faq-master.md | package pages, FAQ, quotation | Madakaripura helmets are NOT a JVTO inclusion (local site management) |
| Ijen Health Screening | website/faq-master.md, people/dr-ahmad-irwandanu.md | destinations/kawah-ijen.md | package pages, FAQ, WhatsApp | Mandatory wording (health certificate required for every guest before crater entry); BBKSDA SE.1658/KSA.9/2024 cited as supporting authority, not a conditional trigger. Adjudicated 2026-07-06, supersedes the 2026-07-05 conditional decision |
| Natural Phenomena | website/brand-voice.md | website/faq-master.md, destinations/kawah-ijen.md | package pages, CS replies | No guarantee for Blue Fire / sunrise |
| ISIC | credentials/trust-signals.md | website/faq-master.md | student pages, FAQ | ISIC is UNESCO-endorsed; do NOT imply UNESCO endorses JVTO |
| Police Escort | credentials/trust-signals.md | website/faq-master.md, website/brand-voice.md | group pages, FAQ | Conditional coordination only (large groups ~18+, when approved by Traffic Police) |
| Anti-Fraud | products/packages-overview.md | website/faq-master.md | checkout, payment instructions | Use only official JVTO channels; never share full card numbers, CVV, passwords, OTP |

## Operating Rules

- **The Cancellation / Package Credit domain is YAML-canonical.** Its single source of logic is `wiki/policies/cancellation-package-credit.yml`. Markdown (`products/packages-overview.md`, `website/faq-master.md`) is *supporting* human-readable copy and must not state any number or outcome that differs from the YAML. The compiler reads the YAML directly.
- **Do not edit generated JSON directly.** (e.g. `output/website/trust-bundle/*.json` and other compiled output — regenerate from canonical source, never hand-edit.)
- **If policy changes, update the canonical source first, then derived FAQ/copy.** Canonical source is the single point of truth; FAQ, website copy, WhatsApp templates, and compiled output flow downstream.
- **Do not introduce old refund/deposit wording without marking it legacy.** New copy must match current canonical wording. Legacy variants only appear if a specific dated legacy booking document requires them, and must be labelled as such.

## Deprecated / Do Not Use Wording

| Deprecated / wrong wording | Correct wording / rule |
|---|---|
| "Trip.com booking flow" (for R065) | Use "JVTO website self-checkout flow" or "JVTO Website Booking Flow". Historical "Trip.com" mentions in `wiki/log.md` are audit-trail only — not canonical source/policy wording. |
| "18+ page PDF" | "4 PDF pages, 18 Tango steps" |
| "Blue Fire guaranteed" | Never use. "Blue Fire is a natural phenomenon subject to weather and gas activity — not guaranteed." |
| "Sunrise guaranteed" | Never use. Weather and natural conditions are outside JVTO's control. |
| "Madakaripura helmet included by JVTO" | Never use. Helmets are provided by the local waterfall site management at the canyon entrance — not a JVTO inclusion. |
| "Police escort included by default" | Never use. JVTO can coordinate an official police escort for eligible large groups / certain segments, subject to Traffic Police approval. |
| "UNESCO endorses JVTO via ISIC" | Never use. ISIC itself is UNESCO-endorsed; this does not mean UNESCO endorses JVTO. |
| "Cash refund available for guest-initiated cancellation" | Never use for **full voluntary** cancellation — that path yields Lifetime Package Credit (≥48h) or forfeiture (<48h), never cash. Cash refunds apply ONLY to *partial passenger* cancellation and verified force-majeure per `policies/cancellation-package-credit.yml`. |
| "50% cancellation fee (<48h)" | Never use as a **full-cancellation** outcome — full <48h is 100% forfeiture, not a 50% fee. (Partial passenger cancellation <48h is a 50% *cash refund* of the cancelled pax price — a different scenario, approved.) Stale "50% fee" survives only in `raw/db_export_raw.json` (read-only source export). |
| "WhatsApp-assisted booking" / "Book through WhatsApp" / "Contact us to confirm your booking" | Never use. Booking is website-only. WhatsApp/email are support channels that never create/confirm/modify/cancel/transfer a booking. |
| "Your money stays in your account" / "Cash value" / "Guaranteed cash refund" | Never use for Package Credit. Approved: "Package Credit is not cash and cannot be exchanged for cash." |
| "Use the credit on any JVTO package" / "Split your travel credit" / "Unlimited transfers" | Never use. Package Credit is locked to the same package, original pax, and original price; it cannot be split; one complete transfer only. |
| "Travel insurance protection" | Never use. The Lifetime Package Guarantee is a cancellation/credit policy, not travel insurance. |
