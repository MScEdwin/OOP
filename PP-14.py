mycourses = {}
while (1):
    print("Digit 1 if you want to insert new elements:")
    print("Digit 2 if you want to replace new elements:")
    print("Digit 3 if you want to delete new elements:")
    print("Digit 4 if you want to print elements:")
    print("Digit 4 if you want to exit:")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ques= int(input("How many elements would you like to add? "))
        for i in range (0,ques):
            name = "c_name",i
            cousename= input("Enter course name: ")
            mycourses.update({name:cousename})
    print(mycourses)
