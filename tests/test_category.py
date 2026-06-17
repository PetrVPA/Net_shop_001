from src.category import Category
from src.product import Product
import logging
import os.path






file_path = os.path.join(r'..\data\tests_file.log')
log_path = os.path.abspath(file_path)
utils_log = logging.getLogger('test_category')
file_utils_log = logging.FileHandler(log_path, encoding='utf-8')
utils_log.addHandler(file_utils_log)
file_utils_log_formater = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
file_utils_log.setFormatter(file_utils_log_formater)
utils_log.setLevel(logging.DEBUG)

def test_category_init1(first_category):

    second_product = Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)

    third_product = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)

    first_category = Category('Ракеты', 'Ракета воздух-воздух', [second_product, third_product])

    assert first_category.name == 'Ракеты'
    assert first_category.description == 'Ракета воздух-воздух'
    #utils_log.debug(f'Делай ноль - проверка геттера = {first_category.products}')
    assert first_category.products == ['Ракета Р-73Э, 117000.0 руб. остаток: 112 шт.', 'Ракета Р-60, 98000.0 руб. остаток: 212 шт.']
    assert first_category.category_count == 2
    assert first_category.product_count == 2


def test_category_init2(second_category):
    first_product = Product('Ракета Х55', 'Ракета воздух-поверхность', 1256000.00, 26)

    second_category = Category('Ракеты', 'Ракета воздух-поверхность', [first_product])

    assert second_category.name == 'Ракеты'
    assert second_category.description == 'Ракета воздух-поверхность'
    #utils_log.debug(f'Делай ноль - проверка геттера = {second_category.products}')
    assert second_category.products == ['Ракета Х55, 1256000.0 руб. остаток: 26 шт.']
    assert second_category.category_count == 4
    assert second_category.product_count == 4
