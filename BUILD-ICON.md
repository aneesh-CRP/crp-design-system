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

## PowerPoint (editable)

```bash
python3 -m venv .venv && .venv/bin/pip install python-pptx   # once
.venv/bin/python make-pptx.py
```

Emits real shapes and text — editable in PowerPoint and Keynote. Content lives
in `make-pptx.py`; `pptx_kit.py` holds the layout vocabulary (head, card, stat,
bar, bullets, panels, section cover).

Set in Arial rather than Area Normal: the brand face is licensed and will not
be on a recipient's machine, and a missing font reflows a text-native deck into
something unrecognisable.

The sponsor logo wall is one pre-rendered PNG (`assets/sponsors/_wall.png`)
because SVG will not embed in PowerPoint. Regenerate it by screenshotting a
grid of the SVGs at 1832x460.

Verify with: `soffice --headless --convert-to pdf <file>.pptx`
