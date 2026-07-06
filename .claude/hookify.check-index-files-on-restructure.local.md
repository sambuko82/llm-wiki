---
name: check-index-files-on-restructure
enabled: true
event: bash
pattern: git mv output/
action: warn
---

⚠️ **Output file move detected.**

After all output moves, verify ALL index/catalog files for stale path references:

- `output/INDEX.md` — catalog of all output files with paths
- `output/website/HANDOFF.md` — route-to-file mapping for developers
- `wiki/index.md` — wiki page catalog

Run: `grep -n 'schema/\|faq/\|aeo/\|website/' output/INDEX.md | head -20` to spot stale paths.

In the last restructure, HANDOFF.md was updated but INDEX.md was missed — leaving 30+ stale path entries.
