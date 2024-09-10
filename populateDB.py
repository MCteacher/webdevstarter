import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('uniform_shop.db')
cursor = conn.cursor()

# Delete existing records from all tables
cursor.execute('DELETE FROM Students')
cursor.execute('DELETE FROM Employees')
cursor.execute('DELETE FROM Inventory')
cursor.execute('DELETE FROM Invoices')
cursor.execute('DELETE FROM InvoiceItems')
cursor.execute('DELETE FROM InventoryTypes')
cursor.execute('DELETE FROM Suppliers')

# Insert dummy data into Students table
cursor.executemany('''
    INSERT INTO Students (first_name, surname, year, house, boarder, date_of_entry, date_of_birth, address1, address2, address3, suburb, state, postcode, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('Ada', 'Lovelace', 10, 'Red', True, '2020-01-15', '2005-12-10',
     '123 Main St', '', '', 'Springfield', 'IL', '62701', True),
    ('Grace', 'Hopper', 11, 'Blue', False, '2019-09-01', '2004-12-09',
     '456 Elm St', 'Apt 5', '', 'Springfield', 'IL', '62701', True),
    ('Katherine', 'Johnson', 12, 'Green', False, '2018-01-25', '2003-08-26',
     '789 Oak St', '', '', 'Springfield', 'IL', '62701', True),
    ('Hedy', 'Lamarr', 9, 'Yellow', True, '2021-03-12', '2006-11-09',
     '101 Pine St', '', '', 'Springfield', 'IL', '62701', True),
    ('Radia', 'Perlman', 10, 'Red', True, '2020-02-17', '2005-06-19',
     '202 Cedar St', '', '', 'Springfield', 'IL', '62701', True),
    ('Anita', 'Borg', 11, 'Blue', False, '2019-08-20', '2004-01-17',
     '303 Birch St', '', '', 'Springfield', 'IL', '62701', True),
    ('Margaret', 'Hamilton', 12, 'Green', False, '2018-04-11', '2003-08-17',
     '404 Maple St', '', '', 'Springfield', 'IL', '62701', True),
    ('Barbara', 'Liskov', 9, 'Yellow', True, '2021-06-05', '2006-11-07',
     '505 Walnut St', '', '', 'Springfield', 'IL', '62701', True),
    ('Jean', 'Sammet', 10, 'Red', True, '2020-07-13', '2005-03-23',
     '606 Chestnut St', '', '', 'Springfield', 'IL', '62701', True),
    ('Frances', 'Allen', 11, 'Blue', False, '2019-05-22', '2004-08-04',
     '707 Ash St', '', '', 'Springfield', 'IL', '62701', True),
    ('Carol', 'Shaw', 12, 'Green', False, '2018-09-14', '2003-03-14',
     '808 Poplar St', '', '', 'Springfield', 'IL', '62701', True),
    ('Evelyn', 'Boyd', 9, 'Yellow', True, '2021-10-10', '2006-09-17',
     '909 Cypress St', '', '', 'Springfield', 'IL', '62701', True)
])

# Insert dummy data into Employees table
cursor.executemany('''
    INSERT INTO Employees (first_name, surname, code, category, is_volunteer, is_active)
    VALUES (?, ?, ?, ?, ?, ?)
''', [
    ('Clark', 'Kent', 'E001', 'Shelf Stacker', False, True),
    ('Natasha', 'Romanoff', 'E002', 'Security', False, True),
    ('Diana', 'Prince', 'E003', 'Boss', False, True),
    ('Bruce', 'Wayne', 'E004', 'Dev Humour Manager', False, True),
    ('Tony', 'Stark', 'E005', 'Programmer', False, True),
    ('Bruce', 'Banner', 'E006', 'Cleaner', False, True),
    ('Peter', 'Parker', 'E007', 'Call Operator', False, True)
])

# Insert dummy data into InventoryTypes table
cursor.executemany('''
    INSERT INTO InventoryTypes (name, description)
    VALUES (?, ?)
''', [
    ('Clothing', 'Various types of clothing items'),
    ('Equipment', 'Specialised equipment for various activities'),
    ('Stationery', 'Items used for writing and other office tasks'),
    ('Safety Gear', 'Protective gear for safety purposes')
])

# Insert dummy data into Inventory table
cursor.executemany('''
    INSERT INTO Inventory (name, type_id, description, price, in_stock, shelf_location, image)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('School Blazer', 1, 'Standard school blazer', 75.00, 50, 'A1', None),
    ('Tartan Dress', 1, 'For most of the year', 75.00, 250, 'A1', None),
    ('Tartan Bow', 1, 'For holding back your hair', 75.00, 5000, 'A1', None),
    ('Tartan Tie', 2, 'School tie', 15.00, 100, 'B2', None),
    ('Tartan Armour', 2, 'For students who undertake jousting', 15.00, 100, 'C1', None),
    ('Flamethrower', 1, 'Not for the faint-hearted', 300.00, 5, 'C3', None),
    ('Jetpack', 1, 'For quick getaways', 1200.00, 3, 'D4', None),
    ('Invisibility Cloak', 1, 'Be unseen', 500.00, 7, 'E5', None),
    ('Grappling Hook', 2, 'For scaling walls', 250.00, 20, 'F6', None),
    ('Utility Belt', 2, 'Store all your gadgets', 150.00, 15, 'G7', None),
    ('Shield', 1, 'Defend yourself', 200.00, 10, 'H8', None),
    ('Medkit', 2, 'First aid essentials', 50.00, 40, 'I9', None),
    ('Night Vision Goggles', 1, 'See in the dark', 300.00, 8, 'J10', None),
    ('Laser Cutter', 1, 'Precision cutting tool', 800.00, 4, 'K11', None),
    ('Hoverboard', 1, 'For smooth rides', 600.00, 6, 'L12', None),
    ('Energy Drink', 2, 'Boost your stamina', 5.00, 200, 'M13', None),
    ('Smoke Bomb', 2, 'Create a smokescreen', 20.00, 50, 'N14', None),
    ('EMP Device', 1, 'Disable electronics', 1000.00, 2, 'O15', None)
])

