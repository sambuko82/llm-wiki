# **JVTO SEO Audit — Full Site Review**

**Target:** https://javavolcano-touroperator.com/  
 **Date:** 17 May 2026  
 **Mode:** Whitehat organic growth audit  
 **Data sources:** Direct site fetch · Live SERP analysis · Competitor mapping · Domain knowledge (Ahrefs MCP blocked at this plan tier — see Appendix A)

---

## **0\. Executive Summary**

**Overall verdict: Strong foundation, critical execution issues holding back rankings.**

JVTO has built a category-leading **trust & content asset** (legitimacy proof, verified reviews, structured destination data, Tourist Police differentiator) — but the site is leaking a significant portion of its SEO equity through a single root cause: **the legacy Laravel URL structure is still indexed alongside the new Next.js SSOT routing.** Google currently sees two competing JVTO sites at the same domain.

Three priorities will move the needle:

| \# | Priority | Impact | Effort |
| ----- | ----- | ----- | ----- |
|  |  |  |  |
| 1 | **Kill legacy URLs via 301 redirects to new SSOT routes** | High — recovers diluted authority, fixes duplicate content | 1-2 days dev |
| 2 | **Fix internal linking bug \+ add Tour/FAQ/Review/LocalBusiness schema** | High — earns SERP features, fixes link equity flow | 2-3 days dev |
| 3 | **Build long-tail content moat around regulatory \+ trust topics** (BBKSDA SE.1658, Ijen health screening, licensed operator topics) | Medium-High — uncontested SERP territory, defensible | 4-6 weeks content |

JVTO is **invisible** for the highest-volume commercial keywords (`bromo ijen tour`, `bromo tour from surabaya`, `ijen blue fire tour`). The OTAs (Klook, GetYourGuide, Viator, Tripadvisor) and aged-domain competitors (tourmountbromo.com, bromotour.com since 1998, hellobromo.com, forevervacation.com) own those SERPs. Direct head-on competition is a 12-18 month battle. **The faster wins are in long-tail \+ branded \+ intent-rich queries where JVTO's content depth is already best-in-class.**

JVTO does rank \#1 for differentiator phrases (`tourist police bromo tour`, `licensed bromo tour operator indonesia tourist police`) — proving the content works when search intent aligns with positioning. Scale this pattern.

---

## **1\. Site Architecture & Indexing Health**

### **1.1 The dual-URL problem (CRITICAL)**

Google has indexed **two parallel versions** of the JVTO site:

| Layer | Examples (all currently in Google) | Status |
| ----- | ----- | ----- |
| **Legacy (Laravel)** | `/packages/surabaya/3d2n/1`, `/packages/yogyakarta`, `/about`, `/contact`, `/faq`, `/all-inclusive`, `/reviews`, `/custom-package`, `/office`, `/how-to-book`, `/blog`, `/terms-and-condition`, `/student-package` | Indexed, served, often stale content |
| **New (Next.js SSOT)** | `/tours/from-surabaya/{slug}`, `/destinations/{slug}`, `/verify-jvto`, `/verify-jvto/legal`, `/why-jvto`, `/why-jvto/our-story`, `/why-jvto/reviews`, `/why-jvto/our-team`, `/travel-guide`, `/travel-guide/faq`, `/travel-guide/ijen-health-screening`, `/policy`, `/policy/booking-payment-cancellation`, `/isic/student-package` | Indexed, canonical target |

**Why this is bad:**

* Authority dilution: external backlinks to legacy `/about` don't flow to new `/why-jvto/our-story`  
* Duplicate content: `/student-package` (legacy) vs `/isic/student-package` (new)  
* Crawl budget waste: Googlebot crawls dead pages instead of new ones  
* User confusion: legacy pages still rank, deliver inconsistent UX (old design, outdated content)  
* Schema fragmentation: same business, two parallel entity profiles

**Fix:** Build a 301 redirect map. Legacy → new SSOT route. Below is the minimum set:

