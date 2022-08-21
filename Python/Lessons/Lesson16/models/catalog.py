from models.product import Product


class Catalog(object):

    def __init__(self):
        self._products = []

    def add_product(self, new_product: Product):
        self._products.append(new_product)

    def display_products(self):
        if len(self._products) == 0:
            print('Продуктов в каталоге нет')
        else:
            for p in self._products:
                print(p)

    def change_product(self, name: str, price: float, count: int):
        for p in self._products:
            if p.name == name:
                p.price = price
                p.count = count

    def delete_product(self, name: str):
        for p in self._products:
            if p.name == name:
                self._products.remove(p)
