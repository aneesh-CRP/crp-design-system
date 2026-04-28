---
name: CRP Design System
description: Brand, tokens, typography, and UI-kit components for Clinical Research Philadelphia (phillyresearch.com, joinresearchstudies.com, and the internal CRP Unified Dashboard). Invoke when a design mentions CRP, Clinical Research Philadelphia, phillyresearch, joinresearchstudies, the eligibility funnel, or the unified dashboard.
---

# CRP Design System — Skill

This project is a design system for **Clinical Research Philadelphia, LLC (CRP)**. Use it whenever you are designing for any CRP surface: the marketing site, the eligibility funnel, the internal operations dashboard, email, or decks that represent the brand.

## Before you design

1. **Read `README.md` first** — it is the spine. Content fundamentals (voice, casing, copy examples), visual foundations (colors, type, spacing, shadows, radii, hover/press, animation), logo rules, and a caveats section that lists what the user still needs to supply.
2. **Import `colors_and_type.css`** in every CRP-branded HTML file you produce. It defines the full token set: brand colors (`--crp-navy #072061`, `--crp-blue #1843AD`, `--crp-cyan #A2DCEB`, `--crp-orange #FF9933`), neutrals, semantic status colors, typography scale, shadow + radius tokens, and the Area Normal + Market Pro `@font-face` declarations.
3. **Pull from a UI kit — don't invent components**:
   - `ui_kits/eligibility/` — single-column funnel (`max-width: 520px`), progress bar, step form, big orange CTA. Use for anything patient-facing on `joinresearchstudies.com` or `phillyresearch.com`.
   - `ui_kits/dashboard/` — sticky nav, KPI tiles (`TimeBanner`, `HeroRow`, `KpiTile`), study cards with risk top-border, coordinator workload rows, finance tables, alerts + pills. Use for anything on the internal CRP Unified Dashboard.
4. **Browse `preview/`** for small visual references — swatches, type samples, button states, nav, alerts, shadows, radii, logos, tagline. Each is a single-purpose HTML card mirroring what the Design System tab renders.

## Voice, in one line

> "The future of medicine begins with you."

- **Second-person always** — "you," never "the patient / subject / participant" on conversion surfaces.
- **Sentence case** on marketing; ALL-CAPS eyebrows (letter-spaced) only for density labels on the dashboard.
- **No exclamation marks, no emoji** — warmth comes from the Market Pro script (orange) and photography, not punctuation.
- **Be specific** — `Check your eligibility` not `Learn more`; `Free health screenings, compensation for time and travel.` not `Great benefits!`.

## Visual rules you cannot break

- **Orange (`#FF9933`) is the single accent.** Use it for primary CTAs, Market Pro script, and hand-drawn accent marks. Everything else is navy/blue or neutral.
- **Gradients flow 135° only** (top-left → bottom-right). Max one per page. Approved pairs: Navy→Blue, Cyan→Blue, Orange→Navy.
- **Two density modes.** Marketing = airy (28–44px padding, 16px radius, 520px column). Dashboard = dense (10–14px padding, 6–10px radius, 12–13px tabular text). Don't cross the streams.
- **No colored left-border-accent cards.** Risk is communicated via a 3px colored *top* border (see `StudyCard`) — the left-stripe pattern is an AI-slop tell and off-brand.
- **Shadows are cool-tinted**, never pure black. Navy tint on dashboard (`rgba(7,32,97,0.04–0.10)`), slate tint on marketing (`rgba(26,39,68,0.08)`).
- **Borders are cool** — `#c8d6e8` blue-gray, never neutral gray.
- **No repeating patterns, no textures, no glass-morphism.** The brand is clean and clinical-trustworthy.
- **Photography** is warm-lit, shallow DoF, human-element (hands, shadows). Portraits are cut out onto flat orange or navy fields. We have none in the repo — use gray placeholder blocks and flag it.

## Logos — quick reference

All in `assets/logos/` as both `.svg` and `.png`:

| File | Use |
|---|---|
| `crp-long.svg` | **Primary** horizontal — headers, nav, email signatures |
| `crp-stacked.svg` | Square/tall frames — social avatars, app-store tiles |
| `crp-short.svg` | `CRP` letters + mark — compact contexts |
| `crp-icon.svg` | Mark only — favicons, isolated uses (≥ 25px) |
| `crp-white.svg` | Reversed for navy or photographic backgrounds |

**Never:** recolor, stretch, skew, separate the mark from the wordmark, or use below the minimum size. Minimum safe space around the logo = the height of the "C" in "Clinical".

## Iconography

- **Marketing feature/process callouts:** use the 6 brand SVG icons in `assets/icons/` (checklist, heart, search-plus, arrow-bold, speech, eye) — orange `#FF9933` stroke, 2px, never filled. These are the primary icon voice for `phillyresearch.com` and `joinresearchstudies.com`.
- **Accents/marks:** `assets/accents/` holds 6 hand-drawn orange marks (arrows, sparkle, circle-lasso, ellipse) — use sparingly, one or two per layout, to emphasize a point or scribble over a photo. Never for body copy.
- **When you need something the set doesn't cover:** fall back to **Lucide** at 2px stroke, brand orange, stroke-only.
- **Dashboard:** prefer Unicode status glyphs (↑ ↓ ⇅ · ✓ ✗) and color-pill badges. Use Lucide at 14–16px with `currentColor` only when unavoidable.
- **No emoji. Ever.**

## Quatrefoil stencil

`assets/stencils/quatrefoil.svg` — the brand signature shape for photo or color moments. Apply as CSS `mask`, SVG `clip-path`, or render inline as a filled shape (it uses `currentColor`). Use sparingly — one per layout.

## Copying into a new design

1. Copy `colors_and_type.css` and the logo(s) you need from `assets/logos/`.
2. Copy the relevant UI-kit components (`*.jsx`) and the kit's `*.css` — they load in the order declared in each kit's `index.html`.
3. Keep the React + Babel + colors_and_type.css script/link stack exactly as shown in the kit `index.html` files (pinned versions with integrity hashes).
4. If you need a component the kits don't have, build it from the tokens in `colors_and_type.css` — do not invent new colors or new type ramps.

## Caveats — flag if blocked

Short list of things **still blocked or missing**:
- Staff portraits, environment shots, lifestyle photography — **not in repo**; use flat color blocks and ask.
- Full original brand guidelines PDF (`guidelines/CRP-Brand-Guidelines.pdf`) — referenced but not committed.

Everything else is wired in: Area Normal + Market Pro OTFs in `assets/fonts/`, hand-drawn accent marks in `assets/accents/`, iconography set in `assets/icons/`, quatrefoil stencil in `assets/stencils/`.
