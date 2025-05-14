# Library class
from modules.book import Book
from decorators.logger import logger 

class Library:
    def __init__(self) -> None:
        self.books = list()

    def allBooks(self) -> list:
        return self.books

    def availableBooks(self):
        for book in self.books:
            if not book.is_borrowed:
                yield book

    @logger('was added')
    def addBook(self, book: Book) -> None:
        self.books.append(book)

    @logger('was borrowed')
    def borrowBook(self, book: Book) -> None:
        index = self.books.index(book)
        self.books[index].is_borrowed = True

    @logger('was returned')
    def returnBook(self, book: Book) -> None:
        index = self.books.index(book)
        self.books[index].is_borrowed = False

    
