import pandas as pd
from db_connection import conn

query = "SELECT * FROM financial_transactions"

df = pd.read_sql(query, conn)

print(df.head())