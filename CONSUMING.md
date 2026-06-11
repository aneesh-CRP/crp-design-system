# Consuming the CRP Design System

This package is the canonical source for the CRP design language — tokens,
components, helper library, vocabulary, lint rules. Both
`crp-unified-dashboard` and `crp-finance-dashboard` consume it as a git
submodule. Future consumers (mail templates, eligibility funnel, sponsor
portfolio) will too.

## What's here

| File / dir | What | Status |
|---|---|---|
| [DOCTRINE.md](DOCTRINE.md) | Locked v1.0 component contract — 60+ components, vocabulary, formats, behavior, a11y, enforcement | Source of truth |
| [manifest.json](manifest.json) | Machine-readable mirror of DOCTRINE §2 — read by lint + audit | Source of truth |
| [components.css](components.css) | Canonical CSS for new component classes (chips, pills, dots, alerts, KPI tile, filter bar, state surfaces, toast, site-tag, purpose-badge) | Source of truth |
| [colors_and_type.css](colors_and_type.css) | Brand tokens — colors, typography scale, spacing, radii, shadows, motion, focus ring, chart palette | Source of truth |
| [src/ds.js](src/ds.js) | Helper library — emits tagged HTML for every component (19 helpers on `window.ds`) | Source of truth |
| [README.md](README.md) | Friendly overview of the system | Reference |
| [SKILL.md](SKILL.md) | Claude-skill manifest for design tasks | Reference |
| [preview/](preview/) | One HTML card per token / component for visual reference | Reference |
| [ui_kits/](ui_kits/) | React-JSX kits mirroring the dashboard + eligibility surfaces | Reference |
| [brand/](brand/) | Brand PDF + master assets | Reference |

## Adding to a new project (git submodule)

```sh
cd <consumer-repo>
git submodule add git@github.com:aneesh-CRP/crp-design-system design-system
git commit -m "chore: add design-system submodule"
```

For consumers without CI, the deploy script must run `git submodule update --init`
or commit the submodule contents directly into `server/public/` so Cloud Run
serves them.

## Wiring it into HTML

```html
<head>
  <link rel="stylesheet" href="design-system/colors_and_type.css">
  <link rel="stylesheet" href="design-system/components.css">
  <script src="design-system/src/ds.js" defer></script>
</head>
```

After the script loads, `window.ds` is available globally:

```js
ds.chip({ variant: 'success', text: 'Completed' })
ds.button({ variant: 'primary', label: 'Send', dataAction: 'send-batch' })
ds.siteTag({ site: 'pnj' })
ds.alert({ variant: 'warning', title: 'Heads up', body: '...' })
```

Full helper inventory: see [DOCTRINE.md §2](DOCTRINE.md#§2-component-manifest).

## Lock + lint enforcement

Three lint rules belong with the doctrine and live in
`crp-unified-dashboard/scripts/lint.js` (the dashboard's lint host).
A consumer that wants the same enforcement should copy those rule
implementations or invoke the dashboard's lint as a sibling. They
require `manifest.json` from this submodule to validate `data-ds`
values, so they auto-pick up new components when the submodule is
updated.

The three rules are:
- `ds-tag-must-exist` — every `data-ds="X"` value must be in manifest.json
- `ds-no-inline-style-on-tagged` — tagged elements can't have inline color/bg/font/padding/margin styles
- `ds-chip-must-use-helper` — `class="chip..."` must pair with `data-ds="chip"` (i.e., come from `ds.chip()`)

Trailing comment `// design-lock-legacy: <reason>` opts a line out (transitional).

## Updating the design-system from a consumer

```sh
cd <consumer-repo>/design-system
# edit files
git add -A && git commit -m "feat(ds): ..."
git push origin main
cd ..
git add design-system   # records the new submodule SHA
git commit -m "chore: bump design-system submodule"
```

Both consumers must bump their submodule SHA to receive the change.

<!-- deep-review f303: document the unified-dashboard mirror so edits here get resynced -->
## Mirrored copies in crp-unified-dashboard (manual resync required)

`crp-unified-dashboard` serves a **tracked mirror** of a subset of these
files under `server/public/crp-design-system/` (the deployed
`it-presentation.html` deck loads them from there):

- `it-presentation.js` — deck behavior script (canonical copy lives HERE)
- `crp-logo-white.svg` — white cover logo (canonical copy lives HERE)
- `colors_and_type.css` / `components.css` — token + component CSS

The mirror is **never auto-synced** (same policy as the finance mirror).
After editing any of these files in this repo, manually copy the changed
file into `crp-unified-dashboard/server/public/crp-design-system/` and
commit it there, or the deployed deck silently diverges from canonical.

`social-posts/` (Instagram/social HTML mockups) lives only in this repo —
it has no mirror and no other copy anywhere; do not delete it.

## Out of scope (for now)

- npm package distribution — the system is self-contained HTML/CSS/JS so
  npm doesn't add value yet; reconsider if the JS layer grows complex
  enough to want a build step or TypeScript types.
- React/Vue component bindings — the helpers return HTML strings; framework
  bindings can be added later as a sibling package.
