import random
from faker import Faker
import pandas as pd
from datetime import datetime

fake, categories, payment_modes = Faker(), ["Food", "Transportation", "Bills", "Fuel", "Entertainment", "Pharmacy", "Office Supplies", "Skills Improvement"], ["Cash", "Netbanking", "UPI", "Credit Card", "Debit Card"]

category_sentences = {
    "Food": ["Bought groceries for the week", "Ordered takeout for lunch", "Tried a new restaurant", "Purchased snacks for a party"],
    "Transportation": ["Refueled the car", "Paid for taxi fare", "Topped up bus card", "Booked a ride-sharing service"],
    "Bills": ["Paid the electricity bill", "Settled the water bill", "Paid monthly internet subscription", "Paid the credit card bill"],
    "Fuel": ["Filled up the car's gas tank", "Bought fuel for the bike", "Refueled the car at the station"],
    "Entertainment": ["Watched a movie at the theater", "Bought tickets for a concert", "Subscribed to a streaming service", "Went out for a night out with friends"],
    "Pharmacy": ["Bought medicine for a cold", "Purchased vitamins and supplements", "Got a prescription filled at the pharmacy"],
    "Office Supplies": ["Bought printer ink", "Purchased office stationary", "Bought a new laptop for work", "Bought desk accessories"],
    "Skills Improvement": ["Enrolled in an online course", "Paid for a professional workshop", "Bought books for learning", "Signed up for a skills training program"]
}

def generate_transactions(month, year, num_records=150):
    transactions = []

    # Ensure each "Bills" description occurs once and on the 3rd of the month
    bill_descriptions = category_sentences["Bills"]
    for description in bill_descriptions:
        transactions.append({
            "Date": datetime(year, month, 3).strftime('%Y-%m-%d'),
            "Category": "Bills",
            "Payment Mode": random.choice(payment_modes),
            "Description": description,
            "Amount Paid": round(random.uniform(10, 500), 2),
            "Cashback": 0
        })
    
    # Ensure remaining transactions are for other categories
    for _ in range(num_records - len(bill_descriptions)):  # Subtract bills transactions from the total count
        category = random.choice(categories)
        
        # Skip "Bills" for other transactions
        while category == "Bills":
            category = random.choice(categories)
        
        payment_mode = random.choice(payment_modes)
        amount_paid = round(random.uniform(10, 500), 2)
        cashback = round(random.uniform(0, 0.1 * amount_paid), 2) if payment_mode in ["UPI", "Credit Card"] else 0
        
        transactions.append({
            "Date": fake.date_between_dates(date_start=datetime(year, month, 1), date_end=datetime(year, month, 28)),
            "Category": category,
            "Payment Mode": payment_mode,
            "Description": random.choice(category_sentences[category]),
            "Amount Paid": amount_paid,
            "Cashback": cashback
        })
    
    return transactions

df = pd.DataFrame([trans for month in range(1, 13) for trans in generate_transactions(month, 2025)])
print(df.tail())



### Create Database

import sqlite3

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        category TEXT NOT NULL,
        payment_mode TEXT NOT NULL,
        description TEXT NOT NULL,
        amount_paid REAL NOT NULL,
        cashback REAL
    );
''')

# Insert the data into the table
df.to_sql('expenses', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()
print("Data successfully inserted into the SQLite database.")
