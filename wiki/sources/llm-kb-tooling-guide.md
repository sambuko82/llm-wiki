---
type: source
title: LLM Knowledge Base Tooling Guide (Karpathy-Inspired Patterns)
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# LLM Knowledge Base Tooling Guide

**Source type:** web-clip (manually captured article)
**Captured:** 2026-05-11
**Topic:** Building LLM-native knowledge bases — tools, patterns, directory structure, operational workflows

## Key Facts

- Core pattern validated: `raw/` (immutable source) → LLM compilation → `wiki/` (agent-maintained) → `output/` (derived artifacts) — matches JVTO's existing structure
- Obsidian CEO (Steph Ango) recommends separate vaults for agent-generated content to prevent contamination of human-curated knowledge
- MCP servers like gnosis-mcp load markdown docs into SQLite for AI search; library-mcp lets Claude Desktop query markdown KBs via structured tools
- Typed ingestion: naming source types (web-clip, pdf-doc, review-feed) and defining per-type extraction targets reduces missed signals
- Compilation profiles: different prompt strategies per output type (AEO, website copy, FAQ, social) produce more consistent results than generic prompts
- Tiered health checks: on-demand (lint), weekly (stale + orphan), monthly (web-verify credentials) — distinct triggers and checklists per tier
- Version control as knowledge history: git commit after each compilation run gives full rollback and diff capability

## Applicable Patterns for JVTO Wiki

1. **Typed ingestion (Workflow 4)** — declare source type (web-clip, pdf-doc, ssot-update, review-feed, press-clip) before Workflow 1; each type has defined extraction targets and default wiki pages to update
2. **Compilation profiles (Workflow 5)** — named profiles (aeo, website-copy, faq, social, slide-deck) specify which wiki pages to draw from, output format, voice constraints, and filename convention
3. **Tiered health checks (Workflow 6)** — on-demand replaces Workflow 3 (Lint); weekly adds stale sweep + index/log completeness; monthly adds credential web-verification + review count delta

## Not Applicable

- Multi-agent setups (single LLM session workflow)
- MCP server integration (CLAUDE.md-only implementation chosen)
- Cross-vault linking (single vault)
- Automated/scheduled triggers (CLAUDE.md-only; no scripts)

## Related Pages

- -> [[ops/ingestion-profiles]] (Workflow 4, derived from this source)
- -> [[ops/compilation-profiles]] (Workflow 5, derived from this source)
- -> [[ops/health-checks]] (Workflow 6, derived from this source)
