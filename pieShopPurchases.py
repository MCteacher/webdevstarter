import sqlite3

# Connect to SQLite database (it will create it if it doesn't exist)
conn = sqlite3.connect("pieShop.db")
cursor = conn.cursor()

# Step 1: Create the purchases table
cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customerId INTEGER NOT NULL,
    productId TEXT NOT NULL,
    purchaseDate TEXT NOT NULL,
    purchaseServedByName TEXT NOT NULL
)
""")

# Step 2: Insert 50 rows of dummy data with specific IDs
dummy_data = [
    (1, 3, 'P001', '11/10/2024', 'Grace Hopper'),
    (2, 10, 'P004', '2/11/2024', 'Dennis Ritchie'),
    (3, 11, 'P003', '18/01/2025', 'Guido van Rossum'),
    (4, 4, 'P005', '21/03/2025', 'Ada Lovelace'),
    (5, 8, 'P007', '14/04/2025', 'Grace Hopper'),
    (6, 5, 'P002', '7/12/2024', 'Dennis Ritchie'),
    (7, 7, 'P006', '8/06/2025', 'Alan Turing'),
    (8, 2, 'P003', '30/09/2024', 'Ada Lovelace'),
    (9, 9, 'P005', '22/05/2025', 'Grace Hopper'),
    (10, 1, 'P007', '19/08/2024', 'Guido van Rossum'),
    (11, 6, 'P002', '29/11/2024', 'Alan Turing'),
    (12, 2, 'P001', '9/01/2025', 'Dennis Ritchie'),
    (13, 1, 'P003', '14/02/2025', 'Guido van Rossum'),
    (14, 4, 'P004', '25/10/2024', 'Grace Hopper'),
    (15, 3, 'P006', '5/03/2025', 'Ada Lovelace'),
    (16, 6, 'P002', '3/07/2025', 'Dennis Ritchie'),
    (17, 3, 'P005', '12/09/2024', 'Alan Turing'),
    (18, 7, 'P003', '1/06/2025', 'Guido van Rossum'),
    (19, 3, 'P007', '10/08/2025', 'Grace Hopper'),
    (20, 7, 'P004', '26/02/2025', 'Dennis Ritchie'),
    (21, 2, 'P001', '4/04/2025', 'Ada Lovelace'),
    (22, 1, 'P002', '16/05/2025', 'Alan Turing'),
    (23, 6, 'P005', '20/12/2024', 'Guido van Rossum'),
    (24, 8, 'P003', '17/03/2025', 'Dennis Ritchie'),
    (25, 3, 'P006', '20/07/2025', 'Grace Hopper'),
    (26, 8, 'P007', '8/11/2024', 'Ada Lovelace'),
    (27, 1, 'P001', '26/01/2025', 'Alan Turing'),
    (28, 1, 'P003', '3/09/2024', 'Grace Hopper'),
    (29, 9, 'P002', '22/04/2025', 'Dennis Ritchie'),
    (30, 6, 'P005', '12/06/2025', 'Guido van Rossum'),
    (31, 6, 'P003', '11/02/2025', 'Ada Lovelace'),
    (32, 3, 'P004', '5/10/2024', 'Grace Hopper'),
    (33, 2, 'P006', '3/08/2025', 'Alan Turing'),
    (34, 6, 'P007', '26/06/2025', 'Dennis Ritchie'),
    (35, 1, 'P001', '21/09/2024', 'Guido van Rossum'),
    (36, 8, 'P002', '2/03/2025', 'Ada Lovelace'),
    (37, 9, 'P003', '14/01/2025', 'Dennis Ritchie'),
    (38, 3, 'P004', '18/11/2024', 'Alan Turing'),
    (39, 8, 'P006', '27/05/2025', 'Grace Hopper'),
    (40, 3, 'P005', '5/04/2025', 'Guido van Rossum'),
    (41, 1, 'P001', '28/10/2024', 'Ada Lovelace'),
    (42, 3, 'P002', '22/02/2025', 'Dennis Ritchie'),
    (43, 3, 'P003', '14/12/2024', 'Grace Hopper'),
    (44, 9, 'P007', '30/07/2025', 'Alan Turing'),
    (45, 7, 'P005', '5/01/2025', 'Guido van Rossum'),
    (46, 1, 'P004', '23/03/2025', 'Grace Hopper'),
    (47, 2, 'P001', '9/09/2024', 'Ada Lovelace'),
    (48, 3, 'P006', '13/08/2025', 'Dennis Ritchie'),
    (49, 1, 'P002', '17/07/2025', 'Alan Turing'),
    (50, 7, 'P003', '18/06/2025', 'Guido van Rossum'),
]

# Use INSERT OR REPLACE to ensure custom IDs work if rerunning
cursor.executemany("""
INSERT OR REPLACE INTO purchases (id, customerId, productId, purchaseDate, purchaseServedByName)
VALUES (?, ?, ?, ?, ?)
""", dummy_data)

# Step 3: Update sqlite_sequence to make sure next AUTOINCREMENT starts from 51
# (Only necessary if we inserted with manual IDs)
cursor.execute("UPDATE sqlite_sequence SET seq = 50 WHERE name = 'purchases'")
# If no record yet exists in sqlite_sequence, insert it
cursor.execute("INSERT OR IGNORE INTO sqlite_sequence (name, seq) VALUES ('purchases', 50)")

# Commit and close
conn.commit()
conn.close()

print("Table created and 50 rows inserted successfully. ID will auto-increment from 51 onward.")
