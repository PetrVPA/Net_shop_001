from src.category import Category


class Product:
    '''
    Класс для формирования объекта товар
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: object, description: object, price: object, quantity: object) -> None:
        """
        Функция инициализации объекта класса Product
        :rtype: None
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
