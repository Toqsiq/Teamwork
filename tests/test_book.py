import pytest
from abc import ABC
from Books.Book import Book
from Books.OnlineBook import OnlineBook

def test_book_is_abstract():
    assert issubclass(Book, ABC)
    with pytest.raises(TypeError):
        Book('x','y',2000)

def test_book_common_fields():
    book=OnlineBook('1984','George Orwell',1949,2.5)
    assert book.title=='1984'
    assert book.author=='George Orwell'
    assert book.year==1949
    assert book.is_available is True

def test_book_str_available():
    book=OnlineBook('1984','Orwell',1949,2.5)
    assert str(book)=='«1984» — Orwell (1949) [доступна]'

def test_book_str_unavailable():
    book=OnlineBook('1984','Orwell',1949,2.5)
    book.is_available=False
    assert str(book)=='«1984» — Orwell (1949) [занята]'
