from models.product import Product
from models.catalog import Catalog
from providers.binary import BinaryProvider

if __name__ == '__main__':
    #
    provider = BinaryProvider
    provider.catalog.add_product(Product(
        'Батон студенческий', 'Продукты питания', 'Рошен', 12.47, 49
    ))
    provider.catalog.add_product(Product(
        'Молоко витаминное', 'Продукты питания', 'Фермер', 24.55, 30
    ))
    provider.catalog.add_product(Product(
        'Колбаса докторская', 'Продукты питания', 'Алан', 99.99, 13
    ))
    provider.catalog.display_products()
    provider.save_data()

