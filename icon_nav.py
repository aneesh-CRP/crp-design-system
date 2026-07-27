#!/usr/bin/env python3
"""Section covers, the home hub, and the in-slide navigation bar.

The nav is rendered INTO every slide rather than as fixed browser chrome, so
the same buttons work on screen and as real link annotations in the PDF.
"""

SECTIONS = [
    ("sec-about",   "About CRP",     "Who we are and what we run",
     "30",     "years, two sites, 500+ trials"),
    ("sec-metab",   "Cardiometabolic", "Our anchor area, and where we have delivered",
     "5 of 5", "recent targets met or beaten"),
    ("sec-neuro",   "Neurology",     "Migraine and MCI to mild Alzheimer's",
     "4",      "certified raters on MMSE, CDR, ADAS-Cog, FAQ"),
    ("sec-derm",    "Derm &amp; Rheum",  "The adjacent bench, on the same model",
     "9",      "recent trials, 2024 to 2025"),
    ("sec-deliver", "How we deliver", "Recruitment, speed, quality, facilities",
     "&lt;21", "days from selection to activation"),
    ("sec-record",  "Track record",  "Sponsors who came back",
     "15",     "protocols placed by Lilly alone"),
    ("sec-partner", "Partnership",   "What we ask, and what we commit to",
     "1",      "contract covering both sites"),
]

NAV_CSS = """

  /* ═══ Section dividers ═══ */
  .icn-sec {
    background: var(--gradient-navy-blue); color: #fff;
    display: flex; flex-direction: column; justify-content: center;
    padding: 0 96px; position: relative;
    /* .slide is content-box, so padding here would push the slide past 1280px
       and make Chrome shrink-to-fit the whole deck when printing. */
    box-sizing: border-box;
  }
  .icn-sec .quat { position: absolute; right: -140px; bottom: -180px; width: 640px; opacity: 0.07; }
  .icn-sec .snum {
    font-size: 15px; font-weight: 800; letter-spacing: 0.22em;
    color: var(--crp-cyan); margin-bottom: 20px; position: relative; z-index: 2;
  }
  .icn-sec h2 {
    font-size: 52px; line-height: 1.06; font-weight: 800; margin: 0 0 26px;
    letter-spacing: -0.02em; color: #fff; max-width: 860px; position: relative; z-index: 2;
  }
  .icn-sec .sdesc {
    font-size: 19px; line-height: 1.5; color: rgba(255,255,255,0.9);
    max-width: 640px; position: relative; z-index: 2; padding-top: 22px;
    border-top: 1px solid rgba(255,255,255,0.22);
  }
  /* Each divider carries the one number that section proves, so flipping
     through the deck tells the story without reading a slide. */
  .icn-sec .sstat { position: relative; z-index: 2; margin-top: 34px; }
  .icn-sec .sstat .v {
    font-size: 78px; font-weight: 800; color: var(--crp-orange);
    line-height: 0.95; letter-spacing: -0.03em;
  }
  .icn-sec .sstat .k {
    font-size: 16px; color: rgba(255,255,255,0.85); margin-top: 12px; max-width: 480px;
  }
  .icn-sec .footer { color: rgba(255,255,255,0.5); }

  /* ═══ Contents ═══ */
  .icn-toc { display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; max-width: 1120px; margin: 0 auto; width: 100%; }
  .icn-toc a {
    display: block; text-decoration: none; border: 1px solid var(--border);
    border-top: 3px solid var(--crp-blue); border-radius: 12px; padding: 20px 18px;
    background: #fff; box-shadow: var(--shadow-sm); transition: box-shadow .15s, transform .15s;
  }
  .icn-toc a:nth-child(2n) { border-top-color: var(--crp-orange); }
  .icn-toc a:hover { box-shadow: var(--shadow-lg); transform: translateY(-2px); }
  .icn-toc .tn { font-size: 12px; font-weight: 800; letter-spacing: 0.16em; color: var(--crp-blue); }
  .icn-toc .tt { font-size: 17px; font-weight: 800; color: var(--crp-navy); margin-top: 12px; line-height: 1.22; }
  .icn-toc .td { font-size: 12.5px; color: var(--fg-2); margin-top: 8px; line-height: 1.4; }


  /* ═══ In-slide navigation — prints, and works as PDF links ═══ */
  .nav {
    position: absolute; left: 56px; right: 56px; top: 22px;
    display: flex; align-items: center; gap: 5px; z-index: 40;
  }
  .nav a {
    text-decoration: none; font-size: 9.5px; font-weight: 700;
    letter-spacing: 0.07em; text-transform: uppercase;
    padding: 5px 10px; border-radius: 999px;
    color: var(--fg-3); border: 1px solid transparent; white-space: nowrap;
  }
  .nav a.home {
    color: var(--crp-blue); border-color: var(--border);
    background: #fff; margin-right: 4px;
  }
  .nav a.on { background: var(--crp-navy); color: #fff; }
  .nav a:hover { color: var(--crp-navy); }
  .nav .sp { flex: 1; }
  /* On navy slides the bar inverts */
  .icn-sec .nav a, .icn-cover .nav a { color: rgba(255,255,255,0.55); }
  .icn-sec .nav a.home, .icn-cover .nav a.home {
    color: #fff; background: rgba(255,255,255,0.14); border-color: rgba(255,255,255,0.25);
  }
  .icn-sec .nav a.on { background: var(--crp-orange); color: #fff; }
  /* Slide bodies start below the bar */
  .slide-pad { padding-top: 60px; }

  /* ═══ Home hub ═══ */
  .hub-top { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1140px; margin: 0 auto 26px; width: 100%; }
  .hub-top .v { font-size: 50px; font-weight: 800; color: var(--crp-navy); line-height: 1; letter-spacing: -0.03em; }
  .hub-top .v.on { color: var(--crp-orange); }
  .hub-top .k { font-size: 13.5px; color: var(--crp-navy); margin-top: 10px; line-height: 1.35; }
  .hub-rule { max-width: 1140px; margin: 0 auto 22px; height: 1px; background: var(--border); width: 100%; }
  .hub-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; max-width: 1140px; margin: 0 auto; width: 100%; }
  .hub-grid a {
    display: block; text-decoration: none; padding: 16px 16px 15px;
    border: 1px solid var(--border); border-top: 3px solid var(--crp-blue);
    border-radius: 12px; background: #fff; box-shadow: var(--shadow-sm);
  }
  .hub-grid a .n { font-size: 15.5px; font-weight: 800; color: var(--crp-navy); line-height: 1.2; }
  .hub-grid a .d { font-size: 12px; color: var(--fg-2); margin-top: 6px; line-height: 1.35; }
  .hub-grid a .s { font-size: 11.5px; font-weight: 700; color: var(--crp-orange); margin-top: 9px; letter-spacing: 0.04em; }
"""


