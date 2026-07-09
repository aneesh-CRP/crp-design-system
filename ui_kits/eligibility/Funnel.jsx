// Funnel.jsx — eligibility funnel primitives (compiled design-system components)
import React from 'react';

export const Funnel = { get ProgressBar(){return ProgressBar}, get RadioCard(){return RadioCard}, get ConsentBlock(){return ConsentBlock} };

export function ProgressBar({ step, total }) {
  return (
    <div style={{display:'flex',alignItems:'center',gap:8,fontFamily:'inherit'}}>
      <div style={{flex:1,height:4,background:'#f1f5f9',borderRadius:999,overflow:'hidden'}}>
        <div style={{width:`${(step/total)*100}%`,height:'100%',background:'#FF9933',borderRadius:999,transition:'width 250ms cubic-bezier(.2,.8,.2,1)'}}/>
      </div>
      <span style={{fontFamily:"'IBM Plex Mono',monospace",fontSize:10,color:'#3d5373',textTransform:'uppercase',letterSpacing:'.08em'}}>{step} of {total}</span>
    </div>
  );
}

export function RadioCard({ selected, onSelect, children }) {
  return (
    <label onClick={onSelect} style={{
      display:'flex',alignItems:'center',gap:12,padding:'12px 14px',
      border:`1.5px solid ${selected?'#1843AD':'#c8d6e8'}`,
      borderRadius:8,background:selected?'#E8EEFF':'#fff',cursor:'pointer',
      fontSize:14,color:selected?'#072061':'#072061',fontWeight:selected?600:400,
      transition:'all 150ms cubic-bezier(.2,.8,.2,1)'}}>
      <span style={{width:20,height:20,borderRadius:999,flexShrink:0,
        border:`1.5px solid ${selected?'#1843AD':'#b0c4d8'}`,
        display:'inline-flex',alignItems:'center',justifyContent:'center'}}>
        {selected ? <span style={{width:10,height:10,borderRadius:999,background:'#1843AD'}}/> : null}
      </span>
      <span>{children}</span>
    </label>
  );
}

export function ConsentBlock({ items, onToggle }) {
  return (
    <div style={{display:'flex',flexDirection:'column',gap:10}}>
      {items.map((it, i) => (
        <label key={i} onClick={() => onToggle && onToggle(i)} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:13,color:'#072061',lineHeight:1.5,cursor:'pointer'}}>
          <span style={{width:20,height:20,borderRadius:4,flexShrink:0,marginTop:1,
            border:`1.5px solid ${it.checked?'#1843AD':'#b0c4d8'}`,
            background:it.checked?'#1843AD':'#fff',
            display:'inline-flex',alignItems:'center',justifyContent:'center',color:'#fff',fontSize:12,fontWeight:800}}>
            {it.checked ? '✓' : ''}
          </span>
          <span>{it.label}</span>
        </label>
      ))}
    </div>
  );
}
