interface BannerItem { label: string; value: string; sub?: string; color?: string }
interface HeroItem { label: string; value: string; sub?: string; color?: string }
interface KpiItem { label: string; value: string; sub?: string; stripe?: string }

export declare function TimeBanner(props: { items: BannerItem[] }): JSX.Element;
export declare function HeroRow(props: { items: HeroItem[] }): JSX.Element;
export declare function KpiTile(props: KpiItem): JSX.Element;
export declare function KpiRow(props: { items: KpiItem[] }): JSX.Element;
export declare const Kpis: { TimeBanner: typeof TimeBanner; HeroRow: typeof HeroRow; KpiTile: typeof KpiTile; KpiRow: typeof KpiRow };
