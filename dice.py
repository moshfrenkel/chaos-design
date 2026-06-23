#!/usr/bin/env python3
# Chaos Design dice - externalizes structural choices away from the model's "average",
# for ANY visual medium. Run:  python dice.py [medium] [N]
#   medium = web | deck | image | video | social   (default web)
#   N      = number of independent rolls            (default 1)
import random, sys

DECKS = {
  # ---------- shared across most media ----------
  "TYPE": [
    "one giant word per screen, oversized, overflowing the frame",
    "serif display + monospace data, hard clash",
    "vertical / rotated running text",
    "kinetic type (letters move, bob, react)",
    "ransom-note (mixed sizes/weights/styles per word)",
    "variable-weight that thickens on scroll/hover",
    "outline type + solid type interleaved",
    "ALL-CAPS condensed poster type vs tiny captions",
  ],
  "PALETTE": [
    "strict duotone (2 colors only, no greys)",
    "near-monochrome + one violently hot accent",
    "intentional clash / 'ugly on purpose' but confident",
    "black & white + a single spot color",
    "risograph 2-spot overprint (offset, misregistered)",
    "neon on near-black",
    "paper cream + ink black, editorial",
    "high-saturation tropical, no dark mode",
  ],
  "ANOMALY": [   # one weird law the whole piece obeys with discipline
    "everything tilted exactly %d degrees" % random.choice([2,3,4,-3,6]),
    "no horizontal lines anywhere - all edges curve or slant",
    "only circles & arcs, zero rectangles",
    "elements allowed to overflow & be clipped by the frame edge",
    "a recurring hand-drawn mascot / scribble appears throughout",
    "one element is ALWAYS moving / alive on every frame",
    "perfect symmetry is forbidden - every pairing is uneven",
    "a deliberate 'broken' glitch that is clearly intentional",
    "scale play - one thing absurdly large or tiny vs the rest",
    "one common color (e.g. blue) is banned from the whole piece",
  ],
  "REFERENCE": [  # anchor the look to a NON-website / non-default thing
    "Swiss brutalist protest poster",
    "1970s vinyl record sleeve",
    "subway / transit map",
    "punk photocopied zine",
    "kidnapper ransom note",
    "Memphis / 80s postmodern design",
    "tarot card / occult plate",
    "hospital heart-rate monitor",
    "vaporwave shopping mall directory",
    "broadsheet newspaper front page",
    "museum wall / gallery label",
    "retro arcade cabinet / game UI",
  ],
  # ---------- spatial organization (web / deck / social) ----------
  "LAYOUT": [
    "collage / overlapping torn pieces, intentional mess",
    "hard diagonal grid (everything skewed on one axis)",
    "scattered absolute 'playground' (objects float in space)",
    "editorial spread with marginalia & pull-quotes in the gutter",
    "full-bleed kinetic TYPE as the layout (words ARE the design)",
    "radial / circular orbit around one center point",
    "anarchic masonry (wildly unequal blocks, no rhythm)",
    "spatial map / blueprint / floor-plan",
    "brutal asymmetric split (70/30, one side invades the other)",
    "horizontal sideways flow (a journey across a wall)",
  ],
  # info grouping - anything BUT a rounded rectangle card
  "CONTAINER": [
    "torn / ripped paper edges", "sticky notes (rotated, taped)",
    "polaroid photo frames", "ticket stub / boarding pass",
    "speech bubbles", "terminal / window chrome",
    "tags & labels on strings", "handwritten list / checklist",
    "ledger / table / spreadsheet rows", "NO container - bleeds onto the page",
  ],
  # ---------- web only ----------
  "INTERACTION": [
    "physics: drag & throw elements, they collide with walls",
    "audio-reactive: generated sound drives the visuals",
    "scroll-jack scenes that morph between fixed states",
    "cursor-as-tool (marker / spotlight / magnet / eraser)",
    "gyro / tilt parallax (phone movement moves the world)",
    "press-and-hold to reveal / charge / unlock",
    "draw-to-reveal (user paints content into view)",
    "time-decay: elements mutate, rot, or grow over time",
    "beat / pulse sync (everything breathes on one clock)",
    "hover-distortion / liquid warp on contact",
  ],
  # ---------- presentation only ----------
  "SLIDE": [
    "one-word slides, zero bullets ever",
    "oversized numbers / stats as the whole slide",
    "full-bleed image slides alternating with pure-type slides",
    "manifesto slides (a single bold sentence, huge)",
    "asymmetric data slides, content shoved to one edge",
    "a running visual motif that mutates slide to slide",
  ],
  # ---------- image / video framing ----------
  "SHOT": [
    "extreme macro close-up", "dutch / tilted angle",
    "flat-lay top-down", "silhouette / hard backlight",
    "double-exposure", "wide frame with vast negative space",
    "fisheye / lens distortion", "hard direct-flash snapshot",
    "off-center portrait, subject pushed to the edge",
    "impossible scale (subject tiny or giant in the scene)",
  ],
  "SUBJECT": [   # how the subject is treated
    "single hero object, isolated, huge",
    "human cropped hard (only hands / eyes / motion)",
    "texture IS the subject (skin, fabric, surface)",
    "color-isolation (one colored thing, rest desaturated)",
    "motion-blur / long exposure energy",
    "cut-out collage / mixed media",
    "surreal juxtaposition (two things that don't belong)",
    "repetition of one element into a pattern",
  ],
  # ---------- video only ----------
  "MOTION": [
    "whip-pan hard cuts", "match-cut morphs between shots",
    "single unbroken one-take drift", "glitch / datamosh transitions",
    "freeze-frame punches with text stabs", "speed-ramp (slow then snap fast)",
    "kinetic text landing on the beat", "jump-cut staccato rhythm",
    "parallax layers sliding at different speeds", "light & shadow as the transition",
  ],
  # meta-cards that bend the roll itself
  "WILDCARD": [
    "do the deliberate OPPOSITE of one rolled card",
    "merge two cards from one deck into a single hybrid",
    "let the creative-seed override the REFERENCE entirely",
    "add a recurring mascot/character that reacts to the user",
    "one section loudly BREAKS the ANOMALY law, on purpose",
    "collapse it all into ONE uninterrupted scene, no sections",
    "ban the most obvious color for this brand",
    "smash a second LAYOUT into the first halfway through",
  ],
}

