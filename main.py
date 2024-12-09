def display_menu(role):
    print("\nMenu:")
    if role == "Admin":
        print("1. Add Book")
        print("2. Search Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. Exit")
    elif role == "Member":
        print("1. Search Books")
        print("2. Return Book")
        print("3. List Books")
        print("4. Exit")
    choice = input("Enter choice: ")
    return choice

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    # Check if any of the inputs are empty
    if not title.strip():
        print("Book not added. Title is required.")
    elif not author.strip():
        print("Book not added. Author is required.")
    elif not isbn.strip():
        print("Book not added. ISBN is required.")
    else:
        # All inputs are valid
        library.append({'title': title, 'author': author, 'isbn': isbn, 'checked_out': False})
        print("Book added successfully.")


def search_books(library):
    search_query = input("Enter title, isbn, or author to search: ").lower()
    found_books = [book for book in library if search_query in book['title'].lower()
                   or search_query in book['author'].lower()
                   or search_query in book['isbn']]

    if not found_books:  # Check if the list of found books is empty
        print("No books found.")
    else:
        for book in found_books:
            status = "Checked Out" if book['checked_out'] else "Available"
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")


def checkout_book(library):
    isbn = input("Enter ISBN of the book to checkout: ")
    book_found = False  # Flag to track if any book is found with the given ISBN

    for book in library:
        if book['isbn'] == isbn:
            book_found = True
            if not book['checked_out']:
                book['checked_out'] = True
                print("Book checked out successfully.")
            else:
                print("This book is already checked out.")
            break

    if not book_found:  # If no book matches the ISBN after searching the entire library
        print("Book not found with the given ISBN.")


def return_book(library):
    isbn = input("Enter ISBN of the book to return: ")
    found = False
    for book in library:
        if book['isbn'] == isbn:
            found = True
            if book['checked_out']:
                book['checked_out'] = False
                print("Book returned successfully.")
            else:
                print("This book was not checked out.")
            break
    if not found:
        print("No book found with the given ISBN.")

def list_books(library):
    if not library:
        print("No books in the library.")
    else:
        print("\nList of Books:")
        for book in library:
            status = "Checked Out" if book['checked_out'] else "Available"
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")

def login():
    print("Please select your role:")
    print("1. Admin")
    print("2. Member")
    role_choice = input("Enter choice: ")
    if role_choice == '1':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        # For simplicity, using hardcoded credentials
        if username == "admin" and password == "admin123":
            return "Admin"
        else:
            print("Invalid credentials.")
            return None
    elif role_choice == '2':
        username = input("Enter member username: ")
        password = input("Enter member password: ")
        # For simplicity, using hardcoded credentials
        if username == "member" and password == "member123":
            return "Member"
        else:
            print("Invalid credentials.")
            return None
    else:
        print("Invalid role choice.")
        return None

def main():
    print("******Welcome to the The Great Hartland Community Library!******")
    library = [
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565', 'checked_out': False},
        {'title': 'Sapiens: A Brief History of Humankind', 'author': 'Yuval Noah Harari', 'isbn': '9780062316097',
         'checked_out': False},
        {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '9780061120084', 'checked_out': False},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'isbn': '9780316769488', 'checked_out': False},
        {'title': 'Educated', 'author': 'Tara Westover', 'isbn': '9780399590504', 'checked_out': False},
        {'title': 'The Gene: An Intimate History', 'author': 'Siddhartha Mukherjee', 'isbn': '9781476733524',
         'checked_out': False},
        {'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman', 'isbn': '9780374533557',
         'checked_out': False},
        {'title': 'The Odyssey', 'author': 'Homer', 'isbn': '9780143039952', 'checked_out': False},
        {'title': 'Cosmos', 'author': 'Carl Sagan', 'isbn': '9780345539434', 'checked_out': False},
        {'title': 'The Better Angels of Our Nature: Why Violence Has Declined', 'author': 'Steven Pinker',
         'isbn': '9780143122012', 'checked_out': False}
    ]
    role = None
    while role is None:
        role = login()
    while True:
        choice = display_menu(role)
        if role == "Admin":
            if choice == '1':
                add_book(library)
            elif choice == '2':
                search_books(library)
            elif choice == '3':
                checkout_book(library)
            elif choice == '4':
                return_book(library)
            elif choice == '5':
                list_books(library)
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")
        elif role == "Member":
            if choice == '1':
                search_books(library)
            elif choice == '2':
                return_book(library)
            elif choice == '3':
                list_books(library)
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
