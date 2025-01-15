##DB to Excel
import sqlite3, pandas as pd
conn = sqlite3.connect('expenses.db')
df = pd.read_sql_query("SELECT * FROM expenses", conn)
df.to_excel('expense101_data.xlsx', index=False, engine='openpyxl') if not df.empty else print("No data found.")
conn.close()