MEDIA = {
  "web":    ["LAYOUT","INTERACTION","CONTAINER","TYPE","PALETTE","ANOMALY","REFERENCE","WILDCARD"],
  "deck":   ["SLIDE","LAYOUT","CONTAINER","TYPE","PALETTE","ANOMALY","REFERENCE","WILDCARD"],
  "image":  ["SHOT","SUBJECT","TYPE","PALETTE","ANOMALY","REFERENCE","WILDCARD"],
  "video":  ["MOTION","SHOT","SUBJECT","TYPE","PALETTE","ANOMALY","REFERENCE","WILDCARD"],
  "social": ["LAYOUT","SUBJECT","TYPE","PALETTE","ANOMALY","REFERENCE","WILDCARD"],
}

BAN = [
  "rounded-rectangle cards stacked/gridded in a row or column",
  "hero / opener followed by 3 symmetric feature blocks",
  "ANY emoji, icon-font, sticker, or dingbat - draw bespoke SVG / art instead",
  "a centered title + paragraph (or bulleted list), repeated frame after frame",
  "equal-width columns / evenly-spaced symmetric grids",
  "the same uniform corner-radius / spacing on everything",
  "generic stock-photo look, centered subject, flat even lighting",
]

MUTATORS = [
  ("INVERT",     "do the deliberate opposite of the {k} card"),
  ("MUTE",       "drop the {k} card entirely; force another axis to carry its job"),
  ("EXAGGERATE", "push the {k} card to an absurd, uncomfortable extreme"),
]
def roll(i, medium):
  print(f"========== ROLL {i}  [{medium}] ==========")
  for k in MEDIA[medium]:
    print(f"  {k:12} -> {random.choice(DECKS[k])}")
  # MUTATION step: ~50% chance to twist one already-rolled axis
  if random.random() < 0.5:
    k = random.choice([a for a in MEDIA[medium] if a != "WILDCARD"])
    if random.random() < 0.5:
      print(f"  MUTATION     -> DOUBLE {k}: force it to coexist with '{random.choice(DECKS[k])}'")
    else:
      name, txt = random.choice(MUTATORS)
      print(f"  MUTATION     -> {name} {k}: " + txt.format(k=k))
  else:
    print("  MUTATION     -> (none this roll)")
  print()

if __name__ == "__main__":
  args = sys.argv[1:]
  medium = "web"; n = 1
  for a in args:
    if a in MEDIA: medium = a
    elif a.isdigit(): n = int(a)
  for i in range(1, n + 1):
    roll(i, medium)
  print("---- HARD BAN-LIST (auto-fail if present) ----")
  for b in BAN: print("  x " + b)
  print("\nObey the roll. No two sections/slides/shots alike. Mobile-first for screens. RTL Hebrew. Bespoke art only.")
