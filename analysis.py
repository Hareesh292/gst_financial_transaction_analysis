import os
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="financial_db"
)

query = "SELECT * FROM financial_transactions"

df = pd.read_sql(query, conn)
os.makedirs("images", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)
plt.savefig("images/revenue_chart.png")
plt.savefig("images/gst_chart.png")

df.to_csv("financial_transactions.csv", index=False)