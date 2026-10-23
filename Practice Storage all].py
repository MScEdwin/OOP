import pickle

class PRACTICE:
    def __init__(self):
        self.score = 0
        self.maximum = 0
        self.minimum = 0

    def average(self):
        self.average = (self.maximum + self.minimum) / 2

    def new_practice(self):
        self.score = int(input("Enter your score: "))
        self.maximum = int(input("Enter your maximum score: "))
        self.minimum = int(input("Enter your minimum score: "))

    def display_practice(self):
        print("\nYour score is: ",self.score)
        print("Your maximum is: ",self.maximum)
        print("Your minimum is: ",self.minimum)
        print("Your average is: ",self.average)


class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def add_person(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")


    def display_people(self):
        print("\nYour name is ",self.name)
        print("Your age is ",self.age)



MyPracticeList = []
MyPeopleList = []

while True:
    print("\n---PRACTICE---")
    print("1. New Person")
    print("2. New Practice")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        Pe = Person()
        Pe.add_person()
        MyPracticeList.append(Pe)

        personfile1 = open("mybookperson.dat", "ab")
        pickle.dump(Pe,personfile1)
        personfile1.close()

    elif choice == "2":
        Pe = Person()
        Pr = PRACTICE()
        Pr.new_practice()
        Pr.average()
        MyPracticeList.append(Pr)

        practicefile1 = open("mybookpractice.dat", "ab")
        pickle.dump(Pr, practicefile1)
        practicefile1.close()

    elif choice == "3":
        print ("1. Display Practice")
        print ("2. Display Person")
        print ("3. Display all")
        print ("4. Exit")
        choice2 = input("Enter your choice: ")

        if choice2 == "1":
            practicefile2 = open("mybookpractice.dat", "rb")
            while True:
                try:
                    data = pickle.load(practicefile2)
                    data.display_practice()
                except (EOFError):
                    break
            practicefile2.close()
        elif choice2 == "2":
            personfile2 = open("mybookperson.dat", "rb")
            while True:
                try:
                    data = pickle.load(personfile2)
                    data.display_people()
                except (EOFError):
                    break
            personfile2.close()
        elif choice2 == "3":
            practicefile3 = open("mybookpractice.dat", "rb")
            while True:
                try:
                    data = pickle.load(practicefile3)
                    data.display_practice()
                except (EOFError):
                    break
            practicefile3.close()

            while True:
                personfile3 = open("mybookperson.dat", "rb")
                try:
                    data = pickle.load(personfile3)
                    data.display_people()
                except (EOFError):
                    break
                personfile3.close()
        elif choice2 == "4":
            break

    elif choice == "4":
        break

    else:
        print ("Please enter a valid choice")
