// ──────────────────────────────────────────────────────────────────────────
// src/ds.js — CRP Design System component helpers
//
// Source of truth: design-system/manifest.json + design-system/DOCTRINE.md §2
//
// Plain script (NOT ES module) — concatenated by scripts/build.py with the
// other src/*.js files; all share global scope. Public API is namespaced
// on window.ds via an IIFE that hides internal helpers.
//
// Every helper returns an HTML string with:
//   • `data-ds="<id>"` attribute for lint + audit + ?ds-debug=1 overlay
//   • Class names matching the manifest
//
// Helpers are PURE rendering — they do not bind events. CSP-safe: no inline
// onclick handlers. Callers wire behavior via data-action attributes + a
// global addEventListener (matches the existing data-action pattern in the
// dashboard).
// ──────────────────────────────────────────────────────────────────────────

window.ds = (function () {
  'use strict';

  // HTML-safe text escape (prevent XSS when interpolating user data)
  function _esc(s) {
    if (s === null || s === undefined) return '';
    return String(s).replace(/[<>&"']/g, function (c) {
      return ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  // HTML-safe attribute value
  function _attr(s) {
    return _esc(s).replace(/\s+/g, ' ').trim();
  }

  // Optional class joiner — drops falsy entries
  function _cls() {
    return Array.prototype.slice.call(arguments).filter(Boolean).join(' ');
  }

  var api = {};

  // ─── §2.1 Buttons ────────────────────────────────────────────────────

  api.button = function (opts) {
    opts = opts || {};
    var variant = opts.variant || 'primary';
    var size = opts.size || 'default';
    var label = opts.label;
    var icon = opts.icon;
    var dataAction = opts.dataAction;
    var dataArg = opts.dataArg;
    var dataArg2 = opts.dataArg2;
    var disabled = !!opts.disabled;
    var ariaLabel = opts.ariaLabel;
    if (!label && !icon) return '';
    var cls = _cls('btn', 'btn-' + variant, size !== 'default' && 'btn-' + size);
    var iconHtml = icon ? '<span class="btn-icon-glyph" aria-hidden="true">' + _esc(icon) + '</span>' : '';
    var labelHtml = label ? '<span class="btn-label">' + _esc(label) + '</span>' : '';
    var dataActionAttr = dataAction ? ' data-action="' + _attr(dataAction) + '"' : '';
    var dataArgAttr = (dataArg !== undefined && dataArg !== null && dataArg !== '') ? ' data-arg="' + _attr(dataArg) + '"' : '';
    var dataArg2Attr = (dataArg2 !== undefined && dataArg2 !== null && dataArg2 !== '') ? ' data-arg2="' + _attr(dataArg2) + '"' : '';
    var disAttr = disabled ? ' disabled' : '';
    var ariaAttr = ariaLabel ? ' aria-label="' + _attr(ariaLabel) + '"' : '';
    return '<button type="button" class="' + cls + '" data-ds="button"' + dataActionAttr + dataArgAttr + dataArg2Attr + disAttr + ariaAttr + '>' + iconHtml + labelHtml + '</button>';
  };

  api.buttonIcon = function (opts) {
    opts = opts || {};
    if (!opts.glyph) return '';
    var dataAttr = opts.dataAction ? ' data-action="' + _attr(opts.dataAction) + '"' : '';
    var ariaAttr = opts.ariaLabel ? ' aria-label="' + _attr(opts.ariaLabel) + '"' : ' aria-label="action"';
    return '<button type="button" class="btn-icon" data-ds="button-icon"' + dataAttr + ariaAttr + '>' + _esc(opts.glyph) + '</button>';
  };

  api.actionRow = function (buttonsHtml) {
    var inner = Array.isArray(buttonsHtml) ? buttonsHtml.join('') : (buttonsHtml || '');
    return '<div class="actions" data-ds="action-row">' + inner + '</div>';
  };

  // ─── §2.2 Status indicators ──────────────────────────────────────────

  // Chip — small inline status label.
  // variant: success | warning | danger | info | meta | ai | ghost
  api.chip = function (opts) {
    opts = opts || {};
    var variant = opts.variant || 'meta';
    var text = opts.text;
    var icon = opts.icon;
    if (text === null || text === undefined || text === '') return '';
    var iconHtml = icon ? '<span class="chip-icon" aria-hidden="true">' + _esc(icon) + '</span>' : '';
    return '<span class="chip chip-' + variant + '" data-ds="chip">' + iconHtml + _esc(text) + '</span>';
  };

  // Study lifecycle pill. status is normalized to lowercase-hyphen-form.
  api.studyPill = function (opts) {
    opts = opts || {};
    if (!opts.status) return '';
    var v = String(opts.status).toLowerCase().replace(/\s+/g, '-');
    // deep-review f306: status is data (CRIO lifecycle strings) — escape the
    // class-attribute side too, so a quote/angle-bracket can't break out.
    return '<span class="pill pill-' + _attr(v) + '" data-ds="pill-study-status">' + _esc(opts.status) + '</span>';
  };

  // Status dot — color only, no label. variant: success | warning | danger | info | meta
  api.statusDot = function (opts) {
    opts = opts || {};
    var variant = opts.variant || 'meta';
    var ariaAttr = opts.ariaLabel
      ? ' aria-label="' + _attr(opts.ariaLabel) + '" role="img"'
      : ' aria-hidden="true"';
    return '<span class="dot dot-' + variant + '" data-ds="status-dot"' + ariaAttr + '></span>';
  };

  // Severity flag — high-emphasis. variant: urgent | warning
  api.severityFlag = function (opts) {
    opts = opts || {};
    var variant = opts.variant || 'warning';
    if (!opts.label) return '';
    return '<span class="flag flag-' + variant + '" data-ds="severity-flag">' + _esc(opts.label) + '</span>';
  };

  // Site tag — PHL / PNJ geographic indicator. Accepts loose site strings
  // ('pnj', 'phl', 'Pennington', 'Philadelphia', etc.) and normalizes.
  api.siteTag = function (opts) {
    opts = opts || {};
    var s = String(opts.site || '').toLowerCase();
    var isPNJ = s === 'pnj' || s.indexOf('penn') >= 0 || s.indexOf('njo') >= 0;
    var label = isPNJ ? 'PNJ' : 'PHL';
    var variant = isPNJ ? 'pnj' : 'phl';
    return '<span class="site-tag site-tag-' + variant + '" data-ds="site-tag">' + label + '</span>';
  };

  // Purpose badge — study/visit-type identifier (DISTINCT from status chip).
  // tone: red | violet | blue | green | indigo | amber
  // Use when: labelling a study, visit type, or campaign so it's scannable
  //   across rows. NOT a status indicator.
  api.purposeBadge = function (opts) {
    opts = opts || {};
    if (!opts.label) return '';
    var tone = opts.tone || 'blue';
    return '<span class="purpose-badge purpose-badge-' + tone + '" data-ds="purpose-badge">' + _esc(opts.label) + '</span>';
  };

  // ─── §2.3 Cards & containers ─────────────────────────────────────────

  api.kpiTile = function (opts) {
    opts = opts || {};
    var label = opts.label;
    var value = opts.value;
    if (!label && (value === null || value === undefined)) return '';
    var size = opts.size || 'default';
    var deltaDir = opts.deltaDir || 'flat';
    var cls = _cls('kpi-tile', size === 'compact' && 'kpi-tile-compact');
    var dataAttr = opts.dataAction ? ' data-action="' + _attr(opts.dataAction) + '"' : '';
    var deltaArrow = deltaDir === 'up' ? '↑' : deltaDir === 'down' ? '↓' : '→';
    var deltaHtml = opts.delta
      ? '<span class="kpi-tile-delta kpi-tile-delta-' + deltaDir + '">' + deltaArrow + ' ' + _esc(opts.delta) + '</span>'
      : '';
    var subHtml = opts.subLabel ? '<span class="kpi-tile-sublabel">' + _esc(opts.subLabel) + '</span>' : '';
    var sparkHtml = opts.sparklineHtml ? '<div class="kpi-tile-sparkline">' + opts.sparklineHtml + '</div>' : '';
    var displayValue = (value === null || value === undefined) ? '—' : value;
    return '<div class="' + cls + '" data-ds="kpi-tile"' + dataAttr + '>'
      + '<div class="kpi-tile-label">' + _esc(label || '') + '</div>'
      + '<div class="kpi-tile-value">' + _esc(displayValue) + '</div>'
      + deltaHtml + subHtml + sparkHtml
      + '</div>';
  };

  api.card = function (opts) {
    opts = opts || {};
    var headerInner = opts.headerHtml || (opts.title ? '<h3 class="card-title">' + _esc(opts.title) + '</h3>' : '');
    var headerBlock = headerInner ? '<div class="card-header">' + headerInner + '</div>' : '';
    var footerBlock = opts.footerHtml ? '<div class="card-footer">' + opts.footerHtml + '</div>' : '';
    return '<div class="card" data-ds="section-card">' + headerBlock + '<div class="card-body">' + (opts.body || '') + '</div>' + footerBlock + '</div>';
  };

  api.alert = function (opts) {
    opts = opts || {};
    if (!opts.body) return '';
    var variant = opts.variant || 'info';
    var defaultIcons = { info: 'ⓘ', success: '✓', warning: '!', danger: '✗' };
    var iconChar = opts.icon || defaultIcons[variant] || 'ⓘ';
    var titleHtml = opts.title ? '<div class="alert-title">' + _esc(opts.title) + '</div>' : '';
    var actionHtml = opts.action ? '<div class="alert-action">' + opts.action + '</div>' : '';
    return '<div class="alert alert-' + variant + '" data-ds="alert" role="alert">'
      + '<span class="alert-icon" aria-hidden="true">' + _esc(iconChar) + '</span>'
      + '<div class="alert-body">' + titleHtml + '<div class="alert-text">' + _esc(opts.body) + '</div>' + actionHtml + '</div>'
      + '</div>';
  };

  // ─── §2.6 Filters ────────────────────────────────────────────────────

  api.filterBar = function (opts) {
    opts = opts || {};
    var search = opts.searchHtml ? '<div class="filter-bar-search">' + opts.searchHtml + '</div>' : '';
    var filtersInner = Array.isArray(opts.filtersHtml) ? opts.filtersHtml.join('') : (opts.filtersHtml || '');
    var filters = filtersInner ? '<div class="filter-bar-filters">' + filtersInner + '</div>' : '';
    var actions = opts.actionsHtml ? '<div class="filter-bar-actions">' + opts.actionsHtml + '</div>' : '';
    return '<div class="filter-bar" data-ds="filter-bar">' + search + filters + actions + '</div>';
  };

  api.filterChip = function (opts) {
    opts = opts || {};
    if (!opts.label) return '';
    var active = !!opts.active;
    var cls = _cls('filter-chip', active && 'filter-chip-active');
    var countHtml = (opts.count !== undefined && opts.count !== null && opts.count !== '')
      ? '<span class="filter-chip-count">' + _esc(opts.count) + '</span>'
      : '';
    var dataAttr = opts.dataFilter ? ' data-filter="' + _attr(opts.dataFilter) + '"' : '';
    return '<button type="button" class="' + cls + '" data-ds="filter-chip"' + dataAttr + ' aria-pressed="' + (active ? 'true' : 'false') + '">' + _esc(opts.label) + countHtml + '</button>';
  };

  // ─── §2.9 State surfaces ─────────────────────────────────────────────

  api.emptyState = function (opts) {
    opts = opts || {};
    if (!opts.headline) return '';
    var illust = opts.illustrationHtml ? '<div class="empty-state-illustration">' + opts.illustrationHtml + '</div>' : '';
    var bodyHtml = opts.body ? '<p class="empty-state-body">' + _esc(opts.body) + '</p>' : '';
    var actionBlock = opts.actionHtml ? '<div class="empty-state-action">' + opts.actionHtml + '</div>' : '';
    return '<div class="empty-state" data-ds="empty-state">' + illust
      + '<h3 class="empty-state-headline">' + _esc(opts.headline) + '</h3>'
      + bodyHtml + actionBlock + '</div>';
  };

  api.errorState = function (opts) {
    opts = opts || {};
    var headline = opts.headline || 'Something went wrong';
    var bodyHtml = opts.body ? '<p class="error-state-body">' + _esc(opts.body) + '</p>' : '';
    var actionBlock = opts.actionHtml ? '<div class="error-state-action">' + opts.actionHtml + '</div>' : '';
    return '<div class="error-state" data-ds="error-state" role="alert">'
      + '<span class="error-state-icon" aria-hidden="true">⚠</span>'
      + '<h3 class="error-state-headline">' + _esc(headline) + '</h3>'
      + bodyHtml + actionBlock + '</div>';
  };

  api.spinner = function (opts) {
    opts = opts || {};
    var size = opts.size || 20;
    var ariaLabel = opts.ariaLabel || 'Loading';
    return '<span class="spinner spinner-' + size + '" data-ds="loading-spinner" role="status" aria-label="' + _attr(ariaLabel) + '"></span>';
  };

  api.skeleton = function (opts) {
    opts = opts || {};
    var shape = opts.shape || 'text';
    var count = opts.count || 1;
    var out = '';
    for (var i = 0; i < count; i++) {
      out += '<span class="skel skel-' + shape + '" data-ds="loading-skeleton" aria-hidden="true"></span>';
    }
    return out;
  };

  api.lastUpdated = function (opts) {
    opts = opts || {};
    if (!opts.stamp) return '';
    return '<span class="last-updated" data-ds="last-updated-stamp" aria-live="polite">Updated ' + _esc(opts.stamp) + '</span>';
  };

  api.toast = function (opts) {
    opts = opts || {};
    if (!opts.body) return '';
    var variant = opts.variant || 'info';
    var titleHtml = opts.title ? '<div class="alert-title">' + _esc(opts.title) + '</div>' : '';
    return '<div class="toast toast-' + variant + '" data-ds="toast" role="status">' + titleHtml + '<div>' + _esc(opts.body) + '</div></div>';
  };

  // ─── §2.11 Phone formatting ──────────────────────────────────────────
  // (deep-review f305: registered in manifest.json + DOCTRINE.md §2.11 —
  //  §2.10 was already Charts & data viz.)
  //
  // ONE chokepoint for every phone display in the dashboards. Handles all
  // the input shapes that arrive from CRIO / forms / BQ:
  //
  //   "5551234567"       → "(555) 123-4567"
  //   "15551234567"      → "(555) 123-4567"
  //   "+15551234567"     → "(555) 123-4567"
  //   "+1 (555) 123-4567"→ "(555) 123-4567"
  //   "+1 15551234567"   → "(555) 123-4567"   ← the +1+1 duplication bug
  //   "+11 5551234567"   → "(555) 123-4567"
  //
  // Returns the original input unchanged if it doesn't look like a US
  // 10-digit number (international, extensions, garbage). Display-only —
  // SMS/email send paths still use E.164 via _e164() server-side.
  //
  // deep-review f307: structurally-invalid NANP numbers (area code starting
  // with 0/1 — e.g. the leading-1-with-dropped-digit capture corruption
  // "1215873953") must NOT be prettified into a legitimate-looking
  // "(121) 587-3953". Return the raw input so the corruption stays visible.
  // Mirrors the area-code guard in crp-unified-dashboard
  // cloud-function/lib/leads-crm.ts (normPhoneDigits). Exchange-digit
  // validation is intentionally NOT enforced: the dashboard contract test
  // uses the reserved 555-123-XXXX fixtures whose exchange starts with 1.
  api.fmtPhone = function (raw) {
    if (raw === null || raw === undefined || raw === '') return '';
    var digits = String(raw).replace(/\D/g, '');
    while (digits.length > 10 && digits.charAt(0) === '1') {
      digits = digits.substring(1);
    }
    if (digits.length !== 10) return String(raw);
    // deep-review f307: NANP area code can never start with 0/1 — corrupted capture, keep raw
    if (!/^[2-9]/.test(digits)) return String(raw);
    return '(' + digits.substring(0, 3) + ') ' + digits.substring(3, 6) + '-' + digits.substring(6);
  };

  // Returns the bare 10 digits (no formatting) — used for tel: hrefs.
  // Returns '' if the input doesn't normalize to 10 US digits.
  api.phoneDigits = function (raw) {
    if (raw === null || raw === undefined || raw === '') return '';
    var digits = String(raw).replace(/\D/g, '');
    while (digits.length > 10 && digits.charAt(0) === '1') {
      digits = digits.substring(1);
    }
    // deep-review f307: reject NANP-impossible area codes (0/1 start) so
    // phoneLink falls back to plain text instead of a fake-dialable tel: href
    return (digits.length === 10 && /^[2-9]/.test(digits)) ? digits : '';
  };

  // Renders a tel: anchor with formatted display text. Falls back to plain
  // text when the input isn't a recognizable 10-digit number, so callers
  // don't need to guard.
  //
  //   ds.phoneLink({ raw: '+15551234567' })
  //     → '<a href="tel:+15551234567">(555) 123-4567</a>'
  api.phoneLink = function (opts) {
    opts = opts || {};
    var raw = opts.raw;
    if (raw === null || raw === undefined || raw === '') return _esc(opts.fallback || '—');
    var digits = api.phoneDigits(raw);
    if (!digits) return _esc(opts.fallback !== undefined ? opts.fallback : raw);
    var display = api.fmtPhone(raw);
    var styleAttr = opts.style ? ' style="' + _attr(opts.style) + '"' : (opts.color ? ' style="color:' + _attr(opts.color) + ';text-decoration:none"' : '');
    var dataAttr = opts.dataAttrs ? ' ' + opts.dataAttrs : '';
    return '<a href="tel:+1' + digits + '" data-ds="phone-link"' + styleAttr + dataAttr + '>' + _esc(display) + '</a>';
  };

  // Imperative toast: mounts to body, auto-dismisses.
  api.toast.show = function (opts) {
    opts = opts || {};
    if (!opts.body || typeof document === 'undefined') return;
    var variant = opts.variant || 'info';
    var dur = opts.duration || (variant === 'danger' ? 8000 : 4000);
    var container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }
    var wrap = document.createElement('div');
    wrap.innerHTML = api.toast(opts);
    var node = wrap.firstElementChild;
    container.appendChild(node);
    setTimeout(function () {
      if (node && node.parentNode) node.parentNode.removeChild(node);
    }, dur);
  };

  return api;
}());
