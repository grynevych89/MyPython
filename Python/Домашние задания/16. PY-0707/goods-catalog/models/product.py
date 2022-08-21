class Product(object):

    def __init__(self, name: str, categ: str, producer: str, price: float, count: int):
        self._name = name
        self._category = categ
        self._producer = producer
        self._price = price
        self._count = count

    def __str__(self) -> str:
        info = f'\n> Товар: {self._name}'
        info += f'\n  Категория: {self._category}'
        info += f'\n  Производитель: {self._producer}'
        info += f'\n  Цена: {self._price}'
        info += f'\n  Количество: {self._count}'
        return info
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        self._price = new_price

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, new_count: int):
        self._count = new_count
