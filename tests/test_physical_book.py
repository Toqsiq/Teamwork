from Library.Books.Book import Book
from Library.Books.PhysicalBook import PhysicalBook


def test_physical_book_inherits_from_book():
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")

    assert isinstance(book, Book)


def test_physical_book_stores_pages_and_shelf():
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")

    assert book.pages == 1225
    assert book.shelf == "A-12"


def test_physical_book_get_info():
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")

    assert book.get_info() == "Физическая книга: «Война и мир», 1225 стр., полка A-12"


def test_physical_book_borrow_days():
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")

    assert book.borrow_days() == 21
