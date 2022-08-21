from models.student import Student
from models.group import Group


if __name__ == '__main__':
    g = Group('Super-Group-123')
    g.display()
    print()

    g.add_student(Student('Student-1', 20, 8.4))
    g.add_student(Student('Student-2', 18, 9.5))
    g.add_student(Student('Student-3', 25, 7.3))
    g.display()
