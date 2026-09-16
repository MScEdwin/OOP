list1 = []

ques = int(input("How many elements would you like to add? : "))
for i in range(ques):
    element = int(input("Enter a number: "))
    list1.append(element)

print("Current list:", list1)

old_element = int(input("Enter the element you want to replace: "))
if old_element in list1:
    new_element = int(input("Enter the new element you want to add: "))
    index = list1.index(old_element)
    list1[index] = new_element
    print("List after replacement:", list1)
else:
    print("That element is not in the list.")

del_element = int(input("Enter the element you want to delete: "))
if del_element in list1:
    list1.remove(del_element)
    print("List after deletion:", list1)
else:
    print("That element is not in the list to delete.")

list1.sort()
print("\nFinal sorted list:", list1)
