import polars as pl
from faker import Faker
import sqlite3

# Create or connect to a database (this will create the file if it doesn't exist)
conn = sqlite3.connect("my_local_db.db")
cur = conn.cursor()

# Create a Faker instance
fake = Faker()

# Number of rows
n_rows = 1000

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    address TEXT,
    phone_number TEXT,
    company TEXT
)
""")
conn.commit()

# Generate fake data
data = {
    "name": [fake.name() for _ in range(n_rows)],
    "email": [fake.email() for _ in range(n_rows)],
    "address": [fake.address() for _ in range(n_rows)],
    "phone_number": [fake.phone_number() for _ in range(n_rows)],
    "company": [fake.company() for _ in range(n_rows)],
}

df = pl.from_dict(data)

# Convert Polars DataFrame to list of tuples
data_to_insert = [tuple(row) for row in df.to_pandas().values]

# Insert data into SQLite (using executemany for batch insert)
insert_query = """
INSERT INTO my_table (name, email, address, phone_number, company)
VALUES (?, ?, ?, ?, ?)
"""

cur.executemany(insert_query, data_to_insert)
conn.commit()  # Commit the transaction after insertion

# Query all data from the table (Reopen connection if needed)
cur.execute("SELECT count(*) FROM my_table")

# Fetch all rows
rows = cur.fetchall()

print(rows)

# Close the cursor and connection
cur.close()
conn.close()

print("Data inserted successfully!")
