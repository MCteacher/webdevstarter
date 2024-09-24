import sqlite3
import os

# delete uniform_shop.db if it exists
if os.path.exists('uniform_shop.db'):
    os.remove('uniform_shop.db')

# Connect to the SQLite database
conn = sqlite3.connect('uniform_shop.db')
cursor = conn.cursor()

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        year INTEGER NOT NULL,
        house TEXT,
        boarder BOOLEAN,
        date_of_entry DATE,
        date_of_birth DATE,
        address1 TEXT,
        address2 TEXT,
        address3 TEXT,
        suburb TEXT,
        state TEXT,
        postcode TEXT,
        is_active BOOLEAN
    )
''')

# Create Employees table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        code TEXT NOT NULL,
        category TEXT,
        is_volunteer BOOLEAN,
        is_active BOOLEAN
    )
''')

# Create Inventory table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type_id INTEGER,
        description TEXT,
        price REAL NOT NULL,
        in_stock INTEGER NOT NULL,
        shelf_location TEXT,
        image TEXT
    )
''')

# Create Invoices table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purchaser INTEGER NOT NULL,
        served_by INTEGER NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL
    )
''')

# Create Invoice items table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoiceItems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        item_price REAL NOT NULL,
        item_discount_to REAL,
        paid BOOLEAN,
        payment_method TEXT
    )
''')

# Create InventoryTypes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventoryTypes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')

# Create Suppliers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_name TEXT,
        contact_email TEXT,
        contact_phone TEXT,
        address1 TEXT,
        address2 TEXT,
        suburb TEXT,
        state TEXT,
        postcode TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
