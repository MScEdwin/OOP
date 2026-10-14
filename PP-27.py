import pickle

class Book_class:
    def __init__(self):
        self.book_id = 0
        self.book_title = ""
        self.author_id = 0
        self.publisher = ""
        self.year_of_publication = 0

    def add_book(self):
        self.book_id = int(input("Enter book ID: "))
        self.book_title = input("Enter book title: ")
        self.author_id = int(input("Enter author ID: "))
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = int(input("Enter year of publication: "))

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of Publication:", self.year_of_publication)


class Author_class:
    def __init__(self):
        self.author_id = 0
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def add_author(self):
        self.author_id = int(input("Enter author ID: "))
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone number: ")
        self.emailid = input("Enter email ID: ")

    def display_author(self):
        print("Author ID:", self.author_id)
        print("Name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.emailid)


class User_class:
    def __init__(self):
        self.user_id = 0
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""

    def add_user(self):
        self.user_id = int(input("Enter user ID: "))
        self.name = input("Enter user name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone number: ")
        self.emailid = input("Enter email ID: ")

    def display_user(self):
        print("--- User Info ---")
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email:", self.emailid)


myBookList = []
myAuthorList = []
myUserList = []

while True:
    print("1. Add a Book")
    print("2. Add a Author")
    print("3. Add a User")
    print("4. Borrow a Book")
    print("5. Display")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        bo = Book_class()
        bo.add_book()
        myBookList.append(bo)

        bookfile1 = open("mybook.dat", "ab")
        pickle.dump(bo, bookfile1)
        bookfile1.close()

    elif choice == 2:
        au = Author_class()
        au.add_author()
        myAuthorList.append(au)

        authorfile1 = open("myauthor.dat", "ab")
        pickle.dump(au, authorfile1)
        authorfile1.close()

    elif choice == 3:
        u = User_class()
        u.add_user()
        myUserList.append(u)

        userfile1 = open("myuser.dat", "ab")
        pickle.dump(u, userfile1)
        userfile1.close()

    elif choice == 4:
        for i, bo in enumerate(myBookList):
            print(i + 1, bo.book_id)
        choice_bo = int(input("Enter choice: "))
        bo = myBookList[choice_bo - 1]


    elif choice == 5:
        print("1. Display Books")
        print("2. Display Authors")
        print("3. Display Users")
        print("4. Display Everything")
        dis_choice = int(input("Enter display choice: "))
        if dis_choice == 1:
            for b in myBookList:
                b.display_book()
                print()
            file3 = open("mybook.dat", "rb")
            while True:
                try:
                    data = pickle.load(file3)
                    print("\nID:", data.book_id)
                    print("Title:", data.book_title)
                    print("Author:", data.author_id)
                    print("Publisher:", data.publisher)
                    print("Year:", data.year_of_publication)
                except (EOFError):
                    break
            file3.close()

        elif dis_choice == 2:
            for a in myAuthorList:
                au=Author_class()
                a.display_author()
                print()

            file3 = open("myauthor.dat", "rb")
            while True:
                try:
                    data = pickle.load(file3)
                    print("\nID:", data.author_id)
                    print("Name:", data.author_name)
                    print("Affiliation:", data.affiliation)
                    print("Country:", data.country)
                    print("Phone:", data.phone)
                    print("email ID:", data.emailid)

                except (EOFError):
                    break
            file3.close()

        elif dis_choice == 3:
            for u in myUserList:
                us = User_class()
                u.display_user()
                print()

                file4 = open("myuser.dat", "rb")
                while True:
                    try:
                        data = pickle.load(file4)
                        print("User ID:", data.user_id)
                        print("Name:", data.name)
                        print("Address:", data.address)
                        print("Phone:", data.phone)
                        print("Email:", data.emailid)

                    except (EOFError):
                        break
                file4.close()

        elif dis_choice == 4:
            for b in myBookList:
                b.display_book()
                print()
            for a in myAuthorList:
                a.display_author()
                print()
            for u in myUserList:
                u.display_user()
                print()
        else:
            print("Invalid choice.")

    elif choice == 6:
        print("Thank you for using this program")
        break
    else:
        print("Invalid choice")
























