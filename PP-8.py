a=0
b=0
c=0
choice=0
x=0

while (1):
    print("Select 1 for Addition")
    print("Select 2 for Subtraction")
    print("Select 3 for Multiplication")
    print("Select 4 for Division")
    print("Select 5 for Exit")
    choice=int(input("Enter your choice:"))

    if choice==5:
        print("Thank you for using this program")
        break
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    if choice==1:
        c=a + b
        print("The sum is: ",c)
    elif choice==2:
        c = a - b
        print("The rest is: ", c)
    elif choice==3:
        c=a * b
        print("The mult is: ",c)
    elif choice==4:
        c=a / b
        print("The division is: ",c)
    else:
        choice= int(input("Please digit a number from 1 - 5:"))

    choice=input("Do you want to continue?(y/n):")
    if choice=="n":
        print("Thank you for using this program")
        break


