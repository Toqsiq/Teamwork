from Library.Books.Book import Book
from Library.Books.AudioBook import AudioBook


def test_audio_book_inherits_from_book():
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)

    assert isinstance(book, Book)


def test_audio_book_stores_duration():
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)

    assert book.duration_hours == 18.5


def test_audio_book_get_info():
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)

    assert book.get_info() == "Аудиокнига: «Мастер и Маргарита» (18.5 ч.)"


def test_audio_book_borrow_days():
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)

    assert book.borrow_days() == 10
