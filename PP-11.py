list1=[]

print("Digil 1 if you want to add an element")
print("Digil 2 if you want to remove an element")
print("Digil 3 if you want to replace an element")
print("Digit 4 if you want to sort the list")
print("Digil 5 if you want to see the list")


if choice==1:
    ques=int(input("How many elements would you like to add? : "))
    for i in range (0,ques):
        element=int(input("Enter a number: "))
        list1.append(element)
if choice==2:
    old_elemet=int(input("Enter the element you want to delete: "))
    if old_elemet in list1:
        index1=list1.index(old_elemet)
        element=int(input("Enter the new element you want to add: "))
if choice==3:
    ques=int(input("How many element would you like to replace? : "))
    for i in range (0,ques):
        element=int(input("Enter an element to replace: "))
        list1.pop(i)
        list1.insert(i,element)
if choice==4:
    list1.sort()
if choice==5:
    print(list1)










index = list1.index(old_elemenet)
while index < len(list1):
    print(list1[index])
    index+=1


