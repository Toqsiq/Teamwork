import pytest
from models import OnlineBook, AudioBook, PhysicalBook, OnlineClient, PhysicalClient
from library import Library


@pytest.fixture
def library():
    lib = Library("Тестовая библиотека")
    lib.add_book(OnlineBook("1984", "Оруэлл", 1949, 2.1))
    lib.add_book(AudioBook("Мастер и Маргарита", "Булгаков", 1967, 18.0))
    lib.add_book(PhysicalBook("Война и мир", "Толстой", 1869, 1300, "А-1"))
    return lib


@pytest.fixture
def online_client():
    return OnlineClient("Анна", "ON-1")


@pytest.fixture
def physical_client():
    return PhysicalClient("Иван", "PH-1")


def test_online_client_can_borrow_online_book(library, online_client):
    result = library.borrow_book(online_client, "1984")
    assert "успешно выдана" in result


def test_online_client_cannot_borrow_physical_book(library, online_client):
    result = library.borrow_book(online_client, "Война и мир")
    assert "не может взять" in result


def test_physical_client_can_borrow_any_book(library, physical_client):
    r1 = library.borrow_book(physical_client, "Война и мир")
    r2 = library.borrow_book(physical_client, "1984")
    assert "успешно выдана" in r1
    assert "успешно выдана" in r2


def test_book_becomes_unavailable_after_borrow(library, physical_client):
    library.borrow_book(physical_client, "Война и мир")
    book = library.find_book("Война и мир")
    assert book.is_available is False


def test_return_book(library, physical_client):
    library.borrow_book(physical_client, "Война и мир")
    result = library.return_book(physical_client, "Война и мир")
    assert "успешно возвращена" in result
    assert library.find_book("Война и мир").is_available is True
