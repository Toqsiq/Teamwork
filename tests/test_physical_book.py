from Library.Books.PhysicalBook import PhysicalBook

def test_physical_book():
    book = PhysicalBook("Война и мир", "Лев Толстой", 1869, 1300, "А-12")
    assert book.pages == 1300
    assert book.shelf == "А-12"
    assert book.get_info() == "Физическая книга: «Война и мир», 1300 стр., полка А-12"
    assert book.borrow_days() == 21
