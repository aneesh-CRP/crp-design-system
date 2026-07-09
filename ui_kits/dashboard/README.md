# CRP Unified Dashboard — UI kit

## Components

- DashboardNav
- Kpis (TimeBanner, HeroRow, KpiTile, KpiRow)
- Panels (Card, Badge, Pill, RiskTag, Alert, Panel)
- StudyCard (StudyCard, CoordRow)

Hi-fi recreation of the internal operations dashboard at `crp-unified-dashboard`. The real app is a 1.9 MB single-page HTML with BigQuery feeds; this kit captures the visual vocabulary and interaction patterns so designs sit on top of the same system.

## Files
| File | What it is |
|---|---|
| `index.html` | Example "Overview" tab — assembled from the components below |
| `dashboard.css` | Ported from `styles.css` in the original repo (trimmed to what the kit uses) |
| `DashboardNav.jsx` | Sticky top nav with tabs, data-freshness badge, refresh + connect CTAs |
| `Kpis.jsx` | `<TimeBanner>`, `<HeroRow>`, `<KpiTile>`, `<KpiRow>` — the four flavors of summary tiles |
| `Panels.jsx` | `<Card>`, `<Panel>`, `<Badge>`, `<Pill>`, `<RiskTag>`, `<Alert>` |
| `StudyCard.jsx` | `<StudyCard>` (risk-top-border variant) and `<CoordRow>` |

## Interactions
- Click a nav tab — it activates visually (no routing; kit is a single-screen demo)
- Hover on `<KpiTile>`, `<HeroRow>` cell, or `<StudyCard>` — border/shadow lift
- Hover a table row — surface-2 wash
