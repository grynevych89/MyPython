class Student(object):

    def __init__(self, name: str, age: int, rate: float):
        self._name = name
        self._age = age
        self._rate = rate

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f'{self._name} - {self._age} years; rate: {self._rate}'
