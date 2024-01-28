class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = new_name

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("Автор книги должен быть типа str")
        self._author = new_author

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}. Количество страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга: {self._name}. Автор: {self._author}. Продолжительность: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


if __name__ == '__main__':
    list_books = [Book("Девятый сон Веры Павловны", "В. Пелевин"), PaperBook("Десять негритят", "А. Кристи", 288), AudioBook("Личное дело Женщины-кошки",
                                                                                               "Д. Донцова", 10.58)]
    for book in list_books:
        print(book)
    print(list_books)