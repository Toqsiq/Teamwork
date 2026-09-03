from .Client import Client
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.Book import Book

class OnlineClient(Client):
    """Онлайн-клиент — может брать только электронные и аудиокниги"""

    def can_borrow(self, book: Book) -> bool:
        return isinstance(book, (OnlineBook, AudioBook))