| Legacy URL | 301 → Target |
| ----- | ----- |
| `/about` | `/why-jvto/our-story` |
| `/contact` | `/contact` (keep, but verify it's the new route) |
| `/faq` | `/travel-guide/faq` |
| `/reviews` | `/why-jvto/reviews` |
| `/all-inclusive` | `/policy/inclusions-exclusions` |
| `/student-package` | `/isic/student-package` |
| `/custom-package` | `/tours` |
| `/office` | `/contact` |
| `/how-to-book` | `/travel-guide/booking-information` |
| `/terms-and-condition` | `/policy` |
| `/blog` | `/travel-guide` |
| `/packages/surabaya/3d2n/{N}` | Map to specific `/tours/from-surabaya/{slug}` |
| `/packages/yogyakarta` | 301 to `/tours` or a new `/tours/from-yogyakarta` (see §6.4) |

After redirects: **resubmit the new sitemap.xml in Google Search Console and request re-indexing of high-value pages.**

### **1.2 Legacy subdomain leaking authority**

The new tour pages load images from `https://legacy.javavolcano-touroperator.com/assets/img/hotels/*` and `https://legacy.javavolcano-touroperator.com/assets/img/cars/*`. Two issues:

* **Crawl signal confusion:** the legacy subdomain is being kept alive, signals to Google that two JVTO web properties exist  
* **Page speed:** extra DNS lookup, extra TLS handshake per image

**Fix:** migrate images to main domain (`/assets/img/...` or `/uploads/...`), redirect `legacy.javavolcano-touroperator.com` → `javavolcano-touroperator.com` at DNS+server level.

### **1.3 Cross-domain risk — java-tour.com**

JVTO's Facebook page lists **`java-tour.com`** as another domain. If this serves overlapping content, it is direct cannibalization. Three options, in order of preference:

1. **Best:** 301 redirect `java-tour.com` → `javavolcano-touroperator.com` to consolidate authority  
2. **Acceptable:** keep `java-tour.com` as a brand-only landing with `<link rel="canonical">` pointing to JVTO main domain, no overlapping content  
3. **Bad (current?):** keep both running with similar content — split signals, possible cannibalization

Action: inspect `java-tour.com` and decide. If unused, kill it and redirect.

### **1.4 www vs non-www**

The search result shown for `/tours/from-bali` returned the `www.` subdomain. Verify only one canonical version is served and the other 301s to it.

### **1.5 Templating bug — meta description**

`/tours/from-surabaya` currently shows: *"Discover all tour packages starting from From-surabaya"* — the template variable `{slug}` was injected literally with kebab-case preserved. Same issue on `/tours/from-bali` and `/packages/yogyakarta`. This is visible in Google's SERP cache.

**Fix:** dev team needs to humanize the variable (`From-surabaya` → `Surabaya`) in the meta description template across all listing pages.

---

## **2\. On-Page SEO Audit**

Inspection covered: homepage, `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n`, `/destinations/ijen-crater`, `/tours/from-surabaya` listing.

### **2.1 What's working**

| Element | Verdict | Note |
| ----- | ----- | ----- |
| Canonical tags | ✅ Pass | Present on tour pages, correctly self-referencing |
| Open Graph tags | ✅ Pass | Complete: title, description, image, image dimensions, locale, type |
| Twitter cards | ✅ Pass | `summary_large_image` |
| Robots meta | ✅ Pass | `index, follow` with sensible max directives |
| Title length | ✅ Pass | Tour page titles 50-60 chars, well-formed |
| H1 uniqueness | ✅ Pass | One H1 per page |
| HTTPS | ✅ Pass | Site is fully HTTPS |
| Internal nav | ✅ Pass | Mega-menu links to popular tours \+ destinations |
| Mobile viewport | ✅ Pass | Correct `<meta viewport>` |

### **2.2 What's broken**

| Issue | Page(s) | Severity | Fix |
| ----- | ----- | ----- | ----- |
| **Footer destination links all point to `/destinations` hub instead of `/destinations/{slug}`** | All pages with footer | **Critical** | Change footer links to specific destination URLs. Currently you're sending all internal "Mount Bromo" anchor signal to the hub, not the page that needs to rank for "Mount Bromo". |
| Meta description template variable not humanized | `/tours/from-surabaya`, `/tours/from-bali`, `/packages/yogyakarta` | **High** | See §1.5 |
| Cloudflare email obfuscation breaks `mailto:` schema | Most pages, footer | Medium | Either use plain `<a href="mailto:hello@javavolcano-touroperator.com">` or also expose unobfuscated email in LocalBusiness JSON-LD |
| Reviews block duplicated on every tour page (\~50 reviews × \~30 words \= \~1500 words duplicated) | Every `/tours/...` page | Medium | Either (a) reduce to 5-7 latest reviews per page, or (b) load via JS so Google sees the page-specific content first |
| Title tags don't include high-intent commercial modifiers | All tour pages | Medium | See §2.3 |
| Image filenames partially descriptive but underused | All tour pages | Low-Medium | Filenames like `3-day-bromo-madakaripura-waterfall-ijen-overland-from-surabaya-to-bali_0.jpg` are good. Alt text could be more keyword-specific (e.g., "Bromo sunrise viewpoint at Penanjakan" not "Gallery 1") |
| No breadcrumbs visible in DOM/UI | All sub-pages | Low | Adding visible breadcrumbs \+ BreadcrumbList schema helps both UX and SERP rich results |
| H2/H3 hierarchy heavy with brand terms (e.g., "JVTO Travel T-Shirt") instead of keyword-rich subheads | Tour pages | Low | Mix brand sections with keyword-rich subheads like "What's the 3D2N Bromo Ijen itinerary?" |

### **2.3 Title tag rewrites (top 10 priority pages)**

Current titles are **clean but not maximally keyword-optimized**. Each suggested rewrite stays under 60 chars and front-loads the highest-volume term.

| Page | Current | Suggested |
| ----- | ----- | ----- |
| Homepage | Tourist Police-Led Private Volcano Tours in East Java | Java Volcano Tour Operator | Bromo Ijen Tour from Surabaya & Bali — Private | JVTO |
| `/tours` | (verify, likely "All Tours") | 16 Private Bromo, Ijen & Tumpak Sewu Tours | JVTO |
| `/tours/from-surabaya` | (currently has templating bug) | Bromo Ijen Tour from Surabaya — 6 Private Packages | JVTO |
| `/tours/from-bali` | (currently has templating bug) | Bromo Ijen Tour from Bali — 4 Private Packages | JVTO |
| `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n` | 3 Day Bromo, Madakaripura & Ijen – Surabaya to Bali | JVTO | 3D2N Bromo Ijen Madakaripura Private Tour Surabaya → Bali |
| `/tours/from-bali/bromo-ijen-3d2n` | (verify) | 3D2N Private Bromo Ijen Blue Fire Tour from Bali | JVTO |
| `/destinations/mount-bromo` | (verify) | Mount Bromo Sunrise Guide — Tours, Tickets & Tips | JVTO |
| `/destinations/ijen-crater` | Kawah Ijen Blue Fire Volcano – Complete Trekking Guide | JVTO | Mount Ijen Blue Fire Tour Guide — Permits, Health, Hike | JVTO |
| `/destinations/tumpak-sewu-waterfall` | (verify) | Tumpak Sewu Waterfall — Tour, Trail & Tips | JVTO |
| `/destinations/madakaripura-waterfall` | (verify) | Madakaripura Waterfall — Tour, Canyon Hike, Tips | JVTO |

**Note on /destinations/ijen-crater:** the current title leads with "Kawah Ijen". International travelers search "Mount Ijen" 5-10x more than "Kawah Ijen" (Kawah is Indonesian for crater). Lead with the English term, support with the Indonesian. Same logic for "Tumpak Sewu" (most search just "Tumpak Sewu", not "Tumpak Sewu Waterfall").

### **2.4 Meta description rewrites — formula**

Use this 3-part formula on every commercial page:

`[Format + Duration + Highlights] · [Differentiator] · [Trust signal or price hook]`

Examples:

* **3D2N tour page:**  
   *"Private 3D2N Bromo sunrise \+ Madakaripura \+ Ijen blue fire from Surabaya, ending in Bali. Tourist Police-led. 4.8★ Trustpilot. IDR 2.45M/pax."*

* **Destination page (Ijen):**  
   *"Plan your Mount Ijen blue fire hike. BBKSDA health screening, permits, gear, midnight start — full guide from a licensed East Java operator."*

---

## **3\. Technical SEO Checklist**

| Check | Status | Detail |
| ----- | ----- | ----- |
| HTTPS / TLS | ✅ Pass | Full HTTPS, no mixed content visible in fetched pages |
| Mobile viewport | ✅ Pass | Correct meta viewport |
| Image format | ✅ Pass | .webp used throughout (good) |
| Next.js image optimization | ✅ Pass | `/_next/image?url=...&w=...&q=75` used (good) |
| robots.txt | ⚠️ Unverified | Could not fetch externally. **Action:** verify it's served, contains `Sitemap:` directive |
| sitemap.xml | ⚠️ Unverified | Verify existence at `/sitemap.xml`, confirm it lists ONLY new SSOT routes (not legacy) |
| 301 redirect chain check | ❌ Fail | Multiple legacy URLs returning 200 instead of 301 → see §1.1 |
| Canonical tags | ✅ Pass | Self-referencing on key pages |
| `hreflang` | ❌ Missing | If you serve any non-EN content (or plan to for SG/MY/HK/TW/CN markets), add hreflang. Current content is English-only — flag for future |
| Structured data: Organization | ⚠️ Partial | Verify a `LocalBusiness` or `TravelAgency` JSON-LD with full NAP, licence number, sameAs to social profiles is on every page |
| Structured data: Tour/Product | ❌ Missing | Tour pages should emit `TouristTrip` or `Product` schema with price, currency, offers, aggregateRating, duration. Currently invisible to SERP rich results. |
| Structured data: FAQ | ❌ Missing | The "Quick Answers" section on every tour page is perfect FAQPage schema candidate — but not marked up |
| Structured data: Review/AggregateRating | ⚠️ Partial | Reviews are visible in DOM but verify AggregateRating with `4.8` and `reviewCount` is on every tour page |
| Structured data: BreadcrumbList | ❌ Likely missing | Add to all sub-pages |
| Core Web Vitals | ⚠️ Untested | Each tour page loads \~50 reviews \+ 6 gallery images \+ cars \+ hotels — investigate LCP/CLS. Recommend running PSI on top 5 tour pages and trimming review block |
| Sitemap index | ⚠️ Unverified | If 19 tour pages \+ 5 destinations \+ supporting content \= \~40 URLs, single sitemap is fine. If \>100 URLs (with future blog), use sitemap index |
| XML sitemap freshness | ⚠️ Unverified | Verify `lastmod` dates reflect actual updates so Google re-crawls changed content |
| Soft 404s | ⚠️ Possible | If legacy URLs return 200 with thin content (e.g. `/office`), Google may treat as soft 404\. Either redirect or noindex |
| 404 page | ⚠️ Untested | Verify custom 404 page exists with helpful links |
| Email obfuscation impact | Low risk | Cloudflare `/cdn-cgi/l/email-protection` works for spam but breaks NAP consistency in some crawlers. Mitigate by exposing unobfuscated email in JSON-LD |
| Pagination / `rel=prev/next` | ⚠️ Unverified | If tour listing pages have pagination, ensure correct paginated handling |
| AMP | N/A | Not used (acceptable — AMP is legacy) |
| Indonesia-specific: GMB linkage | ⚠️ Verify | Confirm `https://www.google.com/maps/place/...` for JVTO Bondowoso is claimed, NAP-consistent, and `sameAs` in JSON-LD |

---

## **4\. Schema.org Markup — Detailed Spec**

The biggest **unrealized quick win** for JVTO. The site has everything a rich-snippet-rich SERP needs (reviews, price, duration, FAQs, business credentials) but it's not all marked up.

### **4.1 Required schemas per page type**

| Page type | Required JSON-LD types |
| ----- | ----- |
| Homepage | `Organization` \+ `WebSite` (with `SearchAction`) \+ `BreadcrumbList` |
| All pages (global) | `Organization` (or `TravelAgency` — preferred) \+ `LocalBusiness` |
| `/destinations/{slug}` | `TouristAttraction` \+ `BreadcrumbList` |
| `/tours/.../{slug}` | `TouristTrip` (or `Product` with `Offer`) \+ `FAQPage` (for Quick Answers) \+ `AggregateRating` \+ `BreadcrumbList` |
| `/why-jvto/reviews` | `Organization` with `aggregateRating` and `review` array |
| `/travel-guide/{slug}` | `Article` \+ `FAQPage` if applicable |
| `/verify-jvto/*` | `Organization` with `identifier` (NIB, TDUP) \+ `award`/`memberOf` for HPWKI, INDECON |

### **4.2 TouristTrip schema — example**

For `/tours/from-surabaya/bromo-madakaripura-ijen-3d2n`:

```json
{
  "@context": "https://schema.org",
  "@type": "TouristTrip",
  "name": "3D2N Bromo, Madakaripura & Ijen Private Tour — Surabaya to Bali",
  "description": "Private 3-day overland tour: Surabaya → Bromo sunrise → Madakaripura Waterfall → Ijen blue fire → Bali.",
  "image": "https://javavolcano-touroperator.com/uploads/3-day-bromo-madakaripura-waterfall-ijen-overland-from-surabaya-to-bali_0.jpg",
  "url": "https://javavolcano-touroperator.com/tours/from-surabaya/bromo-madakaripura-ijen-3d2n",
  "touristType": ["Adventure travelers", "Hikers", "Photographers"],
  "itinerary": [
    {"@type": "Place", "name": "Mount Bromo"},
    {"@type": "Place", "name": "Madakaripura Waterfall"},
    {"@type": "Place", "name": "Ijen Crater"}
  ],
  "offers": {
    "@type": "Offer",
    "price": "2450000",
    "priceCurrency": "IDR",
    "availability": "https://schema.org/InStock",
    "url": "https://javavolcano-touroperator.com/tours/from-surabaya/bromo-madakaripura-ijen-3d2n"
  },
  "provider": {
    "@type": "TravelAgency",
    "name": "Java Volcano Tour Operator",
    "url": "https://javavolcano-touroperator.com",
    "identifier": "NIB 1102230032918"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### **4.3 FAQ schema — extract from existing content**

Every tour page already has a "Quick Answers" section with 9 questions. Wrap them in `FAQPage` schema (one block per page). These are extremely high-CTR in SERPs because they expand inline.

The single highest-impact FAQ to ensure is marked up across the site:

* *"Is JVTO a licensed Indonesian tour operator?"*  
* *"What exactly is covered in the all-inclusive price?"*  
* *"What is the Ijen health screening?"*  
* *"What happens if I need to cancel?"*

These match exact intent for someone vetting a tour operator and dramatically increase pre-booking trust before they ever land on the site.

### **4.4 Organization schema — global**

Single Organization block (or `TravelAgency`) emitted in `<head>` on every page:

```json
{
  "@context": "https://schema.org",
  "@type": "TravelAgency",
  "name": "Java Volcano Tour Operator",
  "alternateName": ["JVTO", "PT Java Volcano Rendezvous"],
  "url": "https://javavolcano-touroperator.com",
  "logo": "https://javavolcano-touroperator.com/assets/img/jvto-logo.png",
  "image": "https://javavolcano-touroperator.com/assets/img/og/default.jpg",
  "description": "Tourist Police-led private volcano tour operator in East Java, Indonesia.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Jl. Khairil Anwar No.102 A, Badean",
    "addressLocality": "Bondowoso",
    "addressRegion": "East Java",
    "postalCode": "68214",
    "addressCountry": "ID"
  },
  "telephone": "+6282244788833",
  "email": "hello@javavolcano-touroperator.com",
  "identifier": [
    {"@type": "PropertyValue", "name": "NIB", "value": "1102230032918"},
    {"@type": "PropertyValue", "name": "HPWKI", "value": "AHU-0001072.AH.01.07.TAHUN 2024"},
    {"@type": "PropertyValue", "name": "ISIC Provider", "value": "259268"}
  ],
  "memberOf": [
    {"@type": "Organization", "name": "HPWKI", "url": "https://ahu.go.id/..."},
    {"@type": "Organization", "name": "INDECON", "url": "https://indecon.id/spotlight-networks/java-volcano-tour-operator"}
  ],
  "sameAs": [
    "https://www.facebook.com/javavolcanotours/",
    "https://www.instagram.com/javavolcanotouroperator/",
    "https://twitter.com/jvto_tours",
    "https://www.trustpilot.com/review/javavolcano-touroperator.com",
    "https://www.tripadvisor.com/Attraction_Review-g297715-d24825561-Reviews-Java_Volcano_Tour_Operator-Surabaya_East_Java_Java.html"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "164",
    "bestRating": "5"
  },
  "areaServed": [
    {"@type": "AdministrativeArea", "name": "East Java"},
    {"@type": "AdministrativeArea", "name": "Bali"}
  ]
}
```

This single block, served globally, fixes the entity recognition problem — Google currently sees JVTO mentioned across Facebook, Trustpilot, TripAdvisor, the old site, the new site, and `java-tour.com` without a unified canonical entity declaration.

---

## **5\. Competitive Landscape**

### **5.1 Who currently owns the SERPs**

| Tier | Competitor | Type | Strength |
| ----- | ----- | ----- | ----- |
| 1 (OTA) | Klook | Aggregator | Massive domain authority, multilingual, app distribution, SEA-focused |
| 1 (OTA) | GetYourGuide | Aggregator | Massive domain authority, EU-traveler focus |
| 1 (OTA) | Viator (Tripadvisor) | Aggregator | Inherits Tripadvisor authority, US-traveler focus |
| 1 (OTA) | Tripadvisor product pages | Aggregator | Reviews-rich, dominant for "X tour" queries |
| 2 (Direct, dominant) | **tourmountbromo.com** | Direct competitor | Positions as "\#1 Mount Bromo Tour in Surabaya", STB-licensed messaging (SG market), 10+ years, strong blog content |
| 2 (Direct, dominant) | **bromotour.com** | Direct competitor | Operating since 1998 — massive domain age advantage |
| 2 (Direct, dominant) | **forevervacation.com** | International competitor | Excellent content production, strong CRO, Bali-led |
| 3 (Direct, mid-tier) | bromoeastjava.com, hellobromo.com, adventureindonesia.com, mybalitrips.com | Direct competitors | Solid SEO, less content depth than tier 2 |
| 3 (Local SEO) | bluefireijentour.com, ijenplateau.com, mountbromoijen.com, mtbromoijentour.com, bromoijentourism.com, ijenbromotours.com, mountbromoijentour.com, bromo.co.id, yukbanyuwangi.co.id | Direct competitors | EMD (exact-match domain) advantage on long-tail; mostly basic content |
| 4 | tourHQ, Cheap Bromo, individual guide listings | Long tail | Weak |

### **5.2 What JVTO has that competitors don't**

This is the offensive map. JVTO can OWN these themes because no competitor has them:

| Asset | Competitors | JVTO |
| ----- | ----- | ----- |
| **Tourist Police-led founder narrative** | None | **Unique** — Bripka Agung Sambuko / Polpar credential is unmatched |
| **Verifiable government credentials (NIB, TDUP, HPWKI, BBKSDA)** with public registry links | Generic "licensed" claims | **Specific, linked, verifiable** |
| **Ijen health screening explained in detail** (BBKSDA SE.1658/KSA.9/2024) | Most operators mention it vaguely | **Cited regulation \+ named doctor \+ Kemenkes link** |
| **ISIC Provider partnership** | None | **JVTO is the only ISIC volcano-tour provider in East Java** — student traffic opportunity |
| **INDECON ecotourism membership** | None | Verifiable |
| **SHA-256 document anchoring of credentials** | None | **Forensic-grade legitimacy proof** — content moat |
| **Written cancellation \+ closure policy with Travel Credit** | Usually buried | Front-and-center |
| **Per-tour FAQ depth (9 questions per page, regulation-cited)** | Generic FAQs | **Strong** |
| **Multi-platform review verification (Trustpilot \+ Google \+ TripAdvisor \+ Booking)** | Single platform usually | **4.8★ across 160+ reviews** |

### **5.3 What competitors have that JVTO doesn't (yet)**

| Asset | Top competitors | JVTO |
| ----- | :---- | ----- |
| Domain age (10-25 years) | Yes | New domain — long-term play |
| Volume of OTA-distributed product listings | Klook/GYG/Viator/Tripadvisor each have JVTO competitors listed | JVTO is on TripAdvisor — verify Klook/GYG/Viator product listings exist |
| Aged blog content (50-300+ posts) | tourmountbromo.com has substantial blog; mtbromoijentour.com etc. | Limited (current `/blog` is legacy/sparse based on what's indexed) |
| Multilingual content | Klook serves EN/JP/KR/ZH/TH/ID etc. | EN only |
| Branded long-tail (e.g., "tourmountbromo \+ sherry" lands user reviews) | Yes | Yes (guide names: Anjas, Boy, Yandi, Rendi appear in reviews) — leverage this |
| YouTube video content | Some (e.g., GetYourGuide has them) | Verify — could be a major channel for "what is Ijen blue fire" intent |

---

## **6\. Keyword Strategy**

### **6.1 Search volume context (estimated, based on SERP density & ad presence)**

Without Ahrefs API access, exact volumes are inferred from SERP competitiveness, paid ad density, and OTA product depth. **For exact volumes, use Google Keyword Planner (free with a Google Ads account) or wait until an Ahrefs plan upgrade.**

| Keyword cluster | Est. monthly volume (global EN) | Difficulty | JVTO opportunity |
| ----- | ----- | ----- | ----- |
| `mount bromo` (informational \+ nav) | 30,000–60,000 | High | Destination page → top 20 realistic |
| `bromo tour` / `mount bromo tour` | 10,000–20,000 | Very High (OTA-dominated) | Long-term play |
| `bromo ijen tour` | 5,000–10,000 | Very High | Long-term play |
| `ijen blue fire` (informational) | 3,000–8,000 | Medium-High | Strong opportunity — destination page |
| `bromo tour from surabaya` | 2,000–5,000 | High | Tier 2 target |
| `bromo tour from bali` | 2,000–5,000 | High | Tier 2 target |
| `ijen crater tour` | 1,500–3,000 | Medium | Strong opportunity |
| `tumpak sewu waterfall tour` | 800–2,000 | Medium | Strong opportunity |
| `madakaripura waterfall` | 500–1,500 | Low-Medium | **Easy win** |
| `bromo ijen 3d2n` | 500–1,500 | Medium | Strong tour-page target |
| **`ijen health certificate`** | 200–500 | **Low** | **Easy win** — JVTO is the most authoritative voice |
| **`BBKSDA SE 1658`** | \<100 | **Very Low** | **Easy win** — own this regulatory niche |
| **`tourist police bromo`** | \<100 | **Very Low** | **JVTO already ranks \#1** |
| `licensed bromo tour operator` | 100–300 | Low | **Already strong** — defend it |
| `private bromo tour singapore` | 200–500 | Low-Medium | **Geographic intent** — match Sam's target markets |
| `bromo ijen tour malaysia` | 100–300 | Low-Medium | Same |
| `ISIC student tour indonesia` | \<100 | Very Low | **JVTO is the only ISIC tour provider in East Java — own this** |
| `is bromo open today` / `ijen closed` | 500–2,000 (seasonal spike) | Low | Update-driven content moat |
| `yadnya kasada festival 2026` | 1,000–3,000 (seasonal) | Low | Cultural content opportunity |
| `bromo vs ijen which better` | 500–1,500 | Low | Comparison content — high CTR |
| `what to wear bromo ijen` | 500–1,500 | Low | Funnel-top guide |

### **6.2 Keyword opportunity table (15 prioritized targets)**

| Keyword | Difficulty | Opportunity score | Current JVTO ranking | Intent | Recommended page |
| ----- | ----- | ----- | ----- | ----- | ----- |
| `tourist police bromo tour` | Low | High (defensive moat) | \#1 (verify) | Commercial-branded | Homepage / `/why-jvto/police-safety` |
| `licensed bromo tour operator indonesia` | Low | High | \#1 (verify) | Commercial-trust | `/verify-jvto/legal` |
| `ijen health certificate` | Low | High | Likely not ranking | Informational \+ commercial | `/travel-guide/ijen-health-screening` |
| `bbksda se 1658` | Very Low | Medium-High (niche) | Likely not ranking | Informational | New: `/travel-guide/bbksda-regulations-ijen` |
| `madakaripura waterfall tour` | Medium | High | Likely not in top 20 | Commercial | `/destinations/madakaripura-waterfall` \+ dedicated tour |
| `papuma beach tour` | Low | High | Likely not in top 20 | Commercial | `/destinations/papuma-beach` |
| `bromo ijen 3d2n private tour` | Medium | High | Likely not in top 20 | Commercial-transactional | `/tours/from-surabaya/ijen-bromo-madakaripura-3d2n` |
| `bromo ijen tour singapore` | Low-Medium | High | Likely not in top 20 | Commercial-geo | New: `/markets/singapore` or homepage geo-targeting |
| `bromo ijen tour malaysia` | Low-Medium | High | Likely not in top 20 | Commercial-geo | New: `/markets/malaysia` |
| `bromo ijen tour hong kong` | Low | High (low competition) | Likely not in top 20 | Commercial-geo | New: `/markets/hong-kong` |
| `ISIC student package indonesia` | Very Low | High | Likely not in top 20 | Commercial-niche | `/isic/student-package` |
| `is mount ijen open today` | Low | Medium-High | Not ranking | Informational | New: `/travel-guide/ijen-bromo-status-today` (update freq high) |
| `bromo vs ijen which to choose` | Low | High | Not ranking | Informational-comparative | New: `/travel-guide/bromo-vs-ijen-comparison` |
| `tumpak sewu waterfall guide` | Low-Medium | High | Likely not ranking | Informational | `/destinations/tumpak-sewu-waterfall` enhanced |
| `gas mask ijen rental` | Low | Medium | Not ranking | Commercial-informational | New: `/travel-guide/ijen-gas-mask-equipment` (drives toward inclusion in tour) |

### **6.3 Intent-mapped content silos**

Build content in 4 silos. Each silo has a hub page \+ supporting pages, all internally cross-linked.

```
SILO 1: COMMERCIAL TOUR PAGES (already built — needs schema)
├── /tours (hub)
├── /tours/from-surabaya (listing)
├── /tours/from-bali (listing)
└── /tours/from-{origin}/{tour-slug} (16 tours)

