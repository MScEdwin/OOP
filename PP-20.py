mystudents= {}

def add_student(n):
    sname=input("Enter the student's name:")
    Lab1=int(input("Enter the Lab 1:"))
    Lab2=int(input("Enter the Lab 2:"))
    Lab3=int(input("Enter the Lab 3:"))
    Lab4=int(input("Enter the Lab 4:"))
    Lab5=int(input("Enter the Lab 5:"))
    Total=Lab1+Lab2+Lab3+Lab4+Lab5
    Porcentage=((Total/50)*100)
    Average=((Total/5))

    mystudents.update({"Student"+str(n):{
        "name":sname,
        "Lab1":Lab1,
        "Lab2":Lab2,
        "Lab3":Lab3,
        "Lab4":Lab4,
        "Lab5":Lab5,
        "Total":Total,
        "Porcentage":Porcentage,
        "Average":Average
        }})

def del_student():
    del_S=input("Enter the student you want to delete:")
    if del_S in mystudents:
        del_S="Student"+str(del_S)
        mystudents.pop(del_S)
    else:
        print("The student you entered is not in the stack")
def display_student():
    print (mystudents)

n=1
print ("-------STUDENT GRADES DICTIONARY-------")
while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Student")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student(n)
        n = n+1
    elif choice=="2":
        del_student()
    elif choice=="3":
        display_student()
    elif choice=="4":
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice")
