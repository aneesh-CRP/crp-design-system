# CRP Design System — Doctrine

> **Purpose.** This file is the contract that makes the CRP dashboard, eligibility funnel, marketing site, email, and SMS feel like one product. Every visible element on every surface must reference an entry below. Anything not in this file is, by definition, off-doctrine.
>
> **Audience.** Claude, future contributors, and the owner. Read top-to-bottom on first encounter; thereafter use as a lookup.
>
> **Status.** LOCKED v1.0 — defaults applied 2026-04-27 per owner authorization. Owner can override any `[LOCKED]` item by editing this file. Items revised from draft: §3.C, §5.A (both reversed to preserve current dashboard behavior — see §10).

---

## §1 Tagging — how elements are identified

Every visible element carries two markers:

```html
<span class="chip chip-warning" data-ds="chip">Stale 7d</span>
```

- `data-ds="<id>"` — the **identity** attribute. Read by lint, audit script, and `?ds-debug=1` overlay. One id per concept.
- `class="<id-base> <id-base>-<variant>"` — the **style** classes. Drive CSS via tokens.

Tags are emitted by helpers in `src/ds.js` — never hand-written:

```js
ds.chip({ variant: 'warning', text: 'Stale 7d' })
ds.button({ variant: 'primary', size: 'sm', label: 'Send', onClick })
ds.kpiTile({ label: 'Active studies', value: 23, delta: '+2' })
```

Three lint rules enforce the contract:
1. `no-inline-style-on-tagged` — bans `style="…color|background|font|padding|margin…"` on any element with `data-ds`.
2. `tag-must-exist` — `data-ds` value must match a manifest id.
3. `helpers-only` — flags hand-rolled HTML for any component the helper covers.

Plus `scripts/check-ds-coverage.js` headless-renders every tab and reports untagged-element percentage. CI fails below the floor (initially 80%, rising to 100% as modules retrofit).

**`[LOCKED 1.A]`** Mechanism is `data-ds` attribute + matching class. Both, not one.
**`[LOCKED 1.B]`** Helpers live in `src/ds.js`, called as `ds.<component>(opts)`. Object args, not positional.
**`[LOCKED 1.C]`** Coverage floor starts at 80%, rises to 100% per module as it retrofits. Existing code grandfathered via `// design-lock-legacy: <module> migration pending` annotation that expires when that module ships.

---

## §2 Component manifest

Every tagged component below. Format per entry:

> **`id`** — short description.
> Anatomy · Variants · Sizes · Use when · Don't use for · Class · Helper

### §2.1 Buttons & action affordances

**`button`** — action affordance: submit, open, navigate, trigger.
- Anatomy: label (req); icon (opt, leading or trailing)
- Variants: `primary` (orange, conversion CTA) · `secondary` (blue, internal action) · `action` (navy, ops action) · `ghost` (outline, secondary) · `ghost-on-dark` (on navy bg) · `danger` (red, destructive) · `link` (text-only, inline)
- Sizes: `default` (36px) · `sm` (30px) · `xs` (24px)
- Use when: any clickable affordance that performs an action
- Don't use for: filter selection (use `filter-chip`); tab nav (use `primary-tab`); sort headers (use `table-sort-header`)
- Class: `btn btn-{variant}` (+ `btn-{size}` if non-default)
- Helper: `ds.button({ variant, size, label, icon, onClick, disabled })`

**`button-icon`** — single-glyph button (close, overflow, expand, etc.).
- Anatomy: glyph (req, Unicode only — `×`, `⋯`, `↗`, `▾`)
- Sizes: 28×28 fixed
- Use when: close affordance on modal/toast/chip; overflow menu; row-level micro-action
- Don't use for: anything with text — that's a `button-link` or `button` with size sm/xs
- Class: `btn-icon`
- Helper: `ds.buttonIcon({ glyph, ariaLabel, onClick })`

**`action-row`** — right-aligned button row, 8px gap, ghost-left primary-right.
- Anatomy: 1+ buttons
- Use when: modal footer; confirm bar; form footer; inline toolbar
- Don't use for: filter toolbar (use `filter-bar`)
- Class: `actions`
- Helper: `ds.actionRow([...buttons])`

### §2.2 Status indicators