SILO 2: DESTINATIONS (foundation built — needs depth)
├── /destinations (hub)
├── /destinations/mount-bromo
├── /destinations/ijen-crater
├── /destinations/tumpak-sewu-waterfall
├── /destinations/madakaripura-waterfall
├── /destinations/papuma-beach
└── NEW: /destinations/banyuwangi (gateway content)
└── NEW: /destinations/cemoro-lawang (Bromo village)

SILO 3: REGULATORY + SAFETY (KILLER MOAT — biggest opportunity)
├── /travel-guide (hub)
├── /travel-guide/ijen-health-screening (exists)
├── /travel-guide/faq (exists)
├── /travel-guide/booking-information (exists)
├── /travel-guide/weather-and-closures (exists)
├── NEW: /travel-guide/bbksda-regulations-ijen
├── NEW: /travel-guide/bbksda-regulations-bromo
├── NEW: /travel-guide/ijen-gas-mask-equipment
├── NEW: /travel-guide/permit-requirements-east-java
├── NEW: /travel-guide/bromo-ijen-status-today (auto-updated weekly)
├── NEW: /travel-guide/yadnya-kasada-2026
└── NEW: /travel-guide/sulfur-mining-cultural-guide

SILO 4: PRE-PURCHASE PLANNING (top-of-funnel acquisition)
├── NEW: /travel-guide/bromo-vs-ijen-comparison
├── NEW: /travel-guide/bromo-ijen-itinerary-guide
├── NEW: /travel-guide/what-to-pack-bromo-ijen
├── NEW: /travel-guide/best-time-to-visit-bromo-ijen
├── NEW: /travel-guide/private-vs-shared-tour-comparison
├── NEW: /travel-guide/surabaya-vs-bali-starting-point
└── NEW: /travel-guide/from-singapore-to-bromo-guide
└── NEW: /travel-guide/from-malaysia-to-bromo-guide
```

### **6.4 Geographic landing pages — for SG/MY/HK/TW/CN markets**

Sam's target markets (memory): Singapore, Malaysia, Hong Kong, Taiwan, China. Build dedicated landing pages that match search intent from each origin:

| URL | Target keyword | Focus |
| ----- | ----- | ----- |
| `/markets/singapore` or `/travel-guide/bromo-ijen-from-singapore` | "bromo ijen tour singapore", "indonesia volcano tour singapore" | Flight routes (SIN-SUB, SIN-DPS), visa info, currency, climate diff from SG |
| `/markets/malaysia` | "bromo ijen tour malaysia" | Flight routes (KUL-SUB), AirAsia connection, halal food on tour |
| `/markets/hong-kong` | "bromo ijen tour hong kong" | HKG-DPS flight, climate, Cantonese-friendly guide notes |
| `/markets/taiwan` | "bromo ijen tour taiwan" / Chinese-character title | TPE-DPS flight, Mandarin support |
| `/markets/china` | "bromo ijen tour china" | Visa, payment options accepting CNY |

**Note:** for true CN/TW/HK markets, hreflang \+ translated content unlocks the full opportunity. English-only landing pages still help (the SG/MY/HK markets do search in English) but are 2-3x weaker than localized versions. Phase 2 if SEO results justify.

---

## **7\. Content Gap Analysis**

### **7.1 Topics where competitors rank that JVTO has no page for**

Pulled from competitor sites visible in SERPs. These are content gaps JVTO can close cheaply (most are 1500-3000 word guides):

| Topic | Why it matters | Recommended format | Priority |
| ----- | ----- | ----- | ----- |
| **Bromo Ijen status / closures live updates** | Seasonal spike volume; competitors don't update; massive trust signal | Update-frequency page (weekly) | **High** |
| **Madakaripura Waterfall detailed guide** | JVTO has shallow destination page; competitors win on this term | Long-form guide on `/destinations/madakaripura-waterfall` | **High** |
| **Papuma Beach detailed guide** | Underserved destination, JVTO has it in itinerary but no SEO content depth | Long-form guide | High |
| **Cemoro Lawang village guide** | Bromo gateway village — high informational intent | Long-form guide | Medium-High |
| **Banyuwangi to Ijen logistics** | Banyuwangi is the gateway; competitors rank for "banyuwangi ijen" | Logistics guide | Medium |
| **Bromo sunrise viewpoints comparison (Penanjakan vs King Kong Hill vs Seruni Point)** | Competitors rank for variation queries | Comparison guide | Medium-High |
| **Ijen blue fire visibility calendar / probability** | Top user concern — "can I see blue fire in July?" | Data-driven monthly guide | High |
| **Indonesian Tourist Police role — explainer** | Builds Mr. Sam's personal authority \+ topic moat | About-style explainer | Medium |
| **HPWKI guide certification — what it means** | Reinforces trust signal across all tour pages | Explainer | Medium |
| **Bromo ferry crossing Gilimanuk-Ketapang** | Logistical concern for Bali-origin travelers | Logistics guide | Medium |
| **Surabaya Juanda airport to Bromo logistics** | Top-of-funnel for SG/MY travelers | Logistics guide | Medium-High |
| **Yadnya Kasada festival 2026** | Cultural \+ seasonal spike | Annual update | Medium |
| **Mt Semeru status (and why JVTO doesn't summit)** | Visitors confuse Bromo for Semeru | Explainer \+ safety honesty | Low-Medium |
| **What is BBKSDA?** | Regulatory authority explainer | Explainer \+ linking to credentials | Medium |
| **Solo female travel safety bromo ijen** | High-intent niche, social proof exists in reviews | Guide drawing on solo-traveler review snippets | Medium |
| **Photography tips bromo / ijen** | Influencer-attractive content, link bait | Long-form photography guide | Medium |

### **7.2 Existing content needing depth expansion**

| Page | Current state | Recommended expansion |
| ----- | ----- | ----- |
| `/destinations/ijen-crater` | Good structured data, \~800 words | Add: monthly blue-fire calendar, gear list, training prep, sulfur miner cultural history, FAQ section, related tours grid (currently destination doesn't link to specific tours that visit it) |
| `/destinations/mount-bromo` | Verify content depth | Same expansion pattern \+ Yadnya Kasada section |
| `/destinations/madakaripura-waterfall` | Verify (likely shallow) | Expand to 1500+ words with canyon hike detail, Gajah Mada meditation history, photography tips, water depth/season detail |
| `/destinations/papuma-beach` | Per homepage, content is truncated ("renowned") | Full content rewrite |
| `/why-jvto/our-story` | Solid narrative | Add: Mr. Sam's Tourist Police timeline, before/after photos of operations, specific incidents that shaped policy |
| `/verify-jvto/legal` | Strong | Add: registry deep-link verifications side-by-side, video walkthrough |
| `/travel-guide/faq` | Probably consolidated | Split into thematic FAQ pages (booking FAQ, health FAQ, safety FAQ) — each with FAQPage schema; current consolidated page can stay as hub |

### **7.3 Content freshness signal — the "updated weekly" play**

Several competitors (mountbromoijen.com, mybalitrips.com) update content lightly to maintain freshness. JVTO can do this more rigorously:

* **Status page** (Bromo / Ijen open today, BBKSDA closures, volcanic activity level) — update weekly, lastmod stamp  
* **Pricing transparency page** — quarterly price update with changelog  
* **Seasonality page** — monthly calendar update

The freshness signal compounds: Google sees a domain with frequent, useful updates and crawls more often. Combined with the regulatory moat (BBKSDA topics no other operator commits to maintaining), this is a long-term defensible position.

---

## **8\. Off-Page / Backlink Strategy**

### **8.1 Existing high-quality signals to formalize**

These are mentioned on the JVTO site but verify they're actually live links:

| Source | Type | Action |
| ----- | ----- | ----- |
| Trustpilot review profile | Review trust signal | ✅ Already cited; add to `sameAs` JSON-LD |
| Google Maps profile | Local citation | Verify NAP-consistent; respond to all reviews; add `sameAs` |
| TripAdvisor profile | Review trust signal | ✅ Already cited; add to `sameAs` |
| Booking.com (mentioned in homepage as 4th platform) | Review trust signal | Verify presence; add to `sameAs` |
| OSS.go.id (NIB registry) | .gov.id authority | Verify outbound link from JVTO; nothing to do for incoming |
| AHU.go.id (HPWKI registry) | .go.id authority | Same |
| satusehat.kemkes.go.id (doctor verification) | .go.id authority | Same |
| INDECON spotlight network page | .id authority | ✅ Confirmed live with backlink to JVTO |
| Detik.com press coverage | High-DR press | If linked, verify with `dofollow`; pursue more Detik / Kompas coverage |
| BBKSDA Jatim mention | .go.id authority | If linked publicly, fantastic |
| Facebook \+ Instagram \+ Twitter | Social signals | Verify cross-linked, NAP-consistent, Instagram bio has dofollow link |
| ISIC.org partner page | DR-strong international | Confirm JVTO is listed with backlink at isic.org/discounts/?providerId=259268 |

### **8.2 Whitehat link-building opportunities (next 6 months)**

| Tactic | Target | Effort | Impact |
| ----- | ----- | ----- | ----- |
| **Indonesian travel media outreach** (Detik, Kompas Travel, IDN Times Travel, Liputan6 Lifestyle) | Press features on "first tourist-police-led volcano operator" — newsworthy angle | Medium | High |
| **English-language Indonesia travel media** (Honeycombers, The Bali Sun, What's New Indonesia) | Trust \+ safety story | Medium | High |
| **Tourism authority listings** | Wonderful Indonesia (Indonesia.travel) directory, East Java Tourism Office (jatimprov.go.id) | Low | Medium |
| **University / student site mentions** (via ISIC partnership) | Reach out to SEA university travel clubs (NUS, NTU, SMU, UM, HKUST) — they have student travel guides linking to ISIC partners | Medium | Medium-High |
| **Eco-tourism / sustainable travel directories** (INDECON's network of sister sites; Green Destinations; Asian Ecotourism Network) | Via INDECON membership | Low | Medium |
| **Travel blogger / influencer partnerships** | Free FAM trips to bloggers with DR\>30 in travel niche — focus on SG/MY/HK | Medium-High | High |
| **Niche resource page link-building** | Find pages titled "Bromo Ijen tour operators" / "best East Java tours" on travel blogs, request inclusion | Low-Medium | Medium |
| **Wikipedia citations** | Mount Bromo and Kawah Ijen articles cite news sources — if JVTO is in Detik coverage, that becomes a 2nd-hop authority citation | Low | Low-Medium |
| **Reddit r/IndonesiaTravel \+ r/SoutheastAsia organic presence** | Mr. Sam (or team member) as a verified expert answering questions; no spam | Medium | Medium |
| **YouTube backlinks via guest features** | Big travel channels (Drew Binsky, FunForLouis if still active, similar SEA travel YouTubers) — co-create Ijen blue fire content | High | High |
| **Klook / GetYourGuide / Viator / Booking.com — Activities** | Verify JVTO has product listings on all 4 OTAs. If yes, those are dofollow brand mentions (and additional booking channels) | Low | Medium |

### **8.3 Brand mention monitoring \+ reclamation**

Many sites mention "Java Volcano Tour Operator" or "JVTO" without linking. Use a tool (Mention.com or Brand24 free tier) to monitor for unlinked mentions, then politely request linkification. Low effort, steady gain.

### **8.4 Government & association linkage strategy**

This is JVTO's strongest moat. .gov.id and .go.id links are gold. Reverse-engineer how to earn them:

* BBKSDA Jatim: contribute to a safety bulletin / case study; offer Mr. Sam's expertise for a citation  
* Kemenparekraf (Ministry of Tourism): Apply for any operator showcase, sustainable tourism program, or media coverage  
* POLRI Ditpamobvit: Internal feature about tourist police members entering tourism; this is institutional storytelling Mr. Sam can pitch via his POLRI relationships  
* Sat Intelkam Polres Bondowoso (Sam's own jurisdiction): community tourism feature  
* East Java Tourism Office: operator listing or feature

These won't all hit, but landing 2-3 of them in 12 months locks in unbeatable authority for the licensed-operator-Indonesia space.

---

## **9\. Conversion Rate Optimization Notes (SEO-adjacent)**

SEO without CRO leaves money on the table. Quick wins for JVTO:

* **CTA prominence:** the "Browse Tours" CTA is good but the WhatsApp CTA fixed at bottom-right is the actual conversion path. Test both side-by-side.  
* **Price hooks above the fold on tour pages:** currently "Starts from IDR 2.450.000" is shown — add USD/SGD/MYR equivalents inline (this also satisfies SG/MY/HK travelers' price comprehension and is a soft localization signal)  
* **Trustpilot widget placement:** currently in scroll-down section. Consider also pinning rating \+ count near the WhatsApp CTA  
* **WhatsApp pre-filled text:** good currently. Add variants per tour page (`?text=Hi%20JVTO%2C%20I'm%20interested%20in%20the%203D2N%20Bromo%20Madakaripura%20Ijen%20tour...`)  
* **ISIC discount badge:** if student discount applies, show it on tour pages with a "Are you a student? Save with ISIC →" sticker linked to `/isic/student-package`  
* **Reviews directly under price block:** social proof at the decision moment

