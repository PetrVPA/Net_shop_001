from src.product import Product


def test_new_product1():
    roc_01 = {"name": 'Ракета Х55', "description": 'Ракета воздух-поверхность', "price": 1256000.00, "quantity": 26}
    answer = Product.new_product(roc_01)
    assert answer.name == 'Ракета Х55'
    assert answer.description == 'Ракета воздух-поверхность'


def test_new_product2():
    roc_01 = {"name": 'Ракета Р-73Э', "description": 'Ракета воздух-воздух', "price": 117000.00, "quantity": 112}
    answer = Product.new_product(roc_01)
    assert answer.name == 'Ракета Р-73Э'
    assert answer.description == 'Ракета воздух-воздух'
