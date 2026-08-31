 # все классы книг и клиентов (наследование)

from abc import ABC, abstractmethod

# ====================== КНИГИ ======================

class Book(ABC):
    """Базовый класс для всех книг"""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    @abstractmethod
    def get_info(self) -> str:
        """Информация о книге (разный формат у разных типов)"""
        pass

    @abstractmethod
    def borrow_days(self) -> int:
        """Сколько дней можно держать книгу"""
        pass

    def __str__(self):
        status = "доступна" if self.is_available else "занята"
        return f"«{self.title}» — {self.author} ({self.year}) [{status}]"


class OnlineBook(Book):
    """Онлайн-книга (электронная)"""

    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def get_info(self) -> str:
        return f"Онлайн-книга: «{self.title}» ({self.file_size_mb} МБ)"

    def borrow_days(self) -> int:
        return 14


class AudioBook(Book):
    """Аудиокнига"""

    def __init__(self, title: str, author: str, year: int, duration_hours: float):
        super().__init__(title, author, year)
        self.duration_hours = duration_hours

    def get_info(self) -> str:
        return f"Аудиокнига: «{self.title}» ({self.duration_hours} ч.)"

    def borrow_days(self) -> int:
        return 10


class PhysicalBook(Book):
    """Физическая (бумажная) книга"""

    def __init__(self, title: str, author: str, year: int, pages: int, shelf: str):
        super().__init__(title, author, year)
        self.pages = pages
        self.shelf = shelf

    def get_info(self) -> str:
        return f"Физическая книга: «{self.title}», {self.pages} стр., полка {self.shelf}"

    def borrow_days(self) -> int:
        return 21


# ====================== КЛИЕНТЫ ======================

class Client(ABC):
    """Базовый класс клиента"""

    def __init__(self, name: str, client_id: str):
        self.name = name
        self.client_id = client_id
        self.borrowed_books = []

    @abstractmethod
    def can_borrow(self, book: Book) -> bool:
        """Может ли клиент взять эту книгу"""
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.client_id})"


class OnlineClient(Client):
    """Онлайн-клиент — может брать только электронные и аудиокниги"""

    def can_borrow(self, book: Book) -> bool:
        return isinstance(book, (OnlineBook, AudioBook))


class PhysicalClient(Client):
    """Физический клиент — может брать любые книги"""

    def can_borrow(self, book: Book) -> bool:
        return True