---
name: chaos-design
description: Anti-template visual engine for ANY expressive visual deliverable - websites, landing pages, presentations/decks, images, posters, carousels, stories, thumbnails, social graphics, and video/reels/ads. Forces genuinely different, non-generic results every run by rolling structural constraints instead of letting the model fall back to its "average" (card grids, emoji, centered hero, symmetric stock look). Triggers - "תעשה אתר/מצגת/פוסטר/תמונה/סרטון", "כאוס עיצובי", "משהו אחר לגמרי", "build a site/deck", "design an image/poster/carousel", "make a video/reel/ad", or any request whose output is a visual the user will look at. Do NOT use for data-precise visuals (functional dashboards, real charts/graphs, data tables) where accuracy beats expression.
---

# Chaos Design

An AI defaults to templates because it generates from the statistical **average** of what it has seen. "Rounded card + emoji + centered hero" is always the next-most-likely choice. Real chaos will not happen if *I* choose the structure, because I will choose the average. So this skill **takes the structural decision away from the model** and hands it to a randomizer + a ban-list + a self-audit.

## When it fires
Before producing ANY expressive visual: site, page, deck/presentation, image, poster, carousel, story, thumbnail, social graphic, or video. (The global CLAUDE.md rule makes this automatic.) Skip only for **data-precise** outputs where correctness beats style - functional dashboards, real charts, data tables.

## The method - run it in order, every time

### 1. Seed the mind
Run the `creative-seeds` skill first (this skill assumes it). Pick ONE seed and translate it into a literal **mechanic / motif**, not a mood. (Seed: "a clock runs faster when unwatched" -> an element that mutates while off-screen, or a slide motif that decays as the deck progresses.)

### 2. Pick the medium, then roll the dice
```bash
python "$HOME/.claude/skills/chaos-design/dice.py" <medium>
# medium = web | deck | image | video | social     (Windows: %USERPROFILE%\.claude\...)
```
Each medium rolls its own decks (e.g. web rolls INTERACTION+CONTAINER; image rolls SHOT+SUBJECT; video rolls MOTION). It returns one card per deck plus the hard ban-list. **The same brief produces a different scaffold every run - that is the whole point. You must obey the roll**, even when it is uncomfortable. Re-roll only if a card is technically impossible, never just because it is hard.

### 3. Build against the roll
- **REFERENCE** anchors the look to something that is NOT a default web/app/stock thing (a poster, a ticket, a heart monitor). Design like that object.
- **CONTAINER** replaces "the card" / "the bullet list". For decks: that is how each slide groups info.
- **ANOMALY** is one law the entire piece obeys with discipline.
- **INTERACTION / MOTION / SHOT** is the single signature behavior or framing the whole piece is built around.
- For **image / video**: feed the rolled cards into the `image-generation` skill prompt (gpt-image-2) or the `commercial-director` brief - they become the art-direction, not an afterthought.

### 4. Hard rules (on top of the roll)
- **Ban-list from dice.py is law.** No emoji / icon-fonts / stickers / dingbats - every glyph-like or decorative element is **bespoke art / inline SVG**. No stacked rounded cards. No centered-hero+3. No generic centered-subject stock look.
- **No two adjacent sections / slides / shots share an archetype.** Vary the skeleton, not just the color.
- **Mobile-first** for any screen output; enhance up with `min-width`.
- **Locale (global CLAUDE.md):** `dir="rtl" lang="he"`, no `letter-spacing` on Hebrew, never mix Hebrew+English on one terminal line. Use the user's brand palette only when the brief is one of their brands; otherwise the rolled PALETTE wins.
- Self-contained `index.html` for web, opens automatically, real CTAs.

### 5. Self-audit gate (score >= 8/10 before showing)
Hunt your own AI tells, fix, regenerate the offending part:
- [ ] Any rounded-rectangle card grid/column, or bulleted slide? -> kill it
- [ ] Any emoji / dingbat / sticker / generic icon? -> bespoke art
- [ ] Centered title+paragraph repeated across frames? -> break the rhythm
- [ ] Two neighboring sections/slides/shots with the same archetype? -> re-skeleton one
- [ ] Equal columns / perfect symmetry / stock-centered subject, unjustified? -> make it uneven
- [ ] Did I obey every rolled card, including ANOMALY and REFERENCE?
- [ ] Does it read like the REFERENCE object, not a generic template?
- [ ] Screen output: mobile view clean, nothing clipped, alive?

## Pairs with
`creative-seeds` (idea disruption, step 1) · `image-generation` (the rolled cards become the gpt-image-2 art direction) · `commercial-director` (video brief) · `anti-ai-linter` (final copy+design AI-tell check).

## Lineage / proof
Born from a session that produced 6 sites, each a different paradigm (neon-tech-glitch, dark liquid, light magazine-collage with drag physics, audio-reactive live stage with a synthesized Latin groove, biometric heart-monitor). The ban-list exists because two of those still slipped into rounded-card-columns and emoji - the exact failure this engine now prevents.

## Maintenance
Source of truth is this active folder. After editing, back up to the hub:
`powershell -File "$env:USERPROFILE\.claude\sync-skills.ps1" backup`
