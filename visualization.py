import pandas as pd
import matplotlib.pyplot as plt
from db_connection import conn

df = pd.read_sql("SELECT * FROM financial_transactions", conn)

df['gst_amount'] = (df['price'] * df['quantity']) * df['gst_percent'] / 100

df['total_amount'] = (df['price'] * df['quantity']) + df['gst_amount']

df['transaction_date'] = pd.to_datetime(df['transaction_date'])

df['month'] = df['transaction_date'].dt.month

monthly_revenue = df.groupby('month')['total_amount'].sum()

monthly_revenue.plot(kind='bar')

plt.title("Monthly Revenue")

plt.show()