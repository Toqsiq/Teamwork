from abc import ABC, abstractmethod

class AudioBook(Book):
    """Аудиокнига"""

    def __init__(self, title: str, author: str, year: int, duration_hours: float):
        super().__init__(title, author, year)
        self.duration_hours = duration_hours #продолжительность книги

    def get_info(self) -> str:
        return f"Аудиокнига: «{self.title}» ({self.duration_hours} ч.)"

    def borrow_days(self) -> int:
        return 10


    PYPY