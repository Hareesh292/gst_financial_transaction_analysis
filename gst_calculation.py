import pandas as pd
from db_connection import conn

df = pd.read_sql("SELECT * FROM financial_transactions", conn)

df['gst_amount'] = (df['price'] * df['quantity']) * df['gst_percent'] / 100

df['total_amount'] = (df['price'] * df['quantity']) + df['gst_amount']

print(df[['product_name','gst_amount','total_amount']])