---
name: "copyright-guard"
description: "Use before publishing site copy, blog drafts, or social posts: run bin/copyright-scan to flag copyright-risk patterns (long quotes, lyrics, copyrighted Bible translations, unattributed quotes, unlicensed images). Heuristic screen, not legal clearance."
---

# Copyright Guard

## Purpose
Pre-publish screen that flags copyright-risk patterns in markdown/text drafts so they can be fixed before anything goes live. It does not decide what is copyrighted — it catches the obvious risks fast and suggests the specific fix for each one.

## When to use
Run it on every draft before it is queued or handed to Antonio for publish approval:
- Blog drafts (e.g. RRG daily drafts, Melanated in Tech posts)
- Website copy changes
- Social posts and captions (X, Threads, Instagram, Facebook, LinkedIn)

It is a gate, not a verdict: FLAG findings must be resolved or explicitly accepted by Antonio. It never auto-clears content.

## Tooling
CLI: `bin/copyright-scan <file.md>` (use `-` for stdin). Exit code 1 when any FLAG exists, 0 otherwise. `--json` for machine-readable output. `--allowlist` (or `COPYRIGHT_GUARD_ALLOWLIST` env) adds owned/safe image hosts.

What it checks:
1. **Long verbatim quotes** — block or inline quotes over ~90 words.
2. **Song-lyric patterns** — verse/chorus labels, "lyrics" next to quoted text, repeated refrain lines.
3. **Copyrighted Bible translations** — NIV, ESV, NKJV, NLT and similar near quoted scripture over ~50 words (KJV/WEB/ASV are public domain and pass with a note).
4. **Unattributed quotes** — quoted passages with no attribution within 3 lines.
5. **External images** — hotlinked images from hosts outside the allowlist and known free-license libraries (Unsplash, Pexels, Pixabay, Wikimedia, Openverse).

## Fixing findings
The scanner suggests a fix per finding; the agent applies it:
- Trim long quotes to brief excerpts with attribution, or paraphrase and link the source.
- Lyrics: reference the song title only, or keep a one-line snippet with attribution.
- Long scripture: switch to KJV/WEB for extended passages; keep modern-translation quotes brief and attributed.
- Add missing attribution lines, or remove the quote.
- Replace unlicensed images with owned, licensed, or AI-generated originals.

## Limitations (read this)
- Heuristic screen only — not legal clearance and not legal advice.
- Cannot verify the provenance of unquoted prose; AI-generated text that closely paraphrases a source will not be caught.
- Fair use is fact-specific; thresholds here are screening conveniences, not legal rules.
- When in doubt, leave the material out — or ask Antonio, and for real questions, a lawyer.

## References
- `references/copyright-practices.md` — the standing practices behind these checks.
