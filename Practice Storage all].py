import pickle
import random

class USERS:
    def __init__(self):
        self.id = random.randint(1,1000000)
        self.name = ""
        self.age = ""

    def new_user(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")

    def display_user(self):
        print("USER: ",self.id )
        print("Name: ",self.name)
        print("Age: ",self.age)


MyUserList = []


while True:
    print("\n1. Add user")
    print("2. Display user")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        u = USERS()
        u.new_user()
        MyUserList.append(u)

        file1= open("usertext.dat","ab")
        pickle.dump(u,file1)
        file1.close()

    if choice == 2:
        u = USERS()
        file2 = open("usertext.dat", "rb")
        u.display_user()
        while True:
            try:
                data = pickle.load(file2)
                data.display_user()
                print()
            except EOFError:
                break
        file2.close()

    if choice == 3:
        break