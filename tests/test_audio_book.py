from Library.Books.AudioBook import AudioBook

def test_audio_book():
    book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 18.5)
    assert book.duration_hours == 18.5
    assert book.get_info() == "Аудиокнига: «Мастер и Маргарита» (18.5 ч.)"
    assert book.borrow_days() == 10