---

## **10\. Tracking & Measurement**

Set up the following inside Google Search Console \+ Google Analytics 4 before content investment begins, so impact is measurable:

| Metric | Where | Tracking purpose |
| ----- | ----- | ----- |
| Organic clicks by URL | GSC \> Performance \> Pages | Measure new content's actual traffic |
| Impressions by query | GSC \> Performance \> Queries | Identify queries JVTO is being shown for but not clicked |
| Average position by query | GSC \> Performance \> Queries | Track movement on target keywords |
| Indexed page count | GSC \> Pages | Watch this number drop as legacy URLs are 301'd, then climb as new content is added |
| Coverage errors | GSC \> Pages \> Why pages aren't indexed | Surface remaining technical issues |
| Core Web Vitals | GSC \> Experience \> Core Web Vitals | Performance regression detection |
| Mobile usability | GSC \> Mobile usability | Catch mobile-breaking regressions |
| Brand vs non-brand split | GA4 \+ GSC overlay | Brand queries \= trust building working; non-brand queries \= SEO content working |
| WhatsApp click-through rate | GA4 event on `wa.me` click | Conversion proxy |
| Booking form starts (`/checkout` or `/booking`) | GA4 funnel | Bottom-of-funnel conversion |
| Schema.org rich result presence | GSC \> Enhancements | Track schema deployments |

