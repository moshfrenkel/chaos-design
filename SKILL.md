---
name: chaos-design
description: Anti-template visual engine for ANY expressive visual deliverable - websites, landing pages, presentations/decks, images, posters, carousels, stories, thumbnails, social graphics, and video/reels/ads. Forces genuinely different, non-generic results every run by rolling structural constraints instead of letting the model fall back to its "average" (card grids, emoji, centered hero, symmetric stock look).
---

# Chaos Design

An AI defaults to templates because it generates from the statistical **average** of what it has seen. "Rounded card + emoji + centered hero" is always the next-most-likely choice. Real chaos will not happen if *I* choose the structure, because I will choose the average. So this skill **takes the structural decision away from the model** and hands it to a randomizer + a ban-list + a self-audit.

## When it fires
Before producing ANY expressive visual: site, page, deck/presentation, image, poster, carousel, story, thumbnail, social graphic, or video. Skip only for **data-precise** outputs where correctness beats style - functional dashboards, real charts, data tables.

## The method - run it in order, every time

### 1. Seed the mind
Run the `creative-seeds` skill first (this skill assumes it). Pick ONE seed and translate it into a literal **mechanic / motif**, not a mood.

### 2. Pick the medium, then roll the dice
    python "$HOME/.claude/skills/chaos-design/dice.py" <medium>
    # medium = web | deck | image | video | social   (Windows: %USERPROFILE%\.claude\...)
Each medium rolls its own decks. It returns one card per deck plus the hard ban-list. The same brief produces a different scaffold every run. You must obey the roll, even when it is uncomfortable. Re-roll only if a card is technically impossible, never just because it is hard.

### 3. Build against the roll
- REFERENCE anchors the look to something that is NOT a default web/app/stock thing.
- CONTAINER replaces "the card" / "the bullet list".
- ANOMALY is one law the entire piece obeys with discipline.
- INTERACTION / MOTION / SHOT is the single signature behavior or framing.

### 4. Hard rules (on top of the roll)
- Ban-list from dice.py is law. No emoji / icon-fonts / stickers - every decorative element is bespoke art / inline SVG. No stacked rounded cards. No centered-hero+3.
- No two adjacent sections/slides/shots share an archetype.
- Mobile-first for any screen output; enhance up with min-width.
- Self-contained index.html for web, opens automatically, real CTAs.

### 5. Self-audit gate (score >= 8/10 before showing)
Hunt your own AI tells, fix, regenerate the offending part. Rounded-card grid? Emoji? Centered title+paragraph repeated? Two neighboring sections with the same archetype? Perfect symmetry unjustified? Did I obey every rolled card?

## Pairs with
`creative-seeds` (step 1) · `image-generation` · `commercial-director` · `anti-ai-linter`.
