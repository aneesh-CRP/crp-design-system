import type { ReactNode } from 'react';

interface ProgressBarProps {
  /** Current step (1-based) */
  step: number;
  /** Total steps */
  total: number;
}

interface RadioCardProps {
  selected?: boolean;
  onSelect?: () => void;
  children?: ReactNode;
}

interface ConsentItem { label: string; checked?: boolean }

interface ConsentBlockProps {
  items: ConsentItem[];
  onToggle?: (index: number) => void;
}

export declare function ProgressBar(props: ProgressBarProps): JSX.Element;
export declare function RadioCard(props: RadioCardProps): JSX.Element;
export declare function ConsentBlock(props: ConsentBlockProps): JSX.Element;
