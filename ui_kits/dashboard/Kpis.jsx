// Kpis.jsx - KPI tiles, hero row, time banner
export function TimeBanner({items}) {
  return (
    <div className="time-banner">
      {items.map((it, i) => (
        <div key={i} className="tb-section">
          <div className="tb-label">{it.label}</div>
          <div className={'tb-value ' + (it.color || '')}>{it.value}</div>
          {it.sub && <div className="tb-sub">{it.sub}</div>}
        </div>
      ))}
    </div>
  );
}

export function HeroRow({items}) {
  return (
    <div className="hero-row">
      {items.map((it, i) => (
        <div key={i} className="hero-cell">
          <div className="hero-label">{it.label}</div>
          <div className="hero-val" style={{color: it.color || 'var(--fg-1)'}}>{it.value}</div>
          <div className="hero-sub">{it.sub}</div>
        </div>
      ))}
    </div>
  );
}

export function KpiTile({label, value, sub, stripe}) {
  return (
    <div className="kpi click">
      {stripe && <div className="kpi-stripe" style={{background: stripe}}/>}
      <div className="label">{label}</div>
      <div className="value">{value}</div>
      {sub && <div className="sub">{sub}</div>}
    </div>
  );
}

export const Kpis = { get TimeBanner(){return TimeBanner}, get HeroRow(){return HeroRow}, get KpiTile(){return KpiTile}, get KpiRow(){return KpiRow} };

export function KpiRow({items}) {
  return (
    <div className="kpi-row">
      {items.map((it, i) => <KpiTile key={i} {...it}/>)}
    </div>
  );
}
