import sqlite3

# Connect (or create) the SQLite database
conn = sqlite3.connect('purchases.db')
cursor = conn.cursor()

# Drop tables if they exist (for a clean slate)
cursor.execute("DROP TABLE IF EXISTS purchases")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS customers")

# Create customers table
cursor.execute('''
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    surname TEXT,
    address1 TEXT,
    address2 TEXT,
    creditCardNumbers TEXT,
    creditCardExpiry TEXT
)
''')

# Create products table
cursor.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    productName TEXT,
    productPrice REAL
)
''')

# Create purchases table
cursor.execute('''
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    custId INTEGER,
    productId INTEGER,
    purchaseDate TEXT,
    purchaseServedByName TEXT,
    FOREIGN KEY(custId) REFERENCES customers(id),
    FOREIGN KEY(productId) REFERENCES products(id)
)
''')

# Data for customers: (id, firstname, surname, address1, address2, creditCardNumbers, creditCardExpiry)
customers_data = [
    (1, "Mason", "Abbott", "321 Code St",
     "Bugtown NT 0800", "4111111111111110.00", "1/06/2026"),
    (2, "Nia", "Baker", "9 Zen Blvd", "Byteville QLD 4101",
     "6011514433546200.00", "1/07/2026"),
    (3, "Xander", "Bell", "8 Guido Rd", "Hackertown NSW 2100",
     "4111111111111110.00", "1/10/2026"),
    (4, "Jenny", "Brown", "6 Syntax Ct", "Nerdonia SA 5000",
     "4000056655665550.00", "1/01/2029"),
    (5, "Tom", "Chen", "321 Code St", "Bugtown NT 0800",
     "3530111333300000.00", "1/03/2029"),
    (6, "Helen", "Choi", "321 Code St", "Bugtown NT 0800",
     "4111111111111110.00", "1/06/2025"),
    (7, "Nora", "Cruz", "7 Snake St", "Pythonopolis WA 6000",
     "4012888888881880.00", "1/08/2027"),
    (8, "Omar", "Davis", "5 Byte Ln", "Loop City ACT 2601",
     "6011000000000000.00", "1/09/2025"),
    (9, "Pia", "Ellis", "88 Poster Rd", "Nerdonia SA 5000",
     "5105105105105100.00", "1/03/2026"),
    (10, "Quentin", "Fraser", "6 Syntax Ct",
     "Nerdonia SA 5000", "6011000990139420.00", "1/09/2025"),
    (11, "Sara", "Gomez", "13 Nerd Dr", "Compville TAS 7000",
     "6011111111111110.00", "1/07/2025"),
    (12, "Victor", "Hill", "9 Zen Blvd", "Byteville QLD 4101",
     "6011000990139420.00", "1/11/2027"),
    (13, "Alice", "Johnson", "123 Pythonic Way",
     "Pythontown NSW 2000", "4532758493021090.00", "1/11/2026"),
    (14, "Lisa", "Kim", "123 Pythonic Way",
     "Pythontown NSW 2000", "6011000400000000.00", "1/05/2027"),
    (15, "Ella", "King", "7 Snake St", "Pythonopolis WA 6000",
     "3530111333300000.00", "1/03/2028"),
    (16, "Dana", "Klein", "88 Poster Rd",
     "Nerdonia SA 5000", "5105105105105100.00", "1/02/2028"),
    (17, "Fay", "Lee", "5 Byte Ln", "Loop City ACT 2601",
     "6011000990139420.00", "1/09/2027"),
    (18, "Quinn", "Lee", "88 Poster Rd",
     "Nerdonia SA 5000", "378734493671000.00", "1/12/2026"),
    (19, "Fay", "Lee", "5 Byte Ln", "Loop City ACT 2601",
     "6011111111111110.00", "1/12/2026"),
    (20, "Derek", "Lim", "321 Code St", "Bugtown NT 0800",
     "6011000990139420.00", "1/07/2029"),
    (21, "Kyle", "Lopez", "12 Hackathon Blvd",
     "Byteville QLD 4101", "3530111333300000.00", "1/10/2025"),
    (22, "Raj", "Mehta", "6 Syntax Ct", "Nerdonia SA 5000",
     "4111111111111110.00", "1/10/2027"),
    (23, "George", "Mills", "13 Nerd Dr",
     "Compville TAS 7000", "5555555555554440.00", "1/03/2026"),
    (24, "Zack", "Moore", "5 Byte Ln", "Loop City ACT 2601",
     "6011111111111110.00", "1/09/2025"),
    (25, "Yara", "Ng", "42 Monty Ave", "Code City VIC 3050",
     "6011000000000000.00", "1/08/2027"),
    (26, "Eli", "Nguyen", "7 Snake St", "Pythonopolis WA 6000",
     "378282246310005.00", "1/08/2026"),
    (27, "Usha", "Park", "123 Pythonic Way",
     "Pythontown NSW 2000", "4000056655665550.00", "1/02/2026"),
    (28, "Ian", "Perez", "8 Guido Rd", "Hackertown NSW 2100",
     "6011111111111110.00", "1/12/2024"),
    (29, "Anna", "Shah", "6 Syntax Ct", "Nerdonia SA 5000",
     "4000056655665550.00", "1/11/2028"),
    (30, "Bob", "Smith", "42 Monty Ave", "Code City VIC 3050",
     "4024007145828280.00", "1/04/2027"),
    (31, "Wendy", "Tran", "7 Snake St", "Pythonopolis WA 6000",
     "5105105105105100.00", "1/06/2025"),
    (32, "Chloe", "West", "13 Nerd Dr", "Compville TAS 7000",
     "5105105105105100.00", "1/05/2027"),
    (33, "Pam", "White", "42 Monty Ave", "Code City VIC 3050",
     "5105105105105100.00", "1/04/2026"),
    (34, "Charlie", "Wong", "9 Zen Blvd",
     "Byteville QLD 4101", "6011514433546200.00", "1/07/2025"),
    (35, "Brad", "Yu", "88 Poster Rd", "Nerdonia SA 5000",
     "4111111111111110.00", "1/02/2027"),
    (36, "Mike", "Zhang", "9 Zen Blvd", "Byteville QLD 4101",
     "4111111111111110.00", "1/06/2026")
]

# Insert customers data
cursor.executemany('''
INSERT INTO customers (id, firstname, surname, address1, address2, creditCardNumbers, creditCardExpiry)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', customers_data)

