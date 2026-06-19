from src.category import Category
from src.product import Product
import logging
import os.path

file_path = os.path.join(r'..\data\tests_categ_add_product.log')
log_path = os.path.abspath(file_path)
utils_log = logging.getLogger('test_categ_add_product')
file_utils_log = logging.FileHandler(log_path, encoding='utf-8')
utils_log.addHandler(file_utils_log)
file_utils_log_formater = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
file_utils_log.setFormatter(file_utils_log_formater)
utils_log.setLevel(logging.DEBUG)


def test_categ_add_product():
    rokets = Category('Ракеты', 'Ракета воздух-воздух', [])
    utils_log.debug(f'Делай ноль - проверка объекта rokets.name  = {rokets.name}')
    roket_r_60 = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)
    rest = roket_r_60
    utils_log.debug(f'Делай ноль - проверка объекта rest.name  = {rest.name}')
    rokets.add_product(rest)
    object_r60 = rokets.products[0]
    utils_log.debug(f'Делай ноль - проверка name object_r60  = {object_r60}')
    assert object_r60 == 'Ракета Р-60, 98000.0 руб. остаток: 212 шт.\n'
