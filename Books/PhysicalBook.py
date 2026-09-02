from abc import ABC, abstractmethod

class PhysicalBook(Book):
    """Физическая (бумажная) книга"""

    def __init__(self, title: str, author: str, year: int, pages: int, shelf: str):
        super().__init__(title, author, year)
        self.pages = pages
        self.shelf = shelf #на какой полке стоит книга

    def get_info(self) -> str:
        return f"Физическая книга: «{self.title}», {self.pages} стр., полка {self.shelf}"

    def borrow_days(self) -> int:
        return 21
