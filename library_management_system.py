import csv

books = []


def load_books():
    try:
        with open("books.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 4:
                    continue
                books.append({
                    "id": row[0],
                    "name": row[1],
                    "author": row[2],
                    "status": row[3]
                })
    except FileNotFoundError:
        pass


def save_book(book):
    with open("books.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book["id"], book["name"], book["author"], book["status"]])


def save_all_books():
    with open("books.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow([book["id"], book["name"], book["author"], book["status"]])


def add_book():
    book_id = input("Enter Book ID: ").strip()
    book_name = input("Enter Book Name: ").strip()
    author = input("Enter Author Name: ").strip()

    if not book_id or not book_name or not author:
        print("All fields are required!")
        return

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    book = {"id": book_id, "name": book_name, "author": author, "status": "Available"}
    books.append(book)
    save_book(book)
    print("Book Added Successfully!")


def view_books():
    if not books:
        print("No Books Found!")
        return
    print("\n========== Library Books ==========")
    for i, book in enumerate(books, start=1):
        print(f'{i} - ID: {book["id"]} | Name: {book["name"]} | Author: {book["author"]} | Status: {book["status"]}')
    print(f"\nTotal Books: {len(books)}")


def search_book():
    if not books:
        print("No Books Found!")
        return
    search = input("Enter Book ID, Name or Author: ").strip().lower()
    if not search:
        print("Search field cannot be empty!")
        return
    for book in books:
        if search in (book["id"].lower(), book["name"].lower(), book["author"].lower()):
            print("\nBook Found")
            print(book)
            return
    print("Book Not Found!")


def issue_book():
    if not books:
        print("No Books Found!")
        return
    book_id = input("Enter Book ID To Issue: ").strip()
    if not book_id:
        print("Book ID cannot be empty!")
        return
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                print("Book is already issued!")
                return
            book["status"] = "Issued"
            save_all_books()
            print("Book Issued Successfully!")
            return
    print("Book Not Found!")


def return_book():
    if not books:
        print("No Books Found!")
        return
    book_id = input("Enter Book ID To Return: ").strip()
    if not book_id:
        print("Book ID cannot be empty!")
        return
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                print("Book is already available!")
                return
            book["status"] = "Available"
            save_all_books()
            print("Book Returned Successfully!")
            return
    print("Book Not Found!")


load_books()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Good Bye!")
        break
    else:
        print("Invalid Choice!")
