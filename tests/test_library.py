from datetime import datetime, timedelta

from Library.library import Library
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Clients.OnlineClient import OnlineClient
from Library.Clients.PhysicalClient import PhysicalClient

def create_library():
    library = Library("Городская библиотека")
    online = OnlineBook("1984", "George Orwell", 1949, 2.5)
    audio = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)
    physical = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1300, "A-12")
    library.add_book(online)
    library.add_book(audio)
    library.add_book(physical)
    return library, online, audio, physical

def test_library_initial_state():
    library = Library("Библиотека")
    assert library.name == "Библиотека"
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

def test_find_book_case_insensitive():
    library, _, audio, _ = create_library()
    assert library.find_book("МАСТЕР И МАРГАРИТА") is audio
    assert library.find_book("мастер и маргарита") is audio

def test_find_book_not_found():
    library = Library("Библиотека")
    assert library.find_book("Нет такой книги") is None

def test_borrow_online_book_success():
    library, book, _, _ = create_library()
    client = OnlineClient("Иван", "C001")

    result = library.borrow_book(client, "1984")

    assert "Книга успешно выдана!" in result
    assert "Иван" in result
    assert book.is_available is False
    assert client.borrowed_books == [book]

    expected_date = (datetime.now() + timedelta(days=14)).strftime("%d.%m.%Y")
    assert expected_date in result

def test_borrow_audio_book_success():
    library, _, book, _ = create_library()
    client = OnlineClient("Иван", "C001")

    result = library.borrow_book(client, "Мастер и Маргарита")

    assert "Книга успешно выдана!" in result
    assert book.is_available is False
    assert client.borrowed_books == [book]

def test_online_client_cannot_borrow_physical_book():
    library, _, _, book = create_library()
    client = OnlineClient("Иван", "C001")

    result = library.borrow_book(client, "Война и мир")

    assert result == "Клиент Иван не может взять книгу этого типа"
    assert book.is_available is True
    assert client.borrowed_books == []

def test_physical_client_can_borrow_physical_book():
    library, _, _, book = create_library()
    client = PhysicalClient("Петр", "C002")

    result = library.borrow_book(client, "Война и мир")

    assert "Книга успешно выдана!" in result
    assert book.is_available is False
    assert client.borrowed_books == [book]

def test_borrow_missing_book():
    library = Library("Библиотека")
    client = OnlineClient("Иван", "C001")

    result = library.borrow_book(client, "Нет такой книги")

    assert result == "Книга «Нет такой книги» не найдена в библиотеке"

def test_borrow_unavailable_book():
    library, book, _, _ = create_library()
    first = OnlineClient("Иван", "C001")
    second = OnlineClient("Петр", "C002")

    library.borrow_book(first, "1984")
    result = library.borrow_book(second, "1984")

    assert result == "Книга «1984» сейчас занята"
    assert book in first.borrowed_books
    assert book not in second.borrowed_books

def test_return_book_success():
    library, book, _, _ = create_library()
    client = OnlineClient("Иван", "C001")

    library.borrow_book(client, "1984")
    result = library.return_book(client, "1984")

    assert result == "Книга «1984» успешно возвращена"
    assert book.is_available is True
    assert client.borrowed_books == []

def test_return_book_case_insensitive():
    library, book, _, _ = create_library()
    client = OnlineClient("Иван", "C001")

    library.borrow_book(client, "1984")
    result = library.return_book(client, "1984")

    assert result == "Книга «1984» успешно возвращена"
    assert book.is_available is True

def test_return_book_when_client_does_not_have_book():
    library, _, _, _ = create_library()
    client = OnlineClient("Иван", "C001")

    result = library.return_book(client, "1984")

    assert result == "У клиента Иван нет книги «1984»"
