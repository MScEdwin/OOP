import pickle

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
        print("\nName: " + self.name)
        print("ID: " + self.id)
        print("Department: " + self.department)

s1 = Student()
s1.new_student()
s1.display_student()

file1= open("Student.dat","wb")
pickle.dump(s1,file1)
file1.close()

file2 = open("Student.dat","rb")
while True:
    try:
        data = pickle.load(file2)
        print("\nName:", data.name)
        print("ID:", data.id)
        print("Department:", data.department)
    except (EOFError):
        break
file2.close()
