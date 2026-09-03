from Books.AudioBook import AudioBook

def test_audio_book_fields():
    b=AudioBook('Аудио','Автор',2020,5.0)
    assert b.duration_hours==5.0
    assert b.title=='Аудио'
    assert b.author=='Автор'
    assert b.year==2020

def test_audio_book_get_info():
    b=AudioBook('Аудио','Автор',2020,5.0)
    assert b.get_info()=='Аудиокнига: «Аудио» (5.0 ч.)'

def test_audio_book_borrow_days():
    assert AudioBook('Аудио','Автор',2020,5.0).borrow_days()==10

def test_audio_book_available_by_default():
    assert AudioBook('Аудио','Автор',2020,5.0).is_available is True
