---
type: ops
title: Compilation Profiles — Workflow 5
last_updated: 2026-05-11
sources: [llm-kb-tooling-guide]
---

# Compilation Profiles

*Workflow 5: state "Use the [profile] profile" before any content generation request.*

Each profile specifies which wiki pages to read, the output format, voice constraints, and the filename convention for saving to `output/`. Always cite the wiki source for every claim in the generated output.

---

## aeo

**Purpose:** Answer Engine Optimization — structured Q&A blocks for AI search ingestion.

**Draw from:** `content/aeo-claims`, `content/faq-master`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- One Q&A pair per block
- Question: ≤15 words, direct (e.g., "Is Java Volcano Tour Operator licensed?")
- Answer: ≤40 words, citable, starts with a direct claim
- Use the NLP atom structure from `content/aeo-claims` (C1–C9) as the template

**Forbidden:** hedging language ("may", "might", "could"), invented statistics, unsourced credential claims

**Output filename:** `output/aeo-YYYY-MM-DD-[topic].md`

---

## website-copy

**Purpose:** Hero paragraphs, section copy, and body text for javavolcano-touroperator.com.

**Draw from:** `content/copy-bank`, `content/brand-voice`, `destinations/[relevant]`, `products/packages-overview`

**Format:**
- Style A voice (direct, evidence-led — see `content/brand-voice` §Style-A)
- Hero: one punchy sentence + one credibility sentence
- Body: 2–4 sentences per paragraph, no bullet lists in hero sections
- All claims must trace to a wiki source; no invented statistics

**Forbidden:** invented statistics, passive voice in hero copy, "safety-focused guide" (use "Tourist Police officer"), superlatives without evidence

**Output filename:** `output/copy-YYYY-MM-DD-[page].md`

---

## faq

**Purpose:** FAQ pages — AEO-compatible, human-readable.

**Draw from:** `content/faq-master`, `products/packages-overview`, `credentials/legal-licenses`, `credentials/trust-signals`

**Format:**
- H3 question heading
- Prose answer: 2–5 sentences, direct, citable
- Each answer ends with a trust signal where relevant (NIB, Trustpilot rating, doctor name)
- Answers must be self-contained — no reliance on adjacent questions for context

**Forbidden:** rhetorical questions, "great question!", invented pricing

**Output filename:** `output/faq-YYYY-MM-DD-[topic].md`

---

## social

**Purpose:** Social media captions, story copy, short-form posts.

**Draw from:** `content/copy-bank`, `reviews/trustpilot-compilation` (for verbatim quotes), `content/brand-voice`

**Format:**
- Style B voice (warmer, still direct — see `content/brand-voice` §Style-B)
- Quote-led: open with a verbatim review excerpt, cite reviewer name if given; or
- Claim-led: open with the strongest differentiator for this post's topic
- ≤280 characters for Twitter/X; ≤150 words for Instagram caption
- End with a call to action or question

**Forbidden:** invented quotes, hashtag spam (≤3 hashtags per post)

**Output filename:** `output/social-YYYY-MM-DD-[topic].md`

---

## slide-deck

**Purpose:** Marp-compatible markdown slide decks for presentations or pitches.

**Draw from:** `wiki/overview` by default + any domain pages specified in the request

**Format:**
- Marp frontmatter: `marp: true`, `theme: default`
- One claim per slide — no bullet walls
- Each slide: headline + ≤30 words of supporting text + one evidence anchor (source, stat, or quote)
- Title slide and summary slide required in every deck

**Forbidden:** slides with >3 bullet points, unsourced claims, placeholder images

**Output filename:** `output/slides-YYYY-MM-DD-[topic].md`
