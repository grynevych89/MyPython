from models.product import Product
from providers.binary import BinaryProvider


if __name__ == '__main__':
    #
    provider = BinaryProvider()
    provider.catalog.add_product(Product(
        'Батон студенческий', 'Продукты', 'Рошен', 12.47, 50
    ))
    provider.catalog.add_product(Product(
        'Молоко витаминное', 'Продукты', 'Фермер', 24.55, 30
    ))
    provider.catalog.add_product(Product(
        'Колбаса докторская', 'Продукты', 'Алан', 120.15, 36
    ))
    provider.catalog.display_products()
    provider.save_data()
