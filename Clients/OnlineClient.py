from .Client import Client
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.Book import Book

class OnlineClient(Client):
    """Онлайн-клиент — может брать только электронные и аудиокниги"""

    def can_borrow(self, book: Book) -> bool:
        return isinstance(book, (OnlineBook, AudioBook))