**`chip`** — small inline status label.
- Anatomy: label (req); icon (opt, leading)
- Variants: `success` (green) · `warning` (amber) · `danger` (red) · `info` (blue) · `meta` (slate, transparent bg) · `ai` (violet) · `ghost` (outline-only)
- Sizes: 11–12px tabular text, ~6px×10px padding, radius `--radius-xs`
- Use when: status, category, count, attribution on a row/card
- Don't use for: study lifecycle status (use `pill-study-status`); filter selection (use `filter-chip`); severity flags (use `severity-flag`)
- Class: `chip chip-{variant}`
- Helper: `ds.chip({ variant, text, icon })`

**`pill-study-status`** — study lifecycle pill (distinct from semantic chip).
- Variants: `enrolling` · `maintenance` · `pre-closed` · `configuring` · `startup` · `closed` · `suspended` · `withdrawn`
- Use when: a row/card representing a study's lifecycle state per CRIO `study.status`
- Don't use for: anything outside CRIO study status
- Class: `pill pill-{variant}`
- Helper: `ds.studyPill({ status })`

**`status-dot`** — color dot, no label.
- Variants: `success` · `warning` · `danger` · `info` · `meta`
- Use when: nav item with implicit status; sparse table cell; sidebar indicator
- Don't use for: anything where the meaning isn't obvious from context (use `chip` instead)
- Class: `dot dot-{variant}`
- Helper: `ds.statusDot({ variant, ariaLabel })`

**`severity-flag`** — high-emphasis attention indicator.
- Variants: `urgent` (red, "next 14 days") · `warning` (amber)
- Use when: risk-card flagging; row-level "this needs attention NOW"
- Don't use for: count chips; routine status (use `chip`)
- Class: `flag flag-{variant}`
- Helper: `ds.severityFlag({ variant, label })`

**`site-tag`** — geographic site indicator (PHL / PNJ).
- Anatomy: site (req — `'pnj'` or `'phl'`, also accepts `'pennington'` / `'philadelphia'` / etc.)
- Variants: `pnj` (green) · `phl` (navy)
- Use when: any place a row/card needs to show site affiliation
- Don't use for: site selection in filters (use `filter-chip`)
- Class: `site-tag site-tag-{variant}`
- Helper: `ds.siteTag({ site })`

**`purpose-badge`** — study / visit-type / campaign identifier (distinct from status `chip`).
- Anatomy: label (req)
- Tones: `red` · `amber` · `green` · `teal` · `blue` · `indigo` · `violet` · `magenta` (8 perceptually distinct hues, named by hue not by study)
- Use when: labelling a study, visit type, or campaign so it's scannable across rows ("Lp(a) Blood Test", "FibroScan", "Diabetes Study")
- Don't use for: status indication (use `chip`); study lifecycle (use `pill-study-status`)
- Class: `purpose-badge purpose-badge-{tone}`
- Helper: `ds.purposeBadge({ tone, label })`
- **Registry (study/visit-type → tone)** lives in code (`_leadsPurpose()` in `src/leads.js`), not in CSS — adding a new study only requires a registry entry, not a doctrine PR. Current mappings:
  - **red**: Lp(a) Blood Test, Heart Health
  - **amber**: Cholesterol, Arthritis
  - **green**: Eczema
  - **teal**: Chronic Hives
  - **blue**: Diabetes, Weight Management
  - **indigo**: Migraine
  - **violet**: FibroScan
  - **magenta**: Lupus
  - **fallback (no badge)**: any other condition renders as `chip-meta` instead.

### §2.3 Cards & containers

**`kpi-tile`** — primary metric display.
- Anatomy: eyebrow label (req) · value (req, tabular) · delta (opt, with arrow ↑↓) · sparkline (opt) · sub-label (opt)
- Sizes: `default` · `compact` (no sparkline, smaller value)
- Use when: dashboard top-of-tab metrics
- Don't use for: in-line stats (use a chip); table cells (use `table-cell-number`)
- Class: `kpi-tile` (+ `kpi-tile-compact`)
- Helper: `ds.kpiTile({ label, value, delta, deltaDir, sparklineData, subLabel, onClick })`

**`section-card`** — generic content container.
- Anatomy: header (opt) · body (req) · footer (opt)
- Use when: any grouped content block on a tab
- Don't use for: KPI metrics (use `kpi-tile`); risk surfaces (use `risk-card`)
- Class: `card`
- Helper: `ds.card({ header, children, footer })`

