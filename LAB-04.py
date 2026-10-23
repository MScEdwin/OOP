class Costumer:
    def __init__(self, name, cost):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = 0
        self.credit_card = []

    def create_customer(self):
        self.acc_no = input("Enter customer account number: ")
        self.cid = input("Enter customer account ID: ")
        self.cname = input("Enter customer account name: ")
        self.balance = input("Enter customer account balance: ")
        self.credit_card = input("Enter customer account credit card: ")

    def transfer_founds(self, bene_cust_obj, amount):
        self.balance -= amount
        bene_cust_obj.balance += amount

    def assign_card (self, card_obj):
        self.credit_card.append(card_obj.card_no)

    def display_costumer(self):
        print("Costumer's name: ", self.cname)
        print("Costumer ID: ",self.cid)
        print("Customer Account Number: ",self.acc_no)
        print("Balance: ",self.balance)
        if self.credit_card not in MyCostumerList:
            print()
        else:
            print("Credit Card: ",self.credit_card)

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


MyCostumerList = []
MyCardList = []

while True:
    print ("1. Create Customer Object")
    print ("2. Create Card Object")
    print ("3. Transfer founds between Customers")
    print ("4. Assign Card Object to customer object")
    print ("5. Display Costumer Info")
    print ("6. Display Card Info")
    print ("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        co=Costumer()
        co.create_customer()
        MyCostumerList.append(co)

    if choice == 2:
        ca=Card()
        ca.create_card()
        MyCostumerList.append(ca)

    if choice == 3:
        co=Costumer()
        for i, cos in enumerate(MyCostumerList):
            print (i + 1, cos.cname)
        choice_co = int(input("What Costumer you want to transfer from?: "))
        costu = MyCostumerList[choice_co + 1]

        for h, cost in enumerate(MyCostumerList):
            print (h + 1, costu.cname)
        choice_co2 = int(input("What Costumer you want to transfer to?: "))
        costu2 = MyCostumerList[choice_co2 + 1]

        amount = int(input("How much do you want to transfer?: "))
        costu.transfer_founds(costu2, amount)

    if choice == 4:
        for f, car in enumerate(MyCardList):
            print (f + 1, car.card_no)
        choice_car = int(input("What card you want to assign?: "))
        for j, costu3 in enumerate(MyCostumerList):
            print (j + 1, costu3.name)
        choice_co3 = int(input("What Costumer you want to assign?: "))
        choice_co3.assign_card(choice_car)

        costu = MyCostumerList[choice_co + 1]