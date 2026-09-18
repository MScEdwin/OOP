students={}
i=1

while (1):
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Edit a Student")
    print("4. Print Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name=input("Enter your name: ")
        major=input("Enter your major: ")
        year=input("Enter your year: ")
        students.update({"S"+str(i):{"name":name,
                                "major":major,
                                "year":year}})
    if choice == 2:
        que="S"+str(input("Digit the number of the student you want to remove: "))
        students.pop(que)
    if choice == 3:
        que = "S" + str(input("Digit the number of the student you want to edit: "))
        if que in students:
            newelemet=input("Enter the new element of the student you want to edit(Name / Major / Year): ")
            Val=input("Enter the new element of the student you want to change: ")
            students.update{que:{newelemet:val}
    if choice == 4:
        print(students)
    if choice == 5:
        break
    i=i+1