class Student:
    def __init__(self, name, times):
        self.name = name
        self.time = times

    def getName(self):
        return self.name

    def getTime(self):
        return self.time


class Class:
    students = []

    def __int__(self):
        self.students = []

    def addStudent(self, theStudent):
        self.students.append(theStudent)

    def findStudent(self, name):
        find = False
        for theStudent in self.students:
            if theStudent.getName() == name:
                find = True
                if theStudent.getTime() < 10:
                    print("0", end="")
                if theStudent.getTime() < 100:
                    print("0", end="")
                if theStudent.getTime() < 1000:
                    print("0", end="")
                print(theStudent.getTime())
        if not find:
            print('9999')

    def checkStudent(self, times):
        find = 0
        for STUDENT in self.students:
            if STUDENT.getTime() <= times:
                find = find + 1
        print(find)


theClass = Class()
n = int(input())
theDate = []
for i in range(n):
    temp = input().split(" ")
    theDate.append(temp)

for i in theDate:
    if i[0] == '1':
        student = Student(i[1], int(i[2]))
        theClass.addStudent(student)
    if i[0] == '2':
        theClass.findStudent(i[1])
    if i[0] == '3':
        theClass.checkStudent(int(i[2]))
