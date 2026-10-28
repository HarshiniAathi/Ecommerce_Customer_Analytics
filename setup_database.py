from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"
import pandas as pd
import sqlite3

# Load the cleaned datasets
sales = pd.read_csv(
    DATASET_DIR / "cleaned_sales.csv",
    encoding="ISO-8859-1",
    dtype={"InvoiceNo": str},
    low_memory=False
)
customers = pd.read_csv(
    DATASET_DIR / "cleaned_customers.csv",
    encoding="ISO-8859-1",
    dtype={"InvoiceNo": str},
    low_memory=False
)

# Create a SQLite database
conn = sqlite3.connect(PROJECT_DIR / "ecommerce.db")

# Import sales data
sales.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

# Import customer-level purchase data
customers.to_sql(
    "customer_purchases",
    conn,
    if_exists="replace",
    index=False
)
print("Database created successfully!")
print("Tables created: sales, customer_purchases")

# Verify the tables
cursor = conn.cursor()
cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
)
print("\nAvailable tables:")
print(cursor.fetchall())
conn.close()
