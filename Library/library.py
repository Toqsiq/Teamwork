# library.py

#  БИБЛИОТЕКА 

from datetime import datetime, timedelta
"""
from Books import Book, OnlineBook, AudioBook, PhysicalBook
from models import Client, OnlineClient, PhysicalClient
"""
"""
from Books.Book import Book
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook
from Clients.Client import Client
from Clients.PhysicalClient import PhysicalClient
from Clients.OnlineClient import OnlineClient
"""
from Library.Books.Book import Book
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Clients.Client import Client
from Library.Clients.PhysicalClient import PhysicalClient
from Library.Clients.OnlineClient import OnlineClient




class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []
        self.clients: list[Client] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_client(self, client: Client):
        self.clients.append(client)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, client: Client, title: str) -> str:
        book = self.find_book(title)

        if book is None:
            return f"Книга «{title}» не найдена в библиотеке"

        if not book.is_available:
            return f"Книга «{title}» сейчас занята"

        if not client.can_borrow(book):
            return f"Клиент {client.name} не может взять книгу этого типа"

        # Выдача книги
        book.is_available = False
        client.borrowed_books.append(book)
        days = book.borrow_days()
        return_date = datetime.now() + timedelta(days=days)

        return (
            f"Книга успешно выдана!\n"
            f"  Клиент: {client.name}\n"
            f"  Книга:  {book.get_info()}\n"
            f"  Вернуть до: {return_date.strftime('%d.%m.%Y')}"
        )
    
    def return_book(self, client: Client, title: str) -> str:
        book = None
        for b in client.borrowed_books:
            if b.title.lower() == title.lower():
                book = b
                break

        if book is None:
            return f"У клиента {client.name} нет книги «{title}»"

        book.is_available = True
        client.borrowed_books.remove(book)
        return f"Книга «{title}» успешно возвращена"



