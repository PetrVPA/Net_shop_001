class Category:
    '''
    Класс для создание объекта категории товаров
    '''
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: object, description: object, products: object) -> None:
        """
        Функция иницилизации объектов класса Category
        :rtype: None
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count = Category.category_count + 1
        Category.product_count = Category.product_count + 1
