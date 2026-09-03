from datetime import datetime, timedelta

from Library.Books.AudioBook import AudioBook
from Library.Books.OnlineBook import OnlineBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Clients.OnlineClient import OnlineClient
from Library.Clients.PhysicalClient import PhysicalClient
from Library.library import Library


def test_library_initial_state():
    library = Library("Городская библиотека")

    assert library.name == "Городская библиотека"
    assert library.books == []
    assert library.clients == []


def test_add_book():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)

    library.add_book(book)

    assert library.books == [book]


def test_add_client():
    library = Library("Библиотека")
    client = OnlineClient("Иван", "C001")

    library.add_client(client)

    assert library.clients == [client]


def test_find_book_returns_book():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    library.add_book(book)

    assert library.find_book("1984") is book


def test_find_book_is_case_insensitive():
    library = Library("Библиотека")
    book = OnlineBook("Война и мир", "Лев Толстой", 1869, 2.5)
    library.add_book(book)

    assert library.find_book("война и мир") is book
    assert library.find_book("ВОЙНА И МИР") is book


def test_find_book_returns_none_when_not_found():
    library = Library("Библиотека")

    assert library.find_book("Несуществующая книга") is None


def test_borrow_online_book_by_online_client():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    client = OnlineClient("Иван", "C001")
    library.add_book(book)

    result = library.borrow_book(client, "1984")

    assert "Книга успешно выдана!" in result
    assert book.is_available is False
    assert client.borrowed_books == [book]


def test_borrow_audio_book_by_online_client():
    library = Library("Библиотека")
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)
    client = OnlineClient("Иван", "C001")
    library.add_book(book)

    result = library.borrow_book(client, "Мастер и Маргарита")

    assert "Книга успешно выдана!" in result
    assert book.is_available is False
    assert client.borrowed_books == [book]


def test_online_client_cannot_borrow_physical_book():
    library = Library("Библиотека")
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")
    client = OnlineClient("Иван", "C001")
    library.add_book(book)

    result = library.borrow_book(client, "Война и мир")

    assert result == "Клиент Иван не может взять книгу этого типа"
    assert book.is_available is True
    assert client.borrowed_books == []


def test_physical_client_can_borrow_all_book_types():
    library = Library("Библиотека")
    client = PhysicalClient("Петр", "C002")

    books = [
        OnlineBook("1984", "George Orwell", 1949, 2.5),
        AudioBook("Аудио", "Автор", 2020, 5.0),
        PhysicalBook("Физическая", "Автор", 2021, 300, "B-1"),
    ]

    for book in books:
        library.add_book(book)
        result = library.borrow_book(client, book.title)

        assert "Книга успешно выдана!" in result
        assert book.is_available is False

    assert client.borrowed_books == books


def test_borrow_book_returns_not_found_message():
    library = Library("Библиотека")
    client = OnlineClient("Иван", "C001")

    result = library.borrow_book(client, "Нет такой книги")

    assert result == "Книга «Нет такой книги» не найдена в библиотеке"


def test_borrow_already_borrowed_book():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    first_client = OnlineClient("Иван", "C001")
    second_client = OnlineClient("Петр", "C002")
    library.add_book(book)

    library.borrow_book(first_client, "1984")
    result = library.borrow_book(second_client, "1984")

    assert result == "Книга «1984» сейчас занята"
    assert second_client.borrowed_books == []


def test_borrow_book_uses_book_borrow_period():
    library = Library("Библиотека")
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")
    client = PhysicalClient("Петр", "C002")
    library.add_book(book)

    before = datetime.now().date()
    result = library.borrow_book(client, "Война и мир")
    after = datetime.now().date()

    date_text = result.split("Вернуть до: ")[1]
    return_date = datetime.strptime(date_text, "%d.%m.%Y").date()

    assert before + timedelta(days=21) <= return_date <= after + timedelta(days=21)


def test_return_book_successfully():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    client = OnlineClient("Иван", "C001")
    library.add_book(book)
    library.borrow_book(client, "1984")

    result = library.return_book(client, "1984")

    assert result == "Книга «1984» успешно возвращена"
    assert book.is_available is True
    assert client.borrowed_books == []


def test_return_book_is_case_insensitive():
    library = Library("Библиотека")
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    client = OnlineClient("Иван", "C001")
    library.add_book(book)
    library.borrow_book(client, "1984")

    result = library.return_book(client, "1984")

    assert result == "Книга «1984» успешно возвращена"


def test_return_book_when_client_does_not_have_it():
    library = Library("Библиотека")
    client = OnlineClient("Иван", "C001")

    result = library.return_book(client, "1984")

    assert result == "У клиента Иван нет книги «1984»"


def test_return_one_book_keeps_other_book_borrowed():
    library = Library("Библиотека")
    first = OnlineBook("1984", "George Orwell", 1949, 2.5)
    second = OnlineBook("Animal Farm", "George Orwell", 1945, 1.5)
    client = OnlineClient("Иван", "C001")
    library.add_book(first)
    library.add_book(second)

    library.borrow_book(client, "1984")
    library.borrow_book(client, "Animal Farm")

    library.return_book(client, "1984")

    assert first.is_available is True
    assert second.is_available is False
    assert client.borrowed_books == [second]
