# Landing Site ↔ Design System Migration

**Audience:** Claude Code working in `aneesh-CRP/crp-unified-dashboard`, file `landing-pages/phillyresearch/css/main.css` (and any other landing-page CSS that mirrors it).
**Goal:** Reconcile `main.css` with `design-system/tokens.css` + `design-system/marketing.css` so the landing site and the design system share one token vocabulary, without breaking visual fidelity.

This is a checklist. Apply top-to-bottom. Each item says **why** so you can judge tradeoffs in context.

---

## 0 · Strategy (read before patching)

1. **The landing site is closer to the design system than the dashboard is.** It already uses long-form `--crp-*` token names. The drift is mostly *missing* tokens (success/danger colors, focus ring, type scale variables) and *duplicate* tokens (gradients, shadows, motion) that should now come from `tokens.css`.
2. **Goal: delete the duplicates, keep the landing-only definitions, add the missing ones.** Final `main.css` `:root` should be small — anything in `tokens.css` is removed; only landing-site-specific overrides remain.
3. **Do not rename existing landing classes** (`.hero`, `.btn-primary`, `.section-navy`, etc). They're load-bearing across `home.html`, `about.html`, etc. The migration is at the token level, not the class level.

---

## 1 · Load `tokens.css` before `main.css`

In every landing page's `<head>`:

```html
<link rel="stylesheet" href="/design-system/tokens.css" />
<link rel="stylesheet" href="/landing-pages/phillyresearch/css/main.css" />
```

If `/design-system/` isn't served at that path, copy `tokens.css` into the landing-pages folder and link to it locally — the file is ~250 lines, no JS, safe to vendor.

After this link is in place, every `var(--crp-navy)` / `var(--shadow-md)` / `var(--ease-out)` reference in `main.css` resolves from the shared file. The landing site keeps rendering identically because the values match exactly.

---

## 2 · Delete duplicated `:root` declarations from `main.css`

