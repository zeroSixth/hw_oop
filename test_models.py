import pytest
from models import Product, Smartphone, LawnGrass, Category, Order


# Тест создания продукта и представления его в виде строки
def test_product_creation_and_str_representation():
    product = Product("Тестовый продукт", "Описание", 100, 10)
    assert str(product) == "Тестовый продукт, 100 руб. В наличии: 10 шт."


# Тест на исключение при попытке создать продукт с нулевым количеством
def test_product_zero_quantity_exception():
    with pytest.raises(ValueError):
        Product("Тестовый продукт", "Описание", 100, 0)


# Тест создания смартфона и проверка его строкового представления
def test_smartphone_creation_and_str_representation():
    smartphone = Smartphone("Телефон", "Описание", 30000, 5, "Высокая", "X100", 128, "Черный")
    expected_str = "Телефон, 30000 руб. В наличии: 5 шт., Модель: X100, Цвет: Черный, Память: 128GB"
    assert str(smartphone) == expected_str


# Тест создания газонной травы и проверка ее строкового представления
def test_lawn_grass_creation_and_str_representation():
    lawn_grass = LawnGrass("Газон", "Описание", 500, 20, "Россия", 7, "Зеленый")
    expected_str = "Газон, 500 руб. В наличии: 20 шт., Страна: Россия, Время прорастания: 7 дней, Цвет: Зеленый"
    assert str(lawn_grass) == expected_str


# Тест добавления продуктов в категорию и расчет средней цены
def test_category_add_product_and_average_price():
    category = Category("Категория", "Описание")
    product1 = Product("Продукт 1", "Описание", 100, 10)
    product2 = Product("Продукт 2", "Описание", 200, 5)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == 150
    assert str(category) == "Категория, всего товаров: 2"


# Тест создания заказа и расчета его общей стоимости
def test_order_creation_and_total_cost():
    product = Product("Продукт", "Описание", 100, 10)
    order = Order(product, 2)
    assert order.total_cost == 200
    assert str(order) == "Заказ: Продукт, Количество: 2, Общая стоимость: 200 руб."


# Тест на исключение при попытке создать заказ с нулевым количеством товара
def test_order_zero_quantity_exception():
    product = Product("Продукт", "Описание", 100, 10)
    with pytest.raises(ValueError):
        Order(product, 0)
