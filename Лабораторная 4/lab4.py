class Book:
    """ Базовый класс книги """

    def __init__(self, name: str, author: str, price: float) -> None:
        """
            Инициализация экземпляра класса
            :param name: название книги
            :param author: имя автора
            :param price: цена книги
        """

        self.name = name
        self.author = author
        self.price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Название произведения должно быть типа str")
        if not new_name:
            raise ValueError("Название произведения не может быть пустой строкой")
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError("Имя автора должен быть типа str")
        if not new_author:
            raise ValueError("Имя автора не может быть пустой строкой")
        self._author = new_author

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if not isinstance(new_price, float):
            raise TypeError("Цена книги должна быть типа float")
        if new_price <= 0:
            raise ValueError("Цена книги должна быть положительным числом")
        self._price = new_price

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}. Цена {self._price}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r})"

    def get_final_price(self) -> float:
        """
            Возвращает конечную цену книги с учётом налога
        """
        return round(self._price * 1.2, 2)


class PaperBook(Book):
    """
        Дочерний класс - бумажная книга
    """

    def __init__(self, name: str, author: str, price: float, binding: str) -> None:
        """
            Инициализация экземпляра класса
            :param name: название книги
            :param author: имя или псевдоним автора
            :param price: цена книги
            :param binding: переплет
        """
        super().__init__(name, author, price)
        self.binding = binding

    @property
    def binding(self) -> str:
        return self._binding

    @binding.setter
    def binding(self, new_binding: str) -> None:
        if not isinstance(new_binding, str):
            raise TypeError("Переплет должен быть типа str")
        self._binding = new_binding

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}. Цена {self._price}. Переплет {self._binding}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r}, " \
               f"material={self._binding!r})"

    def get_final_price(self, shipping_cost: float) -> float:
        """
            К конечной цене бумажной книги добавляется стоимость доставки
            :param shipping_cost: стоимость доставки
        """
        if not isinstance(shipping_cost, float):
            raise TypeError("Стоимость доставки должна быть типа float")
        if shipping_cost < 0:
            raise ValueError("Стоимость доставки должна быть неотрицательным числом")
        return super().get_final_price() + shipping_cost


class DigitalBook(Book):
    """
        Дочерний класс - цифровая книга
    """

    def __init__(self, name: str, author: str, price: float, format: str) -> None:
        """
            Инициализация экземпляра класса
            :param name: название книги
            :param author: имя автора
            :param price: цена книги
            :param format: аудио- или классическая
        """
        super().__init__(name, author, price)
        self.format = format

    @property
    def format(self) -> str:
        return self._format

    @format.setter
    def format(self, new_format: str) -> None:
        if not isinstance(new_format, str):
            raise TypeError("Формат книги должен быть типа str")
        if not new_format:
            raise ValueError("Формат книги не может быть пустой строкой")
        self._format = new_format

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}. Цена {self._price}. Формат {self._format}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, price={self._price!r}, " \
               f"file_format={self._format!r})"

    def is_valid_format(self, file_formats: list[str]) -> bool:
        """
            Проверяет допустимость формата
        """
        return self._format in file_formats


if __name__ == "__main__":
    p1 = Book("Личное дело женщины-кошки", "Дарья Донцова", 999.9)
    p2 = PaperBook("Нежный супруг олигарха", "Дарья Донцова", 420.0, "Мягкий")
    p3 = DigitalBook("Таня Гроттер и магический контрабас", "Дмитрий Емец", 1.6, "mp4")
    list_p = [p1, p2, p3]

    for p in list_p:
        print(p)
    print(list_p)
    print(p2.get_final_price(100.0))
    print(p3.get_final_price())

    formats = ["mp4", "fb2"]
    print(p3.is_valid_format(formats))
    pass
