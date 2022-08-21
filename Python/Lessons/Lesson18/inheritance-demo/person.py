class Person(object):

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f'\n> Person: \n  Name: {self._name} \n  Age: {self._age}'
