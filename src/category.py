#без такой записи не работает if isinstance(product, Product):
from .product import Product


class Category:
    '''
    Класс для создание объекта категории товаров
    '''
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Функция иницилизации объектов класса Category
        :rtype: None
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count = Category.category_count + 1
        Category.product_count = Category.product_count + 1

    def __str__(self):
        cool = 0
        for prod in self.__products:
            cool = prod.quantity + cool
        return fr'{self.name}, количество продуктов: {cool} шт.'

    @property
    def products(self) -> list:  # Задание №2
        product = self.__products
        remains = []
        for prod in product:
            name = prod.name
            price = prod.price
            quantity = prod.quantity
            remains.append(f'{name}, {price} руб. остаток: {quantity} шт.\n')
        return remains

    def add_product(self, product: object) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count = Category.product_count + 1
        else:
            raise TypeError
