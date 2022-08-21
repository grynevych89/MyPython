from providers.binary import BinaryProvider
from models.student import Student


class Manager(object):

    def __init__(self):
        self._provider = BinaryProvider()
        self._choice = 0
        self._answer = ''

    @property
    def provider(self):
        return self._provider

    def display_menu(self) -> None:

        print('--------------------------------------------')
        print('          Список групп и студентов          ')
        print('--------------------------------------------')
        print('     1 - Просмотр всех студентов            ')
        print('     2 - Просмотр студентов по группам      ')
        print('     3 - Добавление нового студента         ')
        print('     4 - Удаление студента                  ')
        print('     5 - Редактирование студента            ')
        print('     6 - Объединение групп                  ')
        print('     7 - Выход из программы                 ')
        print('--------------------------------------------')

    def get_choice(self) -> int:
        self._choice = int(input('> Выберите нужное действие: '))
        return self._choice

    def allow_continue(self) -> bool:
        self._answer = input('> Продолжать (y/n)? - ')
        return self._answer == 'y'

    def add_student(self) -> None:
        print('> Введите данные о студенте:')
        name = input('   ФИО: ')
        group = input('   Группа: ')
        age = int(input('   Возраст: '))
        student = Student(name, group, age)
        self._provider.group.add_student(student)
        print('Add-OK')
