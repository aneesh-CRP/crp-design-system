# Dashboard ↔ Design System Migration

**Audience:** Claude Code working in `aneesh-CRP/crp-unified-dashboard`
**Goal:** Reconcile `styles.css` (live dashboard) with `design-system/colors_and_type.css` so both surfaces share one token vocabulary, without breaking the dashboard's existing class names.

This is a checklist. Apply top-to-bottom. Each item says **why** so you can judge tradeoffs in context.

---

## 0 · Strategy (read before patching)

1. **Keep all dashboard class names and short token names.** They're load-bearing — `--navy`, `--blue`, `.btn-primary`, `.badge-purple` etc. ship in 280k of `index.html` and 1.6MB of `dashboard.js`. Don't rename them.
2. **Add the design-system long names as aliases**, not replacements. `--crp-navy: var(--navy)` lets design-system-authored CSS work without a rewrite.
3. **Fill the missing token families** (typography scale, spacing, focus ring, chart palette, motion) so future code has them available.
4. **Fix the brand-rule violations** (button color, missing fonts, hardcoded hexes) on a separate, smaller pass.

---

## 1 · Add long-name aliases to `:root` in `styles.css`

Add this block at the **end** of the existing `:root { … }` (right before the `[data-theme="dark"]` block). Pure aliasing — no behavior change.

```css
  /* ═══ Design-system long-name aliases ═══
     Lets design-system CSS (`var(--crp-navy)`, `var(--fg-1)`)
     work alongside legacy short names. Do not remove. */
  --crp-navy:    var(--navy);
  --crp-blue:    var(--blue);
  --crp-cyan:    var(--cyan);
  --crp-orange:  var(--orange);

  --crp-black:      #000000;
  --crp-dark-gray:  #828282;
  --crp-light-gray: #D2D2D2;
  --crp-white:      #FFFFFF;

  --surface-2: var(--surface2);
  --border-2:  var(--border2);
  --fg-1: var(--text);
  --fg-2: var(--muted);
  --fg-3: var(--light);
  /* NOTE: design-system canonical values for --fg-2 / --fg-3 are #3d5373 / #5e7694
     (slightly darker than the dashboard's --muted / --light). If body copy reads
     too light after design-system CSS lands on a dashboard surface, override
     the alias inline rather than changing --muted / --light (which would shift
     every existing dashboard rule). */

  --success:        var(--green);
  --success-bg:     var(--green-bg);
  --success-border: var(--green-border);
  --danger:         var(--red);
  --danger-bg:      var(--red-bg);
  --danger-border:  var(--red-border);
  --warning:        var(--yellow);
  --warning-bg:     var(--yellow-bg);
  --warning-border: var(--yellow-border);
```

Mirror these inside `[data-theme="dark"]` — none needed, because aliases follow whatever the short name resolves to. Verify by checking that `getComputedStyle(document.body).getPropertyValue('--crp-navy')` returns the same value as `--navy` in both themes.

---

## 2 · Add the missing token families to `:root`

The dashboard never defined typography scale, spacing scale, focus ring, chart colors, or extra motion tokens. Add them so design-system code compiles.

```css
  /* ═══ Brand gradients (135deg, top-left → bottom-right only) ═══ */
  --gradient-navy-blue:   linear-gradient(135deg, #072061 0%, #1843AD 100%);
  --gradient-cyan-blue:   linear-gradient(135deg, #A2DCEB 0%, #1843AD 100%);
  --gradient-orange-navy: linear-gradient(135deg, #FF9933 0%, #072061 100%);

  /* ═══ Type scale ═══ */
  --font-sans:   'Area Normal', -apple-system, BlinkMacSystemFont, 'Segoe UI',
                 'IBM Plex Sans', Roboto, Arial, sans-serif;
  --font-mono:   'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, Monaco, monospace;
  --font-script: 'Market Pro', 'Caveat', 'Brush Script MT', cursive;

  --fs-display: 64px;
  --fs-h1:      48px;
  --fs-h2:      36px;
  --fs-h3:      24px;
  --fs-h4:      18px;
  --fs-body:    15px;
  --fs-small:   13px;
  --fs-xs:      11px;
  --fs-micro:   10px;

  --fw-regular:   400;
  --fw-medium:    500;
  --fw-semibold:  600;
  --fw-bold:      700;
  --fw-extrabold: 800;

  --lh-tight:  1.15;
  --lh-snug:   1.35;
  --lh-normal: 1.5;
  --lh-loose:  1.65;

  /* ═══ Spacing (4-based) ═══ */
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;

  /* ═══ Motion additions ═══ */
  --ease-in-out:    cubic-bezier(.4,0,.2,1);
  --ease-spring:    cubic-bezier(.34,1.56,.64,1);
  --dur-instant:    100ms;
  --dur-deliberate: 600ms;

  /* ═══ Focus ring (WCAG 2.2 SC 2.4.11) ═══ */
  --ring-color: #1843AD;
  --ring-halo:  rgba(24,67,173,0.25);
  --ring: 0 0 0 2px var(--ring-color), 0 0 0 5px var(--ring-halo);

  /* ═══ Data viz ═══ */
  --chart-1: #1843AD;  /* brand blue   */
  --chart-2: #FF9933;  /* brand orange */
  --chart-3: #10b981;  /* emerald      */
  --chart-4: #8b5cf6;  /* violet       */
  --chart-5: #f59e0b;  /* amber        */
  --chart-6: #06b6d4;  /* cyan-dark    */

  --chart-seq-1: #E8EEFF;
  --chart-seq-2: #B8C8F0;
  --chart-seq-3: #7B98DC;
  --chart-seq-4: #3A6BC5;
  --chart-seq-5: #1843AD;
  --chart-seq-6: #072061;

  --chart-div-neg-2: #dc2626;
  --chart-div-neg-1: #fca5a5;
  --chart-div-zero:  #f1f5f9;
  --chart-div-pos-1: #86efac;
  --chart-div-pos-2: #16a34a;

  --chart-grid:      #e5ecf5;
  --chart-grid-fine: #f1f5f9;
  --chart-axis:      #7a90b0;
  --chart-axis-line: #c8d6e8;
```

