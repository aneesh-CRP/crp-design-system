// Panels.jsx - cards, tables, badges
function Card({title, meta, children, actions}) {
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

function Badge({kind = 'gray', children}) {
  return <span className={'badge badge-' + kind}>{children}</span>;
}

function Pill({kind, children}) {
  return <span className={'pill pill-' + kind}>{children}</span>;
}

function RiskTag({level}) {
  return <span className={'risk-tag risk-' + level}>{level}</span>;
}

function Alert({kind = 'info', icon, children}) {
  return (
    <div className={'alert-bar alert-' + kind}>
      {icon && <span>{icon}</span>}
      <span>{children}</span>
    </div>
  );
}

function Panel({title, actions, children, pad = true}) {
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

Object.assign(window, { Card, Badge, Pill, RiskTag, Alert, Panel });
