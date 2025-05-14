from modules.book import Book
from modules.library import Library

def display_books(books):
    if not books:
        print("No books found.")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book}")

def add_book_ui(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if title and author:
        library.addBook(Book(title, author))
    else:
        print("❌ Invalid input.")

def borrow_book_ui(library):
    available_books = list(library.availableBooks())
    if not available_books:
        print("📕 No available books to borrow.")
        return

    print("\nSelect a book to borrow:")
    display_books(available_books)

    try:
        choice = int(input("Enter the number: "))
        if 1 <= choice <= len(available_books):
            book = available_books[choice - 1]
            library.borrowBook(book)
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def return_book_ui(library):
    borrowed_books = [book for book in library.books if book.is_borrowed]
    if not borrowed_books:
        print("📘 No borrowed books to return.")
        return

    print("\nSelect a book to return:")
    display_books(borrowed_books)

    try:
        choice = int(input("Enter the number: "))
        if 1 <= choice <= len(borrowed_books):
            book = borrowed_books[choice - 1]
            library.returnBook(book)
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. View all books")
        print("2. View available books")
        print("3. Add a new book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n📚 All Books:")
            display_books(library.allBooks())
        elif choice == "2":
            print("\n✅ Available Books:")
            display_books(list(library.availableBooks()))
        elif choice == "3":
            add_book_ui(library)
        elif choice == "4":
            borrow_book_ui(library)
        elif choice == "5":
            return_book_ui(library)
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()