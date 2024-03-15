import pytest
from models import Product, Smartphone, LawnGrass, Category, Order

def test_product_init_and_str():
    product = Product("TestProduct", "Description", 100.0, 5)
    assert product.__str__() == "TestProduct, 100.0 руб. Остаток: 5 шт."
    assert "Product(name=TestProduct, description=Description, price=100.0, quantity=5)" == product.__repr__()

def test_smartphone_init_and_str():
    smartphone = Smartphone("TestPhone", "Smartphone Description", 30000, 10, "High", "ModelX", 128, "Black")
    expected_str = "TestPhone, 30000 руб. Остаток: 10 шт., Модель: ModelX, Цвет: Black, Память: 128GB"
    assert smartphone.__str__() == expected_str

def test_lawn_grass_init_and_str():
    grass = LawnGrass("TestGrass", "Grass Description", 500, 20, "USA", 7, "Green")
    expected_str = "TestGrass, 500 руб. Остаток: 20 шт., Страна: USA, Время прорастания: 7 дней, Цвет: Green"
    assert grass.__str__() == expected_str

def test_category_add_product_and_str():
    category = Category("TestCategory", "Category Description")
    product = Product("TestProduct", "Description", 100.0, 5)
    category.add_product(product)
    assert category.__str__() == "TestCategory, 1 продукт(ов)"
    with pytest.raises(ValueError):
        category.add_product("not a product")

def test_order_init_calculate_total_cost_and_str():
    product = Product("TestProduct", "Description", 100.0, 5)
    order = Order(product, 2)
    assert order.calculate_total_cost() == 200.0
    assert order.__str__() == "Заказ: TestProduct, Количество: 2, Итоговая стоимость: 200.0 руб."
    with pytest.raises(ValueError):
        Order("not a product", 1)
