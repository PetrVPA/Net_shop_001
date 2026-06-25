from src.product import Product


if __name__ == "__main__":
    product1 = Product('Ракета Х55', 'Ракета воздух-поверхность', 1256000.00, 26)
    product2 = Product('Ракета Р-73Э', 'Ракета воздух-воздух', 117000.00, 112)
    product3 = Product('Ракета Р-60', 'Ракета воздух-воздух', 98000.00, 212)

    print(f"Стоимость единицы: {product3.price} рублей.")
    print(f"Можем поствить: {product3.quantity} штук.")