**`study-card`** — per-study summary tile.
- Anatomy: 3px top-border (risk indicator color) · title · metrics row · chips row · footer
- Use when: Studies tab, Resources tab
- Don't use for: any non-study container
- Class: `study-card` (+ `study-card-risk-{level}` for top border)
- Helper: `ds.studyCard({ study, riskLevel })`

**`risk-card`** — flagged at-risk patient/study card.
- Anatomy: 3px top-border (red/amber) · severity-flag · title · meta · CTA
- Use when: Overview risk panel; at-risk patient surfaces
- Don't use for: non-risk surfaces (use `section-card`)
- Class: `risk-card risk-{severity}`
- Helper: `ds.riskCard({ severity, title, meta, action })`

**`alert`** — full-width inline notice.
- Anatomy: icon (variant-tied) · title (opt) · body (req) · action (opt)
- Variants: `info` · `success` · `warning` · `danger`
- Use when: page-level notices; banner above content; confirm bar
- Don't use for: row-level status (use `chip`); transient feedback (use `toast`)
- Class: `alert alert-{variant}`
- Helper: `ds.alert({ variant, title, body, action })`

**`detail-panel-header`** — gradient hero header for detail panels.
- Anatomy: gradient navy→blue · title · subtitle (opt) · close button
- Use when: large detail panels (Patient Card, Study Drill-down)
- Don't use for: routine modals (use `modal` header)
- Class: `detail-panel-header`
- Helper: rendered inside `ds.modal({ size: 'lg', heroHeader: true })`

### §2.4 Tables

**`data-table`** — wrapper for any tabular data.
- Anatomy: caption (opt) · thead · tbody · tfoot (opt)
- Use when: any 2+ row × 2+ col data display
- Don't use for: form layouts (use `field` wrappers); KPI grids (use `kpi-tile` row)
- Class: `data-table`
- Helper: `ds.table({ columns, rows, caption, sortable })`

**`table-row`** — tbody row.
- Modifiers: `clickable` · `selected` · `disabled` · `subdued` (cancelled visits etc.)
- Use when: every tbody row
- Class: `tr` (+ `tr-{modifier}`)

**`table-cell-text`** — left-aligned text.
**`table-cell-number`** — right-aligned, tabular-nums, monospaced for diff cols.
**`table-cell-chip`** — chip embedded in cell.
**`table-cell-button`** — button(s) embedded in cell, single or grouped.
**`table-cell-link`** — anchor in cell.
- Class per type: `td td-text` · `td-num` · `td-chip` · `td-button` · `td-link`

**`table-sort-header`** — clickable column header with sort indicator.
- States: unsorted · sorted-asc (▲) · sorted-desc (▼)
- Use when: any sortable thead cell
- Class: `th-sort` (+ `th-sort-asc` / `th-sort-desc`)
- Helper: `ds.sortHeader({ label, field, currentSort, onSort })`

**`table-empty-row`** — single full-span "no data" row.
- Anatomy: empty-state copy + (opt) action
- Use when: zero rows match current filter/state
- Class: `tr-empty`

**`table-footer-row`** — totals/summary row.
- Use when: aggregating numbers (totals, averages); never just for visual padding
- Class: `tr-footer`

### §2.5 Forms & inputs

**`input-text`** — single-line text.
- Anatomy: input (req) · prefix icon (opt) · suffix icon (opt) · clear button (opt)
- Use when: name, email, phone, single-line free text
- Class: `input`

**`input-textarea`** — multi-line text.
- Class: `input input-textarea`

**`input-select`** — native or custom select.
- Class: `input input-select`

**`input-checkbox`** — single boolean.
- Class: `checkbox`

**`input-radio`** — exclusive group.
- Class: `radio`

**`input-toggle`** — boolean, on/off pill.
- Class: `toggle`

**`input-date`** — date picker.
- Format: see §4 (ISO under hood, "Mar 15, 2026" displayed)
- Class: `input input-date`

**`input-search`** — search box with magnifier glyph + clear.
- Use when: filtering a table; never as the only filter on multi-attr surfaces (pair with `filter-chip`)
- Class: `input input-search`

**`field`** — wrapper for label + input + helper + error.
- Anatomy: label (req, top-positioned) · input (req) · helper (opt) · error (opt, replaces helper when present)
- Use when: every form input
- Class: `field` (+ `field-error` when error present)
- Helper: `ds.field({ label, input, helper, error, required })`

### §2.6 Filters & controls

