myEmployee={}
i=1

def addEmployee():
    name=input("Enter the employee's name:")
    basicPay= int(input("Enter the basic pay:"))
    allowence= int(input("Enter the allowence:"))
    deduction= int(input("Enter the deduction:"))
    taxes= int(input("Enter the taxes:"))
    grossPay=basicPay+allowence
    netPay=basicPay-deduction-taxes
    myEmployee.update({"Employee-"+str(i):{"Employee":name,
                                          "BasicPay":basicPay,
                                          "Allowance":allowence,
                                          "Deduction":deduction,
                                          "Taxes":taxes,
                                          "Gross Pay":grossPay,
                                          "NetPay":netPay}})
def delEmployee():
    removeEmployee=int(input("Enter the employee's number:"))
    de= "Employee-"+str(removeEmployee)
    if de in myEmployee:
        myEmployee.pop(de)
    else:
        print("The employee you entered is not in the stack")

def modifyEmployee():
    modiEmployee=int(input("Enter the employee's number:"))
    mo="Employee-"+str(modiEmployee)
    if mo in myEmployee:
        oldelement=int(input("Enter the element you want to modify:\n 1.Name \n 2.Basic Pay \n 3.Alowance \n 4.Deduction \n 5.Taxes \n"))
        if oldelement == 1:
            newelement= input("Enter the the new name: ")
            myEmployee[mo]["Employee"] = newelement
        elif oldelement == 2:
            newelement= int(input("Enter the new Basic Pay: "))
            myEmployee[mo]["BasicPay"] = newelement
        elif oldelement == 3:
            newelement= int(input("Enter the new Allowance: "))
            myEmployee[mo]["Allowance"] = newelement
        elif oldelement == 4:
            newelement= int(input("Enter the new Deduction: "))
            myEmployee[mo]["Deduction"] = newelement
        elif oldelement == 5:
            newelement= int(input("Enter the new Taxes: "))
            myEmployee[mo]["Taxes"] = newelement
        else:
            print("Please enter a valid choice")
    else:
        print("The employee you entered is not in the stack")


def displayEmployee():
    if not myEmployee:
        print("The employee you entered is not in the stack")
    for key, value in myEmployee.items():
        print (f"Employee Number: {key}")
        print (f"Name: {value['Employee']}")
        print (f"Basic Pay: {value['BasicPay']}")
        print (f"Allowance: {value['Allowance']}")
        print (f"Deduction: {value['Deduction']}")
        print (f"Taxes: {value['Taxes']}")
        print (f"Gross Pay:{value["Gross Pay"]}")
        print (f"NetPay:{value["NetPay"]}")



while True:
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Modify Employee")
    print("4. Display Employee")
    print("5. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        addEmployee()
        i=i+1
    elif choice == 2:
        delEmployee()
    elif choice == 3:
        modifyEmployee()

    elif choice == 4:
        displayEmployee()
    elif choice == 5:
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice")
