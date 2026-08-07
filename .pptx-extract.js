// Extract painted boxes, rich text blocks and images from each rendered slide.
// Paste as the body of a chrome-devtools evaluate_script call.
//
// The subtlety is text: an element like `.ta-actual` owns the text "Target 15 · "
// AND contains a <strong> owning "Actual 51 · 340%". Emitting a box for each
// prints the value twice, overlapping. So collect only the OUTERMOST elements
// that own text, then walk their children into styled runs.
() => {
  const rgb = (s) => {
    const m = (s || '').match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
    if (!m) return null;
    const a = m[4] === undefined ? 1 : parseFloat(m[4]);
    if (a < 0.06) return null;
    return { hex: [1, 2, 3].map(i => (+m[i]).toString(16).padStart(2, '0')).join(''), a };
  };
  const ownsText = (el) =>
    [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());

  const slides = [];
  document.querySelectorAll('.slide').forEach((slide) => {
    const sr = slide.getBoundingClientRect();
    const shapes = [], images = [];
    const all = [slide, ...slide.querySelectorAll('*')];

    all.forEach((el) => {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return;
      const r = el.getBoundingClientRect();
      const x = r.left - sr.left, y = r.top - sr.top;
      if (r.width < 1 || r.height < 1 || y > 760 || x > 1320) return;
      if (el.tagName === 'IMG') {
        images.push({ x, y, w: r.width, h: r.height, src: el.getAttribute('src') });
        return;
      }
      const fill = rgb(cs.backgroundColor);
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => parseFloat(cs['border' + s + 'Width']) || 0);
      const bc = ['Top', 'Right', 'Bottom', 'Left'].map(s => rgb(cs['border' + s + 'Color']));
      if (fill || bw.some(v => v > 0.4)) {
        shapes.push({ x, y, w: r.width, h: r.height, fill, bw, bc,
                      radius: parseFloat(cs.borderTopLeftRadius) || 0,
                      cls: (el.className || '').toString().slice(0, 40) });
      }
    });

    // outermost text owners only
    const owners = all.filter(el => {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
      return ownsText(el);
    });
    const blocks = owners.filter(el => !owners.some(o => o !== el && o.contains(el)));

    const texts = blocks.map((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const base = { weight: parseInt(cs.fontWeight) || 400, color: rgb(cs.color),
                     italic: cs.fontStyle === 'italic', size: parseFloat(cs.fontSize) };
      const runs = [];
      const walk = (node, style) => {
        node.childNodes.forEach((n) => {
          if (n.nodeType === 3) {
            if (n.textContent) runs.push(Object.assign({ t: n.textContent }, style));
          } else if (n.nodeType === 1) {
            if (n.tagName === 'BR') { runs.push(Object.assign({ t: '\n' }, style)); return; }
            const c2 = getComputedStyle(n);
            if (c2.display === 'none') return;
            walk(n, { weight: parseInt(c2.fontWeight) || 400, color: rgb(c2.color),
                      italic: c2.fontStyle === 'italic', size: parseFloat(c2.fontSize) });
          }
        });
      };
      walk(el, base);
      return {
        x: r.left - sr.left, y: r.top - sr.top, w: r.width, h: r.height,
        runs, align: cs.textAlign, size: base.size,
        lh: parseFloat(cs.lineHeight) || base.size * 1.3,
        upper: cs.textTransform === 'uppercase', family: cs.fontFamily,
      };
    }).filter(t => t.runs.some(r => r.t.trim()));

    slides.push({ shapes, texts, images });
  });
  return { slides, title: document.title, n: slides.length };
}
