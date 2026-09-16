myDictionary= {"name1":"Edwin",     #Syntax mydictionary={key,value}
               "name2":"Justus",
               "name3":"Maria"}
print(myDictionary)
print(myDictionary["name1"])

myDictionary.update({"name4":"Justin", "name5":"Josh"})     #Add elements
print(myDictionary)

del myDictionary["name2"]    #Remove elements, Selecting the Key
print(myDictionary)

myDictionary["name4"]= "Marta"     #Remplace select the key and change it directly
print(myDictionary)



fullname= input("Enter your full name : ")
myDictionary.update({"name5":fullname})
print(myDictionary)




