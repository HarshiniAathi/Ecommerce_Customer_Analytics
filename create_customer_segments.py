from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_DIR / "dataset"

import pandas as pd
df = pd.read_csv(DATASET_DIR / "customer_rfm.csv")

# Assign customer segments
def assign_segment(row):
    recency = row["recency_days"]
    frequency = row["frequency"]
    monetary = row["monetary_value"]

    if recency <= 30 and frequency >= 4 and monetary >= 500:
        return "Champion"
    elif frequency >= 4:
        return "Loyal Customer"
    elif recency <= 30 and frequency <= 2:
        return "Recent Customer"
    elif 31 <= recency <= 90:
        return "At Risk"
    else:
        return "Dormant Customer"

df["Customer_Segment"] = df.apply(assign_segment, axis=1)

# Calculate transparent Customer Health Score (0–100)
def calculate_health(row):
    score = 0

    # Recency: maximum 40 points
    if row["recency_days"] <= 30:
        score += 40
    elif row["recency_days"] <= 60:
        score += 30
    elif row["recency_days"] <= 90:
        score += 20
    elif row["recency_days"] <= 180:
        score += 10

    # Purchase frequency: maximum 30 points
    if row["frequency"] >= 10:
        score += 30
    elif row["frequency"] >= 5:
        score += 25
    elif row["frequency"] >= 3:
        score += 20
    elif row["frequency"] >= 2:
        score += 10

    # Monetary value: maximum 30 points
    if row["monetary_value"] >= 5000:
        score += 30
    elif row["monetary_value"] >= 2000:
        score += 25
    elif row["monetary_value"] >= 1000:
        score += 20
    elif row["monetary_value"] >= 500:
        score += 15
    elif row["monetary_value"] > 0:
        score += 10

    return score
df["Customer_Health_Score"] = df.apply(calculate_health, axis=1)

# Recommend an action for each customer
def recommend_action(row):
    segment = row["Customer_Segment"]

    if segment == "Champion":
        return "Reward loyalty and offer VIP benefits"
    elif segment == "Loyal Customer":
        return "Encourage repeat purchases and referrals"
    elif segment == "Recent Customer":
        return "Send a welcome offer to encourage a second purchase"
    elif segment == "At Risk":
        return "Send a personalized re-engagement offer"
    else:
        return "Launch a win-back campaign"
df["Recommended_Action"] = df.apply(recommend_action, axis=1)

# Export enriched customer data
df.to_csv(DATASET_DIR / "customer_segments.csv", index=False)
print("Customer segmentation completed!")
print("Total customers:", len(df))
print("\nCustomer segment counts:")
print(df["Customer_Segment"].value_counts().to_string())
print("\nSample customer records:")
print(
    df[
        [
            "CustomerID",
            "Customer_Segment",
            "Customer_Health_Score",
            "Recommended_Action",
        ]
    ].head(5).to_string(index=False)
)
print("\nSaved to dataset/customer_segments.csv")
