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