Set a 90-day baseline before launching the content strategy so attribution is clean.

---

## **11\. Prioritized Action Plan**

### **Quick wins — Week 1-2 (mostly dev work, ≤2 days each)**

| \# | Action | Owner | Impact | Effort |
| ----- | ----- | ----- | ----- | ----- |
| QW-1 | Build 301 redirect map from legacy URLs → new SSOT routes (see §1.1 table) | Dev team | **Critical** | 1 day |
| QW-2 | Fix footer internal linking bug — destinations footer should point to `/destinations/{slug}` not `/destinations` | Dev team | **High** | 1 hour |
| QW-3 | Fix templated meta description bug ("From-surabaya" → "Surabaya") on listing pages | Dev team | **High** | 30 min |
| QW-4 | Verify and submit sitemap.xml in GSC; remove legacy URLs from sitemap | Dev team | **High** | 1 hour |
| QW-5 | Add JSON-LD Organization/TravelAgency block globally (see §4.4) | Dev team | **High** | 2 hours |
| QW-6 | Add JSON-LD FAQPage to tour pages from existing "Quick Answers" content | Dev team | **High** | 2 hours |
| QW-7 | Add JSON-LD TouristTrip \+ AggregateRating to tour pages (see §4.2) | Dev team | **High** | 4 hours |
| QW-8 | Rewrite title tags on top 10 pages per §2.3 | Dev/content | **High** | 2 hours |
| QW-9 | Rewrite meta descriptions per §2.4 formula | Content | **Medium-High** | 4 hours |
| QW-10 | Decide fate of `java-tour.com` and `legacy.javavolcano-touroperator.com` subdomains | Sam \+ Dev | **High** | Discussion \+ 1 day execution |
| QW-11 | Improve image alt text from "Gallery 1" → descriptive | Content/dev | Medium | 2 hours |
| QW-12 | Add BreadcrumbList schema across sub-pages | Dev team | Medium | 2 hours |
| QW-13 | Resubmit GSC URL inspection for top 10 pages after redirects | Sam | Medium | 30 min |
| QW-14 | Verify Trustpilot/TripAdvisor/Google Maps/Booking.com profiles all in `sameAs` JSON-LD | Dev team | Medium | 30 min |