**`filter-bar`** — toolbar containing filters + search + actions.
- Anatomy: search-box (left) · filter-chips/dropdowns (middle, wrap allowed) · clear-all (right) · action-row (far right, opt)
- Position: ABOVE the table it filters, full-width, sticky on scroll. **Locked across all tabs.**
- Use when: any tab with a primary table that takes filters
- Don't use for: KPI-only tabs
- Class: `filter-bar`
- Helper: `ds.filterBar({ search, filters, clearAll, actions })`

**`filter-chip`** — toggleable filter (single-value).
- States: inactive · active · disabled
- Use when: 2–6 mutually exclusive options (status, site, period)
- Don't use for: 7+ options (use `filter-dropdown`); free text (use `input-search`)
- Class: `filter-chip` (+ `filter-chip-active`)
- Helper: `ds.filterChip({ label, active, count, onToggle })`

**`filter-dropdown`** — multi-select or large-set filter.
- Anatomy: button trigger (label + count + ▾) · panel (search + checkbox list) · footer (clear / apply)
- Use when: 7+ options; multi-select; hierarchical
- Don't use for: 2–6 mutually-exclusive options (use `filter-chip`)
- Class: `filter-dropdown`

**`period-toggle`** — pre-set time-window picker.
- Variants: `5-period` (12mo, This Mo, Last Mo, This Q, Last Q) — Leadership tab default
- Use when: any analytics surface with period comparison
- Class: `period-toggle`

**`group-by-toggle`** — re-group display by an axis.
- Use when: list/grid with meaningful grouping axis (Resources groups by therapeutic area / coordinator)
- Class: `group-by-toggle`

**`clear-filters-button`** — one-click filter reset.
- Use when: any `filter-bar` with 2+ active filters
- Class: `btn btn-ghost btn-sm filter-clear`

### §2.7 Navigation

**`primary-tab-bar`** — top tab strip.
- Anatomy: `primary-tab` × N · sticky on scroll
- Position: top of dashboard, below page header, full-width
- Class: `tab-bar tab-bar-primary`

**`primary-tab`** — top tab.
- States: inactive · active · hidden (RBAC) · locked (admin/finance for non-owner)
- Class: `tab tab-primary` (+ `tab-active` / `tab-locked`)

**`sub-tab-bar`** — second-level tab strip inside a primary tab.
- Use when: a primary tab has 2+ canonical sub-views (Leads = Inbox/Orders/Pre-Screening)
- Position: below primary-tab-bar, less prominent
- Class: `tab-bar tab-bar-sub`

**`sub-tab`** — second-level tab.
- Class: `tab tab-sub` (+ `tab-active`)

### §2.8 Modals & overlays

**`modal`** — center-screen dialog.
- Anatomy: backdrop · header (title + close) · body (scrollable) · footer (action-row)
- Sizes: `sm` (480px) · `md` (640px) · `lg` (920px) · `fullscreen`
- Use when: focused task that's not page-worthy; detail view; confirmation
- Don't use for: contextual hints (use `tooltip`); brief notices (use `toast`)
- Class: `modal modal-{size}`
- Helper: `ds.modal({ size, title, body, footer, onClose })`

**`drawer`** — edge-anchored panel.
- Direction: `right` (default) · `left` · `bottom`
- Use when: progressive disclosure where context behind matters
- Don't use for: tasks that need full attention (use `modal`)
- Class: `drawer drawer-{direction}`

**`tooltip`** — hover/focus ephemeral text.
- Anatomy: short text (req, 1 line preferred)
- Trigger: 400ms hover delay; focus immediate
- Use when: clarifying icon-only buttons; abbreviation expansion
- Don't use for: actionable content (use `popover`); long explanations (use a small inline note)
- Class: `tooltip`

**`popover`** — click-triggered, persistent until dismissed.
- Anatomy: header (opt) · body (rich) · footer (opt action-row)
- Trigger: click; click-outside dismisses
- Use when: rich context that needs interaction (filter dropdown is a special-case popover)
- Don't use for: hover-only UX (use `tooltip`)
- Class: `popover`

**`kpi-popup`** — drill-down from a KPI tile.
- Anatomy: detail-panel-header · body (chart + table) · close
- Use when: any KPI tile click that surfaces breakdown
- Don't use for: navigation (use `switchTab`)
- Class: `modal kpi-popup`
- Helper: `ds.kpiPopup({ metric, period, breakdown })`

