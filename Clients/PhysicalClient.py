from .Client import Client
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook
from Books.Book import Book

class PhysicalClient(Client):
    """Физический клиент — может брать любые книги"""

    def can_borrow(self, book: Book) -> bool:
        return True