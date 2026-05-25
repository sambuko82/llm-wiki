---
name: verify-claudemd-after-restructure
enabled: true
event: bash
pattern: git mv (wiki|output)/
action: warn
---

⚠️ **File move in wiki/ or output/ detected.**

After all moves are complete, verify CLAUDE.md for stale references:

1. **Frontmatter type list** — does the `type:` enum in Frontmatter Conventions include all current types?
2. **Workflow paths** — do Workflow 1-6 instructions reference correct folder paths?
3. **Directory Structure** — does the tree match actual folder layout?
4. **Cross-references** — do any `[[folder/page]]` links point to old paths?

Run: `grep -n 'content/\|ops/' CLAUDE.md` to find potential stale paths.

CLAUDE.md governs all future AI sessions — stale values here silently degrade every conversation.
