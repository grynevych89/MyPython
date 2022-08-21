from models.product import Product
from providers.binary import BinaryProvider
from menu.manager import Manager


if __name__ == '__main__':
    #
    manager = Manager()
    manager.provider.load_data()
    #
    while True:
        manager.display_menu()
        k = manager.get_choice()
        if k == 1:
            manager.provider.catalog.display_products()
        elif k == 2:
            pass
        elif k == 3:
            manager.add_product()
        elif k == 4:
            pass
        elif k == 5:
            pass
        elif k == 6:
            pass
        elif k == 7:
            pass
        else:
            pass
        if not manager.allow_continue():
            break
    #
    print('Finish')
