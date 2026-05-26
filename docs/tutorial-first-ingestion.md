# Tutorial: Your First Source Ingestion

Walk through ingesting a new source document into the JVTO LLM Wiki from start to finish. By the end, you'll have created a source summary page, updated domain pages, and logged the operation.

## What you'll need

- The llm-wiki repository cloned and open
- An LLM session with access to the repository files (Claude Code, Obsidian + Copilot, etc.)
- A source document to ingest (we'll use a web clip as the example)

## Step 1: Place the source file

Drop your raw source into the appropriate location:

```
raw/_inbox/2026-06-01-example-press-article.md
```

For this tutorial, imagine you've clipped a news article about JVTO from a travel blog using Obsidian Web Clipper. The file is a Markdown file with the article text.

You should now have the file in `raw/_inbox/`.

## Step 2: Read the wiki index

Before ingesting, check what already exists. Open `wiki/index.md` and scan it. This is the AI entry point — it lists every source, every domain page, and the current page count.

Look for:
- **Existing sources** that might overlap with your new document
- **Domain pages** that your source could enrich (destinations, credentials, reviews, etc.)

For our example press article about JVTO, relevant pages might include:
- `wiki/credentials/press-coverage.md`
- `wiki/credentials/trust-signals.md`
- `wiki/people/agung-sambuko.md` (if the article mentions the founder)

## Step 3: Classify the source

Match your source against the ingestion profiles. Say:

> "Use the `press-clip` ingestion profile."

The press-clip profile tells you to extract:
- Publication name, date, journalist name
- Key quote verbatim in original language
- Topic: police-led, safety, destination feature, or award
- Whether it is independent or paid placement

Each profile is documented in `wiki/ops/ingestion-profiles.md`.

## Step 4: Read the source and extract facts

Read the source document end-to-end. Pull out the specific items the profile requires.

For our press article, you might extract:

| Fact | Value | Location in source |
|------|-------|--------------------|
| Publication | TravelBlog.com | Header |
| Date | 2026-06-01 | Byline |
| Topic | Police-led tours in East Java | Title + body |
| Key quote | "The only tour operator in East Java led by an active police officer" | Paragraph 3 |
| Independent? | Yes (editorial, not sponsored) | No disclosure present |
| Mentions founder? | Yes — "Agung Sambuko, a Bripka in the Tourist Police" | Paragraph 2 |

## Step 5: Create the source summary page

Create `wiki/sources/travelblog-2026-06.md` using the `templates/source.md` template:

```markdown
---
type: source
title: TravelBlog.com — Police-Led Tours in East Java (2026-06-01)
slug: travelblog-2026-06
last_updated: 2026-06-01
original_url: https://example.com/article
ingested: 2026-06-01
format: web-clip
location: raw/_inbox/2026-06-01-example-press-article.md
sources: [travelblog-2026-06]
---

# Source: TravelBlog.com — Police-Led Tours (2026-06-01)

## Metadata

- **File**: `raw/_inbox/2026-06-01-example-press-article.md`
- **Format**: Web clip (Obsidian Web Clipper)
- **Source URL**: https://example.com/article
- **Capture date**: 2026-06-01

## Role in Vault

Auxiliary source. Independent editorial coverage confirming JVTO's
police-led positioning (C1) and founder identity.

## Authority Status

Treat as independent press corroboration for C1 (Safety-led operations)
and C9 (Press & Recognition). Not canonical for any structured facts.

## Key Facts Extracted

| Fact | Value | Source location |
|------|-------|----------------|
| Publication | TravelBlog.com | Header |
| Journalist | Jane Doe | Byline |
| Date | 2026-06-01 | Byline |
| Key quote (EN) | "The only tour operator in East Java led by an active police officer" | ¶3 |
| Mentions founder | Agung Sambuko, Bripka, Tourist Police | ¶2 |
| Independent | Yes (no sponsorship disclosure) | — |

## Content Angles This Source Unlocks

1. New independent press citation for C9 press-coverage page
2. Verbatim quote usable in AEO/FAQ content for C1
3. Corroborates founder's police rank (Bripka) from a third-party source
```

## Step 6: Update domain pages

The press-clip profile says to update:
- `wiki/credentials/press-coverage.md` — add the new press item
- `wiki/credentials/trust-signals.md` — increment press count if applicable

Open each page, add the new information, and update the `last_updated` date in frontmatter.

For example, in `wiki/credentials/press-coverage.md`, add a new row to the press items table:

```markdown
| TravelBlog.com | 2026-06-01 | Police-Led Tours in East Java | Independent editorial | C1, C9 |
```

## Step 7: Update index and log

Add the source to `wiki/index.md`:

```markdown
- [[sources/travelblog-2026-06]] — TravelBlog.com press clip (2026-06-01). Independent coverage of police-led positioning. Supports C1, C9.
```

Update the `total_pages` count in the index frontmatter (increment by 1).

Append to `wiki/log.md`:

```markdown
## [2026-06-01] ingest | TravelBlog.com — Police-Led Tours

Pages updated: sources/travelblog-2026-06 (new), credentials/press-coverage, credentials/trust-signals.
Key additions: new independent press citation for C1/C9, verbatim founder quote.
```

## Step 8: Commit

```bash
git add -A && git commit -m "ingest | TravelBlog.com — Police-Led Tours"
```

## What you built

You've completed a full Workflow 4 (Typed Ingest) cycle:

1. **Classified** the source as a `press-clip`
2. **Extracted** facts following the profile's targets
3. **Created** a source summary page with full metadata and provenance
4. **Updated** domain pages with new information
5. **Maintained** the index and operations log
6. **Committed** with a standard message format

The new source is now part of the wiki's knowledge graph. Future queries about JVTO's press coverage will find it. Future output generation (AEO, website copy) can cite it. Future health checks will verify it hasn't gone stale.

## Next steps

- [How-to: Generate Output](howto-generate-output.md) — produce content from the updated wiki
- [How-to: Health Checks](howto-health-checks.md) — verify wiki consistency
- [Reference: Wiki Structure](reference-wiki-structure.md) — full directory and frontmatter spec
- [Explanation: Architecture](explanation-architecture.md) — understand why the system works this way
