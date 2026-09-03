from .Client import Client
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Books.Book import Book

class PhysicalClient(Client):
    """Физический клиент — может брать любые книги"""

    def can_borrow(self, book: Book) -> bool:
        return True