# How to Run Health Checks

Audit the wiki for contradictions, orphan pages, stale claims, and coverage gaps. Three tiers: on-demand, weekly, and monthly.

## Prerequisites

- Access to the wiki (all files under `wiki/`)
- For monthly checks: internet access for web-verification of credentials and review counts

## On-Demand Health Check

**Trigger**: Say "Run health check"

### Steps

1. **Contradiction scan** — Read all wiki pages. Flag any claim that directly contradicts a claim on another page:

   ```markdown
   > Contradiction with [[other-page]]: <detail>
   ```

2. **Orphan detection** — List all wiki pages with no inbound `[[wikilinks]]` from other pages:

   ```markdown
   > Orphan: no inbound links
   ```

3. **Stale claim flags** — Flag claims referencing a specific date, rating, or statistic where the source page has `last_updated` more than 90 days ago:

   ```markdown
   > [stale?] <claim>
   ```

4. **Gap page identification** — List concepts referenced in multiple pages that have no dedicated wiki page. Add to the "Open Gaps" section of `wiki/index.md`.

5. **Append report** to `wiki/log.md`:

   ```markdown
   ## [2026-MM-DD] health-check | on-demand

   Contradictions: [count]. Orphans: [count]. Stale claims: [count]. Gaps: [count].
   Details: [summary of findings].
   ```

## Weekly Health Check

**Trigger**: Say "Run weekly health check"

Runs all on-demand checks, plus:

1. **30-day stale sweep** — Same as the 90-day check but with a 30-day threshold. Flag with `> [stale?]` inline.

2. **New orphan detection** — Check pages created since the last log entry that have no inbound links from any page other than `wiki/index.md`.

3. **Index completeness** — Verify every `.md` file under `wiki/` (excluding index.md, log.md, overview.md) has a corresponding entry in `wiki/index.md`. List any missing entries.

4. **Log completeness** — Verify every file under `raw/` has a corresponding `## [date] ingest | [title]` entry in `wiki/log.md`. List any raw files with no log entry.

## Monthly Health Check

**Trigger**: Say "Run monthly health check"

Runs all weekly checks, plus:

1. **Credential web-verification** — Use web search to verify:
   - NIB 1102230032918 is still active (OSS Indonesia registry)
   - Trustpilot rating and review count match `wiki/credentials/trust-signals`
   - Bripka Agung Sambuko's Polpar status matches the evidence chain in `wiki/people/agung-sambuko`

   Flag discrepancies: `> [stale?] Web-check [date]: <finding>`

2. **Trustpilot new review sweep** — Compare current Trustpilot review count against `wiki/reviews/trustpilot-compilation`. If more than 2 new reviews exist:

   ```markdown
   > Action needed: [N] new Trustpilot reviews since last review-feed ingest
   ```

3. **Gap page audit** — Check each entry in the "Open Gaps" section of `wiki/index.md`. Remove entries that have been filled. Note resolved gaps in the report.

4. **Output staleness** — List all files under `output/` with a date in the filename more than 90 days old:

   ```markdown
   > [stale?] Output may no longer reflect current wiki
   ```

## Verification

After running a health check:
- [ ] All contradictions flagged inline on both pages involved
- [ ] Orphan pages listed (consider adding inbound links or merging)
- [ ] Stale claims marked with `> [stale?]` for follow-up
- [ ] Report appended to `wiki/log.md` with the correct tier label
- [ ] For monthly: web-verified credentials match wiki values (or discrepancies flagged)

## Troubleshooting

**Too many stale claims**: This usually means a major source hasn't been re-ingested recently. Check if the SSOT JSON has a newer version, or if Trustpilot reviews need a fresh `review-feed` ingest.

**Orphan page found**: Either add `[[wikilinks]]` from related pages, or if the page is genuinely isolated, consider whether it should be merged into an existing page.

**Contradiction between source pages**: Both claims may be correct in different contexts (e.g., "Founded 2015" for the guesthouse era vs "PT incorporated 2016" for the legal entity). Document the distinction explicitly rather than removing either claim.

**Web-verification fails**: External sites may be temporarily down. Note the failure in the report and retry in the next monthly check. Don't remove wiki values based on a single failed verification.

## Related

- [Reference: Wiki Structure](reference-wiki-structure.md) — frontmatter conventions and cross-referencing
- [How-to: Ingest Sources](howto-ingest-sources.md) — resolve stale claims by ingesting updated sources
- [How-to: Generate Output](howto-generate-output.md) — regenerate stale output files
- [wiki/ops/health-checks.md](../wiki/ops/health-checks.md) — the canonical health check spec
