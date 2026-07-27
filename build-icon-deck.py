#!/usr/bin/env python3
"""Compose the single ICON Elite Sites deck.

Pulls slides from three sources — the ICON-authored front slides, the section
dividers, and the canonical executive overview — and lays them out in one
explicit order. Nothing is duplicated: each slide is placed exactly once and
the script asserts every marker resolved.
"""
import pathlib, re

DS = pathlib.Path.home() / "crp-design-system"
SCRATCH = pathlib.Path(
    "/private/tmp/claude-501/-Users-aneeshvaze/87a944af-9de1-4676-a628-87aed6874952/scratchpad")

exec_html = (DS / "executive-overview.html").read_text()
icon_html = (SCRATCH / "icon_slides.html").read_text()
sect_html = (SCRATCH / "icon_sections.html").read_text()
extra     = (SCRATCH / "icon_extra.html").read_text()
polish    = (SCRATCH / "icon_polish.html").read_text()

# --- content guards on the exec deck -------------------------------------
for probe, why in [
    ("Eight investigators cover our therapeutic areas", "investigator count"),
    ("dr-rustgi.jpg", "Rustgi card"),
    ("site-philadelphia.png", "Philadelphia site photo"),
    ("site-pennington.jpg", "Pennington site photo"),
    ("Patients across our referring provider panels", "1.5M framing"),
    ("PubMed 30227522", "NIH cycle-time citation"),
    ("July 2026", "date"),
]:
    assert probe in exec_html, "exec deck missing: " + why
assert "no double entry" not in exec_html, "double-entry phrase should be gone"

SECTION_RE = r'<section class="slide.*?</section>'

def index(html):
    """Map every slide to the markers it contains."""
    return re.findall(SECTION_RE, html, re.S)

def take(pool, marker, label):
    hits = [s for s in pool if marker in s]
    assert len(hits) == 1, "%s: expected 1 slide matching %r, got %d" % (
        label, marker, len(hits))
    pool.remove(hits[0])
    return hits[0]

icon_pool = index(icon_html)
sect_pool = index(sect_html)
exec_pool = index(exec_html)

# Explicit running order. (source, marker) — every slide placed exactly once.
ORDER = [
    ("icon", 'class="slide icn-cover"'),          # 1  cover
    ("sect", ">Contents<"),                       # 2  contents
    ("sect", 'id="sec-case"'),                    # 3  §1
    ("icon", "The case in four numbers"),         # 4
    ("sect", 'id="sec-ta"'),                      # 5  §2
    ("icon", "commitment versus delivery"),       # 6  cardiometabolic
    ("icon", "what one site absorbed"),           # 7  EZEF
    ("icon", 'slide-eyebrow">Neurology'),          # 8  neurology
    ("icon", "Also available to the program"),    # 9  derm & rheum
    ("sect", 'id="sec-deliver"'),                 # 10 §3
    ("icon", ">Recruitment<"),                    # 11
    ("exec", ">Performance proof<"),              # 12 cycle times
    ("exec", ">What our technology gets you<"),   # 13
    ("exec", ">Investigators<"),                  # 14
    ("exec", "Operations &amp; coordinators"),    # 15
    ("exec", ">Facilities<"),                     # 16
    ("exec", ">Risk profile<"),                   # 17
    ("exec", ">Diversity in enrollment<"),        # 18
    ("sect", 'id="sec-record"'),                  # 19 §4
    ("icon", ">Sponsor relationships<"),          # 20
    ("exec", ">Track record<"),                   # 21 sponsor logo wall
    ("exec", "Treatments we've helped advance"),  # 22
    ("sect", 'id="sec-together"'),                # 23 §5
    ("icon", "How we would operate"),             # 24 one network
    ("icon", ">Next steps<"),                     # 25
]

POOLS = {"icon": icon_pool, "sect": sect_pool, "exec": exec_pool}
slides = [take(POOLS[src], marker, "%s/%s" % (src, marker)) for src, marker in ORDER]

# Anything left in the ICON or section pools is an authoring mistake.
assert not icon_pool, "unplaced ICON slides: %d" % len(icon_pool)
assert not sect_pool, "unplaced section slides: %d" % len(sect_pool)

# Page numbers run 01..N across the assembled deck.
n = [0]
def renumber(_m):
    n[0] += 1
    return '<span class="pageno">%02d</span>' % n[0]
body = "\n\n".join(slides)
body = re.sub(r'<span class="pageno">\d{2}</span>', renumber, body)
assert n[0] == len(ORDER), "renumbered %d of %d" % (n[0], len(ORDER))

# Reuse the exec deck's <head> and styles, swap in our slide body.
head, _, _ = exec_html.partition('<div class="deck">')
styles = (icon_html.split("</style>")[0] + "</style>\n"
          + sect_html.split("<!-- MARK:toc -->")[0] + "\n" + polish)
core = head + '<div class="deck">\n' + styles + "\n" + body + "\n</div>\n"
core = core.replace(
    "<title>CRP — Executive Overview, July 2026</title>",
    "<title>CRP — Metabolic and Neurology Experience · ICON Elite Sites Program</title>")

# Two artifacts from one set of slides. The interactive build carries the nav,
# keyboard handling and clickable contents; the print build is the same slides
# with no screen chrome at all, so Chrome never shrink-to-fits the page box.
interactive = core + extra + "\n</body>\n</html>"
printable   = core + "</body>\n</html>"

dest = DS / "crp-icon-elite-sites-metabolic-neurology.html"
dest.write_text(interactive)
print_dest = DS / "crp-icon-elite-sites-metabolic-neurology.print.html"
print_dest.write_text(printable)
print("wrote", dest)
print("wrote", print_dest)
print("slides:", interactive.count('<section class="slide'))
