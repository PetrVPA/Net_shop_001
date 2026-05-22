

def test_product_init(first_product, second_product, third_product):
    assert first_product.name == "Ракета Х55"
    assert first_product.description == "Ракета воздух-поверхность"
    assert first_product.price == 1256000.00
    assert first_product.quantity == 26
    assert second_product.name == 'Ракета Р-73Э'
    assert second_product.description == 'Ракета воздух-воздух'
    assert second_product.price == 117000.00
    assert second_product.quantity == 112
    assert third_product.name == 'Ракета Р-60'
    assert third_product.description == 'Ракета воздух-воздух'
    assert third_product.price == 98000.00
    assert third_product.quantity == 212
