#  ПРИМЕР РАБОТЫ 

from library import Library
from Books.Book import Book
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook
from Clients.Client import Client
from Clients.PhysicalClient import PhysicalClient
from Clients.OnlineClient import OnlineClient

if __name__ == "__main__":
    library = Library("Городская библиотека")

    # Книги разных типов
    library.add_book(OnlineBook("1984", "Джордж Оруэлл", 1949, 2.5))
    library.add_book(AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5))
    library.add_book(PhysicalBook("Война и мир", "Лев Толстой", 1869, 1300, "А-12"))
    library.add_book(PhysicalBook("Преступление и наказание", "Фёдор Достоевский", 1866, 670, "Б-3"))

    # Клиенты разных типов
    anna = OnlineClient("Анна Смирнова", "ON-001")
    ivan = PhysicalClient("Иван Петров", "PH-001")

    library.add_client(anna)
    library.add_client(ivan)

    print("=== Примеры выдачи книг ===\n")

    print(library.borrow_book(anna, "1984"))
    print()
    print(library.borrow_book(anna, "Война и мир"))      # отказ
    print()
    print(library.borrow_book(ivan, "Война и мир"))
    print()
    print(library.borrow_book(ivan, "Мастер и Маргарита"))