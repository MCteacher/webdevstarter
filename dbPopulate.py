import sqlite3

connie = sqlite3.connect('school.db')

# insert three rows into the students table
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Harry", "Potter", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Hermione", "Granger", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Ron", "Weasley", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Draco", "Malfoy", "Slytherin", 4, "SLY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Luna", "Lovegood", "Ravenclaw", 3, "RAV1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Cedric", "Diggory", "Hufflepuff", 6, "HUF1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Neville", "Longbottom", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Ginny", "Weasley", "Gryffindor", 3, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Fred", "Weasley", "Gryffindor", 6, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("George", "Weasley", "Gryffindor", 6, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Percy", "Weasley", "Gryffindor", 7, "GRY1", "Y")')
connie.execute(
    'INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Cho", "Chang", "Ravenclaw", 5, "RAV1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Seamus", "Finnigan", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Dean", "Thomas", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Parvati", "Patil", "Gryffindor", 4, "GRY1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Padma", "Patil", "Ravenclaw", 4, "RAV1", "Y")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Lavender", "Brown", "Gryffindor", 4, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Colin", "Creevey", "Gryffindor", 3, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Nigel", "Wespurt", "Gryffindor", 1, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Ernie", "Macmillan", "Hufflepuff", 4, "HUF1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Hannah", "Abbott", "Hufflepuff", 4, "HUF1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Justin", "Finch-Fletchley", "Hufflepuff", 4, "HUF1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Susan", "Bones", "Hufflepuff", 5, "HUF1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Zacharias", "Smith", "Hufflepuff", 3, "HUF1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Cormac", "McLaggen", "Gryffindor", 5, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Romilda", "Vane", "Gryffindor", 4, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Katie", "Bell", "Gryffindor", 5, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Angelina", "Johnson", "Gryffindor", 5, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Alicia", "Spinnet", "Gryffindor", 5, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Oliver", "Wood", "Gryffindor", 6, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Lee", "Jordan", "Gryffindor", 6, "GRY1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Penelope", "Clearwater", "Ravenclaw", 7, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Terry", "Boot", "Ravenclaw", 4, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Michael", "Corner", "Ravenclaw", 3, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Anthony", "Goldstein", "Ravenclaw", 4, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Mandy", "Brocklehurst", "Ravenclaw", 1, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Morag", "MacDougal", "Ravenclaw", 1, "RAV1", "N")')
connie.execute('INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Lisa", "Turpin", "Ravenclaw", 1, "RAV1", "N")')
connie.execute(
    'INSERT INTO students(firstName, lastName, house, year, holmeGroup, boarder) VALUES("Su", "Li", "Ravenclaw", 1, "RAV1", "N")')

# insert data into the staff table
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Albus", "Dumbledore", "Headmaster", 1)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Minerva", "McGonagall", "Teacher", 1)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Severus", "Snape", "Teacher", 1)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Alastor", "Moody", "Teacher", 0)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Remus", "Lupin", "Teacher", 0)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Gilderoy", "Lockhart", "Teacher", 0)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Argus", "Filch", "Janitor", 1)')
connie.execute(
    'INSERT INTO staff(firstName, lastName, role, isActive) VALUES("Mrs", "Norris", "Deputy Janitor", 1)')

# insert data into the house table
connie.execute(
    'INSERT INTO house(name, colour, crest) VALUES("Gryffindor", "Red", "Lion")')
connie.execute(
    'INSERT INTO house(name, colour, crest) VALUES("Slytherin", "Green", "Snake")')
connie.execute(
    'INSERT INTO house(name, colour, crest) VALUES("Hufflepuff", "Yellow", "Badger")')
connie.execute(
    'INSERT INTO house(name, colour, crest) VALUES("Ravenclaw", "Blue", "Eagle")')

# insert data into the subjects table (code, name, isActive)
connie.execute(
    'INSERT INTO subjects(code, name, isActive) VALUES("POT", "Potions", 1)')
connie.execute(
    'INSERT INTO subjects(code, name, isActive) VALUES("DADA", "Defence Against the Dark Arts", 1)')
connie.execute(
    'INSERT INTO subjects(code, name, isActive) VALUES("TRA", "Transfiguration",1)')
connie.execute(
    'INSERT INTO subjects(code, name, isActive) VALUES("CHA", "Charms", 1)')


# insert data into the classes table (code, name, year, term, isActive)
connie.execute(
    'INSERT INTO classes(code, name, year, term, isActive) VALUES("POT101", "Potions", 1, 1, 1)')
connie.execute(
    'INSERT INTO classes(code, name, year, term, isActive) VALUES("DADA101", "Defence Against the Dark Arts", 1, 1, 1)')
connie.execute(
    'INSERT INTO classes(code, name, year, term, isActive) VALUES("TRANS101", "Transfiguration", 1, 1, 1)')
connie.execute(
    'INSERT INTO classes(code, name, year, term, isActive) VALUES("CHARM101", "Charms", 1, 1, 1)')
connie.execute(
    'INSERT INTO classes(code, name, year, term, isActive) VALUES("DADA201", "Defence Against the Dark Arts", 1, 1, 1)')

# insert data into the classMembership table (classID, studentID)
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(1, 1)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(1, 2)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(1, 3)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(2, 1)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(2, 2)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(2, 3)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(3, 1)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(3, 2)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(3, 3)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(4, 1)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(4, 2)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(4, 3)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(5, 4)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(5, 5)')
connie.execute('INSERT INTO classMembership(classID, studentID) VALUES(5, 6)')

# insert data into the rooms table (name, capacity, type)
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Dungeon", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Divination Tower", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Classroom 01", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Classroom 02", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Classroom 03", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Classroom 04", 20, "Classroom")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Great Hall", 200, "Dining Hall")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Room of Requirement", 100, "Misc")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Library", 50, "Library")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Quidditch Pitch", 5000, "Sports")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Forbidden Forest", null, "Outdoor Education")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Hospital Wing", 20, "Medical")')
connie.execute(
    'INSERT INTO rooms(name, capacity, type) VALUES("Owlery", 10, "Services")')

connie.execute('INSERT INTO patronus(characterID, animal, learnt) VALUES (1, "Stag", 1)')
connie.execute('INSERT INTO patronus(characterID, animal, learnt) VALUES (2, "Otter", 1)')
connie.execute('INSERT INTO patronus(characterID, animal, learnt) VALUES (3, "Jack Russell Terrier", 1)')
connie.execute('INSERT INTO patronus(characterID, animal, learnt) VALUES (4, "Eagle", 1)')
connie.execute('INSERT INTO patronus(characterID, animal, learnt) VALUES (5, "Hare", 1)')

connie.commit()
