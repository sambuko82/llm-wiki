---
type: credential
title: JVTO Trust Signals — Reviews, Press, Partners, Historical
last_updated: 2026-05-11
sources: [ssot-v6, jvto-homepage-clip]
---

# JVTO Trust Signals

Third-party evidence. Use in content to **prove claims, not assert them**. All entries below are independently verifiable.

## Live Review Platforms (verified 2026-05-09)

| Platform | Rating | Count | URL |
|---|---|---|---|
| **Trustpilot** (primary) | **4.8 / 5** | 51 | https://trustpilot.com/review/javavolcano-touroperator.com |
| **Google Maps** | 4.90 / 5 | 92 | https://www.google.com/maps?cid=1266403973589689021 |
| **TripAdvisor** | 4.95 / 5 | 21 | https://www.tripadvisor.com/Attraction_Review-g297715-d19983165-Reviews-Java_Volcano_Tour_Operator-Surabaya_East_Java_Java.html |
| **GetYourGuide** | — | — | https://www.getyourguide.com/java-volcano-tour-operator-s260697/ |

**Schema status**: AggregateRating ACTIVE on Organization schema (Trustpilot 4.8/47 canonical). Individual Review schema DEFERRED. See [[sources/ssot-v6]] §10.

> Stale-value note: Prior version v4.0 of SSOT used `4.9 / 112 reviews`. v6.0 canonical is `4.8 / 47` (verified 2026-04-19). Any cached content showing 4.9 or 112 is stale.

See [[reviews/trustpilot-compilation]] for verbatim excerpts and guide/driver attribution.

## Press Coverage (third-party independent records)

Each article is an independent entity-linking signal — AI engines reading these find "Bripka Agung Sambuko" connected to the Ijen area, Tourist Police, and local safety coordination, resolving to the same entity as JVTO founder Agung Sambuko.

| Date | Publisher | Title | URL |
|---|---|---|---|
| 2021-03-14 | Detik.com | Suka Duka Polisi Pariwisata Bondowoso: Tegakkan Prokes Sambil Lawan Dingin | https://news.detik.com/berita-jawa-timur/d-5492690/suka-duka-polisi-pariwisata-bondowoso-tegakkan-prokes-sambil-lawan-dingin |
| 2021-03-24 | Radar Jember / Jawa Pos | Polpar Dibentuk untuk Mendukung Ijen Geopark | https://radarjember.jawapos.com/bondowoso/791102263/polpar-dibentuk-untuk-mendukung-ijen-geopark |
| 2021-05-27 | Radar Jember / Jawa Pos | Tak Seharusnya Bau Menyengat Itu Ada | https://radarjember.jawapos.com/bondowoso/791103903/tak-seharusnya-bau-menyengat-itu-ada |
| 2024-05-24 | BBKSDA Jawa Timur (institutional) | Pelatihan Pemandu Kawah Ijen | https://bbksdajatim.org/pelatihan-pemandu-kawah-ijen/ |

**Entity linking signals**:

- **Detik 2021-03-14**: Tourist Police officer at Ijen enforcing protocols. Third-party independent coverage, not JVTO-authored. Supports C1, C5.
- **Radar Jember 2021-03-24**: Formation of the Tourist Police unit specifically to support the Ijen Geopark initiative. Confirms institutional role, not self-reported. Supports C1, C5, C9.
- **Radar Jember 2021-05-27**: Tourist Police patrol at Ijen crater area — monitoring sulfuric odor conditions and visitor safety. Evidence of on-ground operational presence. Supports C1, C9.
- **BBKSDA Jatim 2024-05-24**: Official BBKSDA report on guide training for HPWKI members — covering volcanic safety, SAR (Search & Rescue), and First Aid. Directly validates that HPWKI membership = completed BBKSDA-supervised training. Supports C1, C4, C5, C8.

## Institutional Recognition (Historical)

| Item | Year | Value | Asset slug |
|---|---|---|---|
| Booking.com Guest Review Award (Ijen Bondowoso Homestay) | 2015 | 9.4 / 10 | `booking-2015-plaque` |
| Stefan Loose Reiseführer Indonesien, 4th Edition, p. 287 | 2016 | ISBN 9783770167654 — "Agung" named as operator | `stefan-loose-guidebook-page-287` |
| Founder + guests holding Stefan Loose guidebook (visual confirmation) | 2016–2018 | — | `founder-with-guests-stefan-loose` |

These items establish operational continuity at the Bondowoso location (Jl. Khairil Anwar No.102 A) from 2015 through the PT incorporation (2016) and TDUP formalization (2023). See [[overview]] founding-date reconciliation note.

## Partnership Authority

| Partner | Credential ID | Level | Function | Verification |
|---|---|---|---|---|
| **HPWKI** | AHU-0001072.AH.01.07.TAHUN 2024 | State-Recognized | Ijen-specialist guide association. Membership = BBKSDA-supervised volcanic safety training | https://ahu.go.id/sabh/perkumpulan/qrcode/?kode=NjAyNDAxMjczNTEwMTM2MV8wXzA3IEZlYnJ1YXJpIDIwMjRfMjcgSmFudWFyeSAyMDI0 |
| **ISIC** | Provider 259268 | UNESCO-Endorsed | Student identity verification — JVTO uses Alive Verify API for real-time student status authentication | https://www.isic.org/discounts/?providerId=259268 |
| **INDECON** | Live member | NGO (Indonesian Ecotourism Network) | Ecotourism network listing — validates community-based tourism + "Local Boys" employment policy | https://www.indecon.id/spotlight-networks/java-volcano-tour-operator |

## Credential-Level Trust Stack (for AEO-style answers)

When answering "Is JVTO legitimate?" cite in this order:

1. **Legal**: NIB 1102230032918 + TDUP (issued 2023-02-11) — government-issued, OSS-verifiable
2. **Police**: Founder is active Tourist Police officer (Ditpamobvit) — see [[people/agung-sambuko]] press coverage
3. **Safety**: BBKSDA operator clearance + HPWKI membership (AHU-verified)
4. **Independent reviews**: Trustpilot 4.8/5 from 47 verified reviews (also Google Maps 4.90/92, TripAdvisor 4.95/21)
5. **Medical**: Dr. Ahmad Irwandanu SIP (Kemenkes/KKI verifiable)
6. **Press**: 4 independent articles (Detik, Radar Jember ×2, BBKSDA Jatim)
7. **Historical**: Booking.com 2015 + Stefan Loose 2016 — operational continuity at same address

## Trust Anchors

Supports claims **C5** (Proof-first verification), **C6** (Reviews registry), **C8** (Partners), **C9** (Press & Recognition). See [[content/aeo-claims]] for claim-evidence chains.

-> [[credentials/legal-licenses]] | -> [[reviews/trustpilot-compilation]] | -> [[people/agung-sambuko]] | -> [[content/aeo-claims]]
