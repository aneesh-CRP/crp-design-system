interface StudyStat { value: string; label: string; color?: string }

export declare function StudyCard(props: {
  name: string;
  risk?: 'critical'|'high'|'medium'|'low';
  stats: StudyStat[];
  onClick?: () => void;
}): JSX.Element;

export declare function CoordRow(props: {
  name: string;
  count: number;
  max?: number;
  initials: string;
}): JSX.Element;
