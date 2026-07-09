# Design System Sync Rules (for Claude Code)

When the user drops a design-system zip into a session and says "sync design system",
apply these rules with no further instruction needed.

## Merge rules — additive, never destructive

1. **Target:** `design-system/` (the submodule). Unzip over it.
2. **Keep untouched** (build/lint dependencies, repo-side only): `src/`,
   `components.css`, `manifest.json`, `DOCTRINE.md`, and anything not present
   in the zip.
3. **Add or overwrite from the zip:** `tokens.css`, `marketing.css`,
   `colors_and_type.css`, `templates/`, `ui_kits/`, `assets/`, `preview/`,
   `README.md`, `SKILL.md`, `brand-governance.html`, `study-detail.html`,
   `*-migration.md`, `style-dictionary.md`.
4. **Never commit:** `scratch/`, `uploads/`, `claude-code-paste.txt`,
   `_ds_manifest.json`, `_ds_bundle.js`, `_adherence.oxlintrc.json` —
   workspace-internal artifacts.
5. **Commits:** two, in order — (a) inside the submodule repo, (b) pointer
   bump in the parent. Push submodule first, then parent.
6. **Do not** execute the migration docs during a sync — they are separate,
   explicitly-requested tasks with their own stop-points.
7. **Verify after:** `scripts/build.py` and `scripts/lint.js` still pass.

## Source of truth

- Brand tokens: `design-system/tokens.css` — new tokens go there, never
  inline in `styles.css` or `main.css`.
- New pages start from `design-system/templates/` — never from blank.
- Voice/copy: `design-system/README.md` + `preview/copy-library.html`.
