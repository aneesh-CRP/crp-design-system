# CRP Design System

A design system for **Clinical Research Philadelphia, LLC (CRP)** — the brand, tokens, and UI patterns that power `phillyresearch.com`, `joinresearchstudies.com`, and the internal CRP Unified Dashboard.

> *"The future of medicine begins with you."*

---

## Index

| File / folder | What it is |
|---|---|
| `colors_and_type.css` | All brand tokens + semantic type/heading styles — import first |
| `brand-governance.html` | **Start here** — approval matrix, asset downloads, do/don't, review request workflow |
| `study-detail.html` | Full assembled study page (CRP-247) — hero to footer, proves the system holds together |
| `assets/logos/` | Official April-2023 brand kit: `crp-long.svg` (primary horizontal), `crp-stacked.svg`, `crp-short.svg`, `crp-icon.svg`, `crp-white.svg` (reversed). PNG copies at the same names. |
| `assets/fonts/` | Brand webfonts: Area Normal (5 weights + italic) + Market Pro, wired via `@font-face` in `colors_and_type.css` |
| `assets/accents/` | 6 hand-drawn orange accent marks (SVG) — scribble, underline, arrow, sparkle, circle, check |
| `assets/icons/` | 6 website icons (SVG) — patient, clipboard, heart, shield, location, phone |
| `assets/stencils/` | Quatrefoil photo-stencil shape (SVG) |
| `preview/` | Individual swatch / type / component cards shown in the Design System tab (inc. `motion.html`, `accessibility.html`, `states.html`, `data-viz.html`, `email-signature.html`, `layouts.html`) |
| `ui_kits/dashboard/` | React-JSX recreation of the internal operations dashboard |
| `ui_kits/eligibility/` | React-JSX recreation of the `joinresearchstudies.com` eligibility funnel |
| `SKILL.md` | Claude Code / Claude skill manifest for invoking this system |
| `landing-page-source.html` | Source reference — original marketing funnel HTML |

**Sources used:**
- `aneesh-CRP/crp-unified-dashboard @ main` → `new-branding/README.md` (brand guide transcription), `new-branding/logos/*.svg`, `landing-pages/public/index.html`, `styles.css`
- Original brand PDF: `brand/CRP Brand Guidelines.pdf` (April 2023) — committed
- Live sites: https://phillyresearch.com and https://joinresearchstudies.com

---

## Company Context

**Clinical Research Philadelphia, LLC** is a Philadelphia-based clinical trial site running paid research studies across multiple indications (lipid disorders, cardiovascular, metabolic, neuro, etc.). They operate two public surfaces and one internal one:

| Surface | Audience | Purpose |
|---|---|---|
| **phillyresearch.com** | General public | Primary marketing site — "about us", study list, contact |
| **joinresearchstudies.com** | Prospective participants | Eligibility pre-screening funnel — the actual conversion surface, Google Ads lands here |
| **CRP Unified Dashboard** (internal) | Operations, finance, coordinators, PIs | BigQuery-backed operations + finance + recruitment cockpit, Cloud Run behind IAP |

The internal dashboard is a large single-page app (`index.html` + `dashboard.js` built by `scripts/build-appscript.py`) with tabs for recruitment horizons, coordinator workload, study risk matrix, finance (AR, invoices, collections), and retention. All three surfaces must feel like the same company — the brand guide is the spine.

**Legal:** Clinical Research Philadelphia, LLC · 9501 Roosevelt Blvd, Suite 208, Philadelphia, PA 19114 · NJ office 21 Route 31 N, Suite A8, Pennington, NJ 08543 · 215-676-6696.

---

## CONTENT FUNDAMENTALS

CRP's voice is anchored by a single tagline — **"The future of medicine begins with you."** Every piece of copy should feel like a continuation of that sentence.

### Voice attributes
- **Future-facing** but grounded — "what you help unlock" rather than "what we discover"
- **Reassuring, empathetic** — trials are scary; copy does the emotional work of making them feel safe
- **Authoritative without superiority** — the reader is a potential research partner, not a subject
- **Plain-English** — clarity is the #1 virtue; jargon is the #1 failure mode

