#!/usr/bin/env python3
"""Build the LEO Pharma and UCB site-capability briefs.

Method per project_bd_globaldata_engine: inject a study-specific slide block
after `<div class="deck">` in crp-design-system/executive-overview.html, write
the combined HTML into the design-system directory (so ./assets paths resolve),
then render with headless Chrome.
"""
import pathlib
import re
import subprocess

DS = pathlib.Path.home() / "crp-design-system"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
EXEC_HTML = (DS / "executive-overview.html").read_text()

# The scoped .sx- styles are lifted verbatim from the proven BMS brief so the
# study slides sit in the same visual system as the capabilities deck.
SX_PEOPLE_FIX = "<style>.sx-people{margin-top:8px;gap:8px;}"\
                ".sx-person{padding:7px 12px;font-size:12px;}</style>"

SX_STYLE = re.search(
    r"STUDY-SPECIFIC SITE BRIEF \(prepended\).*?-->\s*(<style>.*?</style>)",
    (DS / "crp-prospecting-BMS-PRAGMATYK-PSORIASIS.html").read_text(),
    re.S,
).group(1)


def cover(eyebrow, h1, sub, why, chips, sponsor, script, tag):
    chip_html = "".join(
        f'<div class="sx-chip"><div class="n">{n}</div><div class="l">{l}</div></div>'
        for n, l in chips
    )
    return f"""
<section class="slide sx-cover2">
  <img class="sx-quat" src="./assets/stencils/quatrefoil.svg" alt="">
  <div class="sx-cov-left">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <div class="sub">{sub}</div>
    <div class="why">{why}</div>
    <div class="sx-strip">{chip_html}</div>
  </div>
  <div class="sx-cov-right">
    <img class="sx-logo" src="./assets/logos/crp-white.svg" alt="Clinical Research Philadelphia">
    <div class="sx-covtag">Site Capabilities Brief</div>
    <div class="sx-covprep">Prepared for<b>{sponsor}</b></div>
    <div class="sx-script">{script}</div>
  </div>
  <div class="sx-cfoot"><span class="m"><img src="./assets/logos/crp-icon.svg" alt=""> phillyresearch.com</span><span>{tag} &middot; Site Brief &middot; S1</span></div>
</section>
"""


def qa_slide(eyebrow, h2, lede, rows, people, tag):
    row_html = "".join(
        f'<div class="sx-row"><div class="q">{q}</div><div class="a">{a}</div></div>'
        for q, a in rows
    )
    ppl_html = "".join(f'<div class="sx-person">{p}</div>' for p in people)
    return f"""
<section class="slide">
  <div class="slide-pad">
    <div class="slide-head">
      <div class="slide-eyebrow">{eyebrow}</div>
      <h2 class="slide-h2">{h2}</h2>
      <p class="slide-lede">{lede}</p>
    </div>
    <div class="sx-qa">{row_html}</div>
    <div class="sx-people">{ppl_html}</div>
  </div>
  <div class="footer"><span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> Clinical Research Philadelphia</span><span class="pageno">{tag} &middot; S2</span></div>
</section>
"""


SX_EXP_STYLE = """<style>
  .sx-exp{display:grid;grid-template-columns:1fr 1fr;gap:26px 34px;max-width:1120px;margin:0 auto;width:100%;}
  .sx-exp .col-h{font-size:12.5px;font-weight:800;color:var(--crp-navy);text-transform:uppercase;
                 letter-spacing:.06em;margin:0 0 10px;padding-bottom:7px;border-bottom:1px solid var(--border);}
  .sx-trial{display:flex;gap:10px;align-items:flex-start;padding:6px 0;}
  .sx-trial .ph{flex:0 0 auto;font-size:10px;font-weight:800;letter-spacing:.04em;
                padding:3px 7px;border-radius:999px;background:var(--blue-bg);color:var(--crp-blue);margin-top:1px;}
  .sx-trial .ph.two{background:#fff3e0;color:var(--crp-orange);}
  .sx-trial .tx{font-size:13px;line-height:1.4;color:var(--crp-navy);opacity:.94;}
  .sx-trial .tx b{font-weight:700;}
  .sx-credstrip{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;
                max-width:1120px;margin:22px auto 0;width:100%;padding-top:16px;border-top:1px solid var(--border);}
  .sx-credcell{border:1px solid var(--border);border-top:3px solid var(--crp-blue);border-radius:10px;
               padding:11px 14px;background:#fff;}
  .sx-credcell:nth-child(2n){border-top-color:var(--crp-orange);}
  .sx-credcell .n{font-size:22px;font-weight:800;color:var(--crp-navy);line-height:1;}
  .sx-credcell .k{font-size:12.5px;font-weight:700;color:var(--crp-navy);margin-top:6px;}
  .sx-credcell .d{font-size:11px;color:var(--fg-2);margin-top:2px;line-height:1.35;}
  .sx-partners{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;
               max-width:1120px;margin:16px auto 0;width:100%;}
  .sx-partners .lbl{font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--fg-3);
                    font-weight:700;margin-right:4px;}
  .sx-partners .p{font-size:12px;color:var(--crp-navy);background:var(--surface-2);
                  border:1px solid var(--border);border-radius:999px;padding:6px 13px;}
</style>"""


