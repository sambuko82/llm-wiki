# How to Ingest a New Source

Add a new raw document to the wiki knowledge base, extracting facts, updating domain pages, and logging the operation.

## Prerequisites

- A raw source file (PDF, web clip, JSON, Excel, database export, etc.)
- The file placed in `raw/` or `raw/_inbox/`
- Familiarity with which wiki domain pages exist (check `wiki/index.md`)

## Quick version (Workflow 1)

1. Read the source fully
2. Discuss key takeaways with the user
3. Create `wiki/sources/[slug].md` using the `templates/source.md` template
4. Update relevant domain pages (typically 5-15 pages)
5. Update `wiki/index.md`
6. Append to `wiki/log.md`
7. Commit: `git add -A && git commit -m "ingest | Source Title"`

## Better version: Typed Ingest (Workflow 4)

Before starting Workflow 1, declare the source type. This focuses extraction on what matters for that type.

### Step 1: Classify the source

Match your source against the profiles in `wiki/ops/ingestion-profiles.md`:

| Source type | Examples |
|-------------|----------|
| `web-clip` | News article, blog post, Obsidian Web Clipper output |
| `pdf-doc` | Policy pack, government regulation, certificate |
| `ssot-update` | New version of the JVTO SSOT JSON |
| `review-feed` | Batch of Trustpilot / Google / TripAdvisor reviews |
| `press-clip` | News coverage, guidebook mention |
| `seo-audit` | SEO audit with keyword data and technical findings |
| `finance-spreadsheet` | Excel cost breakdown for a tour package |
| `db-export` | Live database dump (SQL DDL, CSV rows) |

### Step 2: State the profile

Say: "Use the `[source-type]` ingestion profile." This activates the type-specific extraction targets.

### Step 3: Extract according to the profile

Each profile specifies what to extract. Examples:

**For `web-clip`**: Voice/tone exemplars, corroborating or contradicting claims, new statistics or credentials.

**For `review-feed`**: New reviews not already in `reviews/trustpilot-compilation`, guide/driver names mentioned, rating delta, complaint/praise patterns.

**For `finance-spreadsheet`**: Per-day cost items, pax tier pricing, total COGS, selling price, component subtotals.

### Step 4: Write the source summary

Create `wiki/sources/[slug].md` with the `templates/source.md` structure:
- Metadata (file, size, format, capture date)
- Role in vault (canonical vs auxiliary)
- Authority status
- Content map (for multi-section sources)
- Key facts extracted (verbatim)
- Internal contradictions
- Content angles

### Step 5: Update domain pages

The ingestion profile lists which wiki pages to update. Common patterns:

| Source type | Pages to update |
|-------------|----------------|
| `web-clip` | `sources/[slug]`, `website/copy-bank`, relevant `destinations/` or `credentials/` |
| `review-feed` | `sources/[slug]`, `reviews/trustpilot-compilation`, `reviews/review-patterns`, `credentials/trust-signals` |
| `ssot-update` | Everything. Treat as a full wiki audit. |
| `seo-audit` | `sources/[slug]`, `seo/seo-strategy`, `seo/competitors`, `seo/redirect-map`, `website/brand-voice` |

### Step 6: Update index and log

1. Add the new source to `wiki/index.md` in the Sources section
2. Update `total_pages` count in `index.md` frontmatter
3. Append to `wiki/log.md`:

```markdown
## [2026-MM-DD] ingest | Source Title

Pages updated: [list]. Key additions: [brief].
```

### Step 7: Commit

```bash
git add -A && git commit -m "ingest | Source Title"
```

## Using the Intake Gate (Workflow 7)

For bulk or uncertain sources, use the intake gate instead of manual classification:

1. Place the file in `raw/_inbox/`
2. Say: "Process inbox" or "Intake gate"
3. The gate classifies, routes, extracts key facts, checks for duplicates, and generates an intake card
4. The gate also runs **correlation checks** against existing registries:
   - **Entity registration**: if the source introduces a new destination, crew member, authority, credential, or system, the gate proposes an entity entry in `entity-registry.yml`
   - **Claim linkage**: if the source supports or challenges an existing trust claim (C1-C9), the gate links evidence to `claim-registry.yml` or flags a conflict
   - **Conflict detection**: contradictions go to `conflict-log.md` and `decision-queue.md` for human review
5. Review the intake card and proceed with the appropriate ingestion profile

## Verification

After ingestion:
- [ ] `wiki/sources/[slug].md` exists with complete frontmatter
- [ ] All claims in the source page cite specific sections of the raw document
- [ ] Relevant domain pages updated with new facts
- [ ] No contradictions introduced (check against existing pages)
- [ ] `wiki/index.md` updated with the new source entry
- [ ] `wiki/log.md` has the operation entry
- [ ] Git commit with `ingest | Source Title` message

## Troubleshooting

**Source contradicts existing wiki facts**: Flag with `> Contradiction with [[other-page]]: <detail>` in both pages. Do not silently overwrite — contradictions must be visible for the next health check.

**Source overlaps heavily with existing sources**: Note the overlap percentage in the source summary (e.g., "~75% overlaps existing sources"). Extract only genuinely new concepts.

**Can't determine authority status**: Default to auxiliary. Only mark as canonical when the source is clearly the most authoritative for its facts (e.g., the SSOT JSON for structured company data, Trustpilot for review counts).

## Related

- [Tutorial: First Ingestion](tutorial-first-ingestion.md) — walk through a complete example
- [Reference: Wiki Structure](reference-wiki-structure.md) — frontmatter spec and domain taxonomy
- [How-to: Health Checks](howto-health-checks.md) — verify ingestion quality
- [wiki/ops/ingestion-profiles.md](../wiki/ops/ingestion-profiles.md) — full profile catalog
- [wiki/ops/intake-gate.md](../wiki/ops/intake-gate.md) — intake gate details
