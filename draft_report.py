"""draft_report.py -- Generates Context-Insight-Implication blocks for flagged regions."""
def draft_report_v1(flagged_regions, metrics_data):
    reports = []
    for region in flagged_regions:
        m_data = metrics_data.get(region, {})
        sales_curr = m_data.get("current_sales", 0)
        sales_prev = m_data.get("previous_sales", 0)
        pct_change = m_data.get("pct_change", 0.0)
        
        context = f"Region: {region} recorded prior sales of INR {sales_prev:,.2f} and current sales of INR {sales_curr:,.2f}."
        insight = f"{region} experienced a Month-on-Month sales movement of {pct_change:+.2f}%, crossing the 8% significance threshold."
        implication = f"Operations desk must review localized category demand drivers in {region} to determine whether this shift requires resource reallocation or inventory adjustment."
        
        reports.append({
            "region": region,
            "context": context,
            "insight": insight,
            "implication": implication
        })
    return reports