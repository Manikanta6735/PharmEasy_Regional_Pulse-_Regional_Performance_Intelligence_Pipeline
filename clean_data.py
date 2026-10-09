"""clean_data.py -- Cleaning pipeline and schema validation for PharmEasy Regional Pulse."""
import pandas as pd

def validate_schema(df, required_columns):
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        return {
            "status": "blocked_schema",
            "row_count": len(df),
            "missing_columns": missing_cols
        }
    return {
        "status": "validated",
        "row_count": len(df),
        "missing_columns": []
    }

def clean_raw_data(raw_csv_path="pharmeasy_orders_raw.csv", output_csv_path="orders_clean.csv"):
    df = pd.read_csv(raw_csv_path, dtype=str)
    
    # 1. Remove exact duplicates
    initial_count = len(df)
    df = df.drop_duplicates()
    dupes_removed = initial_count - len(df)
    print(f"Removed {dupes_removed} exact duplicate rows.")
    
    # 2. Normalize region column
    df["region"] = df["region"].str.strip().str.title()
    
    # Convert numerical columns
    df["quantity"] = pd.to_numeric(df["quantity"])
    df["sales_inr"] = pd.to_numeric(df["sales_inr"])
    df["profit_inr"] = pd.to_numeric(df["profit_inr"], errors="coerce")
    
    # 3. Impute missing category using product -> category mapping
    valid_cat_df = df[df["category"].notna() & (df["category"] != "")]
    prod_to_cat = valid_cat_df.set_index("product")["category"].to_dict()
    
    missing_cat_mask = df["category"].isna() | (df["category"] == "")
    df.loc[missing_cat_mask, "category"] = df.loc[missing_cat_mask, "product"].map(prod_to_cat)
    
    # 4. Impute missing profit_inr using category mean margin
    valid_prof_df = df[df["profit_inr"].notna() & (df["sales_inr"] > 0)]
    valid_prof_df = valid_prof_df.copy()
    valid_prof_df["margin"] = valid_prof_df["profit_inr"] / valid_prof_df["sales_inr"]
    cat_margins = valid_prof_df.groupby("category")["margin"].mean().to_dict()
    
    missing_prof_mask = df["profit_inr"].isna()
    for cat, margin in cat_margins.items():
        mask = missing_prof_mask & (df["category"] == cat)
        df.loc[mask, "profit_inr"] = round(df.loc[mask, "sales_inr"] * margin, 2)
    
    required_cols = ["order_id", "order_date", "region", "category", "product", "quantity", "sales_inr", "profit_inr"]
    val_result = validate_schema(df, required_cols)
    print(f"Schema validation status: {val_result['status']} (Row count: {val_result['row_count']})")
    
    df.to_csv(output_csv_path, index=False)
    print(f"Saved clean dataset to {output_csv_path} with {len(df)} rows.")
    return df

if __name__ == "__main__":
    clean_raw_data()