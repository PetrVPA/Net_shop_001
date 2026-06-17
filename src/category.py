

class Category:
    '''
    Класс для создание объекта категории товаров
    '''
    name: str
    description: str
    products: list


    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Функция иницилизации объектов класса Category
        :rtype: None
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count = Category.category_count + 1
        Category.product_count = Category.product_count + 1


    def add_product(self, product: object) -> None:  # Задание №1
        self.__products.append(product)


    @property
    def products(self) -> list:  # Задание №2
        product = self.__products
        top = []
        for prod in product:
            name = prod.name
            price = prod.price
            quantity = prod.quantity
            top.append(f'{name}, {price} руб. остаток: {quantity} шт.')
        return top

    # @property
    # def products(self) -> list:  # Задание №2
    #     der = []
    #     product = self.__products
    #     for top in product:
    #         der.append(top.name)
    #     return der
