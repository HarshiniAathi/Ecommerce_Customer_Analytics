from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"

import pandas as pd
df = pd.read_csv(DATASET_DIR / "OnlineRetail.csv", encoding="ISO-8859-1")

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATASET INFORMATION ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Display basic statistics
print("\n--- BASIC STATISTICS ---")
print(df.describe(include="all"))

# Check duplicate records
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

# Check negative or zero quantities
print("\n--- QUANTITY CHECK ---")
print("Zero quantities:", (df["Quantity"] == 0).sum())
print("Negative quantities:", (df["Quantity"] < 0).sum())

# Check zero or negative prices
print("\n--- PRICE CHECK ---")
print("Zero prices:", (df["UnitPrice"] == 0).sum())
print("Negative prices:", (df["UnitPrice"] < 0).sum())

# Check cancelled invoices
print("\n--- CANCELLED INVOICES ---")
print(df["InvoiceNo"].str.startswith("C", na=False).sum())

# Convert invoice dates into datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("\n--- DATE RANGE ---")
print("Earliest:", df["InvoiceDate"].min())
print("Latest:", df["InvoiceDate"].max())

