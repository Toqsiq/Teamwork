from abc import ABC, abstractmethod

class OnlineBook(Book):
    """Онлайн-книга (электронная)"""

    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def get_info(self) -> str:
        return f"Онлайн-книга: «{self.title}» ({self.file_size_mb} МБ)"

    def borrow_days(self) -> int:
        return 14