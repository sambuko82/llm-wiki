# LLM Knowledge Base Tooling Guide

*Source: article pasted 2026-05-11. Immutable — do not edit.*

---

## Tools & Ecosystem

Several tools and projects already align with Karpathy's vision. Here's the current landscape:

### Obsidian + AI Plugins

Obsidian (1.5M+ users) is the foundation of Karpathy's setup. The Obsidian CEO, Steph Ango (kepano), responded to Karpathy's post suggesting developers keep personal vaults clean and create separate vaults for agent-generated content — preventing contamination of human-curated knowledge.

Obsidian Skills, a project by kepano, teaches AI agents to work with Obsidian's native formats: [[wikilinks]], callouts, Bases, and Canvas. It's the interface layer between AI agents and your vault.

### Knowledge Base Tools

| Tool | What It Does | Best For |
|------|-------------|---------|
| Notemd | Chunks docs, auto-generates wiki-links, creates concept notes | Obsidian users wanting AI-powered linking |
| AI Knowledge Filler | Generates structured files with validated YAML and WikiLinks | Generating Obsidian-ready content from LLMs |
| library-mcp | MCP server for exploring Markdown KBs through Claude Desktop | Querying existing knowledge bases via AI |
| Obsidian Skills | Agent skills for Markdown, Bases, Canvas, CLI | Teaching AI agents Obsidian-native formats |
| LLM Workspace | Integrates local LLMs directly into Obsidian vaults | Private, offline knowledge work |

### MCP Servers for Knowledge

The MCP ecosystem is growing fast with knowledge-focused servers. Servers like gnosis-mcp load markdown docs into SQLite for AI search, while library-mcp lets you explore markdown KBs through Claude Desktop. These turn your knowledge base into a tool that any AI assistant can use.

---

## How to Build Your Own LLM Knowledge Base

You don't need Karpathy's setup to start. Here's a practical approach using tools available today:

### The Minimum Viable Knowledge Base

**Directory structure:**

```
my-research/
  raw/                # Source documents (articles, papers, notes)
  wiki/               # LLM-compiled wiki (don't edit manually)
    INDEX.md
    concepts/
  output/             # Query results, slides, charts
  _meta/              # Compile state, config
```

### Step-by-Step Setup

1. **Install Obsidian + Web Clipper.** Free and local-first. Web Clipper saves any web article as clean .md with one click.

2. **Create your raw/ directory.** Drop in source material: articles, papers, code snippets, images, screenshots.

3. **Write a compilation prompt.** Give your AI agent a system prompt that tells it how to compile the wiki:

> You are a wiki compiler. Read all files in raw/ and compile them into wiki/ following these rules:
> 1. Identify all key concepts mentioned across documents
> 2. Create one .md article per concept in wiki/concepts/
> 3. Each article should summarize what raw/ says about it
> 4. Use [[wiki-links]] to connect related concepts
> 5. Update wiki/INDEX.md with a table of contents
> 6. Only process raw files modified since last compile
>
> Frontmatter for each article:
> ---
> title: Concept Name
> sources: [list of raw/ files referenced]
> related: [[linked-concepts]]
> last_compiled: 2026-04-03
> ---

4. **Run the compilation.** Point your agent at the directory. First run takes time; incremental builds are fast.

5. **Query your wiki.** Ask the agent questions like: "What are the key differences between X and Y?" or "Create a Marp slide deck summarizing the top 5 concepts."

6. **Run health checks.** Periodically ask the agent to audit: find contradictions, missing links, thin articles, orphaned concepts.

### Agent Setup Tips

If you're using an agentic IDE, create a skill that watches raw/ for changes and triggers incremental compilation. For multi-agent setups, dedicate one agent to ingestion, another to compilation, a third to health checks.

---

## Advanced Patterns

### Multi-Source Ingestion Pipeline

Build automated ingestion from multiple source types:

- Web articles: Obsidian Web Clipper → raw/articles/
- PDFs (papers, reports): PDF → Claude Vision / pdf2md → raw/papers/
- YouTube videos: Transcript API → clean markdown → raw/videos/
- GitHub repos: Clone → README + key files → raw/repos/
- Podcasts / audio: Whisper → transcript → raw/audio/
- RSS feeds (automated): Cron + RSS parser → raw/feeds/

### Compilation Profiles

Different wikis need different compilation strategies:

- **Research profile:** Extract claims, evidence strength, methodology, citations, contradictions
- **Competitive profile:** Extract product features, pricing, positioning, team size, funding
- **Learning profile:** Extract concepts, prerequisites, difficulty levels, practical exercises
- **Decision log profile:** Extract decisions, alternatives considered, rationale, who decided, when

### Scheduled Health Checks

- Daily: Check for new raw files and trigger incremental compilation
- Weekly: Run full consistency check across all articles
- Monthly: Web-verify facts in the wiki against current sources (catches outdated info)
- On-demand: Deep analysis for specific queries or decision points

### Cross-Wiki Linking

If you maintain multiple knowledge bases, the LLM can find connections across them. Cross-wiki health checks surface non-obvious connections between separate vaults.

### Version Control Your Knowledge

Since the entire wiki is plain markdown, it works naturally with Git. Commit after each compilation run:

- Full history of how your knowledge evolved
- Ability to diff between compilation runs
- Rollback if a compilation introduces errors
- Collaboration via branches and pull requests
- CI/CD for knowledge — automated health checks on every commit
