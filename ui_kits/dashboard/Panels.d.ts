import type { ReactNode } from 'react';

interface CardProps { title?: string; meta?: string; actions?: ReactNode; children?: ReactNode }
interface BadgeProps { kind?: 'red'|'green'|'yellow'|'blue'|'gray'; children?: ReactNode }
interface PillProps { kind: 'new'|'contacted'|'escalated'|'disputed'|'resolved'; children?: ReactNode }
interface RiskTagProps { level: 'critical'|'high'|'medium'|'low' }
interface AlertProps { kind?: 'info'|'warn'|'crit'|'success'; icon?: ReactNode; children?: ReactNode }
interface PanelProps { title: string; actions?: ReactNode; pad?: boolean; children?: ReactNode }

export declare function Card(props: CardProps): JSX.Element;
export declare function Badge(props: BadgeProps): JSX.Element;
export declare function Pill(props: PillProps): JSX.Element;
export declare function RiskTag(props: RiskTagProps): JSX.Element;
export declare function Alert(props: AlertProps): JSX.Element;
export declare function Panel(props: PanelProps): JSX.Element;
export declare const Panels: { Card: typeof Card; Badge: typeof Badge; Pill: typeof Pill; RiskTag: typeof RiskTag; Alert: typeof Alert; Panel: typeof Panel };
