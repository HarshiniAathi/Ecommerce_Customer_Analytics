from pathlib import Path
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"

import sqlite3
import pandas as pd
conn = sqlite3.connect(PROJECT_DIR / "ecommerce.db")

query = """
WITH customer_first_purchase AS (
    SELECT
        CustomerID,
        MIN(date(InvoiceDate)) AS first_purchase_date
    FROM customer_purchases
    GROUP BY CustomerID
),
customer_activity AS (
    SELECT DISTINCT
        CustomerID,
        strftime('%Y-%m', InvoiceDate) AS activity_month
    FROM customer_purchases
),
customer_cohorts AS (
    SELECT
        CustomerID,
        strftime('%Y-%m', first_purchase_date) AS cohort_month
    FROM customer_first_purchase
),
cohort_activity AS (
    SELECT
        cc.cohort_month,
        ca.activity_month,
        cc.CustomerID,
        (
            (CAST(substr(ca.activity_month, 1, 4) AS INTEGER)
             - CAST(substr(cc.cohort_month, 1, 4) AS INTEGER)) * 12
            +
            (CAST(substr(ca.activity_month, 6, 2) AS INTEGER)
             - CAST(substr(cc.cohort_month, 6, 2) AS INTEGER))
        ) AS cohort_age
    FROM customer_cohorts cc
    JOIN customer_activity ca
        ON cc.CustomerID = ca.CustomerID
)
SELECT
    cohort_month,
    cohort_age,
    COUNT(DISTINCT CustomerID) AS active_customers
FROM cohort_activity
WHERE cohort_age >= 0
GROUP BY cohort_month, cohort_age
ORDER BY cohort_month, cohort_age;
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Calculate each cohort's original customer count
cohort_sizes = (
    df[df["cohort_age"] == 0][["cohort_month", "active_customers"]]
    .rename(columns={"active_customers": "cohort_size"})
)
df = df.merge(cohort_sizes, on="cohort_month", how="left")

# Calculate retention percentage
df["retention_rate"] = (
    df["active_customers"] / df["cohort_size"] * 100
).round(2)

df.to_csv(DATASET_DIR / "cohort_retention.csv", index=False)
print("Cohort analysis completed!")
print("Cohort records:", len(df))
print("\nSample results:")
print(df.head(10).to_string(index=False))
print("\nSaved to dataset/cohort_retention.csv")
