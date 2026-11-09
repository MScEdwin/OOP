import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="StudentMaster"
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE StudentMaster")
print("Database created successfully!")
mydb.close()

class StudentMaster:
    def __init__(self):
        self.stu_id = 0
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_cgpa = ""

    def enroll_student(self):
        self.stu_id = input("Enter student ID: ")
        self.stu_name = input("Enter student name: ")
        self.stu_major = input("Enter major: ")
        self.stu_courses = input("Enter course: ")
        self.stu_cgpa = input("Enter GPA: ")

class FacultyMaster:
    def __init__(self):
        self.fac_id = 0
        self.fac_name = ""
        self.fac_department = ""
        self.fac_teaches_courses = ""

    def enroll_faculty(self):
        self.fac_id = input("Enter faculty ID: ")
        self.fac_name = input("Enter faculty name: ")
        self.fac_department = input("Enter faculty department: ")
        self.fac_teaches_courses = input("Enter faculty teaches courses: ")


studentMasterList = []
facultyMasterList = []

while True:
    print("1. Enroll Faculty")
    print("2. Enroll Student")
    print("3. Display Faculty")
    print("4. Display Student")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        fm = FacultyMaster()
        fm.enroll_faculty()
    elif choice == 2:
        sm = StudentMaster()
        sm.enroll_student()
    elif choice == 5:
        break

