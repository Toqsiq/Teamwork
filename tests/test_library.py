from library import Library
from Books.OnlineBook import OnlineBook
from Books.AudioBook import AudioBook
from Books.PhysicalBook import PhysicalBook
from Clients.OnlineClient import OnlineClient
from Clients.PhysicalClient import PhysicalClient

def create_library():
    lib=Library('Библиотека')
    online=OnlineBook('1984','Оруэлл',1949,2.5)
    audio=AudioBook('Мастер и Маргарита','Булгаков',1967,18.5)
    physical=PhysicalBook('Война и мир','Толстой',1869,1300,'А-12')
    lib.add_book(online); lib.add_book(audio); lib.add_book(physical)
    return lib,online,audio,physical

def test_library_initial_state():
    lib=Library('Библиотека')
    assert lib.name=='Библиотека' and lib.books==[] and lib.clients==[]

def test_add_book():
    lib=Library('Библиотека'); b=OnlineBook('1984','Orwell',1949,2.5)
    lib.add_book(b)
    assert lib.books==[b]

def test_add_client():
    lib=Library('Библиотека'); c=OnlineClient('Иван','001')
    lib.add_client(c)
    assert lib.clients==[c]

def test_find_book_case_insensitive():
    lib,book,_,_=create_library()
    assert lib.find_book('1984') is book
    assert lib.find_book('1984'.lower()) is book

def test_find_book_not_found():
    assert create_library()[0].find_book('Нет такой книги') is None

def test_borrow_online_book_success():
    lib,book,_,_=create_library(); client=OnlineClient('Иван','001')
    result=lib.borrow_book(client,'1984')
    assert 'Книга успешно выдана!' in result
    assert 'Иван' in result
    assert book.is_available is False
    assert client.borrowed_books==[book]

def test_borrow_audio_book_success():
    lib,_,book,_=create_library(); client=OnlineClient('Иван','001')
    result=lib.borrow_book(client,'Мастер и Маргарита')
    assert 'Книга успешно выдана!' in result
    assert book.is_available is False
    assert client.borrowed_books==[book]

def test_borrow_physical_by_online_client_fails():
    lib,_,_,book=create_library(); client=OnlineClient('Анна','001')
    result=lib.borrow_book(client,'Война и мир')
    assert result=='Клиент Анна не может взять книгу этого типа'
    assert book.is_available is True
    assert client.borrowed_books==[]

def test_borrow_physical_by_physical_client_success():
    lib,_,_,book=create_library(); client=PhysicalClient('Иван','002')
    result=lib.borrow_book(client,'Война и мир')
    assert 'Книга успешно выдана!' in result
    assert book.is_available is False
    assert client.borrowed_books==[book]

def test_borrow_missing_book():
    lib=create_library()[0]; client=OnlineClient('Иван','001')
    assert lib.borrow_book(client,'Нет такой книги')=='Книга «Нет такой книги» не найдена в библиотеке'

def test_borrow_unavailable_book():
    lib,book,_,_=create_library(); c1=OnlineClient('Иван','001'); c2=OnlineClient('Пётр','002')
    lib.borrow_book(c1,'1984')
    assert lib.borrow_book(c2,'1984')=='Книга «1984» сейчас занята'
    assert book.is_available is False

def test_return_book_success():
    lib,book,_,_=create_library(); client=OnlineClient('Иван','001')
    lib.borrow_book(client,'1984')
    assert lib.return_book(client,'1984')=='Книга «1984» успешно возвращена'
    assert book.is_available is True
    assert client.borrowed_books==[]

def test_return_book_case_insensitive():
    lib,book,_,_=create_library(); client=OnlineClient('Иван','001')
    lib.borrow_book(client,'1984')
    assert lib.return_book(client,'1984'.upper())=='Книга «1984» успешно возвращена'

def test_return_book_missing():
    lib=create_library()[0]; client=OnlineClient('Иван','001')
    assert lib.return_book(client,'1984')=='У клиента Иван нет книги «1984»'
