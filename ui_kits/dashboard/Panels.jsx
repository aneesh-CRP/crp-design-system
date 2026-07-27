// Panels.jsx - cards, tables, badges
export function Card({title, meta, children, actions}) {
  return (
    <div className="card">
      {(title || meta || actions) && (
        <div className="card-header">
          <div>
            {title && <div className="card-title">{title}</div>}
            {meta && <div className="card-meta">{meta}</div>}
          </div>
          {actions}
        </div>
      )}
      {children}
    </div>
  );
}

export function Badge({kind = 'gray', children}) {
  return <span className={'badge badge-' + kind}>{children}</span>;
}

export function Pill({kind, children}) {
  return <span className={'pill pill-' + kind}>{children}</span>;
}

export function RiskTag({level}) {
  return <span className={'risk-tag risk-' + level}>{level}</span>;
}

export function Alert({kind = 'info', icon, children}) {
  return (
    <div className={'alert-bar alert-' + kind}>
      {icon && <span>{icon}</span>}
      <span>{children}</span>
    </div>
  );
}

export const Panels = { get Card(){return Card}, get Badge(){return Badge}, get Pill(){return Pill}, get RiskTag(){return RiskTag}, get Alert(){return Alert}, get Panel(){return Panel} };

export function Panel({title, actions, children, pad = true}) {
  return (
    <div className="panel">
      <div className="panel-head">
        <span>{title}</span>
        {actions}
      </div>
      <div className="panel-body" style={pad ? {padding: '14px 18px'} : null}>{children}</div>
    </div>
  );
}
