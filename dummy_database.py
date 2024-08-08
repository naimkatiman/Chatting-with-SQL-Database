database_url = "sqlite:///dummy_database.db"

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('dummy_database.db')
cursor = connection.cursor()

# Create a sample table: customers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        purchase_date DATE NOT NULL
    )
''')

# Insert dummy data into the customers table
customers_data = [
    (1, 'Alice Smith', 'alice@example.com', '2024-07-15'),
    (2, 'Bob Johnson', 'bob@example.com', '2024-07-20'),
    (3, 'Charlie Brown', 'charlie@example.com', '2024-08-01'),
    (4, 'Diana Prince', 'diana@example.com', '2024-08-05'),
]

cursor.executemany('''
    INSERT INTO customers (id, name, email, purchase_date)
    VALUES (?, ?, ?, ?)
''', customers_data)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Dummy database created successfully.")
