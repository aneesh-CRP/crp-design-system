# Token Automation — Style Dictionary

**Audience:** Claude Code in `crp-unified-dashboard`.
**Goal:** one JSON token source generates CSS for all three surfaces (dashboard, landing, design system), ending drift permanently.

## 1 · Install

```bash
npm i -D style-dictionary
```

## 2 · Source of truth — `design-system/tokens.json`

Translate `design-system/tokens.css` `:root` into nested JSON. Excerpt (follow this shape for all 127 tokens):

```json
{
  "color": {
    "crp": {
      "navy":   { "value": "#072061" },
      "blue":   { "value": "#1843AD" },
      "cyan":   { "value": "#A2DCEB" },
      "orange": { "value": "#FF9933" }
    },
    "fg": {
      "1": { "value": "#072061" },
      "2": { "value": "#3d5373" },
      "3": { "value": "#5e7694" }
    },
    "success": { "value": "#059669" },
    "danger":  { "value": "#dc2626" },
    "warning": { "value": "#f59e0b" }
  },
  "size": {
    "space": { "1": { "value": "4px" }, "2": { "value": "8px" } },
    "radius": { "sm": { "value": "6px" }, "pill": { "value": "999px" } }
  },
  "font": {
    "sans":   { "value": "'Area Normal', -apple-system, 'Segoe UI', 'IBM Plex Sans', Arial, sans-serif" },
    "script": { "value": "'Market Pro', 'Caveat', cursive" },
    "mono":   { "value": "'IBM Plex Mono', ui-monospace, monospace" }
  },
  "motion": {
    "ease-out": { "value": "cubic-bezier(.2,.8,.2,1)" },
    "dur-fast": { "value": "150ms" }
  }
}
```

## 3 · Config — `style-dictionary.config.js`

```js
module.exports = {
  source: ['design-system/tokens.json'],
  platforms: {
    designSystem: {
      transformGroup: 'css',
      buildPath: 'design-system/',
      files: [{ destination: 'tokens.generated.css', format: 'css/variables',
                options: { selector: ':root' } }]
    },
    dashboard: {
      transformGroup: 'css',
      buildPath: './',
      files: [{ destination: 'styles.tokens.css', format: 'css/variables',
                options: { selector: ':root' } }]
    },
    landing: {
      transformGroup: 'css',
      buildPath: 'landing-pages/phillyresearch/css/',
      files: [{ destination: 'tokens.generated.css', format: 'css/variables',
                options: { selector: ':root' } }]
    }
  }
};
```

## 4 · Naming map

Style Dictionary outputs `--color-crp-navy`; the codebase uses `--crp-navy`. Two options:
- **A (preferred):** add a custom `name/cti/kebab-flat` transform that drops the top-level category prefix so output names match today's tokens exactly. ~15 lines; ask me for the transform if needed.
- **B:** keep generated names and append an alias block (`--crp-navy: var(--color-crp-navy);`) — zero risk, slightly uglier.

## 5 · Wire-up

1. `npx style-dictionary build` in CI (or a pre-commit hook alongside `build-appscript.py`).
2. Each surface `<link>`s its generated file FIRST, then its semantic stylesheet.
3. Delete the hand-maintained `:root` blocks once parity is verified (diff generated vs. current computed values — must be identical).
4. Rule going forward: **edit tokens.json only.** Never hand-edit a generated file; never add a raw hex to a semantic stylesheet.

## 6 · Verification

- `getComputedStyle(document.body).getPropertyValue('--crp-navy') === '#072061'` on all three surfaces.
- Screenshot diff before/after on dashboard home, landing home, design-system cards — pixel-identical.
