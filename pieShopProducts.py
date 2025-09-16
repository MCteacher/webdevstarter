import sqlite3

# Connect to the same SQLite database as before
conn = sqlite3.connect("pieShop.db")
cursor = conn.cursor()

# Step 1: Create the products table with AUTOINCREMENT id
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Step 2: Insert product data (excluding IDs)
product_data = [
    ('Pythonista Plush Toy', 20),
    ('Snake USB Drive', 15),
    ('Python Code T-Shirt', 25),
    ('Zen of Python Poster', 9.99),
    ('Guido van Rossum Bobblehead', 29.95),
    ('Monty Python Mug', 12.49),
    ('Python Logo Sticker Pack', 4.5),
]

cursor.executemany("""
INSERT INTO products (name, price)
VALUES (?, ?)
""", product_data)

# Commit and close
conn.commit()
conn.close()

print("Products table created with auto-incrementing IDs and populated successfully.")
