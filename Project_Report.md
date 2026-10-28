# E-commerce Customer Behaviour & Retention Analytics

## 1. Project Overview

This project analyzes e-commerce transaction data to understand sales performance, customer purchasing behaviour, customer segments, and retention patterns.

The objective is to transform raw transaction data into meaningful business insights and create an interactive Power BI dashboard that supports customer retention and business decision-making.

## 2. Business Objectives

* Analyze overall sales performance and transaction trends.
* Identify customer purchasing patterns.
* Segment customers based on purchasing behaviour.
* Examine customer retention across acquisition cohorts.
* Identify at-risk and dormant customers.
* Suggest appropriate customer engagement and retention actions.
* Explore hypothetical customer retention scenarios.

## 3. Dataset

**Dataset:** UCI Online Retail dataset

The dataset contains transaction records from an online retail business.

Important columns include:

* `InvoiceNo` — Invoice identifier.
* `StockCode` — Product identifier.
* `Description` — Product description.
* `Quantity` — Number of items in a transaction.
* `InvoiceDate` — Transaction date and time.
* `UnitPrice` — Price per item.
* `CustomerID` — Customer identifier.
* `Country` — Customer's country.

The dataset contains transactions from December 2010 through December 2011. The available December 2011 data ends on December 9, making that month incomplete.

## 4. Tools and Technologies

* **Python:** Data inspection, cleaning, customer segmentation, and cohort analysis.
* **Pandas:** Data manipulation and transformation.
* **SQLite:** Storing transaction data and executing SQL queries.
* **SQL:** Sales analysis and customer-level analysis.
* **Power BI:** Interactive dashboards and visual analytics.
* **CSV:** Data exchange between the analysis stages.

## 5. Data Preparation

The original dataset contained 541,909 rows and eight columns.

The preparation process included:

1. Inspecting the dataset structure and data types.
2. Identifying and removing duplicate records.
3. Preparing transaction-level sales data.
4. Preparing customer-level data for RFM analysis.
5. Excluding cancellation invoices and non-positive prices from the cleaned sales dataset.
6. Preparing separate datasets for customer segmentation and cohort retention.
7. Exporting the processed datasets for use in SQL and Power BI.

After removing duplicate records, 536,641 rows remained.

The cleaned sales dataset contained 524,878 rows. The customer analysis dataset contained 392,692 rows with known customer IDs and positive quantities and prices.

**Revenue calculation note:** The current sales dataset still contains negative-quantity return transactions. Therefore, the revenue figures should be treated as preliminary transaction revenue that includes returns, rather than finalized sales revenue excluding returns.

## 6. SQL Analysis

The transaction data was stored in an SQLite database named `ecommerce.db`.

SQL was used to examine business performance, including:

* Total transaction revenue.
* Distinct invoice count.
* Distinct customer count.
* Total recorded quantity.
* Monthly revenue trends.

### Preliminary Results

| Metric                                   |        Result |
| ---------------------------------------- | ------------: |
| Transaction revenue                      | 10,642,110.80 |
| Distinct invoices                        |        19,960 |
| Distinct customers                       |         4,338 |
| Net recorded quantity, including returns |     5,572,420 |

These figures reflect the current analysis and cleaning rules. Revenue and quantity include negative-quantity return transactions.

### Monthly Trend

The monthly analysis showed that November 2011 had the highest recorded revenue, approximately 1,503,866.78. February 2011 had the lowest recorded revenue, approximately 522,545.56.

December 2011 is incomplete in the dataset, so it should not be compared directly with full months without accounting for the difference in coverage.

## 7. RFM Analysis

RFM stands for:

* **Recency:** How recently a customer made a purchase.
* **Frequency:** How often a customer purchased.
* **Monetary Value:** The monetary value of a customer's purchases.

The RFM analysis was generated for 4,338 customers.

Recency was calculated relative to December 10, 2011. Frequency and monetary value were calculated from the prepared customer purchase data.

RFM metrics provide a structured way to compare customer purchasing behaviour and support customer segmentation.

## 8. Customer Segmentation

Customers were grouped into five segments using transparent, rule-based logic.

| Customer Segment | Number of Customers |
| ---------------- | ------------------: |
| Dormant Customer |               1,500 |
| Champion         |                 979 |
| At Risk          |                 854 |
| Loyal Customer   |                 523 |
| Recent Customer  |                 482 |
| **Total**        |           **4,338** |

The At Risk and Dormant Customer segments together contain 2,354 customers, approximately 54.3% of the analyzed customer base.

This result highlights a potential area for customer re-engagement efforts.

The segmentation, customer health score, and recommended actions are based on defined business rules. They are not outputs from a trained or validated churn prediction model.

## 9. Cohort Retention Analysis

Cohort analysis groups customers according to their first recorded purchase month and examines their subsequent purchasing activity.

The project generated a cohort retention dataset containing 91 cohort-age records.

The analysis includes:

* Cohort month.
* Cohort age.
* Active customers.
* Original cohort size.
* Retention rate.

For example, the December 2010 cohort contained 885 customers, and its recorded retention rate at cohort age 1 was approximately 36.61%.

Cohort retention helps reveal how customer activity changes over time after the first recorded purchase.

## 10. Power BI Dashboard

The Power BI report contains five pages.

### Page 1: Executive Overview

Displays key business metrics and the monthly revenue trend.

### Page 2: Customer Segmentation

Compares customer segment sizes and supports exploration of customer health and segment-level patterns.

### Page 3: Customer Cohort Retention

Displays cohort retention rates by cohort month and cohort age.

### Page 4: Customer 360° & Retention Action Center

Provides customer-level information, including customer segment, health score, frequency, monetary value, recency, and recommended action.

A customer ID slicer supports customer-level exploration.

### Page 5: Retention Scenario Analysis

Explores hypothetical retention uplift scenarios of 5%, 10%, and 15% using the 854 customers classified as At Risk.

The estimated number of potentially retained customers is calculated by applying each scenario percentage to the At Risk segment.

These values are scenario calculations, not forecasts or validated predictions.

## 11. Business Recommendations

Based on the current analysis:

1. Investigate the At Risk and Dormant Customer segments to understand their purchasing patterns.
2. Consider targeted re-engagement campaigns for customers who have not purchased recently.
3. Develop appropriate loyalty initiatives for Champions and Loyal Customers.
4. Monitor cohort retention to identify changes in repeat purchasing behaviour.
5. Track the effectiveness of retention campaigns before concluding that they improve retention.
6. Recalculate sales KPIs using an explicitly defined returns policy before presenting them as finalized business results.

## 12. Limitations

* The dataset covers a historical period from 2010 to 2011.
* December 2011 contains only partial-month data.
* The current revenue calculation includes negative-quantity return transactions.
* Customer segmentation and health scores use rule-based logic.
* Retention scenarios are hypothetical and do not establish actual campaign effectiveness.
* The analysis does not include a trained, validated churn prediction model.

## 13. Conclusion

This project demonstrates an end-to-end data analysis workflow, from raw transaction inspection and cleaning to SQL analysis, RFM metrics, customer segmentation, cohort retention analysis, and Power BI visualization.

The resulting dashboard provides a structured view of sales performance and customer behaviour and identifies areas for further investigation and customer retention efforts.
