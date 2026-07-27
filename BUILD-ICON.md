# Building the ICON Elite Sites deck

```bash
python3 build-icon-deck.py     # writes the interactive + print HTML
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$HOME/CRP-ICON-Elite-Sites-Metabolic-Neurology.pdf" \
  --virtual-time-budget=12000 \
  "file://$PWD/crp-icon-elite-sites-metabolic-neurology.print.html"
python3 add-pdf-outline.py     # bookmarks — Chrome emits none
```

Inputs: `icon_slides.html` (ICON-authored slides), `icon_sections.html`
(dividers + contents + their CSS), `icon_polish.html` (unified cards, bars,
section marker), `icon_extra.html` (screen-only nav + JS), and
`executive-overview.html` for the shared slides.

Two outputs on purpose. The interactive file carries the sticky nav, arrow-key
navigation and progress bar; the `.print.html` has none of it. **Render the PDF
from the print file** — printing the interactive one makes Chrome shrink-to-fit.

Traps:
- `.slide` is content-box. Padding applied directly to a slide pushes it past
  1280px and scales every page to ~93%. Use `box-sizing: border-box`.
- The print HTML must sit in this directory or `./assets/` paths break silently
  (the PDF drops from ~4MB to ~700KB — check the file size).

## PowerPoint

```bash
python3 -m venv .venv && .venv/bin/pip install python-pptx   # once
.venv/bin/python make-pptx.py
```

Renders each PDF page at 150 dpi and places it full-bleed on a 13.333×7.5in
slide, with the slide's title in the notes so the outline pane is usable.
Text is not editable — the trade is that it looks identical everywhere with
no font dependency. Run it after the PDF is rebuilt.
