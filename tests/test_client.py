import pytest
from Clients.Client import Client
from Clients.OnlineClient import OnlineClient
from Books.OnlineBook import OnlineBook

def test_client_is_abstract():
    with pytest.raises(TypeError):
        Client('Иван','001')

def test_client_fields():
    c=OnlineClient('Иван','001')
    assert c.name=='Иван'
    assert c.client_id=='001'
    assert c.borrowed_books==[]

def test_client_str():
    assert str(OnlineClient('Иван','001'))=='Иван (ID: 001)'

def test_client_borrowed_books_is_independent():
    c1=OnlineClient('A','1'); c2=OnlineClient('B','2')
    c1.borrowed_books.append(OnlineBook('x','y',2000,1.0))
    assert c2.borrowed_books==[]
