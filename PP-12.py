list1=[]
ques=int(input("How many elements would you like to add? : "))
for i in range (0,ques):
    element=int(input("Enter a number: "))
    list1.append(element)

old_element=int(input("Enter the element you want to delete: "))
list1.remove(old_element)

ques=int(input("How many element would you like to replace? : "))
if old_element in list1:
    element = int(input("Enter the new element you want to add: "))
    index=0
    for i in list1:
        if i==old_element:
            break
        else:
            index= index+1
            element=int(input("Enter an element to replace: "))
        mylist
        list1.pop(i)
        list1.insert(i,element)

list1.sort()

print(list1)
