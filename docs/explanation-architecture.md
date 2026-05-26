# Explanation: Why This Architecture

The JVTO LLM Wiki is an LLM-operated knowledge base that produces all content for Java Volcano Tour Operator. This document explains why it works the way it does — the problems it solves, the trade-offs it makes, and the principles behind its design.

## The problem

JVTO's content needs are unusual. A small East Java tour operator with 14 crew members needs:
- 100+ pages of website copy across 22 tour packages, 5 destinations, trust/verification pages, and travel guides
- JSON-LD structured data for every page type
- FAQ and AEO (Answer Engine Optimization) content for AI search engines
- Social media posts grounded in real reviews
- Financial analysis from a live backoffice database
- All of this must be factually accurate, internally consistent, and traceable to verified sources

No human copywriter could maintain this volume while cross-checking every claim against source documents. The wiki solves this by making the LLM both the writer and the consistency engine.

## The three-layer separation

The core design decision: split everything into three layers with strict data flow.

```
raw/  →  wiki/  →  output/
(immutable)  (knowledge)  (artifacts)
```

### raw/ — Immutable sources

Files in `raw/` are never modified after placement. They are the ground truth: SSOT JSON files, policy PDFs, Excel spreadsheets, database dumps, web clips. The LLM reads from `raw/` but never writes to it.

Why immutable? Because content production is a trust problem. If the LLM could modify its own source material, there would be no way to audit whether a claim traces back to a real document. The immutability guarantee means any fact in `wiki/` or `output/` can be traced back to an unchanged source file.

### wiki/ — LLM-maintained knowledge

The wiki is the synthesis layer. Each wiki page digests one or more raw sources into structured knowledge: extracted facts, cross-references, contradictions flagged, content angles identified. The LLM writes and maintains every wiki page.

Why a separate wiki layer instead of generating output directly from raw sources? Three reasons:

1. **Deduplication**. A single fact (e.g., "NIB 1102230032918") appears in the SSOT JSON, the policy pack, the homepage clip, and the verification dossier. The wiki page `credentials/legal-licenses` is the single place that reconciles all four mentions.

2. **Cross-referencing**. When generating a tour page, the LLM needs facts from destinations, pricing, reviews, and credentials simultaneously. The wiki provides pre-digested, cross-linked knowledge rather than forcing re-extraction from raw files every time.

3. **Contradiction detection**. The wiki explicitly flags contradictions (e.g., "Founded 2015" vs "PT incorporated 2016-01-01") with `> Contradiction with [[other-page]]` markers. Raw sources don't know about each other; the wiki does.

### output/ — Generated artifacts

Output files are the end product: website copy, JSON-LD schemas, FAQ pages, AEO snippets, social posts. They're generated from wiki pages using compilation profiles (Workflow 5), reviewed for accuracy, and handed off to the website codebase.

Why separate from wiki? Because output files are disposable. When a wiki page updates (new review count, price change, credential update), the corresponding output files become stale and can be regenerated. The wiki is the durable knowledge; output is the ephemeral packaging.

## The workflow system

Seven workflows govern how information flows through the three layers.

| Workflow | Direction | Purpose |
|----------|-----------|---------|
| 1. Ingest | raw → wiki | Extract knowledge from a new source |
| 2. Query | wiki → answer | Find and synthesize information |
| 3. Lint | wiki → wiki | Detect contradictions, orphans, stale claims |
| 4. Typed Ingest | raw → wiki (structured) | Ingest with a source-type-specific extraction profile |
| 5. Compilation | wiki → output | Generate content artifacts using a compilation profile |
| 6. Health Check | wiki → report | Tiered audit (on-demand / weekly / monthly) |
| 7. Intake Gate | raw → routing | Classify and route new raw items before ingestion |

Workflows 4 and 7 were added after the initial system (Workflows 1-3) proved that untyped ingestion missed extraction targets and that raw items needed classification before ingestion. This is a pattern: the system grows by adding structure to observed pain points, not by redesigning from scratch.

## The trust architecture

