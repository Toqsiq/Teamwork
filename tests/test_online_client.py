from Library.Clients.OnlineClient import OnlineClient
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.PhysicalBook import PhysicalBook

def test_online_client_can_borrow_online_book():
    client = OnlineClient("Иван", "C001")
    assert client.can_borrow(OnlineBook("1984", "George Orwell", 1949, 2.5)) is True

def test_online_client_can_borrow_audio_book():
    client = OnlineClient("Иван", "C001")
    assert client.can_borrow(AudioBook("Аудио", "Автор", 2020, 5.0)) is True

def test_online_client_cannot_borrow_physical_book():
    client = OnlineClient("Иван", "C001")
    assert client.can_borrow(PhysicalBook("Война и мир", "Толстой", 1869, 1000, "A-12")) is False
