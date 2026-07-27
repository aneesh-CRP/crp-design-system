interface DashboardNavProps {
  /** Active tab label */
  active?: string;
  /** Called with the tab label on click */
  onTab?: (tab: string) => void;
}

export declare function DashboardNav(props: DashboardNavProps): JSX.Element;
