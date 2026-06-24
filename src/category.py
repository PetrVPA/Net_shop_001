from product import Product
from product import Smartphone
import logging
import os.path


# file_path = os.path.join(r'..\data\Category.log')
# log_path = os.path.abspath(file_path)
# utils_log = logging.getLogger('Category')
# file_utils_log = logging.FileHandler(log_path, encoding='utf-8')
# utils_log.addHandler(file_utils_log)
# file_utils_log_formater = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
# file_utils_log.setFormatter(file_utils_log_formater)
# utils_log.setLevel(logging.DEBUG)


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

    # def add_product(self, product: object) -> None:
    #     self.__products.append(product)

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

    # def add_product(self, product: Product) -> None:
    #     if isinstance(product, Product):
    #         self.__Category_products.append(product)
    #     else:
    #         raise TypeError

    def add_product(self, product: object) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count = Category.product_count + 1
        else:
            raise TypeError
