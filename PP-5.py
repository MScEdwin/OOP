name=input("Enter your name: ")
grade1=float(input("Enter your grade of Programming: "))
grade2=float(input("Enter your grade of Introduction to Cybersecurity: "))
grade3=float(input("Enter your grade of Gateway: "))

total= (grade1+grade2+grade3)/3

if total < 60:
    print("The Student:",name,"'s Grade is F")
if total >= 60 and total < 65:
    print("The Student:",name,"'s Grade is E")
elif total >= 65 and total < 70:
    print("The Student:",name,"'s Grade is D")
elif total >= 70 and total < 80:
    print("The Student:",name,"'s Grade is C")
elif total >= 80 and total < 90:
    print("The Student:",name,"'s Grade is B")
elif total >= 90 and total < 94:
    print("The Student:",name,"'s Grade is A")
elif total >= 94 and total < 100:
    print("The Student:",name,"'s Grade is A+")
