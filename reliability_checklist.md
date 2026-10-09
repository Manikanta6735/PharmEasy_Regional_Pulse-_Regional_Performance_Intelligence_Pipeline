# Reliability Checklist — PharmEasy Regional Pulse

1. **Safety Check**: No personally identifiable customer data appears in the memo or narrative—only region-level aggregates and order counts [HIGH].
2. **Validation**: All financial metrics, sales figures, and growth percentages have been verified directly against SQL queries executed on `pharmeasy.db` [HIGH].
3. **Critique / Refine**: Hypotheses regarding external market drivers are clearly separated from verified database facts and placed in the Assumptions field [MEDIUM].
4. **Human Sign-Off**: The report and recommendation memo have successfully passed the review gate with explicit approval logged in `audit_log.jsonl` [LOW].