import pytest
from models import Product, Smartphone, LawnGrass, Category, Order


def test_product_initialization_and_str():
    product = Product("TestProduct", "A product for testing", 100.0, 10)
    assert str(product) == "TestProduct, 100.0 руб. Остаток: 10 шт."


def test_smartphone_specific_behavior():
    smartphone = Smartphone("TestPhone", "A smartphone for testing", 30000, 5,
                            "High", "ModelX", 128, "Black")
    assert str(smartphone).endswith(", Модель: ModelX, Цвет: Black, Память: 128GB")


def test_lawn_grass_specific_behavior():
    grass = LawnGrass("TestGrass", "Grass for testing", 500, 20, "USA",
                      7, "Green")
    assert str(grass).endswith(", Страна: USA, Время прорастания: 7 дней, Цвет: Green")


def test_category_handling_products():
    category = Category("TestCategory", "A category for testing")
    product = Product("TestProduct", "A product for testing", 100.0, 10)
    category.add_product(product)
    assert str(category) == "TestCategory, 1 продукт(ов)"
    with pytest.raises(ValueError):
        category.add_product("not a product")


def test_order_calculation_and_str():
    product = Product("TestProduct", "A product for testing", 100.0, 10)
    order = Order(product, 2)
    assert order.calculate_total_cost() == 200.0
    assert str(order) == "Заказ: TestProduct, Количество: 2, Итоговая стоимость: 200.0 руб."

    with pytest.raises(ValueError):
        Order("not a product", 1)
