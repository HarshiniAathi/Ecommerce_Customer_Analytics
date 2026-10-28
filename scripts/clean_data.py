from pathlib import Path
import pandas as pd
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"

df = pd.read_csv(
    DATASET_DIR / "OnlineRetail.csv",
    encoding="ISO-8859-1"
)

# Convert data types
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype("Int64")

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Identify cancelled invoices
df["IsCancelled"] = df["InvoiceNo"].str.startswith(
    "C", na=False
)

# Calculate transaction amount
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Save the full cleaned dataset for further investigation
df.to_csv(
    DATASET_DIR / "cleaned_all_transactions.csv",
    index=False
)

# Keep non-cancelled records for sales analysis
sales = df[~df["IsCancelled"]].copy()

# Positive-price records for our main revenue analysis
sales_positive = sales[sales["UnitPrice"] > 0].copy()

sales_positive.to_csv(
    DATASET_DIR / "cleaned_sales.csv",
    index=False
)

# Customer-level purchase analysis
# Require a known customer, positive quantity and positive price
customers = sales_positive[
    sales_positive["CustomerID"].notna()
    & (sales_positive["Quantity"] > 0)
].copy()

customers.to_csv(
    DATASET_DIR / "cleaned_customers.csv",
    index=False
)

# Display summary
print("CLEANING COMPLETED")

print("\nOriginal rows:", 541909)
print("Rows after removing exact duplicates:", len(df))
print("Eligible sales rows:", len(sales_positive))
print("Eligible customer-analysis rows:", len(customers))

print("\nFiles created:")
print("1. cleaned_all_transactions.csv")
print("2. cleaned_sales.csv")
print("3. cleaned_customers.csv")

