from Library.Books.OnlineBook import OnlineBook

def test_online_book():
    book = OnlineBook("1984", "George Orwell", 1949, 2.5)
    assert book.file_size_mb == 2.5
    assert book.get_info() == "Онлайн-книга: «1984» (2.5 МБ)"
    assert book.borrow_days() == 14
