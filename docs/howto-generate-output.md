# How to Generate Output

Produce content artifacts (website copy, FAQ pages, AEO snippets, JSON-LD schemas, social posts, slide decks, or custom tour quotes) from the wiki knowledge base.

## Prerequisites

- Wiki pages up to date for the target topic (run a health check if unsure)
- Familiarity with the available compilation profiles in `wiki/ops/compilation-profiles.md`

## Steps

### Step 1: Select a compilation profile

Choose the profile matching your output type:

| Profile | Output type | Example filename |
|---------|------------|-----------------|
| `aeo` | Answer Engine Optimization Q&A blocks | `output/website/aeo/ijen.md` |
| `website-copy` | Hero paragraphs, section copy, body text | `output/website/pages/homepage.md` |
| `faq` | FAQ pages (AEO-compatible, human-readable) | `output/website/faq/bromo.md` |
| `social` | Social media captions and posts | `output/social/batch-2026-05-18.md` |
| `schema` | JSON-LD structured data | `output/website/schema/ijen-crater-schema.json` |
| `slide-deck` | Marp-compatible markdown slides | `output/slides-YYYY-MM-DD-[topic].md` |
| `custom-tour-quote` | Itemized cost estimate from rate cards | `output/finance/quote-{slug}-{duration}.md` |

### Step 2: Activate the profile

Say: "Use the `[profile]` profile." This tells the LLM which wiki pages to draw from, the output format constraints, and the forbidden patterns.

### Step 3: Specify the target

Tell the LLM what to generate. Examples:
- "Generate AEO blocks for the Ijen Crater destination page"
- "Write website copy for the Bromo 2D1N tour page"
- "Create JSON-LD TouristTrip schema for all Surabaya-origin packages"
- "Build a custom tour quote for Ijen + Bromo, 3D2N, 2 pax, mid-tier hotels"

### Step 4: Review the output

The LLM generates the output and saves it to `output/` following the profile's filename convention. Check:

- [ ] All claims trace to a wiki source (no invented statistics)
- [ ] Voice matches the profile constraints (Style A for website, Style B for social)
- [ ] Forbidden patterns avoided (no hedging in AEO, no passive voice in hero copy, no invented quotes in social)
- [ ] For `schema` profile: all numeric values verified against `wiki/credentials/trust-signals.md` §Schema Canonical Values

### Step 5: Update the output index

Add the new file to `output/INDEX.md` with status `draft`:

```markdown
| `website/aeo/new-topic.md` | `/target-url` (AEO overlay) | 2026-MM-DD | draft | [source list] |
```

### Step 6: Promote status after review

After copy-checking:
1. Change status from `draft` to `reviewed` in `output/INDEX.md`
2. Log the review in `wiki/log.md`:

```markdown
## [2026-MM-DD] review | Output file description

Changes made: [list any corrections]. Status: draft → reviewed.
```

## Profile-specific rules

### AEO profile
- Question: max 15 words, direct
- Answer: max 40 words, starts with a direct claim
- Uses the NLP atom structure from `wiki/website/aeo-claims.md` (C1-C9)

### Website-copy profile
- Style A voice (direct, evidence-led)
- Meta description: 3-part formula from `wiki/website/brand-voice.md` §Meta Description Formula
- Max 160 chars, no first-person
- "Tourist Police officer" not "safety-focused guide"

### Schema profile
- Mandatory verification step: extract every numeric value, grep against `wiki/credentials/trust-signals.md`
- `reviewCount` must match current canonical count
- Google Maps rating (4.90) and Trustpilot rating (4.8) are never interchangeable
- Currency: `"priceCurrency": "IDR"`, price as full integer (e.g., `2450000`)
- Output includes a `.receipt.md` verification file alongside the `.json`

### Custom-tour-quote profile
- Input: destination list, duration, pax count, hotel tier, special activities
- Draws from `wiki/finance/rate-cards.md` for all cost components
- Total COGS must equal sum of all line items (verified before output)

## Definition of Done: Trust Fortress Ready

All content pages must satisfy four layers before publishing:

1. **Human Layer**: Medically and operationally factual, "Safety-Led" brand voice, clear CTA
2. **Trust Layer**: Trust Strip (license number, Police-led badge), links to /verify-jvto
3. **Machine Layer**: Schema.org markup nested, title/meta tags locked, Answer Block optimized for RAG
4. **Operational Layer**: Verified against SSOT — all numeric values match §Schema Canonical Values

## Verification

After generating output:
- [ ] File saved to correct `output/` subdirectory with proper filename convention
- [ ] Entry added to `output/INDEX.md`
- [ ] All claims traceable to wiki sources
- [ ] No forbidden patterns present
- [ ] For schema: `.receipt.md` verification file created

## Troubleshooting

**Output contains stale data**: Check if the source wiki pages have been updated since the output was last generated. Regenerate from current wiki state.

**Schema reviewCount mismatch**: The review count changes when new reviews are ingested. Always grep `wiki/credentials/trust-signals.md` before finalizing schema output.

**Voice doesn't match**: Re-read the profile's voice constraints and `wiki/website/brand-voice.md`. Style A (website) is direct and evidence-led. Style B (social) is warmer but still direct.

## Related

- [Reference: Wiki Structure](reference-wiki-structure.md) — output lifecycle and directory map
- [How-to: Ingest Sources](howto-ingest-sources.md) — ensure wiki is current before generating
- [How-to: Health Checks](howto-health-checks.md) — detect stale output
- [wiki/ops/compilation-profiles.md](../wiki/ops/compilation-profiles.md) — full profile catalog
