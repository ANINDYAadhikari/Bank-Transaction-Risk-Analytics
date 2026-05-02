# ======================================
# Customer-Transaction-Analytics PROJECT
# --------------------------------------
# Author -- Anindya Adhikari
# ======================================


# --- Import Libraries ---
import pandas as pd 
import numpy as np 



# --- Load DataSet ---
df = pd.read_csv(r"C:\Users\anind\OneDrive\Desktop\PythonVSC\Project\Customer-Transaction-Analytics\data\bank_transactions_data.csv")
print("DataSet Loaded Successfully \n")



# How many rows and columns are in the dataset, and what are the data types of each column?
'''
df.info()
print(df.shape)
'''


# Are there any duplicate transactions, and how should they be removed?
'''
df.duplicated().sum()
df_clean = df.drop_duplicates(inplace = True)
print(df.shape) 
'''


# Are there any missing values in the dataset, and which columns contain them?
'''
df.isnull().sum()
'''

# Convert to datetime first
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
df['PreviousTransactionDate'] = pd.to_datetime(df['PreviousTransactionDate'], errors='coerce')


# Are TransactionDate and PreviousTransactionDate in proper datetime format?
'''
print(df[['TransactionDate', 'PreviousTransactionDate']].dtypes)
'''


# What new time features can be extracted from TransactionDate such as month, day of week, and hour?
'''
df['year'] = df['TransactionDate'].dt.year
df['month'] = df['TransactionDate'].dt.month
df['day'] = df['TransactionDate'].dt.day
df['day_of_week'] = df['TransactionDate'].dt.day_name()
df['hour'] = df['TransactionDate'].dt.hour
print(df.head(10))
'''


# Which transaction amounts are unusually high compared to the rest of the data?
'''
Q1 = df['TransactionAmount'].quantile(0.25)
Q3 = df['TransactionAmount'].quantile(0.75)
upper_bound = Q3 + 1.5 * (Q3 - Q1)
high_tx = df[df['TransactionAmount'] > upper_bound]
print(high_tx[['TransactionID', 'TransactionAmount']])
'''


# Create a SpendingTier column using transaction amount ranges
'''
df['SpendingTier'] = pd.cut(
    df['TransactionAmount'],
    bins=[0, 100, 500, 1000, float('inf')],
    labels=['Low', 'Medium', 'High', 'Very High']
)
print(df[['TransactionAmount', 'SpendingTier']].head())
'''


# Create a LateNightTransaction flag using the transaction hour
'''
df['LateNightTransaction'] = (
    (df['TransactionDate'].dt.hour >= 22) | 
    (df['TransactionDate'].dt.hour < 6)
)
print(df[['TransactionDate', 'LateNightTransaction']])
'''


# create a HighLoginAttempt flag based on the number of login attempts
'''
df['HighLoginAttempt'] = df['LoginAttempts'] >= 3
print(df[['LoginAttempts', 'HighLoginAttempt']].head(10))
'''


# create a LongDurationTransaction flag based on transaction duration
'''
df['LongDurationTransaction'] = df['TransactionDuration'] > 60
print(df[['TransactionDuration', 'LongDurationTransaction']].head(10))
'''

# Which transactions look suspicious when multiple risk signals happen together?
'''
# Late Night flag
df['LateNightTransaction'] = (
    (df['TransactionDate'].dt.hour >= 22) | 
    (df['TransactionDate'].dt.hour < 6)
)
# High login attempts
df['HighLoginAttempt'] = df['LoginAttempts'] >= 3
# Long duration (using quantile)
threshold = df['TransactionDuration'].quantile(0.95)
df['LongDurationTransaction'] = df['TransactionDuration'] > threshold

# Create a risk score by adding flags
df['RiskScore'] = (
    df['LateNightTransaction'].astype(int) +
    df['HighLoginAttempt'].astype(int) +
    df['LongDurationTransaction'].astype(int)
)
df['SuspiciousTransaction'] = df['RiskScore'] >= 2 # Flag suspicious transactions (2 or more signals)
suspicious = df[df['SuspiciousTransaction']] # Show suspicious transactions
print(suspicious[['TransactionID', 'RiskScore', 'SuspiciousTransaction']])
'''


# Save the cleaned dataset in a new CSV file for MySQL import