# Data for products: (id, productName, productPrice)
products_data = [
    (1, "Python Plush Toy", 19.99),
    (4, "Snake USB Drive", 14.99),
    (3, "Python Code T-Shirt", 24.95),
    (5, "Zen of Python Poster", 9.99),
    (7, "Guido van Rossum Bobblehead", 29.95),
    (2, "Monty Python Mug", 12.49),
    (6, "Python Logo Sticker Pack", 4.5)
]

cursor.executemany('''
INSERT INTO products (id, productName, productPrice)
VALUES (?, ?, ?)
''', products_data)

# Data for purchases: (custId, productId, purchaseDate, purchaseServedByName)
purchases_data = [
    (13, 1, "11/10/2024", "Grace Hopper"),
    (30, 4, "2/11/2024", "Dennis Ritchie"),
    (34, 3, "18/01/2025", "Guido van Rossum"),
    (16, 5, "21/03/2025", "Ada Lovelace"),
    (26, 7, "14/04/2025", "Grace Hopper"),
    (17, 2, "7/12/2024", "Dennis Ritchie"),
    (23, 6, "8/06/2025", "Alan Turing"),
    (6, 3, "30/09/2024", "Ada Lovelace"),
    (28, 5, "22/05/2025", "Grace Hopper"),
    (4, 7, "19/08/2024", "Guido van Rossum"),
    (21, 2, "29/11/2024", "Alan Turing"),
    (14, 1, "9/01/2025", "Dennis Ritchie"),
    (36, 3, "14/02/2025", "Guido van Rossum"),
    (7, 4, "25/10/2024", "Grace Hopper"),
    (8, 6, "5/03/2025", "Ada Lovelace"),
    (33, 2, "3/07/2025", "Dennis Ritchie"),
    (18, 5, "12/09/2024", "Alan Turing"),
    (22, 3, "1/06/2025", "Guido van Rossum"),
    (11, 7, "10/08/2025", "Grace Hopper"),
    (5, 4, "26/02/2025", "Dennis Ritchie"),
    (27, 1, "4/04/2025", "Ada Lovelace"),
    (12, 2, "16/05/2025", "Alan Turing"),
    (31, 5, "20/12/2024", "Guido van Rossum"),
    (3, 3, "17/03/2025", "Dennis Ritchie"),
    (25, 6, "20/07/2025", "Grace Hopper"),
    (24, 7, "8/11/2024", "Ada Lovelace"),
    (29, 1, "26/01/2025", "Alan Turing"),
    (35, 3, "3/09/2024", "Grace Hopper"),
    (32, 2, "22/04/2025", "Dennis Ritchie"),
    (20, 5, "12/06/2025", "Guido van Rossum"),
    (15, 3, "11/02/2025", "Ada Lovelace"),
    (16, 4, "5/10/2024", "Grace Hopper"),
    (26, 6, "3/08/2025", "Alan Turing"),
    (19, 7, "26/06/2025", "Dennis Ritchie"),
    (23, 1, "21/09/2024", "Guido van Rossum"),
    (6, 2, "2/03/2025", "Ada Lovelace"),
    (28, 3, "14/01/2025", "Dennis Ritchie"),
    (4, 4, "18/11/2024", "Alan Turing"),
    (1, 6, "27/05/2025", "Grace Hopper"),
    (2, 5, "5/04/2025", "Guido van Rossum"),
    (8, 1, "28/10/2024", "Ada Lovelace"),
    (9, 2, "22/02/2025", "Dennis Ritchie"),
    (10, 3, "14/12/2024", "Grace Hopper"),
    (16, 7, "30/07/2025", "Alan Turing"),
    (26, 5, "5/01/2025", "Guido van Rossum"),
    (19, 4, "23/03/2025", "Grace Hopper"),
    (23, 1, "9/09/2024", "Ada Lovelace"),
    (6, 6, "13/08/2025", "Dennis Ritchie"),
    (28, 2, "17/07/2025", "Alan Turing"),
    (4, 3, "18/06/2025", "Guido van Rossum")
]

cursor.executemany('''
INSERT INTO purchases (custId, productId, purchaseDate, purchaseServedByName)
VALUES (?, ?, ?, ?)
''', purchases_data)

conn.commit()
print("All tables created and data inserted successfully.")
conn.close()
