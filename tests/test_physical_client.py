import pytest

from Library.Books.AudioBook import AudioBook
from Library.Books.OnlineBook import OnlineBook
from Library.Books.PhysicalBook import PhysicalBook
from Library.Clients.Client import Client
from Library.Clients.PhysicalClient import PhysicalClient


@pytest.fixture
def client():
    return PhysicalClient("Петр", "C002")


@pytest.mark.parametrize(
    "book",
    [
        OnlineBook("1984", "George Orwell", 1949, 2.5),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5),
        PhysicalBook("Война и мир", "Лев Толстой", 1869, 1225, "A-12"),
    ],
)
def test_physical_client_can_borrow_any_book(client, book):
    assert client.can_borrow(book) is True


def test_physical_client_inherits_from_client(client):
    assert isinstance(client, Client)