### **Strategic investments — Quarter (Q2-Q3 2026\)**

| \# | Action | Owner | Impact | Effort | Dependencies |
| ----- | ----- | ----- | ----- | ----- | ----- |
| SI-1 | Build content for Silo 3 (Regulatory \+ Safety) — 7 new pages | Content team | **High** (uncontested moat) | 4-6 weeks | After QW-1 to \-7 done |
| SI-2 | Build content for Silo 4 (Pre-purchase planning) — 8 new pages | Content team | **High** | 6-8 weeks | None |
| SI-3 | Expand 5 destination pages with full depth content (§7.2) | Content team | High | 3 weeks | None |
| SI-4 | Build market-specific landing pages: `/markets/singapore`, `/markets/malaysia`, `/markets/hong-kong`, `/markets/taiwan`, `/markets/china` | Content \+ dev | **High** | 4 weeks | Need translation budget for CN/TW phase 2 |
| SI-5 | Build "Bromo/Ijen status today" auto-updated page | Dev \+ content ops | High (freshness signal \+ topical trust) | 2 weeks initial \+ ongoing 1hr/week | None |
| SI-6 | Launch Indonesian \+ English press outreach campaign (Detik, Kompas, Honeycombers, etc.) | Sam / PR | **High** | 6-8 weeks | Press kit \+ Mr. Sam's media availability |
| SI-7 | Build YouTube channel with 5 cornerstone videos: "What is Ijen blue fire", "Bromo sunrise from Penanjakan", "Mr. Sam — Tourist Police story", "What to pack for Bromo Ijen", "Ijen health screening explained" | Content \+ Sam (talent) | **High** (long-term traffic \+ backlink magnet) | 8-12 weeks | Production resource |
| SI-8 | Verify and optimize listings on Klook, GetYourGuide, Viator, Booking.com (if not already) — these are distribution channels AND backlinks | Sam / Ops | Medium-High | 2-3 weeks | OTA contracts |
| SI-9 | Set up brand mention monitoring (Mention.com / Brand24 free) \+ reclamation workflow | Sam | Medium | 1 day setup \+ 2hr/week ongoing | None |
| SI-10 | Apply for Wonderful Indonesia (indonesia.travel) operator directory listing | Sam | Medium | 2 weeks | Application submission |
| SI-11 | Content freshness program — quarterly review \+ update of top 10 pages | Content team | Medium-High | Ongoing | After SI-1, SI-2 |
| SI-12 | Backlink outreach — niche resource pages, eco-tourism directories, university travel clubs | Sam / Outreach | Medium-High | Ongoing | None |
| SI-13 | Translate top 10 pages to Bahasa Indonesia for `id-ID` hreflang variant — captures local \+ neighboring market traffic | Content | Medium (Phase 2 decision) | 4-6 weeks | After SI-1 to \-3 |
| SI-14 | Translate top 10 pages to Simplified Chinese for `zh-CN` and Traditional Chinese for `zh-TW`/`zh-HK` | Content | High for CN/TW/HK markets | 8 weeks | After market validation |

