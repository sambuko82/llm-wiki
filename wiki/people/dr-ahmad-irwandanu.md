---
type: person
title: Dr. Ahmad Irwandanu — Medical Officer (Ijen Health-Screening Coordination)
last_updated: 2026-07-06
sources: [ssot-v6, jvto-homepage-clip]
role: Medical Officer — Ijen Health-Screening Coordination
schema_id: "/#dr-ahmad-irwandanu"
schema_type: Person
health_wording_mode: mandatory
owner: wiki-llm
stale_after_days: 60
---

# Dr. Ahmad Irwandanu

## Identity & Role

- **Title**: Licensed Medical Doctor (SIP-credentialed)
- **Role in JVTO**: Medical officer for Ijen health-screening coordination
- **Base**: Bondowoso, East Java
- **Registry**: Kemenkes RI · SatuSehat SDMK · KKI (Konsil Kedokteran Indonesia)

## Verification URLs (publicly auditable)

- **STR lookup (Kemenkes SatuSehat)**: https://satusehat.kemkes.go.id/sdmk/nakes/QN00001073380217
- **KKI license check**: https://www.kki.go.id/cekdokter/form

Guests can verify the license independently before booking.

## Why "Mandatory," Not "Conditional"

> **Voice invariant — critical (adjudicated 2026-07-06, supersedes the 2026-07-05 conditional decision and the [[sources/ssot-v6]] §2_4 conditional framing)**: a health certificate is **mandatory for every guest** before Kawah Ijen crater entry. BBKSDA SE.1658/KSA.9/2024 is cited as supporting regulatory authority/evidence, not as a conditional trigger. JVTO **coordinates** the mandatory screening workflow — it does not unilaterally impose the rule, but the rule applies to every guest, not conditionally.

Approved phrasings:

- ✅ "A health certificate is mandatory for every guest before Kawah Ijen crater entry."
- ✅ "JVTO coordinates the mandatory clinic workflow under BBKSDA SE.1658/KSA.9/2024."
- ✅ "Health screening is mandatory under BBKSDA SE.1658/KSA.9/2024, cited here as supporting authority."

Forbidden:

- ❌ "Ijen access rules can require a recent local health certificate" (conditional framing — superseded 2026-07-06)
- ❌ "Required by JVTO" (the rule is regulatory, not operator-imposed)

## Regulatory Basis

- **BBKSDA Surat Edaran SE.1658/KSA.9/2024** — regulatory screening requirement for Ijen crater access (`bbksda-surat-edaran-se-1658-ksa-9-2024` proof asset)
- **BBKSDA ticket terms** at tiket.bbksdajatim.org — health certificate required for crater access (`bbksda-ticket-terms-screenshot`)

See [[credentials/trust-signals]] for full BBKSDA proof chain.

## Screening Protocol

JVTO coordinates the mandatory protocol per **Ijen Digital Health Security System** (https://health.mountijen.com), under BBKSDA SE.1658/KSA.9/2024.

### Process (4 steps)

1. JVTO coordinates pre-hike health check — either at partner clinic or hotel/office session
2. Guest vitals recorded digitally
3. QR-verified surat sehat (health certificate) issued by licensed doctor — Dr. Ahmad Irwandanu
4. Certificate presented at crater access gate for BBKSDA QR verification

### Data Points Measured

| Metric | What's checked |
|---|---|
| Oxygen Saturation (SpO2) | Lung function baseline |
| Blood Pressure (Systolic / Diastolic) | Cardiovascular risk |
| Resting Heart Rate | Cardiovascular baseline |
| Respiratory History Check | Asthma / bronchitis (gas exposure relevant) |

### Logic Gate

> **No Valid QR Code = No Access to Crater Zone**

### Failure Protocol

If a guest is assessed unfit, the **climb is cancelled for that individual** (not the group). Cost for the screening session is non-refundable. Alternatives: wait at base camp or safe zone while group continues.

This is regulatory, not JVTO discretion. See [[sources/ssot-v6]] §7_2 health_screening_protocol.

## Partner Facilities (medical-screening institutional chain)

| Facility | Location | Type | Verification |
|---|---|---|---|
| Klinik Bakti Husada | Bondowoso | Certified medical clinic (Kemenkes RI) | Physical clinic, not a mobile service |
| Puskesmas Licin | Banyuwangi | Government health centre | Official government-run facility — Ijen screening partner (Dinkes Banyuwangi) |
| **Dr. Ahmad Irwandanu** | Bondowoso | Licensed medical professional | STR + KKI registry (URLs above) |

This multi-facility chain matters because the surat sehat carries a SIP number and BBKSDA-verifiable QR code — **the certificate cannot be faked without a valid licensed doctor's identity behind it**. The doctor and the clinic are independently auditable.

## Proof Assets

- `bbksda-surat-edaran-se-1658-ksa-9-2024` — canonical regulation document
- `bbksda-ticket-terms-screenshot` — public-facing crater-access terms
- `health-screening-form-sample-2026-02-17` — sample certificate
- `sip-dr-ahmad-irwandanu-2026` — SIP (Surat Izin Praktik) credential
- `ijen-screening-hotel-01` — operational evidence
- `jvto-office-screening-1` — operational evidence
- `print-surat-sehat-preview` — print artifact

See [[credentials/trust-signals]].

## Schema

- `@type: Person`
- `@id: /#dr-ahmad-irwandanu`
- Page type for any /travel-guide/ijen-health-screening surface: `MedicalWebPage`

## Trust Anchors

Owns claim **C4** (Ijen Health Screening — safety layer) per [[website/aeo-claims]] and [[sources/ssot-v6]] §12.C4. Supports **C1** (safety-led operations).

-> [[credentials/medical-screening]] | -> [[destinations/kawah-ijen]] | -> [[credentials/trust-signals]] | -> [[website/faq-master]] | -> [[website/aeo-claims]]
