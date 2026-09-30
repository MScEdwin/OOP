from ctypes.wintypes import SMALL_RECT


class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""

    def new_student(self):
        self.name = input("Enter your name: ")
        self.id = input("Enter your id number: ")
        self.department = input("Enter your department: ")
    def display_student(self):
        print("Name: " + self.name)
        print("ID: " + self.id)
        print("Department: " + self.department)
    def assigne_advisor(self):
        print("Advisor: " + self.department)

class faculty:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""
        self.course = ""

mystudent = []
for i in range (1,5):
    Stu = Student()
    Stu.new_student()
    Stu.display_student()
    mystudent.append(Stu)

print (mystudent)


