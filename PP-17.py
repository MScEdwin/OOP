#USER DEFINED FUNCTIONS

def add():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a+b
    print("\nThe sum is:",c)
def sub():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a-b
    print("\nThe difference is:",c)
def mult():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a*b
    print("\nThe product is:",c)
def div():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if b==0:
        print("Cannot divide by zero")
    else:
        c=a/b
        print("\nThe division is:",c)

while True:
    print ("\n1. To make a sum")
    print ("2. To make a rest")
    print ("3. To make a multiplication")
    print ("4. To divide")
    print ("5. To exit")

    choice=int(input("Enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mult()
    elif choice==4:
        div()
    elif choice==5:
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice")


