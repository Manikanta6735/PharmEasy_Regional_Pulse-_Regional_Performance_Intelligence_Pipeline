"""queries.py -- Executes JOIN validations, duplicate checks, and metrics SQL."""
import sqlite3
import pandas as pd

def run_queries():
    conn = sqlite3.connect("pharmeasy.db")
    
    print("=== 1. JOIN Row-Count Check ===")
    left_count = pd.read_sql("SELECT COUNT(*) as cnt FROM regions_master r LEFT JOIN orders_clean o ON r.region = o.region", conn).iloc[0]["cnt"]
    inner_count = pd.read_sql("SELECT COUNT(*) as cnt FROM regions_master r INNER JOIN orders_clean o ON r.region = o.region", conn).iloc[0]["cnt"]
    print(f"LEFT JOIN count: {left_count} | INNER JOIN count: {inner_count} | Delta: {left_count - inner_count}")
    
    print("\n=== 2. Duplicate-Key Check ===")
    dupes = pd.read_sql("SELECT order_id, COUNT(*) FROM orders_clean GROUP BY order_id HAVING COUNT(*) > 1", conn)
    print(f"Duplicate order_ids found: {len(dupes)}")
    
    print("\n=== 3. Null Check (COUNT(*) vs COUNT(order_id) for Kurnool) ===")
    null_check_sql = """
        SELECT r.region, COUNT(*) as count_star, COUNT(o.order_id) as count_fk 
        FROM regions_master r 
        LEFT JOIN orders_clean o ON r.region = o.region 
        WHERE r.region = 'Kurnool'
        GROUP BY r.region;
    """
    print(pd.read_sql(null_check_sql, conn))
    
    print("\n=== 4. Per-Region Order Counts via LEFT JOIN ===")
    region_counts_sql = """
        SELECT r.region, COUNT(o.order_id) as order_count
        FROM regions_master r
        LEFT JOIN orders_clean o ON r.region = o.region
        GROUP BY r.region
        ORDER BY order_count ASC;
    """
    print(pd.read_sql(region_counts_sql, conn))
    
    print("\n=== 5. Region x Month Sales & MoM Growth ===")
    monthly_sales_sql = """
        SELECT region, SUBSTR(order_date, 1, 7) as month, SUM(sales_inr) as total_sales
        FROM orders_clean
        GROUP BY region, month
        ORDER BY region, month;
    """
    df_sales = pd.read_sql(monthly_sales_sql, conn)
    print(df_sales.head(12))
    
    conn.close()

if __name__ == "__main__":
    run_queries()