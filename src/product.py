
class Product:
    '''
    Класс для формирования объекта товар
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Функция инициализации объекта класса Product
        :rtype: None
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return fr'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other: object) -> int:
        return (self.__price*self.quantity)+(other.__price*other.quantity)

    @classmethod
    def new_product(cls, checklist: dict) -> object:  # Задание №3
        return cls(checklist["name"], checklist["description"], checklist["price"], checklist["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, input_price: float) -> None:
        if input_price > 0:
            self.__price = input_price
        else:
            print('Цена не может быть равна нулю или меньше.')


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str
    def __init__(self, name: str, description: str,  price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: object) -> int:
        if type(other) is Smartphone:
            return (self._Product__price*self.quantity)+(other._Product__price*other.quantity)
        raise TypeError



class LawnGrass(Product):
    country: str
    germination_period: float
    color: str
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str,
                 germination_period: float, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: object) -> int:
        if type(other) is LawnGrass:
            return (self._Product__price*self.quantity)+(other._Product__price*other.quantity)
        raise TypeError