JVTO's market position is "proof-first trust" — every marketing claim must be verifiable. The wiki encodes this as nine canonical claims (C1-C9), each backed by an evidence chain.

The evidence chain for each claim works like this:

```
Raw document (e.g., SPRIN POLPAR letter)
  → SHA-256 hash recorded in wiki/credentials/legal-licenses
    → Claim text in wiki/website/aeo-claims (with source citation)
      → Output copy in output/website/pages/ (with inline trust signal)
        → JSON-LD schema in output/website/schema/ (with verifiable URL)
```

Every link in this chain is auditable. The monthly health check (Workflow 6) verifies that credential IDs, review counts, and ratings in the wiki still match external sources (Trustpilot, OSS Indonesia).

## Trade-offs

### Chosen: LLM-operated wiki over human-written docs

The LLM writes and maintains all wiki pages. A human (Sam, the founder) provides sources and direction but doesn't edit wiki files directly.

**What this gives up**: Human editorial judgment on every page. The LLM may miss nuance or local knowledge that Sam would catch.

**What this gains**: Volume and consistency. 88+ wiki pages and 100+ output files stay internally consistent because one system maintains them all. A human writer managing this volume would inevitably introduce contradictions.

### Chosen: Obsidian wikilinks over standard Markdown links

The wiki uses `[[folder/page-name]]` syntax instead of standard `[text](path.md)` links.

**What this gives up**: Portability. These links only resolve in Obsidian or tools that understand wikilink syntax.

**What this gains**: Frictionless cross-referencing. Creating a link is as simple as typing `[[` and the page name. This low friction means more links get created, which means better knowledge connectivity and easier orphan detection.

### Chosen: Frontmatter-driven taxonomy over folder-only organization

Every page declares its `type:` in YAML frontmatter, not just by folder location.

**What this gives up**: Simplicity. You need to maintain both the folder structure and the frontmatter type.

**What this gains**: Machine-queryable taxonomy. The LLM can find all pages of type `credential` regardless of where they live in the folder tree. Health checks can verify that every page has valid frontmatter. The `sources:` array in frontmatter creates an explicit provenance chain.

### Chosen: Append-only log over wiki edit history

`wiki/log.md` records every operation (ingestions, health checks, reviews) in reverse chronological order, alongside git history.

**What this gives up**: Redundancy with git log. The log duplicates some of what `git log` already records.

**What this gains**: Structured operation history that the LLM can read without running git commands. Each log entry follows a format (`## [date] type | title`) that makes it easy to find "when was the last Trustpilot ingest?" or "what changed on 2026-05-25?" without parsing commit messages.

## Alternatives considered

### Alternative: Static site generator with CMS

A traditional approach would use a CMS (WordPress, Strapi) or static site generator (Hugo, Astro) with human editors writing content.

Rejected because: JVTO doesn't have a content team. Sam is a police officer who runs a tour company. The content volume (100+ pages, cross-referenced, with JSON-LD schemas) exceeds what one person can maintain manually.

### Alternative: Single SSOT JSON as the only source of truth

The SSOT JSON (currently v6, 13 domains) could be the sole canonical source, with all content generated directly from it.

Rejected because: The SSOT doesn't capture everything. Press coverage, review patterns, competitor analysis, SEO strategy, brand voice guidelines, and operational facts come from dozens of sources beyond the SSOT. The wiki is where all these sources converge.

### Alternative: Database-backed knowledge graph

A structured database (PostgreSQL, Neo4j) could store entities and relationships more formally than Markdown files.

Rejected because: Markdown files are readable by both humans and LLMs without tooling. They work in Obsidian for visual navigation, in git for version control, and in any text editor for quick edits. The simplicity of flat files outweighs the query power of a database for this scale.

## Related

- [Reference: Wiki Structure](reference-wiki-structure.md) — the concrete directory and frontmatter spec
- [Tutorial: First Ingestion](tutorial-first-ingestion.md) — see the architecture in action
- [How-to: Health Checks](howto-health-checks.md) — how the trust architecture gets verified
