from src.category import Category
from src.product import Product


def test_midl_price1():
    third_product = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)
    second_product = Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)
    answer = Category('Ракеты', 'Ракета воздух-воздух', [second_product, third_product])
    assert answer.middle_price() == 107500.0


def test_midl_price2():
    answer = Category('Ракеты', 'Ракета воздух-воздух', [])
    assert answer.middle_price() == 0
