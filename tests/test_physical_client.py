from Clients.PhysicalClient import PhysicalClient
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook

def test_physical_client_can_borrow_online_book():
    assert PhysicalClient('Иван','001').can_borrow(OnlineBook('1984','Orwell',1949,2.5)) is True

def test_physical_client_can_borrow_audio_book():
    assert PhysicalClient('Иван','001').can_borrow(AudioBook('Аудио','Автор',2020,5.0)) is True

def test_physical_client_can_borrow_physical_book():
    assert PhysicalClient('Иван','001').can_borrow(PhysicalBook('Война','Толстой',1869,1300,'А-12')) is True

def test_physical_client_str():
    assert str(PhysicalClient('Иван','001'))=='Иван (ID: 001)'