def nav_bar(active=None):
    out = ['<div class="nav">',
           '<a class="home" href="#home">&#8962; Home</a>']
    for sid, label, *_ in SECTIONS:
        cls = ' class="on"' if sid == active else ''
        out.append('<a href="#%s"%s>%s</a>' % (sid, cls, label))
    out.append('<span class="sp"></span></div>')
    return "".join(out)


def home_slide():
    cards = []
    for sid, label, desc, v, k in SECTIONS:
        cards.append(
            '        <a href="#%s"><div class="n">%s</div><div class="d">%s</div>'
            '<div class="s">%s &middot; %s</div></a>' % (sid, label, desc, v, k))
    return '''<section class="slide" id="home">
  %s
  <div class="slide-pad">
    <div class="slide-head">
      <div class="slide-eyebrow">Clinical Research Philadelphia &middot; for ICON Elite Sites</div>
      <h2 class="slide-h2">A two-site network that delivers more patients per site than the plan assumes.</h2>
    </div>
    <div class="slide-body">
      <div class="hub-top">
        <div><div class="v on">3.5&times;</div><div class="k">the patients per site the sponsor's plan assumed</div></div>
        <div><div class="v">5 of 5</div><div class="k">recent cardiometabolic targets met or beaten</div></div>
        <div><div class="v">70&ndash;95<span style="font-size:26px">%%</span></div><div class="k">retention across those trials</div></div>
        <div><div class="v">0</div><div class="k">FDA Form 483s in thirty years</div></div>
      </div>
      <div class="hub-rule"></div>
      <div class="hub-grid">
%s
      </div>
    </div>
  </div>
  <div class="footer">
    <span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> Start anywhere &mdash; every slide links back here</span>
    <span class="pageno">02</span>
  </div>
</section>''' % (nav_bar(), "\n".join(cards))


def section_cover(sid, label, desc, v, k, num):
    return '''<section class="slide icn-sec" id="%s">
  <img class="quat" src="./assets/stencils/quatrefoil.svg" alt="">
  %s
  <div class="snum">SECTION %02d</div>
  <h2>%s</h2>
  <div class="sdesc">%s</div>
  <div class="sstat"><div class="v">%s</div><div class="k">%s</div></div>
  <div class="footer">
    <span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> %s</span>
    <span class="pageno">00</span>
  </div>
</section>''' % (sid, nav_bar(sid), num, label, desc, v, k,
                 label.replace("&amp;", "and"))


if __name__ == "__main__":
    import pathlib
    SP = pathlib.Path("/private/tmp/claude-501/-Users-aneeshvaze/87a944af-9de1-4676-a628-87aed6874952/scratchpad")
    covers = "\n\n".join(
        section_cover(sid, label, desc, v, k, i)
        for i, (sid, label, desc, v, k) in enumerate(SECTIONS, 1))
    SP.joinpath("icon_hub.html").write_text(
        "<style>%s</style>\n\n%s\n\n%s\n" % (NAV_CSS, home_slide(), covers))
    print("hub + %d section covers written" % len(SECTIONS))
