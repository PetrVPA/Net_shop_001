import os
import json
import logging
from src.product import Product
from src.category import Category

file_path = os.path.join(r'..\data\utils.log')
log_path = os.path.abspath(file_path)
utils_log = logging.getLogger('utils')
file_utils_log = logging.FileHandler(log_path, encoding='utf-8')
utils_log.addHandler(file_utils_log)
file_utils_log_formater = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
file_utils_log.setFormatter(file_utils_log_formater)
utils_log.setLevel(logging.DEBUG)


def download_file(path: str) -> dict:
    '''
    Функция для загрузки информации отоваре и его категориях из json файла
    :param path: Адрес пути нахождения файла
    :return: answer_data Список словарей для создания объектов классов Product и Category
    '''
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        answer_data = json.load(file)
    return answer_data


def create_category_from_json(data: list(dict)) -> list(object):
    '''
    Функция для создания объектов Category и Product
    :param data: Список словарей для формирования объектов класса Category и Product
    :return: возвращает объекты Category и Product
    '''
    fin = []
    for red in data:
        products = []
        for green in red['products']:
            utils_log.debug(f'Делай ноль - green = {green}')
            products.append(Product.new_product(green))
            utils_log.debug(f'Делай один - products = {products}')
            red['products'] = products
            utils_log.debug(f'Делай два - red = {red}')
            categor = Category(**red)
        fin.append(categor)
        utils_log.debug(f'Делай три - fin = {fin}')
    utils_log.debug(f'Делай четыре - fin = {fin}')
    return fin
