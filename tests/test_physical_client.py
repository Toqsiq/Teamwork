from Library.Clients.PhysicalClient import PhysicalClient
from Library.Books.OnlineBook import OnlineBook
from Library.Books.AudioBook import AudioBook
from Library.Books.PhysicalBook import PhysicalBook

def test_physical_client_can_borrow_all_types():
    client = PhysicalClient("Петр", "C002")
    assert client.can_borrow(OnlineBook("1984", "George Orwell", 1949, 2.5)) is True
    assert client.can_borrow(AudioBook("Аудио", "Автор", 2020, 5.0)) is True
    assert client.can_borrow(PhysicalBook("Война и мир", "Толстой", 1869, 1000, "A-12")) is True
