from xml.dom.minidom import ProcessingInstruction

print("Digit employee's name: ")
name= input()

print("Digit your basic Pay: ")
a= int(input())

print("Digit the deductions of your pay: ")
b= int(input())

r=a-b
print("Employee: ",name)
print("Total Pay: ",r)


