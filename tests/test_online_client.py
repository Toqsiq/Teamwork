import pytest

from Library.Books.AudioBook import AudioBook
from Library.Books.OnlineBook import OnlineBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Clients.Client import Client
from Library.Clients.OnlineClient import OnlineClient


@pytest.fixture
def client():
    return OnlineClient("Иван", "C001")


@pytest.mark.parametrize(
    "book",
    [
        OnlineBook("1984", "George Orwell", 1949, 2.5),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5),
    ],
)
def test_online_client_can_borrow_online_and_audio_books(client, book):
    assert client.can_borrow(book) is True


def test_online_client_cannot_borrow_physical_book(client):
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12")

    assert client.can_borrow(book) is False


def test_online_client_inherits_from_client(client):
    assert isinstance(client, Client)
