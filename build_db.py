"""build_db.py -- Builds local SQLite database pharmeasy.db from CSVs."""
import sqlite3
import pandas as pd

def build_database():
    conn = sqlite3.connect("pharmeasy.db")
    cursor = conn.cursor()
    
    # Load masters and clean orders
    regions_df = pd.read_csv("regions_master.csv")
    orders_df = pd.read_csv("orders_clean.csv")
    
    regions_df.to_sql("regions_master", conn, if_exists="replace", index=False)
    orders_df.to_sql("orders_clean", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    print("Successfully built pharmeasy.db with 'regions_master' and 'orders_clean' tables.")

if __name__ == "__main__":
    build_database()