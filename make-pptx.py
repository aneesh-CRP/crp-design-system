#!/usr/bin/env python3
"""Build a PowerPoint of the ICON deck.

The deck is HTML, so each slide is rendered at print resolution and placed
full-bleed on a 16:9 PowerPoint slide. Text is not editable — the trade is
that it looks exactly like the PDF on any machine, with no font dependency.
Speaker-facing titles go into the slide notes so the outline pane is usable.
"""
import html as htmlmod, pathlib, re, subprocess, sys
from pptx import Presentation
from pptx.util import Inches, Emu

HOME = pathlib.Path.home()
DS = HOME / "crp-design-system"
SRC = DS / "crp-icon-elite-sites-metabolic-neurology.print.html"
PDF = HOME / "CRP-ICON-Elite-Sites-Metabolic-Neurology.pdf"
OUT = HOME / "CRP-ICON-Elite-Sites-Metabolic-Neurology.pptx"
WORK = pathlib.Path("/private/tmp/claude-501/-Users-aneeshvaze/"
                    "87a944af-9de1-4676-a628-87aed6874952/scratchpad/pptx_pages")

def clean(frag):
    return re.sub(r'\s+', ' ', htmlmod.unescape(re.sub(r'<[^>]+>', '', frag))).strip()

def titles():
    doc = SRC.read_text()
    out = []
    for sec in re.findall(r'<section class="slide.*?</section>', doc, re.S):
        if 'icn-cover' in sec:
            out.append("Cover"); continue
        if 'icn-sec' in sec:
            out.append(clean(re.search(r'<h2>(.*?)</h2>', sec, re.S).group(1))); continue
        h = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sec, re.S)
        out.append(clean(h.group(1)) if h else "Slide")
    return out

WORK.mkdir(parents=True, exist_ok=True)
for old in WORK.glob("pg-*.png"):
    old.unlink()
# 150 dpi over a 13.333in slide = 2000px wide: crisp on a projector, sane file size
subprocess.run(["pdftoppm", "-png", "-r", "150", str(PDF), str(WORK / "pg")], check=True)
pages = sorted(WORK.glob("pg-*.png"))
names = titles()
if len(pages) != len(names):
    sys.exit("page/slide mismatch: %d rendered vs %d in source" % (len(pages), len(names)))

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]
for img, name in zip(pages, names):
    slide = prs.slides.add_slide(blank)
    slide.shapes.add_picture(str(img), Emu(0), Emu(0),
                             width=prs.slide_width, height=prs.slide_height)
    slide.notes_slide.notes_text_frame.text = name
prs.save(str(OUT))
print("wrote %s — %d slides, %.1f MB" % (OUT, len(pages), OUT.stat().st_size / 1e6))
