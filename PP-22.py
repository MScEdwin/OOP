class Faculty:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.experience = ""
        self.department = ""
        self.course = ""
        self.student_list = []

    def new_faculty(self):
        self.id = int(input("Enter faculty ID: "))
        self.name = input("Enter faculty name: ")
        self.experience = int(input("Enter years of experience: "))
        self.department = input("Enter department: ")
        self.course = input("Enter course taught: ")

    def enroll_students(self, student_obj):
        self.student_list.append(student_obj)
        print(f"Student {student_obj.name} enrolled under faculty {self.name}")

    def display_faculty(self):
        print("---Faculty info---")
        print("ID:", self.id)
        print("name:", self.name)
        print("experience:", self.experience, "years.")
        print("department:", self.department)
        print("course:", self.course)
        for i in self.student_list:
            print ("Assigned student "+str(i), i.name )

class Students:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.major = ""
        self.department = ""
        self.advisor = ""

    def new_student(self):
        self.name = input("Enter student name: ")
        self.id = int(input("Enter student ID: "))
        self.major = input("Enter major: ")
        self.department = input("Enter department: ")

    def assign_advisor(self, faculty_object):
        self.advisor = faculty_object.name
        print ("The advisor:",faculty_object.name , "Has been assigned to the student", self.name)

    def display_student(self):
        print("---Student info---")
        print("name:", self.name)
        print("ID:", self.id)
        print("department:", self.department)
        if self.advisor:
            print("advisor:", self.advisor.name)
        else:
            print("Advisor: None")

class Course:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.credits = 0
        self.faculty = ""
        self.students = []

    def new_course(self):
        self.name = input("Enter course name: ")
        self.department = input("Enter department: ")
        self.credits = int(input("Enter number of credits: "))

    def faculty_enroll(self, faculty_object):
        self.faculty = faculty_object.name
        print ("The course ", self.name, "Has been assigned to the faculty:", self.faculty)

    def enroll_students(self, student_obj):
        self.students.append(student_obj)
        print("The student ", student_obj.name, "Has been added to the course:", self.name)

    def display_courses(self):
        print("---Course info---")
        print("name:", self.name)
        print("department:", self.department)
        print("credits:", self.credits)
        if self.faculty:
            print("faculty:", self.faculty)
        else :
            print("Faculty: None")
        for f in self.students:
            print ("Students in course"+str(f), f.name )




myStudentsList= []
myFacultyList = []
myCourseList = []
stu = Students()
fac = Faculty()
crs = Course()
while True:
    print ("1. Add a student")
    print ("2. Add a faculty")
    print ("3. Add a course")
    print ("4. Assign a course to a student")
    print ("5. Assign advisor to a Student")
    print ("6. Enroll a student in a Faculty")
    print ("7. Enroll a course in a Faculty")
    print ("8. Display info")
    print ("9. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        stu.new_student()
        myStudentsList.append(stu)
    elif choice == 2:
        fac.new_faculty()
        myFacultyList.append(fac)
    elif choice == 3:
        crs.new_course()
        myCourseList.append(crs)
    elif choice == 4:
        crs.enroll_students(stu)
    elif choice == 5:
        stu.assign_advisor(fac)
    elif choice == 6:
        crs.faculty_enroll(fac)
    elif choice == 7:
        crs.enroll_students(stu)
    elif choice == 8:
        print ("1. Display Students")
        print ("2. Display Faculty")
        print ("3. Display Courses")
        print ("4. Display all info")
        choice2= int(input("Enter your choice: "))
        if choice2 == 1:
            stu.display_student()
        elif choice2 == 2:
            fac.display_faculty()
        elif choice2 == 3:
            crs.display_courses()
        elif choice2 == 4:
            for s in myStudentsList:
                s.display_student()
            for f in myFacultyList:
                f.display_faculty()
            for c in myCourseList:
                c.display_course()
        else:
            print ("Invalid choice")
    elif choice == 9:
        print ("Thanks for using the program")
    else:
        print ("Please enter a valid choice")





