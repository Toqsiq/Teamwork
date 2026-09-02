from abc import ABC, abstractmethod

class OnlineClient(Client):
    """Онлайн-клиент — может брать только электронные и аудиокниги"""

    def can_borrow(self, book: Book) -> bool:
        return isinstance(book, (OnlineBook, AudioBook))