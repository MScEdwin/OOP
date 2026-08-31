number1 = int(input("enter the first number: "))
operator = input("enter your operator   '+ , - , * , / ':")
number2 = int(input("enter the second number: "))

if number2==0:
    print("Please digit another number")
    number2 = int(input("enter the second number: "))

if operator == "+":
    c=number1+number2
    print("The result of the sum is:",c)
elif operator == "-":
    c=number1-number2
    print("The result of the difference is:",c)
elif operator == "*":
    c=number1*number2
    print("The result of the multiplication is:",c)
elif operator == "/":
    c=number1/number2
    print("The result of the division is:",c)
elif operator == "/" and number2==0:
    print("The operation cannot be performed")
else:
    print("The operator is invalid")

