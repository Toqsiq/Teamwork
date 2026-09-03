from Books.OnlineBook import OnlineBook

def test_online_book_fields():
    b=OnlineBook('1984','Orwell',1949,2.5)
    assert b.file_size_mb==2.5
    assert b.title=='1984'
    assert b.author=='Orwell'
    assert b.year==1949

def test_online_book_get_info():
    b=OnlineBook('1984','Orwell',1949,2.5)
    assert b.get_info()=='Онлайн-книга: «1984» (2.5 МБ)'

def test_online_book_borrow_days():
    assert OnlineBook('1984','Orwell',1949,2.5).borrow_days()==14

def test_online_book_available_by_default():
    assert OnlineBook('1984','Orwell',1949,2.5).is_available is True
