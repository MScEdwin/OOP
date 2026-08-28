number1=int(input("Digit the first number: "))
number2=int(input("Digit the first number: "))
number3=int(input("Digit the first number: "))

if number1>number2 and number1>number3:
    print ("number1 is the biggest")
elif number2 > number1 and number2 > number3:
    print("number2 is the biggest")
elif number3 > number2 and number3 > number1:
    print("number3 is the biggest")
elif number1==number2 and number2>number3:
    print ("number1 and number2 are the biggest")
elif number1 == number3 and number1 > number2:
    print ("number1 and number3 are the biggest")
elif number3 == number2 and number2 > number1:
    print ("number2 and number3 are the biggest")


if number1<number2 and number1<number3:
    print ("number1 is the smallest")
elif number2<number1 and number2<number3:
    print ("number2 is the smallest")
elif number3 < number2 and number3 < number1:
    print("number3 is the smallest")
elif number1==number2 and number2==number3:
    print ("All numbers are equal")
elif number1 == number2 and number2 < number3:
    print("number1 and number2 are the smallest")
elif number1 == number3 and number1 < number2:
    print("number1 and number3 are the smallest")
elif number3 == number2 and number2 < number1:
    print("number2 and number3 are the smallest")


