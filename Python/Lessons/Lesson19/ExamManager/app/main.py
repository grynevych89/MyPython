# from models.teacher import Teacher
from lib.manager import Manager


if __name__ == '__main__':

    # model1 = Teacher()
    # model1.add('Ангела Меркель', '1980-8-19')
    # model1.remove('Ирина Шубкина')
    # model1.update('Наталья Петрова', '2001-2-12', 'Петя Зубкин')
    # teachers = model1.get_all()

    manager = Manager()
    manager.display_all_teacher()

    print('ok-7')
