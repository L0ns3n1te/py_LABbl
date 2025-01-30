class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f'PaperBook(name={self.name}, author={self.author}, pages={self.pages})'

    def __repr__(self):
        return f'PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages!r})'

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом!")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше 0!")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        return f'AudioBook(name={self.name}, author={self.author}, duration={self.duration})'

    def __repr__(self):
        return f'AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration!r})'

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть целым числом!")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше 0!")
        self._duration = float(value)
