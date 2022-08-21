class Student(object):

    def __init__(self, name: str, group: str, age: int):
        self._name = name
        self._group = group
        self._age = age

    def __str__(self) -> str:
        info = f'\n> Товар: {self._name}'
        info += f'\n  Группа: {self._group}'
        info += f'\n  Возраст: {self._age}'
        return info

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int):
        self._age = new_age
