import os
import json
from src.product import Product
from src.category import Category


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


def create_category_from_json(data):
    '''
    Функция для создания объектов Category и Product
    :param data: Список словарей для формирования объектов класса Category и Product
    :return: возвращает объекты Category и Product
    '''
    categorys = []
    for red in data:
        products = []
        for green in red['products']:
            products.append(Product(**green))
        red['name'] = products
        categorys.append(Category(**red))
    return categorys
