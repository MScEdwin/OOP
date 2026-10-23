import random

class Costumer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = 0
        self.credit_card = []

    def create_customer(self):
        self.acc_no = random.randint(100000, 999999)
        self.cid = input("Enter customer account ID: ")
        self.cname = input("Enter customer account name: ")
        self.balance = float(input("Enter customer account balance: "))

    def transfer_founds(self, bene_cust_obj, amount):
        if amount > self.balance:
            print("Insufficient funds. Transfer cancelled.")
        else:
            self.balance -= amount
            bene_cust_obj.balance += amount
            print("Transfer completed.")

    def assign_card (self, card_obj):
        self.credit_card.append(card_obj.card_no)

    def display_costumer(self):
        print("Costumer's name: ", self.cname)
        print("Costumer ID: ",self.cid)
        print("Customer Account Number: ",self.acc_no)
        print("Balance: ",self.balance)
        if len(self.credit_card) == 0:
            print()
        else:
            print(f"Credit Card: {self.credit_card}")
        print()

class Card:
    def __init__(self):
        self.card_no = 0
        self.cvv = 0
        self.expiry_date = ""
        self.balance = 0

    def create_card(self):
        self.card_no = input("Enter card number: ")
        self.cvv = input("Enter cv number: ")
        self.expiry_date = input("Enter expiry date: ")
        self.balance = input("Enter card balance: ")

    def display_card(self):
        print("Card's Number: ", self.card_no)
        print("CVV: ", self.cvv)
        print("Expiry Date: ", self.expiry_date)
        print("Balance: ", self.balance)


MyCustomerList = []
MyCardList = []

while True:
    print("1. Create Customer Object")
    print("2. Create Card Object")
    print("3. Transfer funds between Customers")
    print("4. Assign Card Object to customer object")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        co = Costumer()
        co.create_customer()
        MyCustomerList.append(co)

    elif choice == 2:
        ca = Card()
        ca.create_card()
        MyCardList.append(ca)

    elif choice == 3:
        c= Costumer()
        if len(MyCustomerList) < 2:
            print("You need at least 2 customers to transfer funds.")
        else:
            for i, cos in enumerate(MyCustomerList):
                print(i + 1, cos.cname)
            choice_co = int(input("What Customer do you want to transfer from?: "))
            costu = MyCustomerList[choice_co - 1]

            for h, cost in enumerate(MyCustomerList):
                print(h + 1, cost.cname)
            choice_co2 = int(input("What Customer do you want to transfer to?: "))
            costu2 = MyCustomerList[choice_co2 - 1]

            amount = float(input("How much do you want to transfer?: "))
            costu.transfer_founds(costu2, amount)

    elif choice == 4:
        for f, car in enumerate(MyCardList):
            print(f + 1, car.card_no)
        choice_car = int(input("What card do you want to assign?: "))
        card_chosen = MyCardList[choice_car - 1]

        for j, costu3 in enumerate(MyCustomerList):
            print(j + 1, costu3.cname)
        choice_co3 = int(input("What Customer do you want to assign it to?: "))
        customer_chosen = MyCustomerList[choice_co3 - 1]

        customer_chosen.assign_card(card_chosen)
        print("Card assigned.")

    elif choice == 5:
        c= Costumer()
        for c in MyCustomerList:
            c.display_costumer()

    elif choice == 6:
        for c in MyCardList:
            c.display_card()

    elif choice == 7:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