**`patient-card-modal`** — 9-section patient detail.
- Use when: patient name clicked anywhere
- Class: `modal patient-card-modal`

### §2.9 State surfaces

**`loading-spinner`** — indeterminate small spinner.
- Sizes: 16 / 20 / 24 / 32px
- Use when: brief loads (<1s expected); inline within rows/buttons
- Don't use for: long loads (use `loading-skeleton`)
- Class: `spinner spinner-{size}`

**`loading-skeleton`** — placeholder shape.
- Anatomy: shimmer animation, sized to mimic real content
- Use when: load >1s; first paint of any data-driven surface
- Don't use for: button states (use disabled + spinner)
- Class: `skel skel-{shape}`

**`empty-state`** — no-data treatment.
- Anatomy: optional small illustration · headline (req) · body (opt) · CTA (opt)
- Use when: filter-yields-zero; surface-genuinely-empty
- Don't use for: error (use `error-state`); loading (use `loading-skeleton`)
- Class: `empty-state`
- Helper: `ds.emptyState({ headline, body, action })`

**`error-state`** — surface-level error.
- Anatomy: icon · headline · body · retry button
- Use when: fetch failed; permission denied; data integrity broken
- Don't use for: form-field errors (use `field-error`); toast errors (use `toast variant=danger`)
- Class: `error-state`

**`refresh-button`** — manual data refresh trigger.
- Anatomy: ↻ icon · "Refresh" label (or icon-only on dense surfaces) · spinning state
- Position: top-right of `filter-bar` when present, else top-right of tab content
- Use when: every data-driven surface
- Class: `btn btn-ghost btn-sm refresh-btn`

**`last-updated-stamp`** — "Updated 3m ago" inline.
- Position: paired with `refresh-button`
- Format: relative time, see §4
- Class: `last-updated`

**`toast`** — transient feedback.
- Variants: `success` · `info` · `warning` · `danger`
- Position: bottom-right, stacked
- Duration: 4s default; 8s for danger; user-dismissible always
- Use when: success of background action; non-blocking notice
- Don't use for: errors that require attention (use `alert` or `error-state`); confirmations (use `modal`)
- Class: `toast toast-{variant}`

### §2.10 Charts & data viz

**`chart-categorical`** — multi-series chart using `--chart-1..6` palette.
- Cap: 6 series; warn at 5
- Class: `chart chart-categorical`

**`chart-sequential`** — single-hue heatmap/density.
- Class: `chart chart-sequential`

**`chart-diverging`** — red↔neutral↔green for variance/delta.
- Class: `chart chart-diverging`

**`sparkline`** — inline mini trend.
- Height: 16/20/24px
- Use when: KPI tile · table cell · row indicator
- Class: `sparkline`

**`trend-line`** — full-size line chart.
- Class: `chart chart-trend`

**`[LOCKED 2.A]`** Component count above is ~50, complete coverage of §§1–11 inventory. If a surface needs something not listed, that's a doctrine PR, not improvisation.
**`[LOCKED 2.B]`** All `chip` use the **redefined** semantic tokens (`--success: #059669`, `--warning: #d97706`) so existing dashboard pixels don't shift.
**`[LOCKED 2.C]`** `pill-study-status` is kept SEPARATE from `chip` because study lifecycle has 8 distinct states with their own color-mapping that doesn't fit the 7 chip variants.

---

## §3 Vocabulary — canonical labels

The dashboard mixes "patient/subject/participant," "Cancelled/Canceled," "Save/Update/Apply." Canonicals below; everywhere else is wrong.

### §3.1 Person nouns

| Surface | Term | Example |
|---|---|---|
| Patient-facing (landing pages, JRS form, comms received by patient) | **you** (second person) | "Check your eligibility" |
| Internal ops (dashboard tables, reports) | **patient** | "Patient: J. Smith" |
| Regulatory / sponsor-facing (audit logs, sponsor reports) | **subject** (matches CRIO) | "Subject 12345" |
| Aggregate / cohort reference | **participants** | "247 participants enrolled" |

**Never:** "user," "client," "individual," "person."

### §3.2 Site labels

- Abbrevs: `PHL` (Philadelphia / Princeton site cluster) · `PNJ` (Pennington NJ)
- Full: `Princeton` · `Pennington`
- Combined when needed: `PHL (#6)` showing site number
- **Never:** "Philly," "PHI," "PA," "NJ" alone (ambiguous), "Site A/B"

