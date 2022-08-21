from providers.binary import BinaryProvider
from models.product import Product
import os


class Manager(object):

    def __init__(self):
        self._provider = BinaryProvider()
        self._choice = 0
        self._answer = ''

    @property
    def provider(self):
        return self._provider

    def display_menu(self) -> None:
        # os.system('clear')
        print('--------------------------------------------')
        print('   Система управления каталогом товаров     ')
        print('--------------------------------------------')
        print('     1 - Просмотр всех товаров              ')
        print('     2 - Просмотр товаров по категориям     ')
        print('     3 - Добавление нового товара           ')
        print('     4 - Удаление существующего товара      ')
        print('     5 - Редактирование данных о товаре     ')
        print('     6 - Поиск товара по каталогу           ')
        print('     7 - Выход из программы                 ')
        print('--------------------------------------------')

    def get_choice(self) -> int:
        self._choice = int(input('> Выберите нужное действие: '))
        return self._choice

    def allow_continue(self) -> bool:
        self._answer = input('> Продолжать (y/n)? - ')
        return self._answer == 'y'

    def add_product(self) -> None:
        print('> Введите характеристики товара:')
        name = input('   Название: ')
        category = input('   Категория: ')
        producer = input('   Производитель: ')
        price = float(input('   Цена: '))
        count = int(input('   Кол-во: '))
        product = Product(name, category, producer, price, count)
        self._provider.catalog.add_product(product)
        print('Add-OK')
