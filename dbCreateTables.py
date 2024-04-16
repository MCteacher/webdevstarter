import sqlite3

connie = sqlite3.connect('school.db')

# create a table for students, with id, firstname, lastName
connie.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstName TEXT,
               lastName TEXT, 
               house TEXT,
               year INTEGER,
               holmeGroup TEXT,
               boarder TEXT
               )
               ''')

connie.execute('''
                CREATE TABLE IF NOT EXISTS staff(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT,
                lastName TEXT,
                role TEXT,
                isActive INTEGER
                )
        ''')

connie.execute('''
            CREATE TABLE IF NOT EXISTS house(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            colour TEXT,
            crest TEXT
            )
''')

connie.execute('''
                CREATE TABLE IF NOT EXISTS terms(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                displayName TEXT,
                isActive INTEGER
                )
               ''')

connie.execute('''
                CREATE TABLE IF NOT EXISTS subjects(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT,
                name TEXT, 
                isActive INTEGER
                )               
               ''')

connie.execute('''
                CREATE TABLE IF NOT EXISTS classes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT,
                name TEXT,
                year INTEGER,
                term INTEGER,
                isActive INTEGER
                )
                ''')

connie.execute('''
                CREATE TABLE IF NOT EXISTS classMembership(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                classID INTEGER,
                studentID INTEGER
                )
            ''')

connie.execute('''
            CREATE TABLE IF NOT EXISTS rooms(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                capacity INTEGER,
                type TEXT
                )
            ''')
