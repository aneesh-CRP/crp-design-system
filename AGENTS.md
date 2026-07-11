# AGENTS.md — crp-design-system

> Cold-start orientation for an AI coding agent. Snapshot 2026-07-11. System-wide context: see `AGENTS.md` + `docs/CRP-SYSTEM-MAP.md` in the **crp-unified-dashboard** repo.

## What this is

The canonical CRP design system — brand tokens, a 60+ component contract, and a helper library. **Pure static HTML/CSS/JS, no build toolchain, no `package.json`.**

Core files: `colors_and_type.css` (tokens) · `components.css` · `src/ds.js` (the `window.ds` helpers) · `manifest.json` + `DOCTRINE.md` (machine + human source of truth) · `SKILL.md` (Claude skill manifest) · `preview/` · `ui_kits/` (React-JSX reference) · `brand/`. It also stores standalone marketing/exec artifacts: `crp-prospecting-*.html` (sponsor decks), `executive-overview.html`, `landing-page-source.html`.

## How it's consumed

This repo is the **upstream of a git submodule**. Both `crp-unified-dashboard` and `crp-finance-dashboard` mount it at `design-system/` (via `.gitmodules`). Standalone HTML pages `<link>` its stylesheets rather than redeclaring tokens.

- **The sync workflow lives consumer-side, not here:** `crp-unified-dashboard/design-system/SYNC.md` describes the "drop a zip → additive merge → two commits (submodule pointer, then parent bump)" flow. An agent editing tokens must know that flow.
- `crp-architecture-share` and `crp-training-wt` carry **flat copies** of the DS CSS (not the submodule), so token changes there must be re-copied manually.
- No build step by design (`CONSUMING.md`: "Out of scope: npm package"). Lint enforcement (`ds-tag-must-exist`, `ds-no-inline-style-on-tagged`, `ds-chip-must-use-helper`, `no-neutral-gray`) runs in the **consumer's** `scripts/lint.js` against this repo's `manifest.json`.

## Git & sensitivity

Remote `github.com/aneesh-CRP/crp-design-system`, branch `main`. ⚠ **Local `main` is ~4 commits ahead of origin** (unpushed Jul-1 prospecting-deck / study-brief work) — flag before cloning.

- **Design tokens / components / helpers are safe** to expose to an external agent.
- ⚠ **The `crp-prospecting-*.html` decks are competitively sensitive** — they name specific sponsors/protocols CRP is targeting (Akero, Arrowhead, BMS, Boehringer, Madrigal, Merck, NewAmsterdam, Novartis) and coordinators. Internal marketing, **not public**.

**Verdict:** handoff-ready for design/component work; warn the agent about the unpushed commits and keep the prospecting decks internal.
