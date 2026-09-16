list1 = []
while (1):
    print("Digit 1 if you want to insert new elements:")
    print("Digit 2 if you want to replace new elements:")
    print("Digit 3 if you want to delete new elements:")
    print("Digit 4 if you want to sort new elements:")
    print("Digit 5 if you want to sort new elements:")
    print("Digit 6 if you want to exit:")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ques = int(input("How many elements would you like to add? : "))
        for i in range(ques):
            element = int(input("Enter a number: "))
            list1.append(element)

    elif choice ==2:
        old_element = int(input("Enter the element you want to replace: "))
        if old_element in list1:
            new_element = int(input("Enter the new element you want to add: "))
            index = list1.index(old_element)
            list1[index] = new_element
        else:
            print("That element is not in the list.")

    elif choice ==3:
        del_element = int(input("Enter the element you want to delete: "))
        if del_element in list1:
            list1.remove(del_element)
            print("List after deletion:", list1)
        else:
            print("That element is not in the list to delete.")

    elif choice ==4:
        list1.sort()

    elif choice ==5:
        print("\nFinal sorted list:", list1)
        
    elif choice ==6:
        break
