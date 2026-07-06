---
name: verify-after-sed-replace
enabled: true
event: bash
pattern: xargs\s+sed\s+-i\s+'s/
action: warn
---

⚠️ **Bulk sed replacement detected.**

After this sed command completes, you MUST immediately run a verification grep to confirm zero remaining matches of the old pattern.

**Required follow-up:**
1. `grep -r 'OLD_PATTERN' TARGET_DIR --include='*.md' | grep -v EXCLUDED_FILES`
2. Expected result: **empty** (no matches)
3. If matches remain, fix them before committing

Do NOT commit until verification grep returns empty. The Phase B restructure missed 12 references because sed ran without post-verification.
