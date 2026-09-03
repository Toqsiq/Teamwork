from Library.Books.Book import Book
from Library.Books.OnlineBook import OnlineBook


def test_online_book_inherits_from_book():
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)

    assert isinstance(book, Book)


def test_online_book_stores_file_size():
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)

    assert book.file_size_mb == 2.5


def test_online_book_get_info():
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)

    assert book.get_info() == "Онлайн-книга: «1984» (2.5 МБ)"


def test_online_book_borrow_days():
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)

    assert book.borrow_days() == 14
