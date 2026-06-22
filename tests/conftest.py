import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product('Ракета Х55', 'Ракета воздух-поверхность', 1256000.00, 26)


@pytest.fixture
def second_product():
    return Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)


@pytest.fixture
def third_product():
    return Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)


@pytest.fixture
def first_category():
    third_product = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)
    second_product = Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)
    return Category('Ракеты', 'Ракета воздух-воздух', [second_product, third_product])


@pytest.fixture
def second_category():
    first_product = Product('Ракета Х55', 'Ракета воздух-поверхность', 1256000.00, 26)
    return Category('Ракеты', 'Ракета воздух-поверхность', [first_product])