### Casing & mechanics
- **Sentence case** for headings on marketing pages (mirrors the friendly tone). Internal dashboard uses **ALL-CAPS eyebrows** for data-density (`.card-title`, `.section-label`) — that is a density choice, not a brand choice.
- "Clinical Research Philadelphia" spelled out on first reference; **CRP** is fine afterward
- **"you"** always — never "patient," "subject," or "participant" in conversion copy. *("Check your eligibility" / "See if you qualify")* Internal ops tools may say "participants" because that's the operational term.
- Numbers: use digits for anything ≥ 10 or money (`Over 500 successful trials`, `$75 per visit`)
- Never exclamation marks as emphasis. Use Market Pro script for warmth instead.

### Examples (lifted from live marketing copy)
- ✅ `Check Your Eligibility` (funnel CTA — title case because it's a button label)
- ✅ `See if you qualify for a paid clinical research study near you.`
- ✅ `Free health screenings, compensation for time and travel.`
- ✅ `Over 500 successful trials.`
- ❌ `Enrollment opportunities await qualified subjects!` (too cold, excl. mark, passive)
- ❌ `Learn more` (weak CTA — always specify the next step)

### Emoji & special chars
- **No emoji** in marketing/brand copy. The internal dashboard uses a small set of Unicode status chars (↑ ↓ ⇅ · ✓ ✗) and rule-line box-drawing glyphs (`═══`) inside CSS comments — internal convention only.
- Bullets: `—` em-dashes or typographic bullets `•`; never `-` hyphens.

---

## VISUAL FOUNDATIONS

### Colors
The brand runs on a tight four-color palette — **Navy (`#072061`)**, **Blue (`#1843AD`)**, **Cyan (`#A2DCEB`)**, **Orange (`#FF9933`)** — with extended neutrals for UI (`#f0f4fa` page, `#c8d6e8` borders, `#4a6080` muted text). Semantic status uses emerald green, amber, red. See `colors_and_type.css` for the full list. **Orange is the single accent color** — it marks CTAs, warmth, and anything hand-drawn (Market Pro script, sparkles, arrows).

### Gradients
Flow **top-left → bottom-right** (`135deg`). Approved pairs: Cyan→Blue, Navy→Blue, Orange→Navy. Used **sparingly** — the brand guide says no more than once per page. The dashboard uses the Navy→Blue gradient only on the modal header. The marketing hero uses it full-bleed behind the H1.

### Typography
- **Primary:** Area Normal (licensed, wired in via `@font-face` from `assets/fonts/Area_*.otf`). Headlines SemiBold 48pt; sub-headlines ExtraBold 36pt; body Regular 15pt.
- **Secondary:** Market Pro Regular (licensed, wired in from `assets/fonts/MarketPro.otf`) — handwritten, **always in orange `#FF9933`**, sparingly, never for body.
- **Digital fallback:** System stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif`) for email.

### Spacing & density
4-px base grid. Marketing is **low-density, airy** (`padding: 28px–44px`, `max-width: 520px` funnel). Dashboard is **high-density** (`padding: 10–14px`, `font-size: 12–13px` for tabular data, `gap: 8–12px`) — this is intentional: it's an operator tool, not a reading surface.

### Backgrounds, imagery & pattern
- **No repeating patterns or textures.** The brand is clean, modern, restrained.
- **No hand-drawn illustrations as backgrounds** — the hand-drawn vocabulary is reserved for small accent marks (arrows, sparkles, circles) over photography.
- **Photography is warm-lit, shallow depth-of-field, human-element** (hands, shadows, reflections). Never cold or clinical.
- **Portraits** are cut out and placed on solid brand orange or navy backgrounds — a deliberate flat-color-field treatment.
- **Stencil masks** in the quatrefoil-mark shape can clip photos for multi-image layouts (brand guide).

### Animation
- Subtle. Durations 150–400ms. Ease `cubic-bezier(.2,.8,.2,1)` (natural out-ease).
- Dashboard modal uses an 18px slide-up + fade (`@keyframes slideUp`). Cards use hover-lift (`translateY(-1px)` + shadow bump). No bounces, no spring overshoots.
- Spinners for loading, never skeletons-with-shimmer — dashboard is data-heavy, keep it calm.

### Hover & press states
- **Links:** underline on hover (marketing); color shift to `--crp-blue` (dashboard)
- **Buttons:** 
  - Primary (orange): darker orange `#e6872e` + `translateY(-1px)` + warm shadow `rgba(255,153,51,.3)`
  - Secondary (navy): darken to `#0f2f7a`
  - Ghost: fill `var(--surface-2)` on hover
- **Cards (clickable):** border-color → `--crp-blue`, lift `translateY(-1px)`, shadow-lg
- **Press:** no explicit shrink; rely on browser default `:active`

### Borders & rules
- Card borders: `1px solid var(--border)` — `#c8d6e8`, a muted blue-gray. Never pure gray; always cool.
- Dividers inside tables: `#f1f5f9` (very subtle).
- Section-label rules: a single 1px line running off the right of an uppercase eyebrow label.
- **Never** use colored left-borders on cards as the only accent (avoid the "AI slop" trope). When a card communicates risk, it uses a **3px colored top-border** (`.study-card.risk-critical`) instead.

### Shadows
Two systems run in parallel:
- **Cool navy tint** on dashboard: `0 1px 3px rgba(7,32,97,0.04)` → `0 4px 16px rgba(7,32,97,0.10)` for hover
- **Cool slate tint** on marketing: `0 2px 12px rgba(26,39,68,0.08)` (softer, more marketing-feel)
Never use pure-black shadows.

### Radii
Stepped: `4 / 6 / 8 / 10 / 12 / 16` with a `pill` (999px) for badges. Marketing = 10–16px; dashboard = 6–10px. Larger = more marketing; smaller = more ops.

### Transparency & blur
- Modal backdrop: `rgba(7,32,97,.45)` with `backdrop-filter: blur(3px)` — navy-tinted, never black.
- Setup overlay: `rgba(15,23,42,0.85)` + `blur(4px)` — for gated onboarding.
- Transparency used **only** for overlays and disabled states. Not for glass-morphism panels — that would conflict with clinical trustworthiness.

### Cards
- `background: var(--surface)` + `border: 1px solid var(--border)` + `border-radius: 10px` + `padding: 14px` + `box-shadow: var(--shadow-sm)`
- Hover: shadow grows to `--shadow-lg`, border shifts blue
- Marketing cards are larger (28px padding, 16px radius, softer shadow)

### Corners & iconography as a system
Corners are consistently round (never sharp except in full-bleed gradient hero sections). Iconography is small-scale and **orange-only** when in the brand-accent voice (website feature-callouts); in the dashboard it uses neutral Unicode + inline color-on-status.

### Layout rules
- Marketing funnel: single-column, `max-width: 520px`, centered. Progress bar at top.
- Dashboard: `max-width: 1800px`, sticky nav (`min-height: 40px`), grid of cards (`.grid-2`, `.grid-3`, `.grid-4`).
- Dark-mode is supported in the dashboard only, via `[data-theme="dark"]`. Marketing is light-only.

---

## ICONOGRAPHY

CRP does **not** ship a proprietary icon font. Per the brand guide, website iconography is "small-scale" and **always in brand orange `#FF9933`** — described as a limited set: *checklist, heart, search+, arrows, speech bubble, eye*. These are used on the marketing website for feature/process callouts only.

### Current state in code
- The **landing page** (`joinresearchstudies.com`) uses zero iconography — it relies on type hierarchy and the progress bar for visual interest. This is intentional: a conversion funnel wants the eye on CTAs, not ornament.
- The **dashboard** uses a **small set of Unicode characters** as icons (↑ ↓ ⇅ · ✓ ✗ + arrows · ↗ for drill-hints). Status is communicated through color + pill shape, not icon.
- No SVG icon system, no icon font, no PNG sprites in the repo.

### Recommendation for this design system
- **Marketing surfaces:** use **Lucide** (CDN: `https://unpkg.com/lucide@latest`) with brand-orange `#FF9933` stroke, 2px weight. Lucide's stroke-based look matches the "clean / clear" CRP voice. This is a **substitution** — flag below.
- **Dashboard:** keep Unicode + color-pill status. If an icon is unavoidable, use Lucide at 14–16px with `currentColor` so it inherits the semantic color.
- **Hand-drawn accent marks** (arrows, sparkles, circles from the brand guide) should be real SVG assets — the brand guide mentions them but they are not in the repo. **Flagged** — we have not recreated them.

### Emoji usage
Never. Not in marketing, not in product, not in email.

---

## Logo rules (recap from brand guide)

- Minimum safe space = height of the "C" in "Clinical"
- Never stretch, skew, or recolor
- Only exists in **full-color** (navy + orange accents), **white** (dark bg), or **navy** (single-color contexts)
- Minimum mark width: 25px
- Variants: **Stacked** (primary), **Long** (horizontal), **Short** ("CRP" + mark), **Icon** (mark only)
- Don't separate the mark from the wordmark — use the Icon variant instead
- **Files in this kit** (provided by client, April 2023 brand refresh):
  - `crp-long.svg` — icon + "Clinical Research Philadelphia" horizontal, **primary** for headers / nav
  - `crp-stacked.svg` — icon over wordmark stacked on two lines, for square / tall frames
  - `crp-short.svg` — "CRP" letters + icon, for compact contexts
  - `crp-icon.svg` — 4-way interlocking mark only, for favicons / isolated uses (≥ 25px)
  - `crp-white.svg` — reversed horizontal for navy / photographic backgrounds

---

## Caveats & things the user should supply

1. **Area Normal font (primary brand typeface)** — ✅ supplied by user (`assets/fonts/Area_*.otf`) and wired in via `@font-face`. Weights available: 200 (Thin), 400 (Regular + Italic), 600 (SemiBold), 700 (Bold), 800 (ExtraBold).
2. **Market Pro OTF** — ✅ supplied by user (`assets/fonts/MarketPro.otf`).
3. **Hand-drawn accent marks** — ✅ recreated from the brand PDF. See `assets/accents/` (6 SVG marks: scribble, underline, arrow, sparkle, circle, check) and `preview/accents.html`.
4. **Iconography set** — ✅ recreated from the brand PDF. See `assets/icons/` (6 SVG icons: patient, clipboard, heart, shield, location, phone) and `preview/icons.html`.
5. **Quatrefoil stencil** — ✅ recreated from the brand PDF. See `assets/stencils/quatrefoil.svg` and `preview/stencil.html`. Used as a `clip-path` or `mask` for photo/color moments.
6. **Photography library** — we have no approved staff portraits, environment shots, or lifestyle photography. All photographic moments in the UI kits are placeholder color-blocks.
7. **Full brand guidelines PDF** — ✅ committed at `brand/CRP Brand Guidelines.pdf`.

## Recent additions (Apr 2026)

Filled the previously-flagged coverage gaps:
- **Motion spec** (`preview/motion.html`) — full duration + easing token set with live samples. Added `--dur-instant`, `--dur-deliberate`, `--ease-in-out`, `--ease-spring` to `colors_and_type.css`.
- **Accessibility card** (`preview/accessibility.html`) — WCAG 2.2 contrast audit across the primary palette pairs, focus-ring token (`--ring`, `--ring-color`, `--ring-halo`) with `:focus-visible` utility, hit-target minimums. Flags white-on-orange as a known AA failure on the live site.
- **Component states** (`preview/states.html`) — default / hover / focus / active / disabled / error across buttons, inputs, cards, checkboxes.
- **Data-viz tokens** (`preview/data-viz.html`) — categorical (6-series, starts on brand navy), sequential navy ramp, diverging red-neutral-green. Chart chrome tokens (`--chart-grid`, `--chart-axis`, etc.).
- **Email signature** (`preview/email-signature.html`) — table-based HTML template (full + minimal variants), Arial fallback, 3px orange divider, tagline always included.
- **Marketing layout patterns** (`preview/layouts.html`) — Hero, 3-up feature grid, 50/50 split, testimonial, cyan CTA band, study-list rows. Composition rules below.
- **Forms** (`preview/forms.html`) — funnel-step pattern, full input/select/textarea/consent set, error + help text.
- **Tables** (`preview/tables.html`) — dense dashboard ops table (sortable, toolbar, pagination) + sparse marketing info table.
- **Toasts & notifications** (`preview/toasts.html`) — toasts, persistent banners, destructive modal, inline undo bar; escalation rules.
- **Dark mode** (`preview/dark-mode.html`) — token map (light→dark), live sample, drop-in CSS block for `[data-theme="dark"]`.
- **Copy library** (`preview/copy-library.html`) — CTAs, section headers, error messages, empty states, reusable phrases.
