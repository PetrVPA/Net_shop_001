from src.utils import create_category_from_json
from src.utils import download_file

data_test = [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации,"
                   " но и получение дополнительных функций для удобства жизни",
                   "products":
    [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
                   " станет вашим другом и помощником", "products":
    [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]


def test_download_file():
    raw_data = download_file(r"C:\Users\Nochtcha\PycharmProjects\Net_shop_001\data\products.json")
    assert raw_data == data_test


def test_create_category_from_json():
    answer = create_category_from_json(data_test)
    assert answer[0].products[0] == 'Samsung Galaxy C23 Ultra, 180000.0 руб. остаток: 5 шт.\n'
    assert answer[0].products == ['Samsung Galaxy C23 Ultra,'
                                  ' 180000.0 руб. остаток: 5 шт.\n', 'Iphone 15, 210000.0 руб. остаток: 8 шт.\n',
                                  'Xiaomi Redmi Note 11, 31000.0 руб. остаток: 14 шт.\n']
    assert answer[1].products[0] == '55" QLED 4K, 123000.0 руб. остаток: 7 шт.\n'
    assert answer[1].description == ("Современный телевизор, который позволяет наслаждаться просмотром,"
                                     " станет вашим другом и помощником")
