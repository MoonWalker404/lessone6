# Задача №3.
# Создайте класс Author и класс Book.
# Класс Book должен использовать композицию для включения автора в качестве объекта.

class Autor():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def get_info_book(self):
        print(f"{self.title} - {self.autor.name}")

autor = Autor("Лев Толстой", "Русский")
book = Book("Война и Мир", autor)

print(autor.name)
book.get_info_book()