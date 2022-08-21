from person import Person


class Student(Person):

    def __init__(self, name: str, age: int, rate: float):
        super().__init__(name, age)
        self._rate = rate

    def __str__(self) -> str:
        return super().__str__() + f'\n  Rate: {self._rate}'