def experience_slide(eyebrow, h2, lede, col1_h, col1, col2_h, col2, creds, tag, foot, partners=None):
    def trials(items):
        out = []
        for desc, phase in items:
            cls = "ph two" if phase.strip().lower().endswith("ii") and "iii" not in phase.lower() else "ph"
            out.append(f'<div class="sx-trial"><span class="{cls}">{phase}</span>'
                       f'<span class="tx">{desc}</span></div>')
        return "".join(out)

    cred_html = "".join(
        f'<div class="sx-credcell"><div class="n">{n}</div><div class="k">{k}</div><div class="d">{d}</div></div>'
        for n, k, d in creds
    )
    partner_html = ""
    if partners:
        chips = "".join(f'<span class="p">{x}</span>' for x in partners)
        partner_html = f'<div class="sx-partners"><span class="lbl">Community</span>{chips}</div>'
    return f"""
<section class="slide">
  <div class="slide-pad">
    <div class="slide-head">
      <div class="slide-eyebrow">{eyebrow}</div>
      <h2 class="slide-h2">{h2}</h2>
      <p class="slide-lede">{lede}</p>
    </div>
    <div class="sx-exp">
      <div><div class="col-h">{col1_h}</div>{trials(col1)}</div>
      <div><div class="col-h">{col2_h}</div>{trials(col2)}</div>
    </div>
    <div class="sx-credstrip">{cred_html}</div>
    {partner_html}
  </div>
  <div class="footer"><span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> {foot}</span><span class="pageno">{tag} &middot; S3</span></div>
</section>
"""


def funnel_slide(eyebrow, h2, lede, stages, arrows, capline, left_h, left, right_h, right, tag, foot):
    bar_colors = ["#072061", "#1843AD", "#3a6bc5", "#5b86d6", "#FF9933"]
    parts = []
    for i, (n, label, sub) in enumerate(stages):
        parts.append(
            f'<div class="sx-stage"><div class="sx-bar" style="background:{bar_colors[i]};">'
            f'<span class="sn">{n}</span><span class="sl">{label}</span></div>'
            f'<div class="sx-conv">{sub}</div></div>'
        )
        if i < len(arrows):
            pc, txt = arrows[i]
            parts.append(f'<div class="sx-arrow"><span class="pc">{pc}</span>{txt}</div>')
    left_html = "".join(f"<li>{x}</li>" for x in left)
    right_html = "".join(f"<li>{x}</li>" for x in right)
    return f"""
<section class="slide">
  <div class="slide-pad">
    <div class="slide-head">
      <div class="slide-eyebrow">{eyebrow}</div>
      <h2 class="slide-h2">{h2}</h2>
      <p class="slide-lede">{lede}</p>
    </div>
    <div class="sx-funnel">{''.join(parts)}</div>
    <div class="sx-capline">{capline}</div>
    <div class="sx-two">
      <div><div class="sx-h">{left_h}</div><ul class="sx-list">{left_html}</ul></div>
      <div><div class="sx-h">{right_h}</div><ul class="sx-list tealdot">{right_html}</ul></div>
    </div>
  </div>
  <div class="footer"><span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> {foot}</span><span class="pageno">{tag} &middot; S4</span></div>
</section>
"""


def cta_slide(h2, lede, need, give, cta_t, cta_c, who, tag):
    need_html = "".join(f"<li>{x}</li>" for x in need)
    give_html = "".join(f"<li>{x}</li>" for x in give)
    return f"""
<section class="slide">
  <div class="slide-pad">
    <div class="slide-head">
      <div class="slide-eyebrow">Next steps</div>
      <h2 class="slide-h2">{h2}</h2>
      <p class="slide-lede">{lede}</p>
    </div>
    <div class="sx-cta-two">
      <div><div class="sx-h">What we'd need from you</div><ul class="sx-list big">{need_html}</ul></div>
      <div><div class="sx-h">What you'll get back &mdash; fast</div><ul class="sx-list big tealdot">{give_html}</ul></div>
    </div>
    <div class="sx-bigcta">
      <div><div class="t">{cta_t}</div><div class="c">{cta_c}</div></div>
      <div class="who">{who}</div>
    </div>
    <div class="sx-cred"><div class="c"><div class="n">30 yrs</div><div class="l">Operating since 1996</div></div><div class="c"><div class="n">500+</div><div class="l">Clinical trials run</div></div><div class="c"><div class="n">2 sites</div><div class="l">Philadelphia + Pennington</div></div><div class="c"><div class="n">95%</div><div class="l">Hit enrollment target</div></div><div class="c"><div class="n">&lt;21d</div><div class="l">Study start-up</div></div></div>
  </div>
  <div class="footer"><span class="mark"><img src="./assets/logos/crp-icon.svg" alt=""> Let's build the future of medicine</span><span class="pageno">{tag} &middot; S5</span></div>
</section>
"""


def build(name, title, slides, pdf_name):
    block = (
        "\n<!-- ============ STUDY-SPECIFIC SITE BRIEF (prepended) ============ -->\n"
        + SX_STYLE
        + SX_PEOPLE_FIX
        + SX_EXP_STYLE
        + "\n"
        + "\n".join(slides)
        + "\n<!-- ============ END STUDY BRIEF — GENERAL CAPABILITIES FOLLOW ============ -->\n"
    )
    html = EXEC_HTML.replace('<div class="deck">', '<div class="deck">\n' + block, 1)
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1)
    out = DS / name
    out.write_text(html)
    pdf = pathlib.Path.home() / pdf_name
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         "--virtual-time-budget=20000", f"--print-to-pdf={pdf}", f"file://{out}"],
        check=True, capture_output=True,
    )
    return out, pdf
