# Presentation Storyline — PharmEasy Regional Pulse

## Part A: Stakeholder Reframings

### 1. Executive Reframing (Situation–Complication–Resolution)
- **Situation**: Regional operations across Telangana, Andhra Pradesh, and Bengaluru generate steady monthly order volume, reviewed previously via manual spreadsheet exports.
- **Complication**: Traditional reviews missed localized operational anomalies, such as Guntur’s sudden +122.19% order value surge between April and May 2026, risking stockouts and unverified reporting.
- **Resolution**: Deploy the PharmEasy Regional Pulse pipeline, enforcing rigorous SQL validation, automated significance flagging, and human review gates to secure all operational decisions.

### 2. Regional Manager Reframing (Overview–Category–Detail)
- **Overview**: Monthly sales and order counts are tracked via verified database metrics, showing strong stability with targeted high-growth outliers.
- **Category**: Growth in Guntur and surrounding hubs is driven primarily by Prescription Medicines and Wellness & Nutrition categories.
- **Detail**: Granular regional tables and interactive dashboard filters confirm exact order counts, distinct customer transactions, and verified profit margins.

---

## Part B: Anticipated Pushback Q&A

1. **"Why should I believe this number?"**
   - **Acknowledge**: Skepticism regarding order numbers is entirely justified given historical manual spreadsheet discrepancies.
   - **Verified vs. Unverified**: Total sales, distinct order counts, and profit margins are fully verified via SQL queries against `pharmeasy.db` and checked for duplicate keys. External market attribution (e.g., local events) remains unverified.
   - **Resolution**: Re-run validation scripts (`queries.py`) on demand to inspect raw database counts and audit logs by the next operational review cycle.

2. **"What if an alternative explanation is driving this surge?"**
   - **Acknowledge**: It is possible that localized promotional discounting or bulk institutional orders rather than organic consumer demand caused Guntur's +122.19% spike.
   - **Verified vs. Unverified**: Order value and quantity increases are verified; underlying consumer intent and external promotional factors are hypothesized.
   - **Resolution**: Conduct a category-level drill-down in the Streamlit dashboard (`app.py`) and review SKU-level purchasing patterns within 48 hours.