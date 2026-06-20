# ====================================================
# Customer-Transaction-Analytics DATA → MySQL PIPELINE
# ====================================================

import pandas as pd
import numpy as np 
import seaborn as sns 
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Float, String

# --- Load DataSet ---
df = pd.read_csv(r'C:\Project\Customer-Transaction-Analytics\data\Clean\cleaned_transactions.csv')
print("DataSet loaded Succssfully")

# STEP 3: CONNECT TO MYSQL
# Create engine
engine = create_engine(
    'mysql+mysqlconnector://root:root@localhost/bank_analytics'
)

# Load DataFrame into MySQL
df.to_sql(
    name='transactions',
    con=engine,
    if_exists='replace',   # options: 'fail', 'replace', 'append'
    index=False,
    dtype={
        'customer_id': Integer(),
        'amount': Float(),
        'transaction_type': String(50)
    },
    chunksize=1000         # improves performance for large data
)
print("Loaded to MySQL successfully!")
