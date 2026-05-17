---
name: wiki-compile
description: Generate JVTO website copy, FAQ, AEO, or social output using the correct compilation profile, then run tool-based verification (voice invariant grep, placeholder scan, price format check, citation check) before writing the file. Use any time content is requested for the website, answer engines, FAQ pages, or social channels. Prevents the generate → review → fix commit cycle by catching violations during generation.
---

## Why this skill exists

Every content generation session ends with a self-reported "0 voice-invariant violations" — but `git log` shows three `fix | website-copy` commits that followed those clean reports. The LLM checks by recall; this skill checks by tool. The verification step runs **Grep against the actual generated text** before the file is written.

---

## When to trigger

Invoke this skill before generating any output that will go into `output/`. Examples:

- "Generate FAQ for Kawah Ijen"
- "Write website copy for the Why JVTO section"
- "Create AEO blocks for police escort"
- "Use the faq profile for Bromo"
- "Write social posts for the screening announcement"
- "Draft homepage copy"
- Any sentence containing: "generate", "write", "draft", "create" + a content type (copy, FAQ, AEO, social, slides)

Do NOT trigger for:
- Wiki page edits (that is Workflow 1/4, not a compilation)
- Health checks (Workflow 6)
- Output refresh of existing files (use wiki-output-refresh instead)

---

## Step 1 — Declare profile

Read the user's request and select one profile from `wiki/ops/compilation-profiles.md`:

| Request signals | Profile |
|---|---|
| FAQ, questions, "how do I", per-destination | `faq` |
| Homepage, page copy, hero, section text | `website-copy` |
| AEO, answer engine, AI search, schema | `aeo` |
| Instagram, Twitter/X, post, caption | `social` |
| Slides, deck, Marp, presentation | `slide-deck` |

State the selection: **"Using [profile] profile."**

If ambiguous, ask: "Which output type — FAQ, website copy, AEO blocks, social, or slides?"

---

## Step 2 — Load sources

Read `wiki/ops/compilation-profiles.md` to get the **Draw from** list for the selected profile.

Read each listed wiki page. Also read any destination/product page named in the request.

**Always read `wiki/content/brand-voice.md` regardless of profile** — this is where the verification rules live.

---

## Step 3 — Generate

Write the complete output following the profile's format rules. Do not truncate or skip sections. Follow all format constraints from the profile.

Do NOT write the output file yet. Hold the text in working memory for verification.

---

## Step 4 — Verify (tool-based — do not skip)

Run each check below using the Grep tool against the generated text. Write the text to a temp path `output/_verify_temp.md` first so Grep can scan it.

### 4A — Forbidden phrase scan

Run these Grep patterns (case-insensitive) against `output/_verify_temp.md`:

| Pattern | What it catches |
|---|---|
| `(?i)blue fire guaranteed` | Over-promise on natural phenomenon |
| `(?i)100% blue fire` | Same |
| `(?i)mandatory health screening` | Must have conditional qualifier |
| `(?i)JVTO provides police escort` | Must include conditional group-size context |
| `(?i)safety.focused guide` | Use "Tourist Police officer" instead |
| `(?i)world.class\|best in class\|unforgettable\|hidden gem\|amazing experience` | Forbidden superlatives |
| `(?i)trust us\|you can count on us\|we care about your safety` | Show-don't-tell violations |

For each match found: record line number, quoted text, and the rule it violates.

### 4B — Price format scan

```
Grep: [$€£]\d|\bRp\s+\d+\.\d|\bUSD\s|\bEUR\s
```

All prices must be `IDR X,XXX,XXX/person`. Any match is a violation.

### 4C — Placeholder scan

```
Grep: \[PLACEHOLDER\]|\[TODO\]|\[INSERT|\[TBD\]|<<<|>>>
```

Zero tolerance. Any match must be filled before finalising.

### 4D — Citation check

Every factual claim in the output must trace to a wiki source. Scan for:
- Trustpilot rating or review count → verify the exact figure matches `wiki/reviews/trustpilot-compilation.md`
- NIB number → must be `1102230032918` exactly
- Doctor's name → must be `Dr. Ahmad Irwandanu`
- Crew count → must match `wiki/people/crew-registry.md` canonical total

Run Grep for `4\.8|4\.9|51 reviews|47 reviews` to find any rating/count claims, then confirm they match the wiki canonical.

### 4E — Ijen-specific conditional check (only if output covers Kawah Ijen)

```
Grep: (?i)(health screening|medical screening|health certificate)
```

Every match must be surrounded by conditional language: "when access rules require", "can require", "coordinates when". A bare "health screening is required" or "health screening is included" is a violation.

---

## Step 5 — Report violations and fix

After all grep checks complete, produce a verification summary:

```
VERIFICATION REPORT
-------------------
4A Forbidden phrases: [N violations / CLEAN]
4B Price format:      [N violations / CLEAN]
4C Placeholders:      [N violations / CLEAN]
4D Citation check:    [N violations / CLEAN]
4E Ijen conditional:  [N violations / CLEAN] (if applicable)

Violations found: [total]
```

If violations > 0:
- Fix each one in the generated text
- Re-run the specific grep check that caught it to confirm fix
- Update the report to show FIXED

If a violation cannot be auto-fixed (e.g., a missing citation requires a wiki page that doesn't exist), flag it explicitly: `⚠ Manual review needed: [description]` and leave a `[NEEDS SOURCE]` marker in the output file.

Delete `output/_verify_temp.md` after verification completes.

---

## Step 6 — Write and log

Write the verified output to `output/` using the profile's filename convention with today's date.

Add frontmatter:
```yaml
---
profile: [profile name]
output_date: YYYY-MM-DD
status: draft
sources: [list of wiki pages read]
verification: PASS | PASS (N fixed) | MANUAL REVIEW NEEDED
---
```

Update `output/INDEX.md`: add a row for the new file.

Append to `wiki/log.md`:
```
## [YYYY-MM-DD] output | [profile] — [topic]
Profile: [name]. Output: [filename]. [N] sections. Voice invariant verification: [PASS/PASS with N fixes]. Sources: [list].
```

---

## Tools required by this skill

| Tool | Role | Status |
|---|---|---|
| `Grep` | 4A–4E verification scans — the entire verification step depends on this | Built-in, always available |
| `Read` | Load brand-voice.md dynamically so rules stay current as invariants evolve | Built-in, always available |
| `Write` | Write temp file for grep scan, then write final output | Built-in, always available |
| `Edit` | Fix violations in-place after detection | Built-in, always available |
| `WebFetch` / `WebSearch` | **Enhancement**: when output cites Trustpilot count or NIB status, fetch the live value to confirm the citation is not stale before publishing | Deferred — load via ToolSearch before using |

### WebFetch verification protocol (optional but recommended for website-copy and aeo profiles)

If the generated output cites:
- Trustpilot review count or rating → fetch `https://www.trustpilot.com/review/javavolcano-touroperator.com` and confirm count matches
- NIB 1102230032918 → check if OSS Indonesia is accessible and confirms active status

Only run WebFetch verification if the user is generating content for imminent publishing (not internal drafts). If WebFetch is unavailable or blocked, note in the verification report: `⚠ Live stat verification skipped — confirm Trustpilot count manually before publishing`.

---

## Self-check: did the verification actually run?

Before closing, confirm:
- [ ] Grep was called at least once (not self-reported — tool was invoked)
- [ ] Violation count is either 0 or each violation has a corresponding fix
- [ ] Output file has `verification:` field in frontmatter
- [ ] Log entry includes verification result
- [ ] `output/_verify_temp.md` was deleted

If Grep was never called, the verification did not run. Do not report PASS.
