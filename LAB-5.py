import mysql.connector
def get_connection():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS StudentMaster")
    cursor.execute("USE StudentMaster")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student_Master (
            stu_id      INT PRIMARY KEY,
            stu_name    VARCHAR(100),
            stu_major   VARCHAR(100),
            stu_courses VARCHAR(255),
            stu_cgpa    DECIMAL(3,2)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Faculty_Master (
            fac_id              INT PRIMARY KEY,
            fac_name            VARCHAR(100),
            fac_department      VARCHAR(100),
            fac_teaches_courses VARCHAR(255)
        )
    """)
    conn.commit()
    cursor.close()
    return conn


class StudentMaster:
    def __init__(self):
        self.stu_id = 0
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_cgpa = ""

    def enroll_student(self):
        self.stu_id = int(input("Enter student ID: "))
        self.stu_name = input("Enter student name: ")
        self.stu_major = input("Enter major: ")
        self.stu_courses = input("Enter courses (comma separated): ")
        self.stu_cgpa = float(input("Enter CGPA: "))

    def save(self, conn):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Student_Master VALUES (%s, %s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE stu_name=VALUES(stu_name), stu_major=VALUES(stu_major), "
            "stu_courses=VALUES(stu_courses), stu_cgpa=VALUES(stu_cgpa)",
            (self.stu_id, self.stu_name, self.stu_major, self.stu_courses, self.stu_cgpa),
        )
        conn.commit()
        cur.close()


class FacultyMaster:
    def __init__(self, fac_id=0, fac_name="", fac_department="", fac_teaches_courses=""):
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.fac_department = fac_department
        self.fac_teaches_courses = fac_teaches_courses

    def enroll_faculty(self):
        self.fac_id = int(input("Enter faculty ID: "))
        self.fac_name = input("Enter faculty name: ")
        self.fac_department = input("Enter department: ")
        self.fac_teaches_courses = input("Enter courses taught (comma separated): ")

    def save(self, conn):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Faculty_Master VALUES (%s, %s, %s, %s) "
            "ON DUPLICATE KEY UPDATE fac_name=VALUES(fac_name), fac_department=VALUES(fac_department), "
            "fac_teaches_courses=VALUES(fac_teaches_courses)",
            (self.fac_id, self.fac_name, self.fac_department, self.fac_teaches_courses),
        )
        conn.commit()
        cur.close()


def display_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student_Master")
    rows = cur.fetchall()
    print("\n--- STUDENTS ---")
    if not rows:
        print("No students found.")
    for r in rows:
        s = StudentMaster(*r)
        print(f"ID: {s.stu_id} | Name: {s.stu_name} | Major: {s.stu_major} | "
              f"Courses: {s.stu_courses} | CGPA: {s.stu_cgpa}")
    print()
    cur.close()


def display_faculty(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Faculty_Master")
    rows = cur.fetchall()
    print("\n--- FACULTY ---")
    if not rows:
        print("No faculty found.")
    for r in rows:
        f = FacultyMaster(*r)
        print(f"ID: {f.fac_id} | Name: {f.fac_name} | Department: {f.fac_department} | "
              f"Teaches: {f.fac_teaches_courses}")
    print()
    cur.close()


def main():
    conn = get_connection()
    print("Connected. Database and tables are ready.\n")

    while True:
        print("1. Enroll Faculty")
        print("2. Enroll Student")
        print("3. Display Faculty")
        print("4. Display Students")
        print("5. Load 5 sample students and 5 sample faculty")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            fm = FacultyMaster()
            fm.enroll_faculty()
            fm.save(conn)
            print("Faculty saved.\n")
        elif choice == 2:
            sm = StudentMaster()
            sm.enroll_student()
            sm.save(conn)
            print("Student saved.\n")
        elif choice == 3:
            display_faculty(conn)
        elif choice == 4:
            display_students(conn)
        elif choice == 5:
            load_sample_data(conn)
        elif choice == 6:
            break
        else:
            print("Invalid choice.\n")

    conn.close()
    print("Goodbye!")


if __name__ == "__main__":
    main()
