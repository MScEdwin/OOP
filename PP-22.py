class Faculty:
    def __init__(self):
        self.teacher = ""
        self.id = ""
        
    def new_faculty(self):
        self.advisor = input("Enter your teacher: ")
        self.id = input("Enter your id: ")

    def enroll(self):
        self.name = input("Enter your name: ")
        self.id = input("Enter your id number: ")

class Student:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""
        self.major = ""

    def new_student(self):
        self.name = input("Enter your name: ")
        self.id = input("Enter your id number: ")
        self.department = input("Enter your department: ")
        self.major = input("Enter your major: ")

    def assign_advisor(self):



    def display_student(self):
        print("Name: " + self.name)
        print("ID: " + self.id)
        print("Department: " + self.department)



class Courses:
    def __init__(self):
        self.course = ""

    def new_course(self):
        self.course = input("Enter your course: ")

    def assign_faculty(self):

    def register_student(self):









mystudent = []
myfaculty = []
mycourses = []

fa=int(input("How many faculties do you want to create"))
for i in range(fa):
    fac = Faculty()
    fac.new_faculty()
    myfaculty.append(fac)

st=int(input("How many students do you want to create"))
for i in range(st):
    stu = Student()
    stu.new_student()
    faculty_id=int(input("Enter the faculty id number: "))
    if faculty_id in myfaculty:
        stu.assign_advisor(faculty_id)
        mystudent.append(stu)
    else:
        break

co=int(input("How many courses do you want to create"))
for i in range(co):
    cou = Courses()
    cou.new_course()
    faculty_id=int(input("Enter the faculty id number: "))
    if faculty_id in myfaculty:
        cou.assign_faculty(faculty_id)
        mystudent.append(cou)
    else:
        print("Does not exist")
    student_id=int(input("Enter the student id number: "))
    if student_id in mystudent:
        cou.register_student(student_id)
        mycourses.append(cou)
    else:
        print("Does not exist")




