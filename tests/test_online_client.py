from Clients.OnlineClient import OnlineClient
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook

def test_online_client_can_borrow_online_book():
    client=OnlineClient('Иван','001')
    assert client.can_borrow(OnlineBook('1984','George Orwell',1949,2.5)) is True

def test_online_client_can_borrow_audio_book():
    client=OnlineClient('Иван','001')
    assert client.can_borrow(AudioBook('Аудио','Автор',2020,5.0)) is True

def test_online_client_cannot_borrow_physical_book():
    client=OnlineClient('Иван','001')
    assert client.can_borrow(PhysicalBook('Война и мир','Толстой',1869,1000,'А-12')) is False

def test_online_client_starts_without_books():
    assert OnlineClient('Иван','001').borrowed_books==[]
