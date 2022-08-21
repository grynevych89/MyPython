from models.student import Student
from models.group import Group


if __name__ == '__main__':
    g1 = Group('Веселые', [])
    g1.add_student(Student('Иван'))
    g1.display()
    print()
    g2 = Group('Айтишники', [])
    g2.add_student(Student('Ирина'))
    g2.display()
    print()
    g3 = g1 + g2
    g3.display()
    print()
