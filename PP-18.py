#Implement all the operation of a Queue using List.

myQueue=[]

def enqueue():
    lon=int(input("Enter how many elements you want to add to the queue:"))
    for i in range(0,lon):
        elem=int(input("Enter the element:"))
        myQueue.append(elem)
def dequeue():
    myQueue.pop(0)
def display_queue():
    print(myQueue)





print("-----QUEUE TABLE-----")
while True:
    print("\n1. Add Element to the end of the queue:")
    print("2. Remove Element from the beginning of the queue:")
    print("3. Display the queue:")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        enqueue()
    if choice==2:
        dequeue()
    if choice==3:
        display_queue()
    if choice==4:
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice")
