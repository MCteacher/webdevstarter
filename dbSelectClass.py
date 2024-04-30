import sqlite3

connie = sqlite3.connect('school.db')

# create a cursor
cursor = connie.cursor()

cursor.execute('''
               SELECT classID, studentID,
               classes.name, 
               students.firstName, students.lastName, students.house
               FROM classMembership
               JOIN classes ON classMembership.classID = classes.id
               JOIN students ON classMembership.studentID = students.id
               ''')

# fetch the data
rows = cursor.fetchall()

for row in rows:
    print(row)
