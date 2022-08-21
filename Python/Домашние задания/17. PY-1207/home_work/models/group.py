from models.student import Student


class Group(object):

    def __init__(self):
        self._students = []

    def add_student(self, new_student: Student):
        self._students.append(new_student)

    def display_students(self):
        if len(self._students) == 0:
            print('Группа пока пуста')
        else:
            for p in self._students:
                print(p)

    def change_student(self, name: str, group: str, age: int):
        for p in self._students:
            if p.name == name:
                p.group = group
                p.age = age

    def delete_student(self, name: str):
        for p in self._students:
            if p.name == name:
                self._students.remove(p)
