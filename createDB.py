import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('uniform_shop.db')
cursor = conn.cursor()

# Create Students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
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
    CREATE TABLE IF NOT EXISTS Employees (
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
    CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type_id INTEGER,
        description TEXT,
        price REAL NOT NULL,
        in_stock INTEGER NOT NULL,
        shelf_location TEXT,
        image TEXT,
        FOREIGN KEY (type_id) REFERENCES InventoryTypes(id)
    )
''')

# Create Invoices table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purchaser INTEGER NOT NULL,
        served_by INTEGER NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        FOREIGN KEY (purchaser) REFERENCES Students(id),
        FOREIGN KEY (served_by) REFERENCES Employees(id)
    )
''')

# Create Invoice items table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS InvoiceItems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        item_price REAL NOT NULL,
        item_discount_to REAL,
        paid BOOLEAN,
        payment_method TEXT,
        FOREIGN KEY (invoice_id) REFERENCES Invoices(id),
        FOREIGN KEY (item_id) REFERENCES Inventory(id)
    )
''')

# Create InventoryTypes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS InventoryTypes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')

# Create Suppliers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suppliers (
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
