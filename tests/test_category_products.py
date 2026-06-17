from src.category import Category
from src.product import Product


def test_category_products1():
    first_product = Product('Ракета Х55', 'Ракета воздух-поверхность', 1256000.00, 26)
    second_category = Category('Ракеты', 'Ракета воздух-поверхность', [first_product])
    assert second_category.products == ['Ракета Х55, 1256000.0 руб. остаток: 26 шт.']


def test_category_products2():
    third_product = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)
    second_product = Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)
    first_category = Category('Ракеты', 'Ракета воздух-поверхность',
                              [second_product, third_product])
    assert first_category.products == ['Ракета Р-73Э, 117000.0 руб. остаток: 112 шт.',
                                       'Ракета Р-60, 98000.0 руб. остаток: 212 шт.']
