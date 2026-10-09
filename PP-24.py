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
            print("advisor:", self.advisor)
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
        stu = Students()
        stu.new_student()
        myStudentsList.append(stu)
    elif choice == 2:
        fac = Faculty()
        fac.new_faculty()
        myFacultyList.append(fac)
    elif choice == 3:
        crs = Course()
        crs.new_course()
        myCourseList.append(crs)
    elif choice == 4:
        if not myStudentsList or not myFacultyList:
            print("Create a student and faculty first.")
        else:
            print("Select student:")
            for i, stu in enumerate(myStudentsList):
                print(i + 1, stu.name)

            student_choice = int(input("Enter student number: "))
            stu = myStudentsList[student_choice - 1]

            print("Select advisor:")
            for i, fac in enumerate(myFacultyList):
                print(i + 1, fac.name)
            faculty_choice = int(input("Enter faculty number: "))
            fac = myFacultyList[faculty_choice - 1]
            stu.assign_advisor(fac)

    elif choice == 5:
        if not myStudentsList or not myCourseList:
            print("Create a student and course first.")
        else:
            print("Select student:")
            for i, stu in enumerate(myStudentsList):
                print(i + 1, stu.name)

            student_choice = int(input("Enter student number: "))
            stu = myStudentsList[student_choice - 1]

            print("Select course:")
            for i, crs in enumerate(myCourseList):
                print(i + 1, crs.name)

            course_choice = int(input("Enter course number: "))
            crs = myCourseList[course_choice - 1]

            crs.register_students(stu)

    elif choice == 6:
        if not myCourseList or not myFacultyList:
            print("Create a course and faculty first.")
        else:
            print("Select course:")
            for i, crs in enumerate(myCourseList):
                print(i + 1, crs.name)

            course_choice = int(input("Enter course number: "))
            crs = myCourseList[course_choice - 1]

            print("Select faculty:")
            for i, fac in enumerate(myFacultyList):
                print(i + 1, fac.name)

            faculty_choice = int(input("Enter faculty number: "))
            fac = myFacultyList[faculty_choice - 1]

            crs.assign_faculty(fac)
    elif choice == 7:
        print("DISPLAY MENU")
        print("1.Display Students")
        print("2.Display Faculty")
        print("3.Display Courses")
        print("4.Display all info")

        choice2 = int(input("Enter choice: "))
        if choice2 == 1:
            for stu in myStudentsList:
                stu.display_student()
        elif choice2 == 2:
            for fac in myFacultyList:
                fac.display_faculty()
        elif choice2 == 3:
            for crs in myCourseList:
                crs.display_course()
        elif choice2 == 4:
            for stu in myStudentsList:
                stu.display_student()
            for fac in myFacultyList:
                fac.display_faculty()
            for crs in myCourseList:
                crs.display_course()
        else:
            print("Invalid choice.")
    elif choice == 9:
        print ("Thanks for using the program")
    else:
        print ("Please enter a valid choice")




#stu = Students()
#stu.new_student()
#myStudentsList.append(stu)

#fac = Faculty()
#fac.new_faculty()
#myFacultyList.append(fac)

#crs = Course()
#crs.new_course()
#myCourseList.append(crs)

#stu.assign_advisor(fac)
#fac.enroll_students(stu)
#crs.faculty_enroll(fac)
#crs.enroll_students(stu)

#print("5.Display info")
#stu.display_student()
#fac.display_faculty()
#crs.display_courses()
