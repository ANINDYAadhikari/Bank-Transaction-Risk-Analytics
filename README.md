<!-- PROJECT SHIELDS -->
<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-cc0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 🏦 Bank-Transaction-Risk-Analytics — Transaction Intelligence & Risk Analytics

> **An end-to-end banking analytics platform that transforms raw transaction records into executive-ready business intelligence — spanning Python data engineering, MySQL querying, and a four-page Power BI dashboard with built-in risk detection.**

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Tools & Technologies](#️-tools--technologies)
- [Dataset](#-dataset)
- [Project Workflow](#-project-workflow--architecture)
- [Python Analysis](#-python-analysis)
- [MySQL Analysis](#️-mysql-analysis--key-queries)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Business Insights](#-key-business-insights)
- [Project Structure](#-project-structure)
- [Local Setup & How to Explore](#-local-setup--how-to-explore)
- [Screenshots & Visuals Preview](#-screenshots--visuals-preview)
- [Dataset Credits](#-dataset--credits)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Overview

Bank-Transaction-Risk-Analytics is a portfolio-grade, end-to-end analytics project built on a real-world bank transaction dataset spanning 2,512 records across 43 US cities from January 2023 to January 2024. The project addresses a core challenge that banking and fintech teams face daily: turning high-volume, multi-dimensional transaction logs into actionable insight — from spotting high-risk customers to understanding seasonal spending shifts.

The pipeline moves through three distinct layers. Python handles all data wrangling and feature engineering, including the construction of a composite risk scoring model that flags suspicious transactions by combining late-night activity, abnormal login attempts, and outlier processing times. MySQL takes the cleaned dataset and answers seven business questions through structured SQL queries, covering customer spend ranking, channel behavior, monthly trends, and geographic risk mapping. Power BI then pulls it all together in an interactive four-page dashboard that lets stakeholders slice the data by month, channel, location, day of week, and transaction type.

This is not a one-tool notebook project — it reflects the kind of cross-functional workflow a junior analyst would operate in inside a bank, insurance company, or payments platform.

---

## 🛠️ Tools & Technologies

| Tool | Version / Platform | Role in Project |
|---|---|---|
| **Python** | 3.14 (VSCode) | Data cleaning, feature engineering, MySQL ingestion pipeline |
| **Pandas** | 2.x | DataFrame operations, datetime parsing, CSV I/O |
| **NumPy** | 1.x | IQR outlier computation, flag type casting |
| **Seaborn** | Latest | Imported in pipeline (available for visual EDA) |
| **SQLAlchemy** | Latest | ORM engine creation and chunked `df.to_sql()` loading |
| **MySQL Workbench** | 8.x | Database hosting, schema management, query execution |
| **Power BI Desktop** | Latest | Four-page interactive dashboard, DAX measures, map visual |
| **VSCode** | Latest | Primary IDE for Python and SQL authoring |

> 📌 **Note on SQL visuals:** All SQL queries were written and executed via a MySQL connection directly inside VSCode. The output screenshots captured in `visuals/SQL_Queries/` are VSCode query views, not MySQL Workbench screenshots — this was intentional for readability.

---

## 📊 Dataset

**Name:** `bank_transactions_data.csv`  
**Source:** Kaggle — *Bank Transaction Dataset for Fraud Detection*  
**Link:** [https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)  
**Size:** 2,512 rows × 16 columns  
**Date Range:** January 2, 2023 – January 1, 2024  

### Column Descriptions

| Column | Type | Description |
|---|---|---|
| `TransactionID` | String | Unique identifier for each transaction (TX000001–TX002512) |
| `AccountID` | String | Customer account identifier (495 unique accounts) |
| `TransactionAmount` | Float | Transaction value in USD ($0.26 – $1,919.11, mean $297.59) |
| `TransactionDate` | Datetime | Full timestamp of the transaction |
| `TransactionType` | String | Debit (1,944 records) or Credit (568 records) |
| `Location` | String | US city where the transaction occurred (43 unique cities) |
| `DeviceID` | String | Device identifier used for the transaction |
| `IP Address` | String | IP address associated with the session |
| `MerchantID` | String | Merchant associated with the transaction |
| `Channel` | String | Transaction channel: Branch (868), ATM (833), Online (811) |
| `CustomerAge` | Integer | Customer age in years (18–80, mean 44.7) |
| `CustomerOccupation` | String | Doctor, Student, Engineer, or Retired |
| `TransactionDuration` | Integer | Processing duration in seconds |
| `LoginAttempts` | Integer | Login attempts before the transaction (1–5, mean 1.12) |
| `AccountBalance` | Float | Account balance at the time of transaction ($101 – $14,978) |
| `PreviousTransactionDate` | Datetime | Timestamp of the customer's prior transaction |

### Data Quality

The raw dataset arrived in clean condition — zero duplicate rows and zero null values across all 16 columns. The primary cleaning tasks were datetime type conversion (both date columns were stored as plain strings), temporal feature extraction, IQR-based outlier profiling, and the creation of several engineered risk columns. No rows were dropped during cleaning.

---

## 🔄 Project Workflow / Architecture

```
Raw CSV (2,512 × 16)
       │
       ▼
┌─────────────────────────────────────┐
│   Python — cleaning.py              │
│   • Datetime conversion             │
│   • Outlier detection (IQR)         │
│   • Feature engineering             │
│     (SpendingTier, RiskScore,       │
│      SuspiciousTransaction, etc.)   │
│   • Export → cleaned_transactions   │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│   Python — Pipeline.py              │
│   • SQLAlchemy engine               │
│   • df.to_sql() → bank_analytics   │
│     (table: transactions)           │
│   • Chunked load (1,000 rows/batch) │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│   MySQL — queries.sql               │
│   • Customer spend ranking          │
│   • Transaction type breakdown      │
│   • Monthly volume trends           │
│   • Geographic risk mapping         │
│   • High-value customer profiling   │
│   • Spending tier segmentation      │
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────────┐
│   Power BI — bank_analytics.pbix    │
│   • Executive Overview              │
│   • Customer Behavior               │
│   • Anomaly & Risk View             │
│   • Transaction Patterns            │
└─────────────────────────────────────┘
```

**Stage 1 — Python (cleaning.py):** The raw CSV is loaded into a Pandas DataFrame and passed through a structured cleaning workflow. Both date columns are cast to proper datetime objects, which then enables downstream temporal feature extraction (hour, day of week, month). A composite risk scoring model is built by combining three binary flags — late-night activity, elevated login attempts, and abnormally long transaction duration — and any transaction scoring 2 or higher across those signals is tagged as suspicious. The cleaned output is exported to `data/Clean/cleaned_transactions.csv`.

**Stage 2 — Python (Pipeline.py):** The cleaned CSV is loaded and pushed directly into a local MySQL database (`bank_analytics`) using a SQLAlchemy engine and Pandas' `to_sql()` method. The load is chunked at 1,000 rows per batch for performance, and `if_exists='replace'` allows the pipeline to be re-run idempotently. Column data types are explicitly mapped to MySQL types (Integer, Float, String).

**Stage 3 — MySQL (queries.sql):** Seven SQL queries run against the `transactions` table to answer specific business questions — from customer-level spend ranking using `GROUP BY` and `ORDER BY`, to monthly trend analysis using `MONTHNAME()`, to a two-pronged suspicious transaction hunt that combines a flag-based filter (`WHERE IsSuspicious = 1`) with a rule-based filter (`WHERE TransactionAmount > 10000 OR LoginAttempts > 3`).

**Stage 4 — Power BI (.pbix):** The cleaned CSV is connected to Power BI Desktop, which renders four themed pages with cross-filtering slicers, KPI cards, a geographic map visual, scatter plots, donut charts, and a transaction activity matrix. The dashboard is designed so that stakeholders can explore the data with no SQL knowledge required.

---

## 🐍 Python Analysis

All Python work is split across two scripts in `py_code/`.

### cleaning.py — Data Wrangling & Feature Engineering

**Structural Inspection**
- `df.info()` and `df.shape` confirmed 2,512 rows and 16 columns with mixed types (7 float/int, 9 object)
- `df.duplicated().sum()` returned 0 — no duplicate transaction records in the raw file
- `df.isnull().sum()` returned all zeros — no null values across any column

**Datetime Handling**
- `TransactionDate` and `PreviousTransactionDate` were both stored as plain strings and converted to `datetime64` using `pd.to_datetime(..., errors='coerce')`
- This enabled downstream extraction of `.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()`, and `.dt.hour` as additional temporal columns

**Outlier Detection (IQR Method)**
- Applied the standard IQR formula on `TransactionAmount`: Q1 = $81.89, Q3 = $414.53, IQR = $332.64, upper bound = $913.49
- Identified 113 transactions exceeding the upper bound — ranging from ~$914 to $1,919.11 — flagged for review rather than dropped, as large legitimate transactions are expected in banking data

**Engineered Columns**

| New Column | Logic | Insight |
|---|---|---|
| `SpendingTier` | `pd.cut()` with bins [0, 100, 500, 1000, ∞] → Low / Medium / High / Very High | Segments the customer base for behavioral analysis |
| `LateNightTransaction` | `TransactionDate.hour >= 22 OR hour < 6` | 0 such transactions in this dataset (no overnight activity) |
| `HighLoginAttempt` | `LoginAttempts >= 3` | 95 transactions had 3 or more login attempts |
| `LongDurationTransaction` | `TransactionDuration > 95th percentile (265s)` | 123 transactions had unusually long processing times |
| `RiskScore` | Sum of the three binary flags above (0–3) | Additive risk indicator per transaction |
| `SuspiciousTransaction` | `RiskScore >= 2` | 7 transactions flagged as potentially suspicious |

**Output**
- Cleaned DataFrame exported to `data/Clean/cleaned_transactions.csv` with `index=False`, preserving all 2,512 rows and 16 original columns alongside the newly engineered features

---

### Pipeline.py — Data Ingestion into MySQL

- Uses `SQLAlchemy.create_engine()` with the `mysql+mysqlconnector` dialect to connect to a local MySQL instance at `localhost/bank_analytics`
- Calls `df.to_sql(name='transactions', if_exists='replace', chunksize=1000)` to load the cleaned DataFrame into the `transactions` table
- Explicit dtype mapping ensures `customer_id` is stored as `INTEGER`, `amount` as `FLOAT`, and `transaction_type` as `VARCHAR(50)` rather than relying on Pandas' auto-inference
- The `chunksize=1000` parameter prevents memory pressure during the insert and is standard practice for production-scale ETL pipelines

---

## 🗄️ MySQL Analysis — Key Queries

All queries run against the `bank_analytics.transactions` table. Screenshots of the query code are available in `visuals/SQL_Queries/`.

### Business Questions Answered

**1. Which customers are the highest spenders?**
```sql
SELECT AccountID,
       COUNT(*) AS total_transactions,
       ROUND(SUM(TransactionAmount), 2) AS total_spend,
       ROUND(AVG(TransactionAmount), 2) AS avg_transaction,
       MAX(TransactionAmount) AS max_transaction
FROM transactions
GROUP BY AccountID
ORDER BY total_spend DESC
LIMIT 20;
```
Ranks the top 20 accounts by cumulative spend. AC00460 leads the dataset, with AC00363 and AC00337 close behind — visible in the Power BI "Top Accounts by Total Spend" chart.

---

**2. Which transaction types drive the most volume and value?**
```sql
SELECT TransactionType,
       COUNT(*) AS transaction_count,
       ROUND(SUM(TransactionAmount), 2) AS total_amount,
       ROUND(AVG(TransactionAmount), 2) AS avg_amount
FROM transactions
GROUP BY TransactionType
ORDER BY total_amount DESC;
```
Debit accounts for 77.4% (1,944) of all transactions and the overwhelming majority of total spend volume, while Credit averages a slightly different per-transaction amount.

---

**3. How does transaction volume shift across the calendar year?**
```sql
SELECT MONTHNAME(TransactionDate) AS month,
       COUNT(*) AS total_transactions,
       ROUND(SUM(TransactionAmount), 2) AS monthly_volume
FROM transactions
GROUP BY MONTH(TransactionDate), MONTHNAME(TransactionDate)
ORDER BY MONTH(TransactionDate);
```
Uses `MONTHNAME()` + `MONTH()` dual grouping to get both the readable label and correct sort order. April shows a sharp volume drop to $41,004 (161 transactions) versus September's peak of $72,832 (214 transactions).

---

**4 & 5. Where are suspicious transactions concentrated geographically?**
Two complementary approaches:
- **Flag-based:** `WHERE IsSuspicious = 1` filters on the engineered column loaded from Python, then groups by Location to count and sum suspicious activity
- **Rule-based:** `WHERE TransactionAmount > 10000 OR LoginAttempts > 3` applies pure SQL thresholds without relying on any pre-computed flags, providing a cross-validation layer

---

**6. Which customers have the highest average spend (with sufficient transaction history)?**
```sql
SELECT AccountID, CustomerAge,
       ROUND(AVG(TransactionAmount), 2) AS avg_spend,
       COUNT(*) AS total_txns
FROM transactions
GROUP BY AccountID, CustomerAge
HAVING COUNT(*) > 2
ORDER BY avg_spend DESC
LIMIT 10;
```
The `HAVING COUNT(*) > 2` clause filters out single-transaction accounts that would otherwise dominate an average-spend ranking. The query surfaces high-value, high-frequency customers — the most commercially valuable segment.

---

**7. How do transaction types break down across spending tiers?**
```sql
SELECT TransactionType,
       CASE
           WHEN TransactionAmount < 1000 THEN 'Low'
           WHEN TransactionAmount BETWEEN 1000 AND 5000 THEN 'Medium'
           ELSE 'High'
       END AS SpendingTier,
       COUNT(*) AS transaction_count,
       ROUND(SUM(TransactionAmount), 2) AS total_amount
FROM transactions
GROUP BY TransactionType,
         CASE WHEN TransactionAmount < 1000 THEN 'Low' ... END
ORDER BY TransactionType, total_amount DESC;
```
An inline `CASE WHEN` expression segments transactions into spending tiers without requiring a pre-existing column, then groups by the computed field — a pattern that demonstrates understanding of SQL aggregation on derived columns.

---

### Techniques Used
- `GROUP BY` + `ORDER BY` + `LIMIT` for top-N ranking
- `ROUND(SUM(...), 2)` and `ROUND(AVG(...), 2)` for clean financial output
- `MONTHNAME()` + `MONTH()` dual grouping for readable, correctly ordered monthly aggregates
- `HAVING` clause for post-aggregation filtering
- Inline `CASE WHEN` as a grouping dimension
- Dual `WHERE` strategies (flag-based and rule-based) for suspicious transaction detection

---

## 📈 Power BI Dashboard

The Power BI file (`powerbi/bank_analytics_powerBI.pbix`) renders a four-page interactive dashboard. All pages share a consistent navy-and-white color scheme and support cross-filtering.

---

### Page 1 — Executive Overview

**Purpose:** A high-level KPI summary for business leaders who need the full picture in under 30 seconds.

**KPI Cards (6):**
- **2.512K** — Total Transactions
- **1.12** — Average Login Attempts
- **$297.59** — Average Transaction Value
- **495** — Total Unique Accounts
- **$747.56K** — Total Transaction Volume
- **$5.11K** — Average Account Balance

**Visuals:**
- **Line chart — Monthly Transaction Amount Trend:** Plots total transaction value by month from January to December. April is a clear outlier at ~$41K (against a ~$62–73K baseline for other months). September and October are the twin peaks at $72.8K and $64.7K respectively.
- **Horizontal bar chart — Top Locations by Transaction Count:** Fort Worth, Los Angeles, and Charlotte lead in transaction frequency, followed by Oklahoma City, Philadelphia, and Tucson. The chart covers 14 cities.

**Slicers:** Filter by Month (radio button, January–December) and Transaction Type (Credit / Debit toggle)

---

### Page 2 — Customer Behavior

**Purpose:** Understand who your most valuable customers are and how spending tier, age, and channel affect behavior.

**Visuals:**
- **Horizontal bar chart — Top Accounts by Total Spend:** AC00460 is the single highest-spending account, followed by AC00363, AC00337, AC00021, and AC00439. The gap between AC00460 and the next tier is meaningful.
- **Horizontal bar chart — Account Spend Comparison (All Accounts):** A scrollable comparison of every account's total spend — useful for quickly identifying the long tail of low-activity customers.
- **Scatter plot — Avg. Transaction Value by Customer Age:** Plots per-account average transaction amount (Y) against CustomerAge (X) across the range of 18–80. A trend line shows a slight negative slope — older customers tend toward marginally lower average transactions — though the correlation is weak, with high variance especially in the 20–40 age band.
- **Donut chart — Customer Distribution by Spending Tier:** 86.39% (2.17K) of transactions fall in the "Low" tier, 9.08% in "Medium," 2.83% in "High," and a small fraction in "Very High" — confirming that the majority of banking activity in this dataset is everyday, small-to-mid-range spending.

**Slicers:** Filter by Month, Filter by Day (free text day-name entry), Transaction Type, and Channel Type (ATM / Branch / Online)

---

### Page 3 — Anomaly & Risk View

**Purpose:** Geographic and temporal risk profiling for fraud and compliance teams.

**Visuals:**
- **Geographic map — Transaction Distribution by Channel:** A Bing Maps visual plots pie-chart markers at each city location, with each pie slice colored by channel (ATM, Branch, Online). The map covers the contiguous United States and shows that all three channels are active across most cities — no single channel dominates geographically.
- **Horizontal bar chart — Transaction Frequency by Time Window & Type:** Groups transactions into afternoon (12–17h) and evening (17–21h) windows and splits by Credit vs. Debit. Debit dominates both windows, with the evening window slightly heavier than afternoon.
- **Table — Suspicious Transaction Activity Log:** A detailed drill-through table showing AccountID, Transaction Amount, Location, Time, and `IsSuspicious` status for individual records. Total volume shown at table footer: $42,960.99. The table confirms that nearly all logged transactions are classified as "normal," providing an audit trail for analysts to verify flag accuracy.

**Slicers:** Suspicious Transaction (Normal / Suspicious toggle), Channel Type, Filter by Month

---

### Page 4 — Transaction Patterns

**Purpose:** Temporal pattern analysis for operations and capacity planning teams.

**Visuals:**
- **Matrix — Hourly Transaction Activity by Day of Week:** A cross-tab of HourLabel (4 PM, 5 PM, 6 PM) vs. Day Name (Friday through Wednesday). Monday 5 PM is the single busiest hour-day combination with 337 transactions. The 4 PM slot is the most active across all days with 1,316 total. The matrix reveals that the dataset spans only 4–6 PM hour buckets, indicating transactions in this dataset are heavily concentrated in late-afternoon working hours.
- **Bar chart — Daily Transaction Volume:** Monday accounts for 1,070 of the 2,512 transactions (42.6%) — by far the busiest day of the week. Friday is the second-highest at 373. Thursday, Tuesday, and Wednesday are roughly even at ~340–370.
- **Donut chart — Credit vs. Debit Transaction Split:** Debit = 77.39% (1.94K), Credit = 22.61% (0.57K). This split is consistent across months and locations.

**Slicers:** Filter by Location (tile-button grid covering 43 cities), Channel Type, Filter by Day, Transaction Type

---

## 💡 Key Business Insights

- **April is a structural anomaly.** With only 161 transactions and $41,004 in volume — roughly 37% below the annual monthly average — April requires further investigation. This could reflect a data collection gap, a bank-specific operational pause, or genuine seasonal disengagement.

- **Monday afternoon is peak banking time.** Monday at 5 PM alone accounts for 337 transactions, and Monday as a whole drives 42.6% of all weekly activity. Staffing, server capacity, and fraud monitoring should be weighted heavily toward Monday afternoons.

- **September and October are the year's revenue peak.** The $72,832 and $64,706 monthly volumes in September and October are the highest in the dataset, suggesting year-end spending acceleration that the bank could target with product campaigns.

- **Debit dwarfs Credit in both volume and count.** 77.4% of all transactions are debit, contributing the large majority of total dollar volume. Credit transactions, though fewer, may carry a different risk profile worth analyzing separately.

- **Fort Worth, Los Angeles, and Charlotte are the highest-activity markets.** These three cities each have 67–70 transactions — roughly 20% above average city-level activity — making them the primary geographic concentration points for business and risk decisions.

- **The customer spending pyramid is heavily bottom-weighted.** 86.39% of transactions fall in the "Low" spending tier. The "High" and "Very High" tiers together represent less than 13% of records but likely contain a disproportionate share of dollar risk.

- **Account AC00460 is the platform's highest-value customer.** It leads total spend across all 495 accounts and appears consistently across multi-month and multi-channel analyses. High-value, high-frequency accounts like this warrant dedicated relationship management and proactive fraud monitoring.

- **The risk detection model flagged 7 transactions as suspicious.** These are cases where at least two of three signals fired simultaneously: login attempts ≥ 3 (95 transactions), processing duration > 265 seconds (123 transactions), and late-night activity (0 transactions in this dataset). The 7 suspicious records all triggered via the first two signals in combination — a finding that informs which behavioral features are most predictive in this specific dataset.

- **All three banking channels serve comparable volumes.** Branch (868), ATM (833), and Online (811) are nearly evenly distributed, suggesting the customer base is genuinely omnichannel. No single channel dominates, which has implications for infrastructure investment and fraud surface area.

---

## 📁 Project Structure

```
Bank-Transaction-Risk-Analytics/
│
├── data/                               # Dataset files
│   ├── bank_transactions_data.csv      # Raw dataset (2,512 × 16)
│   └── Clean/
│       └── cleaned_transactions.csv   # Cleaned output from cleaning.py
│
├── mysql_code/
│   └── queries.sql                    # All 7 SQL queries with inline comments
│
├── powerbi/
│   └── bank_analytics_powerBI.pbix    # Power BI Desktop project file
│
├── py_code/
│   ├── cleaning.py                    # Data cleaning & feature engineering (run first)
│   └── Pipeline.py                    # SQLAlchemy ingestion into MySQL (run second)
│
├── visuals/
│   ├── Data/
│   │   ├── raw.png                    # VSCode view of raw CSV
│   │   └── cleaned.png                # VSCode view of cleaned CSV
│   ├── PowerBI/
│   │   ├── 1.png                      # Executive Overview page
│   │   ├── 2.png                      # Customer Behavior page
│   │   ├── 3.png                      # Anomaly & Risk View page
│   │   └── 4.png                      # Transaction Patterns page
│   ├── Py_Code/
│   │   ├── cleaning_1.png             # cleaning.py — VSCode screenshot (lines 1–37)
│   │   ├── cleaning_2.png             # cleaning.py — VSCode screenshot (lines 99–134)
│   │   └── pipeline.png               # Pipeline.py — VSCode screenshot
│   └── SQL_Queries/
│       ├── queries_1.png              # queries.sql — VSCode screenshot (lines 1–36)
│       └── queries_2.png              # queries.sql — VSCode screenshot (lines 37–72)
│
├── LICENSE                            # MIT License
└── README.md                          # This file
```

> **Execution order:** `cleaning.py` → `Pipeline.py` → `queries.sql` → Open `.pbix` in Power BI

---

## 💻 Local Setup & How to Explore

### 🐍 Python Setup (VSCode)

```bash
# 1. Clone the repository
git clone https://github.com/ANINDYAadhikari/Bank-Transaction-Risk-Analytics
cd Bank-Transaction-Risk-Analytics

# 2. Open the folder in VSCode
code .

# 3. Create a virtual environment (recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS / Linux:
source venv/bin/activate

# 4. Install required libraries
pip install pandas numpy seaborn sqlalchemy mysql-connector-python

# 5. Run the scripts in order:
#    First — data cleaning and feature engineering
python py_code/cleaning.py

#    Second — push cleaned data into MySQL (requires MySQL running locally)
python py_code/Pipeline.py
```

> **Before running Pipeline.py**, update the connection string in `Pipeline.py` line 18 to match your MySQL credentials:
> ```python
> engine = create_engine('mysql+mysqlconnector://YOUR_USER:YOUR_PASSWORD@localhost/bank_analytics')
> ```

---

### 🗄️ MySQL Setup (VSCode / MySQL Workbench)

```sql
-- 1. Install MySQL Community Server (if not already installed)
--    Download: https://dev.mysql.com/downloads/mysql/

-- 2. Connect to your local instance via MySQL Workbench or the VSCode MySQL extension

-- 3. The database and table are created automatically by Pipeline.py
--    To verify after running the pipeline:
SHOW DATABASES;
USE bank_analytics;
SHOW TABLES;
SELECT COUNT(*) FROM transactions;  -- Should return 2512

-- 4. Run the analysis queries from mysql_code/queries.sql
--    Open the file in VSCode (with MySQL extension) or MySQL Workbench
--    and execute each query block individually
```

> 💡 **No MySQL?** All SQL query code is visible in `visuals/SQL_Queries/queries_1.png` and `queries_2.png` — captured directly from VSCode. You can review the queries and logic without running MySQL.

---

### 📊 Power BI Setup

```
1. Install Power BI Desktop (Free)
   Download: https://powerbi.microsoft.com/en-us/desktop/

2. Open the file:
   powerbi/bank_analytics_powerBI.pbix

3. If prompted about the data source path:
   Go to: Home → Transform Data → Data Source Settings → Change Source
   Point it to your local: data/Clean/cleaned_transactions.csv

4. Click "Refresh" to reload data, then explore all four dashboard pages:
   - Executive Overview
   - Customer Behavior
   - Anomaly & Risk View
   - Transaction Patterns
```

> 💡 **No Power BI?** All four dashboard pages are available as high-resolution screenshots in `visuals/PowerBI/` (1.png through 4.png).

---

## 🖼️ Screenshots & Visuals Preview

### Power BI — Executive Overview
![Executive Overview](visuals/PowerBI/1.png)
*KPI cards (2.512K transactions, $747.56K total volume, 495 accounts), monthly trend line showing the April dip and September peak, and top-14 city bar chart.*

---

### Power BI — Customer Behavior
![Customer Behavior](visuals/PowerBI/2.png)
*Top accounts by total spend, scatter plot of average transaction value vs. customer age, and spending tier donut showing 86.39% Low-tier concentration.*

---

### Power BI — Anomaly & Risk View
![Anomaly & Risk View](visuals/PowerBI/3.png)
*Geographic transaction map with channel-level pie markers across the US, afternoon vs. evening time bucket chart, and the suspicious transaction activity log.*

---

### Power BI — Transaction Patterns
![Transaction Patterns](visuals/PowerBI/4.png)
*Hourly × day-of-week activity matrix (Monday 5 PM peak: 337 transactions), daily volume bar chart, and Credit vs. Debit donut (77.4% Debit).*

---

### Python — cleaning.py (VSCode)
![Python Cleaning Script Part 1](visuals/Py_Code/cleaning_1.png)
*Data loading, structural inspection (`df.info()`, `df.shape`), duplicate check, null check, and datetime conversion — the foundational cleaning steps.*

![Python Cleaning Script Part 2](visuals/Py_Code/cleaning_2.png)
*The risk model: `LongDurationTransaction` flag (>265s), `LateNightTransaction` flag, `HighLoginAttempt` flag (≥3), additive `RiskScore`, and `SuspiciousTransaction` filter at threshold ≥ 2.*

---

### Python — Pipeline.py (VSCode)
![Pipeline Script](visuals/Py_Code/pipeline.png)
*SQLAlchemy engine creation, `df.to_sql()` call with `chunksize=1000`, dtype mapping, and connection to the `bank_analytics` MySQL database.*

---

### SQL Queries (VSCode)
![SQL Queries Part 1](visuals/SQL_Queries/queries_1.png)
*Database setup, customer total-spend ranking query, transaction type breakdown, and monthly volume trend using `MONTHNAME()` + `MONTH()` dual grouping.*

![SQL Queries Part 2](visuals/SQL_Queries/queries_2.png)
*Suspicious transaction queries (flag-based and rule-based), high-value customer profiling with `HAVING COUNT(*) > 2`, and spending tier segmentation via inline `CASE WHEN`.*

---

### Raw & Cleaned Dataset (VSCode)
![Raw Dataset](visuals/Data/raw.png)
*VSCode view of `bank_transactions_data.csv` showing all 16 original columns — TransactionID through PreviousTransactionDate — with mixed transaction types, channels, and occupations visible in the first rows.*

---

## 📚 Dataset & Credits

- **Dataset:** [Bank Transaction Dataset for Fraud Detection](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection) — sourced from Kaggle, made available for open use under the site's standard terms.
- **Libraries:** Pandas, NumPy, Seaborn (Python Software Foundation / open-source contributors), SQLAlchemy (Mike Bayer / SQLAlchemy contributors), MySQL Connector/Python (Oracle Corporation).
- **Visualization:** Microsoft Power BI Desktop (free public edition).

This project was built as part of a professional portfolio to demonstrate end-to-end data analytics capabilities — from raw data wrangling and relational database querying to interactive business intelligence dashboarding.

---

## 👤 Author

```
Anindya Adhikari
B.Tech — Swami Vivekananda University
Specialization: Data Analytics & Cybersecurity 

🔗 LinkedIn: https://linkedin.com/in/anindya-adhikari-55aa89239
💻 GitHub:   https://github.com/ANINDYAadhikari
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with Python · MySQL · Power BI · and a lot of <code>GROUP BY</code></sub>
</div>
