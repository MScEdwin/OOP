mycourses = {}
while True:
    print("1. Insert new elements")
    print("2. Replace an element")
    print("3. Delete an element")
    print("4. Print elements")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        ques = int(input("How many elements would you like to add? "))
        for i in range(ques):
            key = input("Enter course code/key (e.g., CS101): ")
            coursename = input("Enter course name: ")
            mycourses[key] = coursename
    elif choice == 2:
        key = input("Enter the course code/key you want to replace: ")
        if key in mycourses:
            new_coursename = input("Enter the new course name: ")
            mycourses[key] = new_coursename
            print("Course updated successfully.")
        else:
            print("Error: Course key not found.")
    elif choice == 3:
        key = input("Enter the course code/key you want to delete: ")
        if key in mycourses:
            mycourses.pop(key)
            print("Course deleted successfully.")
        else:
            print("Error: Course key not found.")
    elif choice == 4:
        print(mycourses)
    elif choice == 5:
        print("Thank you for using this program")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