# Insert dummy data into Invoices table
cursor.executemany('''
    INSERT INTO Invoices (purchaser, served_by, date, time)
    VALUES (?, ?, ?, ?)
''', [
    (1, 1, '2024-08-01', '09:30:00'),
    (2, 2, '2024-08-02', '11:45:00'),
    (3, 2, '2024-08-08', '11:40:00'),
    (4, 2, '2024-08-16', '11:34:00')
])

# Insert dummy data into InvoiceItems table
cursor.executemany('''
    INSERT INTO InvoiceItems (invoice_id, item_id, item_name, item_price, item_discount_to, paid, payment_method)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    (1, 1, 'School Blazer', 75.00, None, True, 'Card'),
    (1, 2, 'School Tie', 15.00, None, True, 'Card'),
    (2, 2, 'School Tie', 15.00, 12.00, True, 'Cash'),
    (3, 3, 'Flamethrower', 300.00, 250.00, True, 'Card'),
    (3, 4, 'Safety Goggles', 20.00, None, True, 'Card'),
    (4, 5, 'Backpack', 50.00, 45.00, False, 'Cash'),
    (4, 6, 'Notebook', 5.00, None, False, 'Cash')
])

# Insert dummy data into Suppliers table
cursor.executemany('''
    INSERT INTO Suppliers (name, contact_name, contact_email, contact_phone, address1, address2, suburb, state, postcode)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', [
    ('Stark Industries', 'Tony Stark', 'tony.stark@starkindustries.com',
     '987-654-3210', '10880 Malibu Point', '', 'Malibu', 'CA', '90265'),
    ('Rebel Alliance', 'Leia Organa', 'leia.organa@rebels.com',
     '123-456-789', '534 Hair Bun Way', '', 'Hosnian Prime', 'Alderan', '58271'),
    ('Acme Corporation', 'Wile E. Coyote', 'wile.e.coyote@acmecorp.com',
     '555-123-4567', '123 Desert Road', '', 'Looneyville', 'NM', '87001')
])

# Commit changes and close the connection
conn.commit()
conn.close()