### §3.3 Visit & cancel statuses

Match CRIO source-of-truth spelling:

| Term | Means | Don't say |
|---|---|---|
| Cancelled | Patient-Cancelled / Site-Cancelled / No-Show parent | "Canceled" (US spelling) |
| No-Show | `cancel_type=1` | "Missed," "DNS" |
| Site Cancelled | `cancel_type=2` | "Site cancellation," "Coord cancelled" |
| Patient Cancelled | `cancel_type=3` | "Patient cancellation," "Pt-cancel" |
| Rescheduled | `cancel_reason=Rescheduled` AND future appt | "Moved," "Pushed" |
| Completed | `subject_visit.status IN (22,23)` | "Done," "Finished" |
| In Progress | `status IN (11,12)` | "Ongoing," "Active visit" |
| Pending | `status IN (0,1)` future-dated | "Scheduled" (also valid; pick one — recommend Pending in chips, Scheduled in tables) |
| Discontinued | `subject.status=13` | "Withdrew" (use Withdrawn) |
| Withdrawn | `subject.status=12` | "Discontinued" (different) |
| Screen Fail | `subject.status=12` | "SF" (chip-only abbrev OK) |

### §3.4 Action verbs (button labels)

| Verb | Use for |
|---|---|
| **Save** | Persisting form changes (no external send) |
| **Send** | Outbound comm (email, SMS, fax) |
| **Submit** | Patient-facing form, intake, application |
| **Confirm** | Modal dialog acknowledgment of irreversible action |
| **Apply** | Activating filters / settings |
| **Update** | Modifying existing data on surfaces that already use this verb |
| **Cancel** | Closing modal or aborting form (no destructive action) |
| **Discard** | Aborting AND losing unsaved changes (paired with Cancel) |
| **Delete** | Removing data (always paired with Confirm dialog) |
| **Open** | Navigating to detail view |

**Never:** "OK" (use Confirm), "Yes" (use the actual verb), "Done" (use Save or Close).

### §3.5 Eyebrow / label casing

- Eyebrows: `UPPERCASE` with 0.1em letter-spacing (per `--fs-micro`/`.eyebrow`)
- Section headers: `Title Case`
- Body labels: `Sentence case`
- Table column headers: `Title Case`
- Chip text: `Sentence case` (or `lowercase` if a count like `12 enrolled`)

**`[LOCKED 3.A]`** Person nouns per surface as in §3.1.
**`[LOCKED 3.B]`** Visit status labels match CRIO spelling (UK "Cancelled").
**`[LOCKED 3.C]`** **Reversed from draft.** "Edit" + "Save" pairs preserved on surfaces that use them; "Update" used only where the dashboard already uses that verb. No forced rename — would have been a UX shift the owner didn't ask for.

---

## §4 Formats — dates, numbers, currency

### §4.1 Dates

- **Relative** for ≤7 days ago: `3h ago` · `2 days ago` · `Just now` (<1m)
- **Absolute short** for older same-year: `Mar 15`
- **Absolute long** for cross-year: `Mar 15, 2026`
- **Audit logs / forensic**: `2026-03-15 14:32:07 ET` (ISO + 24h time + TZ)
- **Inputs**: ISO under the hood (`2026-03-15`), display "Mar 15, 2026"

### §4.2 Times

- **12-hour** for user-facing surfaces: `2:30 PM ET` (always with TZ)
- **24-hour** for audit logs only: `14:30 ET`
- **Timezone**: always `ET` displayed (the team is single-TZ; explicit prevents drift)

### §4.3 Date ranges

- Same month: `Mar 15 – 22`
- Cross-month: `Mar 15 – Apr 3`
- Cross-year: `Dec 28, 2025 – Jan 4, 2026`
- En-dash `–`, not hyphen `-`

### §4.4 Numbers

- **Counts**: comma-separated, no abbreviation in tables: `1,234`
- **Counts in chips/sparklines**: abbreviated: `1.2K` · `12K` · `1.2M`
- **Percentages**: integer in chips: `42%` · one decimal in tables: `42.3%`
- **Currency**: `$1,234.56` standard · `$1.2K` abbreviated · `$1.23M` abbreviated · never `$1,234.5` (single decimal)
- **Negatives**: `-$1,234` · `(1,234)` only in finance contexts (locked tabs)

### §4.5 Missing values

