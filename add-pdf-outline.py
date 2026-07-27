#!/usr/bin/env python3
"""Add a bookmark outline to the ICON deck PDF.

Chrome's print-to-pdf emits no /Outlines, so a reader opening the PDF gets no
sidebar and no way to jump between sections. This walks the built HTML for the
section dividers, works out their page numbers, and writes a two-level outline:
each section, with its slides nested underneath.
"""
import html, pathlib, re, sys
from pypdf import PdfReader, PdfWriter

DS  = pathlib.Path.home() / "crp-design-system"
SRC = DS / "crp-icon-elite-sites-metabolic-neurology.print.html"
PDF = pathlib.Path.home() / "CRP-ICON-Elite-Sites-Metabolic-Neurology.pdf"

doc = SRC.read_text()          # not "html" — that shadows the stdlib module
sections = re.findall(r'<section class="slide.*?</section>', doc, re.S)

def clean(frag):
    """Bookmarks are plain text, so entities must be decoded, not stripped."""
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', frag))).strip()


def title_of(sec):
    if 'icn-sec' in sec:
        return clean(re.search(r'<h2>(.*?)</h2>', sec, re.S).group(1))
    if 'icn-cover' in sec:
        return "Cover"
    h = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sec, re.S)
    if not h:
        return "Slide"
    t = clean(h.group(1))
    return (t[:68] + "…") if len(t) > 69 else t

reader = PdfReader(str(PDF))
if len(reader.pages) != len(sections):
    sys.exit("page/slide mismatch: %d pages vs %d slides" % (len(reader.pages), len(sections)))

writer = PdfWriter(clone_from=str(PDF))
parent, added = None, 0
for i, sec in enumerate(sections):
    title = title_of(sec)
    if 'icn-sec' in sec:                      # a divider starts a new section
        parent = writer.add_outline_item(title, i, bold=True)
    elif parent is None:                      # cover + contents sit at top level
        writer.add_outline_item(title, i)
    else:
        writer.add_outline_item(title, i, parent=parent)
    added += 1

writer.page_mode = "/UseOutlines"             # open with the sidebar showing
with open(PDF, "wb") as fh:
    writer.write(fh)
print("outline written: %d entries across %d pages" % (added, len(reader.pages)))
