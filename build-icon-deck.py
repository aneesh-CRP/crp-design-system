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
    ("icon", 'class="slide icn-cover"'),          # 01 cover
    ("sect", ">Contents<"),                       # 02 contents
    ("sect", 'id="sec-case"'),                    # 03 §1
    ("icon", "The case in four numbers"),         # 04
    ("sect", 'id="sec-ta"'),                      # 05 §2
    ("icon", "Five for five"),                    # 06 cardiometabolic
    ("icon", "three and a half"),                 # 07 footprint math
    ("icon", "Four certified raters are why"),    # 08 neurology
    ("sect", 'id="sec-deliver"'),                 # 09 §3
    ("icon", "We do not buy patients"),           # 10 recruitment
    ("exec", ">Performance proof<"),              # 11 cycle times
    ("exec", ">Investigators<"),                  # 12
    ("exec", ">Diversity in enrollment<"),        # 13
    ("exec", ">Risk profile<"),                   # 14
    ("sect", 'id="sec-record"'),                  # 15 §4
    ("icon", "Sponsors come back"),               # 16
    ("exec", ">Track record<"),                   # 17 logo wall
    ("exec", "Treatments we've helped advance"),  # 18
    ("sect", 'id="sec-together"'),                # 19 §5
    ("icon", "Two locations. One contract"),      # 20 one network
    ("icon", "Put a number on us"),               # 21 commitment
    ("sect", 'id="sec-appendix"'),                # 22 appendix
    ("icon", "Appendix &middot; adjacent"),       # 23 derm & rheum
    ("exec", ">What our technology gets you<"),   # 24
    ("exec", "Operations &amp; coordinators"),    # 25
    ("exec", ">Facilities<"),                     # 26
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
# Stamp the running section marker into every slide's footer.
sec_label, stamped = None, []
for sec in slides:
    if 'icn-sec' in sec:
        h = re.search(r'<h2>(.*?)</h2>', sec, re.S).group(1)
        m_num = re.search(r'SECTION (\d+)', sec)          # the appendix has no number
        title = re.sub(r'<[^>]+>', '', h).strip()
        sec_label = ("%s &middot; %s" % (m_num.group(1), title)) if m_num else title
        stamped.append(sec)
        continue
    if sec_label:
        sec = sec.replace('<span class="pageno">',
                          '<span class="secmark">%s</span><span class="pageno">' % sec_label, 1)
    stamped.append(sec)
slides = stamped

body = "\n\n".join(slides)
body = re.sub(r'<span class="pageno">\d{2}</span>', renumber, body)
assert n[0] == len(ORDER), "renumbered %d of %d" % (n[0], len(ORDER))

# Reuse the exec deck's <head> and styles, swap in our slide body.
head, _, _ = exec_html.partition('<div class="deck">')
styles = (icon_html[:icon_html.index("<section")]
          + sect_html[:sect_html.index("<section")] + "\n" + polish)
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
