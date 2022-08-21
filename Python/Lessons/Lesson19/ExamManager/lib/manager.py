from models.teacher import Teacher


class Manager(object):

    def __init__(self):
        self._teacher = Teacher()

    def display_all_teacher(self):
        teachers = self._teacher.get_all()
        for t in teachers:
            print(f'ID: {t[0]}; Name: {t[1]}; Birth: {t[2]}')
