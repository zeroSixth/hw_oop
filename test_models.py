import pytest
from unittest.mock import patch
from models import Category, Product


# Сброс статических переменных перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_class():
    Category.total_categories = 0
    Category.total_unique_products = 0


def test_product_initialization():
    product = Product("Apple", "Fresh Apples", 1.99, 50)
    assert product.name == "Apple"
    assert product.description == "Fresh Apples"
    assert product.price == 1.99
    assert product.quantity == 50


def test_category_initialization():
    category = Category("Fruits", "All kinds of fruits")
    assert category.name == "Fruits"
    assert category.description == "All kinds of fruits"
    assert category.products == ""


def test_add_product_to_category():
    category = Category("Fruits", "All kinds of fruits")
    product = Product("Apple", "Fresh Apples", 1.99, 50)
    category.add_product(product)
    assert "Apple, 1.99 руб. Остаток: 50 шт." in category.products


def test_create_product_class_method_no_duplicates():
    category = Category("Fruits", "All kinds of fruits")
    product = Product.create_product("Banana", "Fresh Bananas", 0.99, 100)
    category.add_product(product)
    assert "Banana, 0.99 руб. Остаток: 100 шт." in category.products


def test_price_setter_invalid_value(capsys):
    product = Product("Apple", "Fresh Apples", 1.99, 50)
    product.price = -1  # Установка некорректной цены
    captured = capsys.readouterr()  # Чтение вывода
    assert "Цена введена некорректно." in captured.out  # Проверка наличия сообщения об ошибке
    assert product.price == 1.99  # Убедимся, что цена не изменилась


def test_price_setter_with_valid_value():
    product = Product("Apple", "Fresh Apples", 2.99, 50)
    with patch('builtins.input', return_value='y'):
        product.price = 2.50
    assert product.price == 2.50


def test_total_categories_and_unique_products():
    product1 = Product("Apple", "Fresh Apples", 1.99, 50)
    product2 = Product("Banana", "Fresh Bananas", 0.99, 100)
    Category("Fruits", "All kinds of fruits", [product1])
    Category("Vegetables", "Fresh Vegetables", [product2])
    assert Category.total_categories == 2
    assert Category.total_unique_products == 2
