#Implement all the operation of a Stack using List.

mystack=[]

def pushbook():
    lon=int(input("Enter how many elements you want to add to the queue:"))
    for i in range(0,lon):
        elem=int(input("Enter the element:"))
        mystack.insert(0,elem)
def popbook():
    lent= len(mystack)
    mystack.pop(lent-1)
def display_book():
    print(mystack)





print("-----QUEUE TABLE-----")
while True:
    print("\n1. Add Element to the beginning of the stack:")
    print("2. Remove Element from the end of the stack:")
    print("3. Display the stack:")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        pushbook()
    if choice==2:
        popbook()
    if choice==3:
        display_book()
    if choice==4:
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice")