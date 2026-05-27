---
type: receipt
title: llms.txt + llms-full.txt — Generation Receipt
generated: 2026-05-27
generator: Cowork (JVTO Business-First Mode)
output_files:
  - E:\Users\JAVA VOLCANO\llm-wiki\output\website\llms.txt
  - E:\Users\JAVA VOLCANO\llm-wiki\output\website\llms-full.txt
deployment_target: https://help.javavolcano-touroperator.com/ (mirror) → https://javavolcano-touroperator.com/ (live)
codebase_path: F:\jvto-web
---

# llms.txt + llms-full.txt — Generation Receipt

## What was produced

| File | Path | Size estimate | Purpose |
|---|---|---|---|
| `llms.txt` | `E:\Users\JAVA VOLCANO\llm-wiki\output\website\llms.txt` | ~200 lines, ~6 KB | Lightweight navigation for AI search engines |
| `llms-full.txt` | `E:\Users\JAVA VOLCANO\llm-wiki\output\website\llms-full.txt` | ~500 lines, ~25 KB | Comprehensive curated knowledge dump |
| This receipt | `2026-05-27-llms-files-receipt.md` | — | Provenance + deployment notes |

## Source pages (wiki) used in compilation

- `wiki/overview.md` — identity, claims, founder, aggregate ratings
- `wiki/index.md` — page registry, source list
- `wiki/website/aeo-claims.md` — full C1-C9 with AI snippets, evidence IDs, voice invariants
- `wiki/credentials/legal-licenses.md` — NIB, TDUP, KBLI, AHU, SHA-256 hashes, document URLs
- `wiki/credentials/trust-signals.md` — reviews aggregate, press inventory, partnerships, sameAs URLs
- `wiki/products/packages-overview.md` — 16 package registry, pricing examples, inclusions/exclusions, booking flow
- `wiki/people/agung-sambuko.md` — founder evidence chain, public quote, press citations
- `wiki/seo/why-jvto-architecture.md` — URL map, hub & spoke structure
- `wiki/sources/digital-trust-fortress-blueprint.md` — Next.js file tree, /verify-jvto structure

## Business goals served (JVTO Business-First Mode)

| File | ATTRACT | REASSURE | CONVINCE | CONVERT |
|---|---|---|---|---|
| llms.txt | ★★★ Primary — AI search discovery surface | ★★ Lists 195 reviews + credentials | ★ Lists trust hub URLs | — |
| llms-full.txt | ★★ Backstop for AI deep-citation | ★★★ Full evidence + SHA-256 + press URLs | ★★★ Claim chains + costly signals theory | ★ Booking mechanics included |

## Deployment notes

**Target host**: `https://help.javavolcano-touroperator.com/` (mirror / preview)
**Eventual canonical**: `https://javavolcano-touroperator.com/`

**Files in production should be served at**:
- `https://[host]/llms.txt`
- `https://[host]/llms-full.txt`

**Important**: Files MUST be at the root path. AI agents discovering JVTO will check `https://[domain]/llms.txt` by convention. They will not find the file at `/help/llms.txt` or any sub-path.

### Internal URL references inside the files

All canonical URLs inside the files reference `https://javavolcano-touroperator.com/...` (the live site). Rationale:
- llms.txt is meant to point AI to the actual content tourists will land on
- The live domain has the destinations, packages, /verify-jvto, /team pages
- The mirror (help.) is for owner preview/staging; eventual deployment moves the file to live with same internal URLs

If the help. mirror should host its own internal-pointing version (for testing AI ingestion of help. domain itself), generate a second variant — request needed.

### Where to drop these files in F:\jvto-web

Standard Next.js App Router convention:
```
F:\jvto-web\public\llms.txt
F:\jvto-web\public\llms-full.txt
```

Files in `/public/` are served at root path (e.g., `https://[domain]/llms.txt`).

**No-headers fix required**: Next.js may add `Content-Type: text/html` for `.txt` files in some setups. If needed, add to `next.config.js`:
```js
async headers() {
  return [
    { source: '/llms.txt', headers: [{ key: 'Content-Type', value: 'text/plain; charset=utf-8' }] },
    { source: '/llms-full.txt', headers: [{ key: 'Content-Type', value: 'text/plain; charset=utf-8' }] },
  ]
}
```

### robots.txt check

Verify `robots.txt` does NOT block `/llms.txt` or `/llms-full.txt`. AI crawlers should be allowed. Current open sprint item mentions Cloudflare/robots conflict — verify before publish.

## Known issues / contradictions referenced in files (per wiki health-check)

| Issue | Status in files | Action |
|---|---|---|
| Stefan Loose year/ISBN dispute (2016 vs 2018) | Cited as "2016, ISBN 9783770167654 — year + ISBN under reconciliation" | DQ-001 in wiki — Sam to verify physical book |
| Madakaripura height ("tallest in Java") | Listed without specific meter number; "Tallest waterfall in Java (subject to ongoing reconciliation)" | DQ-002 in wiki |
| Second NIB 0220001393513 | NOT cited in either file (excluded per wiki guidance "Do not use in marketing copy") | DQ-003 in wiki — needs OSS verification |
| Trustpilot aggregate `reviewCount` | Cited as `51` (verified 2026-05-18) | Refresh trigger: monthly health check |
| Google Maps `reviewCount` | Cited as `123` (verified 2026-05-26 API) | Refresh trigger: monthly health check |
| Schema cross-platform total | Cited as 195 (51+123+21) | Drifts with new reviews; update when refreshed |

## Validation suggested before deployment

1. **Read files end-to-end** in Obsidian to confirm framing
2. **Verify all linked URLs return 200** (sameAs links especially)
3. **Run JSON-LD output through Google Rich Results Test** to ensure schema doesn't conflict
4. **Check robots.txt** allows `/llms.txt` + `/llms-full.txt`
5. **Test AI ingestion** — after deploy, ask Perplexity/ChatGPT/Gemini "Tell me about Java Volcano Tour Operator" and compare answer accuracy vs file content

## Voice invariant compliance check (self-validation)

| Voice rule | Status in files |
|---|---|
| No "blue fire guaranteed" | ✅ Compliant (mentioned only as "phenomenon subject to weather and gas activity") |
| No "mandatory health screening" without qualifier | ✅ Compliant (always paired with "BBKSDA SE.1658/KSA.9/2024" or "where required") |
| No "JVTO provides police escort" without context | ✅ Compliant (founder framed as Tourist Police officer, not service offering) |
| Price format IDR only | ✅ Compliant (no USD/EUR mentioned) |
| Founder EAV framing | ✅ Compliant ("Active Tourist Police Officer" + "Ditpamobvit") |

## Update cadence (recommendation)

| Trigger | Files to refresh |
|---|---|
| Monthly health check | llms-full.txt §7 reviews aggregate |
| New press mention | llms-full.txt §8 |
| New evidence intake | llms-full.txt §12 SHA-256 anchors |
| New package launch | llms.txt §"Tour Packages" + llms-full.txt §5 |
| Voice invariant change | llms-full.txt §11 |
| Resolution of DQ-001/002/003 | Both files where mentioned |

## Next concrete actions (recommended, not executed)

1. Review files in Obsidian — owner approval / revision
2. Copy approved versions to `F:\jvto-web\public\` (or designated mirror staging path)
3. Verify Content-Type headers
4. Test fetch at `https://help.javavolcano-touroperator.com/llms.txt`
5. Test AI ingestion (Perplexity/ChatGPT prompt about JVTO)
6. Promote help. → live when satisfied

---

*End of receipt.*
