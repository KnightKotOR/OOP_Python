# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Toy:
    def __init__(self, name: str, owner: str, type: str):
        """
                Создание и подготовка к работе объекта "Игрушка"

               :param name: Название игрушки
               :param owner: Название кота-владельца
               :param type: Вид игрушки

               Пример:
               >>> toy = Toy("knitted mouse", "Marsel", "mouse")  # инициализация экземпляра класса
               """
        if not isinstance(name, str):
            raise TypeError("Название игрушки должно быть типа str")
        self.name = name
        if not isinstance(owner, str):
            raise TypeError("Владелец игрушки должен быть типа str")
        self.owner = owner
        if not isinstance(type, str):
            raise TypeError("Вид игрушки должен быть типа str")
        self.type = type

    def is_mouse(self) -> bool:
        """
                Проверяет является ли игрушка мышью
                :return: Является ли игрушка мышью

                Пример:
                >>> toy = Toy("squeaky mouse", "Marsel", "mouse")
                >>> toy.is_mouse()
        """
        ...

    @staticmethod
    def change_owner(new_owner: str) -> None:
        """
                Меняет владельца игрушки

                :param new_owner: новый владелец игрушки

                Пример:
                >>> toy = Toy("spring", "Marsel", "teaser")
                >>> toy.change_owner("Pzhn")
        """
        if not isinstance(new_owner, str):
            raise TypeError("Владелец должен быть типа str")
        ...


class PlayBox:
    def __init__(self, toys: list[str]):
        """
              Создание и подготовка к работе объекта "Коробка"

               :param toys: Список игрушек, относящихся к коробке

               >>> playbox = PlayBox(["knitted mouse", "squeaky mouse", "spring"])
        """
        if not isinstance(toys, list):
            raise TypeError("Коробка должна быть списком")
        for toy in toys:
            if not isinstance(toy, str):
                raise TypeError("Игрушки должны быть типа str")
        self.toys = toys

    @staticmethod
    def add_toy(toy: str) -> None:
        """
                Добавляет игрушку в коробку

                :param toy: игрушка, добавляемая в коробку

                Пример:
                >>> playbox = PlayBox(["spring"])
                >>> playbox.add_toy("knitted")
        """
        if not isinstance(toy, str):
            raise TypeError("Игрушка должна быть типа str")
        ...

    def sort_toys(self) -> list[str]:
        """
                Возвращает список игрушку, отсортированных в алфавитном порядке

                :return: Список с объектами типа str, отсортированных в алфавитном порядке

                Пример:
                >>> playbox = PlayBox(["knitted mouse", "squeaky mouse", "spring"])
                >>> playbox.sort_toys()
        """
        ...


class Cat:
    def __init__(self, name: str, color: str):
        """
                Создание и подготовка к работе объекта "Кот"

                :param name: Имя кота
                :param color: Окрас шерсти кота (или ее отсутствие)

                Пример:
                       >>> cat = Cat("Marsel", "Orange")
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть типа str")
        self.name = name
        if not isinstance(color, str):
            raise TypeError("Окрас шерсти кота должен быть типа str")
        self.color = color

    def buy_toy(self, name: str, type: str) -> Toy:
        """
                Покупка новой игрушки котика

               :param name: Название игрушки
               :param type: Вид игрушки
                :return: Объект класса Toy

                Пример:
                >>> cat = Cat("Pzhn", "Tabby")
                >>> cat.buy_toy("knitted mouse", "mouse")
        """
        ...

    def change_name(self, new_name: str) -> None:
        """
                Меняет кличку

                :param new_name: новая кличка кота

                Пример:
                >>> cat = Cat("Sus", "Tabby")
                >>> cat.change_name("Pzhn")
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
