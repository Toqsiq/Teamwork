class book:
    def __init__(self, style, author):
        self.style=style
        self.author=author

class online_book:
    def __init__(self, style, author):
        self.style=style
        self.author=author

class audio_book:
       def __init__(self, style, author, voice):
        self.style=style
        self.author=author
        self.voice=voice

book1=book ("fantastic", "Dostoevskiy")
book2=book ("fantazy", "Tolkin")
book3=book ("dramma", "Tolstoi")

book4=online_book ("dramma", "Palanik")
book5=online_book ("detectiv", "Donzova")
book6=online_book ("triller", "London")

book7=audio_book ("fantastic", "Dostoevskiy", "Alisa")
book8=audio_book ("detectiv", "Donzova", "Harlamov")
book9=audio_book ("dramma", "Tolstoi", "Bondarchuk")

