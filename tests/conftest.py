import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(name='Ракета Х55', description='Ракета воздух-поверхность', price=1256000.00, quantity=26)


@pytest.fixture
def second_product():
    return Product(name='Ракета Р-73Э', description='Ракета воздух-воздух', price=117000.00, quantity=112)


@pytest.fixture
def third_product():
    return Product(name='Ракета Р-60', description='Ракета воздух-воздух', price=98000.00, quantity=212)


@pytest.fixture
def first_category():
    return Category(name='Ракеты', description='Ракета воздух-воздух', products=['second_product', 'third_product'])


@pytest.fixture
def second_category():
    return Category(name='Ракеты', description='Ракета воздух-поверхность', products=['first_product'])
