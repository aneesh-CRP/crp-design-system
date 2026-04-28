// StudyCard.jsx - risk-top study card
function StudyCard({name, risk = 'low', stats, onClick}) {
  return (
    <div className={'study-card risk-' + risk} onClick={onClick}>
      <div className="study-card-name">{name}</div>
      <div className="study-card-stats">
        {stats.map((s, i) => (
          <div key={i} className="sc-stat">
            <div className="sc-num" style={{color: s.color || 'var(--fg-1)'}}>{s.value}</div>
            <div className="sc-lbl">{s.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function CoordRow({name, count, max = 10, initials}) {
  const pct = Math.min(100, (count / max) * 100);
  return (
    <div className="coord-row">
      <div className="coord-avatar">{initials}</div>
      <div className="coord-name">{name}</div>
      <div className="coord-track"><div className="coord-fill" style={{width: pct + '%', background: pct > 80 ? 'var(--danger)' : pct > 60 ? 'var(--warning)' : 'var(--crp-blue)'}}/></div>
      <div className="coord-count">{count}</div>
    </div>
  );
}

Object.assign(window, { StudyCard, CoordRow });
