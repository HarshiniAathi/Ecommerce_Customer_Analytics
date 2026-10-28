SELECT
    ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_invoices,
    COUNT(DISTINCT CustomerID) AS total_customers,
    SUM(Quantity) AS total_units_sold
FROM sales;

SELECT
    strftime('%Y-%m', InvoiceDate) AS sales_month,
    ROUND(SUM(Quantity * UnitPrice), 2) AS monthly_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_invoices,
    COUNT(DISTINCT CustomerID) AS total_customers
FROM sales
GROUP BY strftime('%Y-%m', InvoiceDate)
ORDER BY sales_month;