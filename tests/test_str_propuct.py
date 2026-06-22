
def test_str_propuct1(first_product):
    assert str(first_product) == 'Ракета Х55, 1256000.0 руб. Остаток: 26 шт.'


def test_str_propuct2(second_product):
    assert str(second_product) == 'Ракета Р-73Э, 117000.0 руб. Остаток: 112 шт.'


def test_str_propuct3(third_product):
    assert str(third_product) == 'Ракета Р-60, 98000.0 руб. Остаток: 212 шт.'
