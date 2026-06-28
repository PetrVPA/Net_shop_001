from src.product import Product
import pytest


def test_zerro_add1():
    with pytest.raises(ValueError):
        Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 0)


def test_zerro_add2():
    with pytest.raises(ValueError):
        Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 0)
