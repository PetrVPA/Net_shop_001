
def test_category_init(first_category):
    assert first_category.name == 'Ракеты'
    assert first_category.description == 'Ракета воздух-воздух'
    assert first_category.products == ['second_product', 'third_product']
    assert first_category.category_count == 1
    assert first_category.product_count == 1
