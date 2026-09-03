from Library.Clients.Client import Client
from Library.Clients.OnlineClient import OnlineClient


def test_client_is_abstract():
    assert hasattr(Client, "__abstractmethods__")
    assert "can_borrow" in Client.__abstractmethods__


def test_online_client_initializes_common_client_fields():
    client = OnlineClient("Иван", "C001")

    assert client.name == "Иван"
    assert client.client_id == "C001"
    assert client.borrowed_books == []


def test_client_str():
    client = OnlineClient("Иван", "C001")

    assert str(client) == "Иван (ID: C001)"