Add an opt-in `:focus-visible` utility right after `:root`:

```css
.focus-ring:focus-visible,
button:focus-visible,
a:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: none;
  box-shadow: var(--ring);
  border-radius: var(--radius-sm);
}
```

---

## 3 · Wire the missing fonts

The `@font-face` block at the top of `styles.css` is missing **Area Thin** and **Market Pro**. Without Market Pro, anywhere `var(--font-script)` resolves it falls through to Caveat or Brush Script — not on-brand.

Add these declarations alongside the existing five:

```css
@font-face {
  font-family: 'Area Normal';
  src: url('/fonts/Area_Thin.otf') format('opentype');
  font-weight: 200; font-style: normal; font-display: swap;
}
@font-face {
  font-family: 'Market Pro';
  src: url('/fonts/MarketPro.otf') format('opentype');
  font-weight: 400; font-style: normal; font-display: swap;
}
```

Confirm `Area_Thin.otf` and `MarketPro.otf` exist under `/fonts/`. They're in the design-system kit at `assets/fonts/` — copy if missing.

---

## 4 · Resolve the button-color conflict (decision: option C)

**The conflict.** Design system says primary buttons are orange (per brand guide: "Orange is the single accent color — it marks CTAs"). Dashboard's `.btn-primary` is navy (`background: var(--accent)` where `--accent: var(--navy)`).

**Decision: keep both, named clearly.**

- `.btn-primary` → **orange** (marketing/conversion surfaces, modal-confirm CTAs, "Save & Submit"). Matches brand guide.
- `.btn-action` → **navy** (dense ops actions, table-row buttons, anything where orange would scream). Internal-only.
- Both share the same shape, padding, height. Color is the only difference.

Replace the existing `.btn-primary` rule with:

```css
.btn-primary {
  background: var(--orange);
  color: #fff;
  border: 1px solid var(--orange);
}
.btn-primary:hover {
  background: #e6872e;
  border-color: #e6872e;
  box-shadow: 0 4px 12px rgba(255,153,51,.3);
}

.btn-action {
  background: var(--navy);
  color: #fff;
  border: 1px solid var(--navy);
}
.btn-action:hover {
  background: #0f2f7a;
  border-color: #0f2f7a;
}
```

**Migration of existing call-sites:**

Most existing `.btn-primary` usages in the dashboard expect navy. Audit before flipping:

```bash
grep -rn 'btn-primary' index.html dashboard.js apps-script.js
```

For each occurrence, decide:
- **Keep `.btn-primary`** if it's a true conversion CTA (rare in ops UI — maybe "Connect Data Source" on the setup overlay).
- **Rename to `.btn-action`** if it's an internal action (most dashboard buttons — "Apply filters", "Export CSV", "Save note", "Resolve").

Don't blanket-rename. Read each call site. The test: would a marketing designer call this a conversion moment? If yes → orange. If it's just "do the thing" → navy.

Also remove the broken `.btn-primary:hover { background: #0284c7; }` — `#0284c7` (sky blue) isn't in the palette. Already overwritten above.

The `.btn-blue` class is fine to keep as a third variant (explicit blue, used by Connect/Setup) — it's already correct.

---

## 5 · Replace hardcoded hexes with tokens

Run `grep -nE '#[0-9a-fA-F]{6}' styles.css` and audit. Most are fine inside CSS variable definitions or vendor-style code blocks. The ones that should be tokenized:

