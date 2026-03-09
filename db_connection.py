import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="financial_db"
)

print("Database Connected")