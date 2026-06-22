

def test_add_product1(first_product, second_product):
    assert first_product + second_product == 45760000.0


def test_add_product2(second_product, third_product):
    assert third_product + second_product == 33880000.0


def test_add_product3(first_product, third_product):
    assert first_product + third_product == 53432000.0
