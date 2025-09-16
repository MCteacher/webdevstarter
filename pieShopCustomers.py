import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("pieShop.db")
cursor = conn.cursor()

# Step 1: Create the customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    surname TEXT NOT NULL,
    address1 TEXT NOT NULL,
    address2 TEXT NOT NULL,
    creditCardNumbers TEXT NOT NULL,
    creditCardExpiry TEXT NOT NULL
)
""")

# Step 2: Insert customer data
customer_data = [
    ('Jenny', 'Brown', '6 Syntax Ct', 'Nerdonia SA 5000', '4000056655665550.00', '1/01/2029'),
    ('Helen', 'Choi', '321 Code St', 'Bugtown NT 0800', '4111111111111110.00', '1/06/2025'),
    ('Alice', 'Johnson', '123 Pythonic Way', 'Pythontown NSW 2000', '4532758493021090.00', '1/11/2026'),
    ('Alice', 'Johnson', '999 Node Corso', 'JavaScript QLD 4020', '4532758493021090.00', '1/11/2026'),
    ('Dana', 'Klein', '88 Poster Rd', 'Nerdonia SA 5000', '5105105105105100.00', '1/02/2028'),
    ('Fay', 'Lee', '5 Byte Ln', 'Loop City ACT 2601', '6011000990139420.00', '1/09/2027'),
    ('Kyle', 'Lopez', '12 Hackathon Blvd', 'Byteville QLD 4101', '3530111333300000.00', '1/10/2025'),
    ('George', 'Mills', '13 Nerd Dr', 'Compville TAS 7000', '5555555555554440.00', '1/03/2026'),
    ('Eli', 'Nguyen', '7 Snake St', 'Pythonopolis WA 6000', '378282246310005.00', '1/08/2026'),
    ('Ian', 'Perez', '8 Guido Rd', 'Hackertown NSW 2100', '6011111111111110.00', '1/12/2024'),
    ('Bob', 'Smith', '42 Monty Ave', 'Code City VIC 3050', '4024007145828280.00', '1/04/2027'),
    ('Charlie', 'Wong', '9 Zen Blvd', 'Byteville QLD 4101', '6011514433546200.00', '1/07/2025'),
]

cursor.executemany("""
INSERT INTO customers (firstname, surname, address1, address2, creditCardNumbers, creditCardExpiry)
VALUES (?, ?, ?, ?, ?, ?)
""", customer_data)

# Commit and close
conn.commit()
conn.close()

print("Customers table created and populated with auto-incrementing IDs.")
