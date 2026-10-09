print ("Enter the value of a:")
a=int(input())

print ("Enter the value of b:")
b=int(input())
c = a + b

print("The summation of a and b =",c)

elif choice == 4:
        if not users_list or not books_list:
            print("Error: You need at least one user and one book in the system first.")
        else:
            print("\nSelect User:")
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
