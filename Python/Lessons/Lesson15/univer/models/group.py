from models.student import Student


class Group(object):

    def __init__(self, name: str):
        self._name = name
        self._students = []

    @property
    def name(self) -> str:
        return self._name

    def display(self) -> None:
        print(f'Группа: {self._name}')
        if len(self._students) == 0:
            print('Список студентов пуст')
        else:
            k = 0
            for s in self._students:
                k += 1
                print(f'{k}. {s.name}')

    def add_student(self, s: Student):
        self._students.append(s)

    def del_student(self, i: int):
        self._students.pop(i)