- **Tables**: `—` (em dash)
- **Chips**: omit entirely (don't render the chip)
- **Inputs**: empty (no placeholder text mimicking a value)

**`[LOCKED 4.A]`** "ET" displayed on every user-facing time. Explicit beats implicit; protects against screenshot-out-of-context drift.
**`[LOCKED 4.B]`** En-dash `–` for ranges, not hyphen.

---

## §5 Behavior patterns

### §5.1 Click affordances

- **Row click in a list/table** → behavior is per-tab and intentional. Leads = `modal` (drilldown). Studies = tab-switch with filter (the row IS a navigation). Schedule = inline expansion (working surface, context matters). Resources = inline expansion (per-study cards). Doctrine documents the convention; not enforced as a single default.
- **KPI tile click** → `kpi-popup` with breakdown.
- **Chip click** → toggles filter (when in `filter-bar`); else inert (chips are status, not actions).
- **Tab click** → switch tab + update hash (`history.replaceState`).
- **Cell-level link** → navigates to most-specific surface (patient → patient-card-modal; study → study tab + filter).

**`[LOCKED 5.A]`** **Reversed from draft.** Row click is per-tab and intentional (see §5.1). Doctrine preserves current behavior; no forced rename to modal-default.

### §5.2 Hover / focus

- **Tooltip delay**: 400ms hover; 0ms focus-visible
- **Hover state on rows**: subtle bg shift (`var(--surface-2)`); no border movement
- **Hover state on buttons**: per `.btn-{variant}:hover` definitions
- **Focus ring**: `var(--ring)` always; never override

### §5.3 Refresh

- **Manual refresh button**: every data-driven surface, top-right of filter-bar
- **Last-updated stamp**: paired with refresh button, relative-time format
- **Auto-refresh**: 15-minute global interval (per CLAUDE.md)
- **Visibility-triggered**: tab hidden 5+ min → refresh on return
- **Loading affordance during refresh**: button spinner; no skeleton over existing data (preserve the user's visual context)

### §5.4 Confirmation dialogs (when required)

- Deleting any data
- Sending external comm (email, SMS, fax) outside the approval queue
- Bulk actions affecting 5+ records
- Irreversible state changes (closing study, discontinuing patient)
- **Never** required for: filter changes, sorting, navigation, opening modals, simple form saves

Confirmation pattern: `modal size=sm` with title stating action, body summarizing impact, action-row with `button variant=ghost label="Cancel"` + `button variant=danger label="<verb>"`.

### §5.5 Optimistic updates

- **Apply optimistically** for: visit status changes, follow-up dispositions, filter changes
- **Wait for server** for: comm sends, payments, anything irreversible
- **On optimistic failure**: revert + show inline error; do NOT toast

### §5.6 Toasts

- **Success**: 4s, dismissible, bottom-right
- **Error**: never use a toast for an error that the user must respond to — use `error-state` or inline error
- **Info**: 4s, dismissible
- Stacking: max 3 visible; older ones fade

**`[LOCKED 5.B]`** Toasts never used for errors needing response.

---

## §6 Voice — defer to README

See `README.md` §Voice for tone rules. Doctrine-level summary:
- Patient-facing: second-person, sentence case, specific, no exclamation marks, no emoji
- Internal ops: terse, label-driven, denser; "participants" allowed
- Regulatory: precise, avoid colloquialism

---

## §7 Accessibility — invariants

- **Color contrast**: WCAG AA minimum on all text. Tokens in §1 of `colors_and_type.css` already meet.
- **Focus indicators**: `var(--ring)`; never invisible. Focus-visible on every interactive element.
- **Keyboard navigation**: every action reachable. Tab order logical. Escape closes modals/popovers/dropdowns.
- **Screen reader**: semantic HTML (`<button>` for buttons, `<a>` for links, `<th>` for headers); ARIA labels on icon-only buttons.
- **Motion**: respect `prefers-reduced-motion`; durations ≤ 250ms by default.
- **Touch targets**: 44px minimum on mobile/touch surfaces.
- **Color alone is never the signal**: every chip/dot/pill pairs color with text label or icon shape.

---

## §8 Enforcement

### §8.1 Lint rules (added to `scripts/lint.js`)

- `no-inline-style-on-tagged` — element with `data-ds` cannot have `style="…color|background|font|padding|margin…"`
- `tag-must-exist` — `data-ds` value must be in manifest
- `helpers-only` — pattern-match for hand-rolled HTML matching a covered component (e.g. `\bclass="chip\b` triggers if not emitted by `ds.chip()`)
- `no-inline-hex-in-modules` — bans `#[0-9a-f]{6}` in `src/*.js` template literals (allowlist: chart data structures, image URLs)
- `chip-must-use-class` — element with class containing `chip|badge|pill|tag|dot` cannot also have inline color/background style

### §8.2 Coverage script

`scripts/check-ds-coverage.js`:
1. Headless-render every tab (Puppeteer or jsdom).
2. Walk DOM, count visible elements, count tagged elements.
3. Output coverage % per tab + overall.
4. CI fails if overall < floor.

### §8.3 Floors and grandfathering

- Floor starts: 80% overall.
- Per-module retrofit raises that module to 100%.
- Grandfather annotation: `// design-lock-legacy: <module-name> migration pending` allows existing inline-styled elements through, per-line. The annotation expires (i.e., must be removed) when the module's retrofit PR ships.

### §8.4 Adding a component

1. Open this file, add an entry under §2 in the right subsection.
2. Add the helper function to `src/ds.js`.
3. Add the spec page to `design-system/preview/<id>.html`.
4. Add CSS to `design-system/components.css` (if not already in `colors_and_type.css`).
5. Update `design-system/manifest.json` (machine-readable mirror of §2).
6. PR with all five.

**`[LOCKED 8.A]`** `manifest.json` is the machine-readable mirror of §2; this file is the human source of truth. Sync is enforced by a CI check.

---

## §9 What is NOT covered

- **Locked tabs** (Finance, Billing, QB, Productivity, Payments, CTAs, Admin) — owner-only edits per CLAUDE.md `LOCKED:*`. When the owner approves design polish on them, the doctrine applies.
- **Apps Script** — decommissioned 2026-04-25; no longer a surface.
- **`ui_kits/eligibility/`** and **`ui_kits/dashboard/`** as React-JSX recreations — these mirror the system but are not active code; updates flow doctrine → live code, then the kits resync.
- **Chart internals** — D3/SVG fills follow `--chart-*` tokens but the chart construction code is exempt from `no-inline-style-on-tagged` because chart elements are programmatically generated.
- **Logo / brand asset rendering** — covered by `brand-governance.html`, not here.
- **Email body content** — copy/voice rules in §3 + §6 apply, but specific email layouts are templated separately in the upcoming mail-templates package.

---

## §10 Resolution log

Resolved 2026-04-27 by Claude per owner authorization. Owner can override any item by editing the corresponding `[LOCKED X.X]` block above.

| # | Section | Item | Status | Notes |
|---|---|---|---|---|
| 1 | §1.A | `data-ds` attr + class together | ✓ Locked as drafted | Plumbing |
| 2 | §1.B | Helpers in `src/ds.js`, object args | ✓ Locked as drafted | Plumbing |
| 3 | §1.C | Coverage 80% → 100%, grandfather annotation | ✓ Locked as drafted | Plumbing |
| 4 | §2.A | ~50 components full coverage | ✓ Locked as drafted | Adding new components is a doctrine PR |
| 5 | §2.B | Redefine `--success`/`--warning` to prod hex | ✓ Locked as drafted | Zero pixel shift |
| 6 | §2.C | `pill-study-status` separate from `chip` | ✓ Locked as drafted | Distinct semantics |
| 7 | §3.A | Person noun per surface | ✓ Locked as drafted | Matches CLAUDE.md voice rules |
| 8 | §3.B | Visit statuses match CRIO spelling | ✓ Locked as drafted | UK "Cancelled" |
| 9 | §3.C | "Update" replaces "Edit + Save" | **✗ Reversed** | Would have forced UX shift; preserving current verbs |
| 10 | §4.A | "ET" always displayed | ✓ Locked as drafted | Explicit beats implicit |
| 11 | §4.B | En-dash for ranges | ✓ Locked as drafted | Standard typography |
| 12 | §5.A | Row click → modal default | **✗ Reversed** | Per-tab variation is intentional; doctrine documents rather than enforces |
| 13 | §5.B | Toasts never for errors needing response | ✓ Locked as drafted | Standard pattern |
| 14 | §8.A | `manifest.json` mirrors §2 | ✓ Locked as drafted | CI sync check |

**To override any locked item**, edit its `[LOCKED X.X]` block directly or call it out in chat by number.
