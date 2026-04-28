// DashboardNav.jsx - sticky top nav
function DashboardNav({active = 'Overview', onTab}) {
  const tabs = ['Overview', 'Recruitment', 'Studies', 'Coordinators', 'Finance', 'Retention'];
  return (
    <div className="nav">
      <div className="nav-brand">
        <img src="../../assets/logos/crp-icon.svg" className="nav-logo-img" alt="CRP"/>
        <div>
          <div className="nav-title">CRP Unified Dashboard</div>
          <div className="nav-sub">Operations · Finance · Recruitment</div>
        </div>
      </div>
      <div className="nav-tabs">
        {tabs.map(t => (
          <div key={t}
            className={'nav-tab' + (t === active ? ' active' : '')}
            onClick={() => onTab && onTab(t)}>{t}</div>
        ))}
      </div>
      <div className="nav-right">
        <div className="data-badge">Synced 2 min ago</div>
        <button className="refresh-btn">↻ Refresh</button>
        <button className="connect-btn">Connect data</button>
      </div>
    </div>
  );
}
Object.assign(window, { DashboardNav });
