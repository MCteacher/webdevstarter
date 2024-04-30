import sqlite3

connie = sqlite3.connect('school.db')

# create a cursor
cursor = connie.cursor()

cursor.execute('''
               SELECT classID, COUNT(studentID),
               classes.name
               FROM classMembership
               JOIN classes ON classMembership.classID = classes.id
               GROUP BY classMembership.classID
               ''')

# fetch the data
rows = cursor.fetchall()

for row in rows:
    print(row)
