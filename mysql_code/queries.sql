CREATE DATABASE bank_analytics;
use bank_analytics;
show tables;

-- Total spend and avg transaction per customer
SELECT
    AccountID,
    COUNT(*) AS total_transactions,
    ROUND(SUM(TransactionAmount), 2) AS total_spend,
    ROUND(AVG(TransactionAmount), 2) AS avg_transaction,
    MAX(TransactionAmount) AS max_transaction
FROM transactions
GROUP BY AccountID
ORDER BY total_spend DESC
LIMIT 20;

-- Analyze transaction volume and spending by transaction type
-- Which transaction types generate the most transactions and highest total transaction amounts?
SELECT
    TransactionType,
    COUNT(*) AS transaction_count,
    ROUND(SUM(TransactionAmount), 2) AS total_amount,
    ROUND(AVG(TransactionAmount), 2) AS avg_amount
FROM transactions
GROUP BY TransactionType
ORDER BY total_amount DESC;

-- Month-wise transaction volume and value
SELECT
    MONTHNAME(TransactionDate) AS month,
    COUNT(*) AS total_transactions,
    ROUND(SUM(TransactionAmount), 2) AS monthly_volume
FROM transactions
GROUP BY MONTH(TransactionDate), MONTHNAME(TransactionDate)
ORDER BY MONTH(TransactionDate);