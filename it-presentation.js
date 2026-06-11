// Operations Portal deck — overflow guard + feedback button
// Extracted from inline <script> blocks to comply with strict CSP.

(function () {
  function checkOverflow() {
    var slides = document.querySelectorAll('.slide');
    var failures = [];
    slides.forEach(function (slide, idx) {
      // tolerance: 2px to absorb subpixel rounding
      var excess = slide.scrollHeight - slide.clientHeight;
      var overflows = excess > 2;
      slide.classList.toggle('overflow', overflows);
      if (overflows) {
        slide.setAttribute('data-overflow-px', excess);
        failures.push({ slide: idx + 1, excess: excess });
      } else {
        slide.removeAttribute('data-overflow-px');
      }
    });
    if (failures.length) {
      console.warn('[overflow guard] ' + failures.length + ' slide(s) over 720px:');
      failures.forEach(function (f) {
        console.warn('  slide ' + f.slide + ' overflows by ' + f.excess + 'px');
      });
    } else {
      console.log('[overflow guard] all slides fit ✓');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', checkOverflow);
  } else {
    checkOverflow();
  }
  window.addEventListener('resize', checkOverflow);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(checkOverflow);
  }
  setTimeout(checkOverflow, 500);
})();

(function () {
  function init() {
    if (document.getElementById('crp-feedback-btn')) return;
    var btn = document.createElement('button');
    btn.id = 'crp-feedback-btn';
    btn.textContent = 'Send Feedback';
    btn.title = 'Press A to annotate, I to inspect, C to copy. Then click here to email annotations.';
    btn.style.cssText = [
      'position:fixed', 'bottom:14px', 'right:14px', 'z-index:2147483646',
      'padding:7px 14px', 'font-size:11.5px', 'font-weight:600',
      'background:#072061', 'color:#fff', 'border:none', 'border-radius:6px',
      'cursor:pointer', 'box-shadow:0 2px 8px rgba(7,32,97,0.18)',
      'font-family:Inter,-apple-system,system-ui,sans-serif',
      'letter-spacing:0.04em', 'transition:transform .15s, box-shadow .15s, opacity .15s',
      'opacity:0.85'
    ].join(';');
    btn.addEventListener('mouseenter', function () {
      btn.style.transform = 'translateY(-1px)';
      btn.style.boxShadow = '0 4px 12px rgba(7,32,97,0.28)';
      btn.style.opacity = '1';
    });
    btn.addEventListener('mouseleave', function () {
      btn.style.transform = '';
      btn.style.boxShadow = '0 2px 8px rgba(7,32,97,0.18)';
      btn.style.opacity = '0.85';
    });
    btn.addEventListener('click', async function () {
      var name = (prompt('Your name (so Aneesh knows who left feedback):') || 'Reviewer').trim();
      var body = '';
      try {
        if (navigator.clipboard && navigator.clipboard.readText) {
          body = await navigator.clipboard.readText();
        }
      } catch (e) { /* clipboard read denied */ }
      var subject = 'CRP Operations Portal — feedback from ' + name;
      var mailBody = [
        'From: ' + name,
        'Deck: ' + location.href,
        'Date: ' + new Date().toISOString(),
        '',
        '--- annotations (paste from clipboard, or write below) ---',
        '',
        body || '(press A in the deck to annotate, then C to copy, then click Send Feedback again)',
        ''
      ].join('\n');
      window.location.href = 'mailto:aneesh@phillyresearch.com'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(mailBody);
    });
    document.body.appendChild(btn);

    var hint = document.createElement('div');
    hint.id = 'crp-feedback-hint';
    hint.innerHTML = 'Press <strong>A</strong> to annotate · <strong>I</strong> to inspect · <strong>C</strong> to copy';
    hint.style.cssText = [
      'position:fixed', 'bottom:14px', 'right:140px', 'z-index:2147483645',
      'padding:6px 12px', 'font-size:10.5px',
      'background:rgba(7,32,97,0.85)', 'color:#fff', 'border-radius:5px',
      'font-family:Inter,-apple-system,system-ui,sans-serif',
      'box-shadow:0 4px 12px rgba(7,32,97,0.25)',
      'transition:opacity .3s', 'pointer-events:none'
    ].join(';');
    document.body.appendChild(hint);
    setTimeout(function () { hint.style.opacity = '0'; }, 6000);
    setTimeout(function () { hint.remove(); }, 6500);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
