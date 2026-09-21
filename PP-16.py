students = {}
i = 1

while True:
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Edit a Student")
    print("4. Print Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        major = input("Enter your major: ")
        year = input("Enter your year: ")
        students.update({"S" + str(i):{
            "name": name,
            "major": major,
            "year": year}})
        i = i + 1
    elif choice == 2:
        num = input("Digit the number of the student you want to remove: ")
        que = "S" + num
        if que in students:
            students.pop(que)
        else:
            print("Error: Student ID does not exist.")
    elif choice == 3:
        num = input("Digit the number of the student you want to edit: ")
        que = "S" + num
        if que in students:
            newelemet = input("Enter the element you want to edit (name / major / year): ")
            if newelemet in ["name", "major", "year"]:
                val = input("Enter the new value: ")
                students[que][newelemet] = val
                print("Student updated successfully.")
            else:
                print("Error: Invalid field name entered.")
        else:
            print("Error: Student ID not found.")
    elif choice == 4:
        print("\n--- Student Directory ---")
        print(students)

    elif choice == 5:
        print("Thanks for using the program")
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")