| Hardcoded | File location | Replace with |
|---|---|---|
| `#0f2f7a` (in `.btn-blue:hover`) | styles.css `.btn-blue:hover` | leave (deliberate hover-darken) |
| `#1843AD`, `#072061` (in `.alert-info`, `.pill-maintenance`, `#detail-panel-header`) | various | `var(--blue)`, `var(--navy)` |
| `#7dd3fc`, `#0f172a` | `.guide-card`, `.connect-form` | acceptable — these are dark-on-dark setup UI; document as "setup-overlay only" |
| `#fef3c7`, `#fcd34d`, `#854d0e` | `.avail-pto`, `.setup-note` | leave for now — they're a narrow PTO/note convention not in the system |
| `#dcfce7`, `#059669` (in `.pill-enrolling`) | styles.css | `var(--green-bg)`, `var(--green)` |
| `#fef3c7`, `#b45309` (in `.pill-pre-closed`) | styles.css | acceptable variation; leave with comment |
| Avatar fills `#e74c3c`, `#d63031`, `#fdcb6e` etc. (in `.lf-*`) | styles.css | leave — these are categorical study-flag colors that intentionally aren't from the brand palette |

The point isn't to eliminate every hex — it's to make sure brand colors aren't repeated by hand where a `var(--…)` would do.

---

## 6 · Fix the legacy purple aliases

The dashboard has:
```css
--purple: var(--blue);
--violet: var(--navy);
--violet-bg: #edf0f8;
.badge-purple { background: var(--violet-bg); color: var(--purple); … }
.pill-maintenance { background: var(--blue-bg); color: #1843AD; }
```

Two cleanup options, pick one:
- **Option A (preferred):** Rename `.badge-purple` → `.badge-info` everywhere it's used. Drop `--purple`, `--violet*` aliases. ~12-line diff plus call-site updates in `index.html` / `dashboard.js`.
- **Option B (deferred):** Leave aliases in place but add a top-of-file comment: `/* Legacy aliases — purple/violet exist for back-compat only. New code uses --blue/--navy directly. */`

If touch-cost is high, do B and put A on a follow-up.

---

## 7 · Dark-mode contract

Document in a comment block above the `[data-theme="dark"]` rule that **`--navy` flips meaning** in dark mode (`#072061` → `#a8b8d8`, a light blue for legibility). Design-system contributors who treat `--navy` as a constant will get burned otherwise.

```css
/* ═══ Dark Theme ═══
   IMPORTANT: --navy, --blue, --cyan, --orange are SEMANTIC in this codebase.
   In dark mode --navy resolves to #a8b8d8 (light blue) so dark-mode text is
   legible. If you need the literal #072061 hex regardless of theme, write
   it inline. The aliases (--crp-navy → var(--navy)) follow this same flip.
*/
[data-theme="dark"] { … }
```

---

## 8 · Verification

After the patches above are in, run these sanity checks:

1. **Token lookup:** in DevTools console on a live page,
   ```js
   getComputedStyle(document.body).getPropertyValue('--crp-navy').trim() === '#072061'
   getComputedStyle(document.body).getPropertyValue('--font-sans').includes('Area Normal')
   ```
   both should be `true` in light mode.

2. **No layout shift:** screenshot the dashboard before/after the alias block. Pixel-identical (we only added new tokens; no existing rule changed).

3. **Button audit:** confirm every `.btn-primary` you renamed to `.btn-action` still renders navy and not orange.

4. **Font load:** Network tab shows `Area_Thin.otf` and `MarketPro.otf` requested.

5. **Dark mode:** toggle `[data-theme="dark"]`, confirm `var(--crp-navy)` resolves to `#a8b8d8` (i.e. the alias correctly inherits the flip).

---

## 9 · Out of scope (don't do these in this pass)

- Migrating dashboard typography from `font-size: 12–14px` defaults to the `--fs-*` scale. The dashboard's density choice is intentional; the scale is for marketing surfaces.
- Renaming `--surface2` → `--surface-2`. Aliasing handles both directions.
- Adding `colors_and_type.css` as a separate `<link>`. Single-file `styles.css` is fine; we just need its `:root` to be a superset.
- Moving accents/icons/stencils into the dashboard repo. They live in the design system; only import on demand.

---

## Summary diff size

| Section | Lines added | Lines changed |
|---|---|---|
| §1 Aliases | ~25 | 0 |
| §2 Missing tokens | ~75 | 0 |
| §3 Fonts | ~10 | 0 |
| §4 Button conflict | ~15 | 1 (the broken sky-blue hover) + N call-site renames |
| §5 Hardcoded hexes | ~6 token swaps | 0 |
| §6 Purple aliases | optional | optional |
| §7 Dark-mode comment | ~5 | 0 |

Net: ~135 additions, 1 hard fix, plus a manual button audit. No layout regressions expected from §1–§3.
