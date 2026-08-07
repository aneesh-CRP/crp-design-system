#!/usr/bin/env python3
"""Re-inject each prospecting brief's study slides into the CURRENT executive
overview and re-render. The committed crp-prospecting-*.html files each embed a
point-in-time SNAPSHOT of the overview, so a brief built in July still carries
that month's slides — re-rendering its own HTML would change nothing."""
import pathlib, re, subprocess

DS = pathlib.Path.home() / "crp-design-system"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
EXEC = (DS / "executive-overview.html").read_text()
BLOCK = re.compile(r"<!--[^>]*STUDY-SPECIFIC SITE BRIEF \(prepended\).*?END STUDY BRIEF.*?-->", re.S)

TARGETS = {
    "AKERO-SYNCHRONY-MASH": "CRP-AKERO-SYNCHRONY-Site-Brief.pdf",
    "ARROWHEAD-SHASTA5-TG": "CRP-ARROWHEAD-SHASTA5-Site-Brief.pdf",
    "BMS-PRAGMATYK-PSORIASIS": "CRP-BMS-PRAGMATYK-Site-Brief.pdf",
    "BOEHRINGER-LIVERAGE-MASH": "CRP-BOEHRINGER-LIVERAGE-Site-Brief.pdf",
    "MADRIGAL-MASH": "CRP-MADRIGAL-Site-Brief.pdf",
    "MERCK-CORALREEF-LIPIDS": "CRP-MERCK-CORALREEF-Site-Brief.pdf",
    "NEWAMSTERDAM-RUBENS-LIPIDS": "CRP-NEWAMSTERDAM-RUBENS-Site-Brief.pdf",
    "NOVARTIS-IANALUMAB-SLE": "CRP-NOVARTIS-IANALUMAB-SLE-Site-Brief.pdf",
}
for slug, pdf_name in TARGETS.items():
    src = DS / f"crp-prospecting-{slug}.html"
    old = src.read_text()
    m = BLOCK.search(old)
    assert m, f"no study block in {slug}"
    title = re.search(r"<title>(.*?)</title>", old, re.S).group(1)
    html = EXEC.replace('<div class="deck">', '<div class="deck">\n' + m.group(0), 1)
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1)
    src.write_text(html)
    pdf = pathlib.Path.home() / pdf_name
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=20000", f"--print-to-pdf={pdf}", f"file://{src}"],
                   check=True, capture_output=True)
    print(f"  {slug:<28} -> {pdf.name}")
