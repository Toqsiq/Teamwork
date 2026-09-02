from abc import ABC, abstractmethod

class PhysicalClient(Client):
    """Физический клиент — может брать любые книги"""

    def can_borrow(self, book: Book) -> bool:
        return True