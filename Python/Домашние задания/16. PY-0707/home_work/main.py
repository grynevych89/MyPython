from menu.manager import Manager
from vector import Vector


if __name__ == '__main__':
    #
    manager = Manager()
    manager.provider.load_data()
    #
    while True:
        manager.display_menu()
        k = manager.get_choice()
        if k == 1:
            manager.provider.group.display_student()
        elif k == 2:
            pass
        elif k == 3:
            manager.add_product()
        elif k == 4:
            pass
        elif k == 5:
            pass
        elif k == 6:
            a = Vector(manager.provider.group.add_student())
            b = Vector()
            c = a + b
        elif k == 7:
            pass
        else:
            pass
        if not manager.allow_continue():
            break
    #
    print('Finish')