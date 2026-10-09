# Data Quality Report — PharmEasy Regional Pulse

This report maps the data-cleaning interventions implemented in `clean_data.py` to the seven standard dimensions of data quality.

## Data Quality Dimensions & Applied Fixes

1. **Uniqueness**
   - *Issue*: Copy-paste errors and multi-source synchronization created 59 exact duplicate rows in the raw dataset.
   - *Fix*: Removed exact duplicate rows using `.drop_duplicates()`, ensuring each order is uniquely represented.

2. **Consistency**
   - *Issue*: Regional teams entered store locations with varying casing and whitespace (e.g., `" hyderabad"`, `"HYDERABAD "`, `"Bengaluru "`), creating 16 distinct raw variants.
   - *Fix*: Applied `.str.strip().str.title()` string normalization to collapse all variants onto the 9 canonical region names defined in `regions_master.csv`.

3. **Completeness**
   - *Issue*: Nightly database sync failures resulted in 48 missing category fields and 94 missing profit figures (`profit_inr`).
   - *Fix*: Imputed missing categories deterministically using a product-to-category lookup mapping derived from complete records. Imputed missing profits using the mean profit margin per category applied to the respective sales figures.

4. **Accuracy**
   - *Issue*: Raw profit margins contained transmission noise and missing entries.
   - *Fix*: Calculated robust category-specific mean profit margins ($\text{profit} / \text{sales}$) and re-estimated missing values to preserve financial fidelity without distorting regional margins.

5. **Validity**
   - *Issue*: Inconsistent formatting across source channels.
   - *Fix*: Enforced strict datatype parsing for numerical fields (`quantity`, `sales_inr`, `profit_inr`) and validated schema headers.

6. **Timeliness**
   - *Issue*: Asynchronous reporting batches across regions.
   - *Fix*: Standardized all transaction dates to ISO format (`YYYY-MM-DD`) spanning April, May, and June 2026 (`MONTHS` definition).

7. **Relevance**
   - *Issue*: Inclusion of unstructured or metadata noise.
   - *Fix*: Maintained focus strictly on the 8 columns required for regional operations and financial oversight.