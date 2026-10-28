from pathlib import Path
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"

import sqlite3
import pandas as pd
conn = sqlite3.connect(PROJECT_DIR / "ecommerce.db")
query = """
SELECT
    CustomerID,
    MAX(InvoiceDate) AS last_purchase_date,
    CAST(
        julianday('2011-12-10') - julianday(MAX(InvoiceDate))
        AS INTEGER
    ) AS recency_days,
    COUNT(DISTINCT InvoiceNo) AS frequency,
    ROUND(SUM(Quantity * UnitPrice), 2) AS monetary_value,
    MIN(InvoiceDate) AS first_purchase_date
FROM customer_purchases
GROUP BY CustomerID
ORDER BY monetary_value DESC;
"""

df = pd.read_sql_query(query, conn)
df.to_csv(DATASET_DIR / "customer_rfm.csv", index=False)
conn.close()

print("RFM export completed!")
print("Total customers:", len(df))
print("Saved to dataset/customer_rfm.csv")
print(df.head(5).to_string(index=False))