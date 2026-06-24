from src.product import LawnGrass
from src.product import Smartphone
import pytest


def test_smart_grass():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                             180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                             98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                             90.3, "Note 11", 1024, "Синий")

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                       "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США",
                       "5 дней", "Темно-зеленый")

    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0

    smart_sum1 = smartphone1 + smartphone2
    assert smart_sum1 == 2580000.0

    smart_sum2 = smartphone1 + smartphone3
    assert smart_sum2 == 1334000.0

    with pytest.raises(TypeError):
        smartphone1 + grass1

    with pytest.raises(TypeError):
        smartphone3 + grass2
