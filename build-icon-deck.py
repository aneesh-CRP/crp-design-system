#!/usr/bin/env python3
"""Compose the ICON Elite Sites deck.

Hub and spoke: a home slide of takeaways with a button per section, seven
section covers, and an in-slide nav bar on every page so a reader can move
between sections or back home — on screen and in the PDF.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from icon_nav import nav_bar, SECTIONS

DS = pathlib.Path.home() / "crp-design-system"
# The slide fragments were authored in a session scratchpad and later committed
# here; a scratchpad is deleted with its session, so read them from the repo.
SCRATCH = DS

exec_html = (DS / "executive-overview.html").read_text()
icon_html = (SCRATCH / "icon_slides.html").read_text()
hub_html  = (SCRATCH / "icon_hub.html").read_text()
arch_html = (SCRATCH / "archived_slides.html").read_text()
polish    = (SCRATCH / "icon_polish.html").read_text()
extra     = (SCRATCH / "icon_extra.html").read_text()

for probe, why in [
    ("Eight investigators on staff", "investigator count"),
    ("dr-rustgi.jpg", "Rustgi card"),
    ("site-philadelphia.png", "site photos"),
    ("PubMed 30227522", "NIH cycle-time citation"),
]:
    assert probe in exec_html, "exec deck missing: " + why

SECTION_RE = r'<section class="slide.*?</section>'
def index(h): return re.findall(SECTION_RE, h, re.S)

def take(pool, marker, label):
    hits = [s for s in pool if marker in s]
    assert len(hits) == 1, "%s: %d matches for %r" % (label, len(hits), marker)
    pool.remove(hits[0]); return hits[0]

POOLS = {"icon": index(icon_html), "hub": index(hub_html),
         "exec": index(exec_html), "arch": index(arch_html)}

# (source, marker, section-id the slide belongs to)
ORDER = [
    ("icon", 'class="slide icn-cover"',            None),
    ("hub",  'id="home"',                          None),

    # ── what we delivered ───────────────────────────────────────────────
    ("hub",  'id="sec-metab"',                     "sec-metab"),
    ("icon", "Five for five",                      "sec-metab"),
    ("arch", "cost 1,180 worked patients",         "sec-metab"),
    ("arch", "Four specialists and nine recent",   "sec-metab"),

    ("hub",  'id="sec-neuro"',                     "sec-neuro"),
    ("icon", "an early Alzheimer's protocol can be placed", "sec-neuro"),
    ("arch", "have each placed neurology work",     "sec-neuro"),
    ("arch", "raters are not starting cold",       "sec-neuro"),

    ("hub",  'id="sec-derm"',                      "sec-derm"),
    ("icon", "Nine derm and rheum trials",        "sec-derm"),

    # ── why it repeats ──────────────────────────────────────────────────
    ("hub",  'id="sec-deliver"',                   "sec-deliver"),
    ("icon", "215 provider partnerships put",       "sec-deliver"),
    ("exec", ">Diversity in enrollment<",          "sec-deliver"),
    ("exec", ">Performance proof<",                "sec-deliver"),
    ("exec", ">What our technology gets you<",     "sec-deliver"),
    ("exec", ">Risk profile<",                     "sec-deliver"),
    ("exec", "Operations &amp; coordinators",      "sec-deliver"),
    ("exec", ">Facilities<",                       "sec-deliver"),

    # ── who confirms it ─────────────────────────────────────────────────
    ("hub",  'id="sec-record"',                    "sec-record"),
    ("arch", "same two communities",               "sec-record"),
    ("exec", ">Investigators<",                    "sec-record"),
    ("icon", "Sponsors come back",                 "sec-record"),
    ("exec", ">Track record<",                     "sec-record"),
    ("exec", "Treatments we've helped advance",    "sec-record"),

    ("hub",  'id="sec-partner"',                   "sec-partner"),
    ("icon", "Two locations. One contract",        "sec-partner"),
    ("icon", "Put a number on us",                 "sec-partner"),
]

slides = []
for src, marker, sec in ORDER:
    s = take(POOLS[src], marker, "%s/%s" % (src, marker))
    if 'class="nav"' not in s and 'icn-cover' not in s:   # covers stay clean
        bar = nav_bar(sec)
        if '<div class="slide-pad">' in s:
            s = s.replace('<div class="slide-pad">', bar + '\n  <div class="slide-pad">', 1)
        else:                                        # the cover slide
            s = s.replace('<img class="quat"', bar + '\n  <img class="quat"', 1)
    slides.append(s)

assert not POOLS["icon"], "unplaced icon slides: %d" % len(POOLS["icon"])
assert not POOLS["hub"],  "unplaced hub slides: %d" % len(POOLS["hub"])
assert not POOLS["arch"], "unplaced archived slides: %d" % len(POOLS["arch"])

# Running section marker, then page numbers across the whole deck
label_by_id = {sid: ("%02d &middot; %s" % (i, lbl))
               for i, (sid, lbl, *_rest) in enumerate(SECTIONS, 1)}
stamped = []
for (src, marker, sec), s in zip(ORDER, slides):
    if sec and 'icn-sec' not in s:
        s = s.replace('<span class="pageno">',
                      '<span class="secmark">%s</span><span class="pageno">' % label_by_id[sec], 1)
    stamped.append(s)

n = [0]
def renumber(_m):
    n[0] += 1
    return '<span class="pageno">%02d</span>' % n[0]
body = re.sub(r'<span class="pageno">\d{2}</span>', renumber, "\n\n".join(stamped))
assert n[0] == len(ORDER), "renumbered %d of %d" % (n[0], len(ORDER))

head, _, _ = exec_html.partition('<div class="deck">')
styles = (icon_html[:icon_html.index("<section")]
          + hub_html[:hub_html.index("<section")] + "\n" + polish)
core = head + '<div class="deck">\n' + styles + "\n" + body + "\n</div>\n"
core = core.replace("<title>CRP — Executive Overview, July 2026</title>",
                    "<title>CRP — Metabolic and Neurology Experience · ICON Elite Sites Program</title>")

(DS / "crp-icon-elite-sites-metabolic-neurology.html").write_text(core + extra + "\n</body>\n</html>")
(DS / "crp-icon-elite-sites-metabolic-neurology.print.html").write_text(core + "</body>\n</html>")
print("slides:", len(ORDER))