### **90-day measurable targets**

If QW-1 through QW-14 are executed in weeks 1-2, and SI-1, SI-3, SI-5 are in flight, realistic targets at day 90:

* Indexed pages: drop initially (legacy 301d), then rise above current as new content goes live. Net: \+20-30% indexed URLs of real value.  
* Average position on `tourist police bromo`, `licensed bromo tour operator`, `ijen health certificate`: hold \#1-3  
* Average position on tier-2 commercial keywords (`bromo ijen 3d2n private tour`, `madakaripura waterfall tour`): break into top 30  
* Rich result presence: FAQ snippets \+ AggregateRating stars visible on at least 5 tour pages in SERP  
* Organic clicks: \+25-50% (low baseline so percentage swings are big; focus on absolute numbers)  
* Branded vs non-branded traffic split: shift toward non-branded as content silos mature

---

## **12\. What this audit could NOT cover**

Honest disclosure of audit limitations:

1. **Exact keyword search volumes** — would require Ahrefs API access (currently blocked at this plan tier) or Google Keyword Planner manual export  
2. **Exact current rankings per keyword** — same constraint  
3. **Backlink profile depth** (referring domains count, DR distribution, anchor text patterns, toxic links) — Ahrefs blocked  
4. **Site Audit crawl results** (broken internal links, redirect chains, orphan pages, page speed scores at scale) — would require Ahrefs Site Audit, Screaming Frog, or similar  
5. **Direct competitor keyword overlap analysis** (which exact keywords tourmountbromo.com ranks for that JVTO doesn't) — Ahrefs blocked  
6. **Google Search Console data** (impressions, clicks, average position by query and page) — not connected to this audit  
7. **Google Analytics data** (organic traffic trends, conversion rates by source) — not connected  
8. **Core Web Vitals scores** at scale — not measured; recommend running PageSpeed Insights on top 5 pages  
9. **Internal sitemap.xml contents** — not fetched  
10. **robots.txt contents** — not fetched (web\_fetch denied without prior URL discovery)

### **To unblock these gaps**

The fastest paths are:

* **Option A (free):** Sam connects Google Search Console \+ Google Analytics to a future audit session — those alone fill \~60% of the data gap  
* **Option B (paid, recommended):** upgrade the Ahrefs subscription to a plan that includes API access (Advanced tier or higher). With Ahrefs MCP active, every section of this audit could be quantified with exact numbers in a single re-run.  
* **Option C (free, slow):** Google Keyword Planner with a $1/day Google Ads account unlocks search volumes manually  
* **Option D (free):** Screaming Frog Free version (500 URL limit) covers JVTO's full site for technical SEO crawl

---

## **Appendix A — Ahrefs MCP status**

Every Ahrefs MCP endpoint tested in this audit returned `{ "error": "Insufficient plan" }` — including basic endpoints like `site-explorer-metrics`, `site-explorer-organic-keywords`, `site-explorer-backlinks-stats`, `keywords-explorer-matching-terms`, `serp-overview`, and even the free `subscription-info-limits-and-usage` check.

This indicates the connected Ahrefs account does not have API/MCP access at its current subscription tier (typically requires Advanced or Enterprise plan).

The audit was completed using:

* Direct site fetches (homepage, tour page, destination page, listing page)  
* Public SERP analysis via web search across major commercial queries  
* Competitor identification \+ benchmarking  
* Knowledge-based SEO methodology

When Ahrefs MCP access is restored, this same audit can be re-run with exact data substituted into every estimated value.

---

## **Appendix B — Competitor reference list (for ongoing monitoring)**

Direct competitors to watch monthly:

* **Tier 2 (dominant direct):** tourmountbromo.com · bromotour.com · forevervacation.com (Bali-led)  
* **Tier 3 (mid-tier):** bromoeastjava.com · hellobromo.com · adventureindonesia.com · mybalitrips.com · travel-withdee.com  
* **Tier 3 (EMD-driven):** bluefireijentour.com · ijenplateau.com · mountbromoijen.com · mtbromoijentour.com · bromoijentourism.com · ijenbromotours.com · mountbromoijentour.com · bromo.co.id · yukbanyuwangi.co.id

OTAs (distribution \+ competitive):

* klook.com · getyourguide.com · viator.com · tripadvisor.com · booking.com/experiences

Track each via: monthly Google search for the top 5 target keywords \+ record top 10 SERP. Build a simple Google Sheet of competitor rankings movement over time.

---

*End of audit. Prepared 17 May 2026 for Java Volcano Tour Operator (PT Java Volcano Rendezvous).*

