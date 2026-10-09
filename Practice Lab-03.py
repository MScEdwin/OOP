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
        print("--- Book Info ---")
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
        print("--- Author Info ---")
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


books_list = []
authors_list = []
users_list = []

while True:
    print("1. Add a Book")
    print("2. Add an Author")
    print("3. Add a User")
    print("4. Borrow a book")
    print("5. Display Information")
    print("6. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        book = Book_class()
        book.add_book()
        books_list.append(book)
        print("Book added successfully!")
    elif choice == 2:
        author = Author_class()
        author.add_author()
        authors_list.append(author)
        print("Author added successfully!")
    elif choice == 3:
        user = User_class()
        user.add_user()
        users_list.append(user)
        print("User added successfully!")
    elif choice == 4:
        for i, u in enumerate(users_list):
            print(f"{i + 1}. {u.name}")
        u_choice = int(input("Enter user number: "))
        selected_user = users_list[u_choice - 1]

        print("\nSelect Book to Borrow:")
        for i, b in enumerate(books_list):
            print(f"{i + 1}. {b.book_title}")
        b_choice = int(input("Enter book number: "))
        selected_book = books_list[b_choice - 1]
        selected_user.borrow_book(selected_book)

    elif choice == 5:
        print("\n--- DISPLAY MENU ---")
        print("1. Display all Books")
        print("2. Display all Authors")
        print("3. Display all Users")
        print("4. Display Everything")

        disp_choice = int(input("Enter display choice: "))

        if disp_choice == 1:
            if not books_list:
                print("No books available.")
            for b in books_list:
                b.display_book()
                print()
        elif disp_choice == 2:
            if not authors_list:
                print("No authors available.")
            for a in authors_list:
                a.display_author()
                print()
        elif disp_choice == 3:
            if not users_list:
                print("No users available.")
            for u in users_list:
                u.display_user()
                print()
        elif disp_choice == 4:
            for b in books_list:
                b.display_book()
                print()
            for a in authors_list:
                a.display_author()
                print()
            for u in users_list:
                u.display_user()
                print()
        else:
            print("Invalid display choice.")
    elif choice == 5:
        print("Exiting Library System. ¡Mucho éxito en tu presentación!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
