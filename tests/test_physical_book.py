from Books.PhysicalBook import PhysicalBook

def test_physical_book_fields():
    b=PhysicalBook('Война и мир','Толстой',1869,1300,'А-12')
    assert b.pages==1300
    assert b.shelf=='А-12'

def test_physical_book_get_info():
    b=PhysicalBook('Война и мир','Толстой',1869,1300,'А-12')
    assert b.get_info()=='Физическая книга: «Война и мир», 1300 стр., полка А-12'

def test_physical_book_borrow_days():
    assert PhysicalBook('Война и мир','Толстой',1869,1300,'А-12').borrow_days()==21

def test_physical_book_available_by_default():
    assert PhysicalBook('Война и мир','Толстой',1869,1300,'А-12').is_available is True
