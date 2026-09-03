 # все классы клиентов (наследование)

from abc import ABC, abstractmethod
from Books.Book import Book

#  КЛИЕНТЫ 

class Client(ABC):
    """Базовый класс клиента"""

    def __init__(self, name: str, client_id: str):
        self.name = name
        self.client_id = client_id
        self.borrowed_books = []

    @abstractmethod
    def can_borrow(self, book: Book) -> bool: #тип книги для физ.клиента или для онлайн-клиента
        """Может ли клиент взять эту книгу"""
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.client_id})"
