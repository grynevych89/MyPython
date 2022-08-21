from models.student import Student


class Group(object):

    def __init__(self):
        self._groups = []

    def add_student(self, new_student: Student):
        self._groups.append(new_student)

    def display_student(self):
        if len(self._groups) == 0:
            print('Группа пока пуста')
        else:
            for p in self._groups:
                print(p)

    def change_book(self, name: str, group: float, age: int):
        for p in self._groups:
            if p.name == name:
                p.group = group
                p.age = age

    def delete_student(self, name: str):
        for p in self._groups:
            if p.name == name:
                self._groups.remove(p)
