class students:
    def __init__(self, name, grade):
        self.name = name
        self.grade =  grade
    def printStudent(self):
        print('we have a new student named ' + self.name + ' and is in grade ' + str(self.grade))

myStudents = []
myStudents.append(students('Adam', 10))
myStudents.append(students('name', 1))

for i in myStudents:
    i.printStudent()