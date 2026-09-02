 # все классы книг  (наследование)

from abc import ABC, abstractmethod
from AudioBook import AudioBook
from OnlineBook import OnlineBook
from PhysicalBook import PhysicalBook

#  КНИГИ 

class Book(ABC):
    """Базовый класс для всех книг"""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True  #доступность книги

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
