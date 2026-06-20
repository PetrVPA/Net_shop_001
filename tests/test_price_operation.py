from src.product import Product


def test_viev_price2():
    roc_01 = {"name": 'Ракета Р-73Э', "description": 'Ракета воздух-воздух', "price": 117000.00, "quantity": 112}
    answer = Product.new_product(roc_01)
    assert answer.price == 117000.00
    answer.price = 203000.00
    assert answer.price == 203000.00
    answer.price = -200000.00
    assert answer.price == 203000.00


def test_edit_price1():
    roc_01 = {"name": 'Ракета Х55', "description": 'Ракета воздух-поверхность', "price": 1256000.00, "quantity": 26}
    answer = Product.new_product(roc_01)
    assert answer.price == 1256000.00
    answer.price = 1360000.00
    assert answer.price == 1360000.00
    answer.price = -200000.00
    assert answer.price == 1360000.00
