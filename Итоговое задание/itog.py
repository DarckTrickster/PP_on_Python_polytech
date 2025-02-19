from typing import Any


class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация животного.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Инкапсулируем имя, чтобы предотвратить прямое изменение
        self.age = age

    def __str__(self) -> str:
        """
        Строковое представление объекта для пользователя.
        """
        return f"{self._name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        """
        Строковое представление объекта для разработчиков.
        """
        return f"Animal(name={self._name!r}, age={self.age!r})"

    def make_sound(self) -> str:
        """
        Метод, который должен быть переопределен в дочерних классах.
        """
        return "Животное издает звук"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        """
        Переопределение метода __str__, чтобы добавить информацию о породе.
        """
        return f"{self._name}, {self.breed}, возраст {self.age} лет"

    def make_sound(self) -> str:
        """
        Переопределенный метод. У собак есть свой характерный звук — лай.
        """
        return "Гав-гав!"


if __name__ == "__main__":
    animal = Animal("Неизвестное животное", 5)
    dog = Dog("Бобик", 3, "Лабрадор")

    print(animal)  # Выведет: Неизвестное животное, возраст 5 лет
    print(dog)  # Выведет: Бобик, Лабрадор, возраст 3 лет

    print(animal.make_sound())  # Выведет: Животное издает звук
    print(dog.make_sound())  # Выведет: Гав-гав!