Inside the `:root { … }` block in `main.css`, **delete** these lines (they're now in `tokens.css` with identical values):

```css
  --crp-navy:   #072061;
  --crp-blue:   #1843AD;
  --crp-cyan:   #A2DCEB;
  --crp-orange: #FF9933;

  --gradient-navy-blue: linear-gradient(135deg, #072061 0%, #1843AD 100%);
  --gradient-cyan-blue: linear-gradient(135deg, #A2DCEB 0%, #1843AD 100%);

  --bg:        #f0f4fa;
  --surface:   #FFFFFF;
  --border:    #c8d6e8;

  --fg-1: #072061;
  --fg-2: #3d5373;
  --fg-3: #5e7694;

  --font-sans: 'Area Normal', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
  --font-script: 'Market Pro', 'Caveat', cursive;

  --shadow-sm: 0 1px 3px rgba(7,32,97,0.06);
  --shadow-md: 0 2px 12px rgba(26,39,68,0.08);
  --shadow-lg: 0 4px 16px rgba(7,32,97,0.10);
  --shadow-hover: 0 4px 16px rgba(24,67,173,0.15);

  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-pill: 999px;

  --ease-out: cubic-bezier(.2,.8,.2,1);
  --dur-fast: 150ms;
  --dur-base: 250ms;
```

Note one **token rename** to fix while you're in there:

- `--fg-2` (`#3d5373`) and `--fg-3` (`#5e7694`) match `tokens.css` exactly — the canonical values are the landing site's darker pair. No change needed.
- `--shadow-hover` was the old name. `tokens.css` calls it `--shadow-hover-blue`. Rename the **two** call sites in `main.css` (`.research-card-v2:hover`, `.blog-card:hover` if present) — or add an alias right after the `<link>`:
  ```css
  :root { --shadow-hover: var(--shadow-hover-blue); }
  ```

Also delete the `@font-face` block at the top of `main.css`. `tokens.css` already declares all six Area weights + Market Pro. Keeping both works but loads the fonts twice — drop the duplicate.

---

## 3 · Replace landing-site `--font-sans` font-stack mismatch

`main.css` had:
```css
--font-sans: 'Area Normal', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
```

`tokens.css` has:
```css
--font-sans: 'Area Normal', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'IBM Plex Sans', Roboto, Arial, sans-serif;
```

Adding `IBM Plex Sans` to the fallback chain matters only when Area Normal fails to load AND the user has IBM Plex installed (rare on consumer machines). No visual regression expected — this is the dashboard fallback creeping into the marketing fallback. Acceptable.

---

## 4 · Adopt the marketing-tier type scale (optional, recommended)

Right now `main.css` hardcodes its heading sizes:
```css
h1 { font-size: 52px; … }
h2 { font-size: 40px; … }
h3 { font-size: 28px; … }
h4 { font-size: 20px; … }
p  { font-size: 18px; … }
```

These match `tokens.css` `--fs-mkt-*` exactly. Optionally tokenize them so a future scale change ripples:

```css
h1, .h1 { font-size: var(--fs-mkt-h1); … }
h2, .h2 { font-size: var(--fs-mkt-h2); … }
h3, .h3 { font-size: var(--fs-mkt-h3); … }
h4, .h4 { font-size: var(--fs-mkt-h4); … }
p       { font-size: var(--fs-mkt-body); … }
```

Same values, just sourced from a token. Skip this if you want to keep the diff minimal; it's nice-to-have, not blocking.

If you adopt `marketing.css` wholesale (`<link>` it after `tokens.css`), you can delete the body, h1-h4, and p rules from `main.css` entirely — they'd be supplied by the design system. **Test thoroughly** before doing this; `marketing.css` and `main.css` overlap on `.section`, `.section-navy`, `.script`, and the hero pair.

---

## 5 · Button recipe — keep `.btn-primary` orange (already correct)

`main.css` `.btn-primary` is already orange — matches the design system. No change needed.

The dashboard's `.btn-primary` is navy and is being renamed to `.btn-action` in `dashboard-migration.md` §4. **Don't worry about the dashboard rename here** — different files, different recipes.

If you want to converge on the design-system marketing button class names (`.btn-mkt-primary`, `.btn-mkt-lg`, etc), that's a bigger refactor: every `<a class="btn btn-primary">` in landing HTML files becomes `<a class="btn-mkt btn-mkt-primary">`. Skip unless explicitly asked. The classes work as-is.

---

## 6 · Status colors (success/danger) — already correct in landing

`main.css` uses `#059669` and `#dc2626` directly in `.benefit-list` and `.risk-list`. These match `tokens.css` `--success` / `--danger`. Optionally tokenize:

```css
.benefit-list  { background: var(--success-bg); border: 1px solid var(--success-border); }
.benefit-list h4, .benefit-list li::before { color: var(--success); }

.risk-list  { background: var(--danger-bg); border: 1px solid var(--danger-border); }
.risk-list h4, .risk-list li::before { color: var(--danger); }
```

Drops 4 hardcoded hexes. Same values.

---

## 7 · Stat / metric / referral numbers

`.stat-number`, `.metric-card .metric-value`, `.referral-amount`, `.diversity-hero .num` all hardcode `color: var(--crp-orange)` — already token-correct. Leave as-is.

---

## 8 · Verification

After patching:

1. **Token resolution.** In DevTools console on `home.html`:
   ```js
   getComputedStyle(document.body).getPropertyValue('--crp-navy').trim() === '#072061'
   getComputedStyle(document.body).getPropertyValue('--shadow-md').includes('0 2px 12px')
   getComputedStyle(document.body).getPropertyValue('--ease-out').includes('.2,.8,.2,1')
   ```
   All three `true`.

2. **No layout shift.** Screenshot home, about, why-crp, sponsors before/after. Pixel-identical except possibly `--fg-2` / `--fg-3` body color (slightly darker) — acceptable, document if asked.

3. **Hero still renders.** Confirm the orange Market Pro script line in the hero loads (not falling back to Caveat). Network tab shows `MarketPro.otf` loaded once, not twice.

4. **Buttons.** `.btn-primary` is orange (#FF9933). `.hero .btn-primary` is white-on-dark. `.btn-navy` is navy.

---

## 9 · Out of scope

- Migrating to `marketing.css` wholesale (§4 paragraph 3). Defer.
- Renaming `.btn-primary` → `.btn-mkt-primary` (§5). Defer.
- Adding viz tokens (`--chart-*`) — landing site has no charts. They're in `tokens.css` and ignored.
- Touching `dashboard-migration.md` work — different file, different team-pass.

---

## Summary diff size

| Section | Lines deleted | Lines added |
|---|---|---|
| §1 `<link>` to tokens.css | 0 | 1 per HTML page |
| §2 Delete duplicated `:root` | ~30 | 0 (or 1 alias for `--shadow-hover`) |
| §2 Delete duplicate `@font-face` | ~7 | 0 |
| §4 Tokenize type scale (optional) | 0 | 5 swaps |
| §6 Tokenize benefit/risk colors (optional) | 0 | 4 swaps |

Net: ~37 deletions, 1 link, optionally ~10 token swaps. No layout regressions expected.
