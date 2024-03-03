import pytest
from models import Product, Category, CategoryIterator


class TestProduct:
    def test_product_str(self):
        product = Product("Test Product", "Description", 100.0, 10)
        assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."

    def test_product_add(self):
        product1 = Product("Product 1", "Description 1", 100.0, 10)
        product2 = Product("Product 2", "Description 2", 200.0, 5)
        assert product1 + product2 == 2000


class TestCategory:
    def test_category_str_and_len(self):
        category = Category("Test Category", "Category Description")
        assert str(category) == "Test Category, количество продуктов: 0 шт."
        assert len(category) == 0

        product = Product("Test Product", "Description", 100.0, 10)
        category.add_product(product)
        assert str(category) == "Test Category, количество продуктов: 10 шт."
        assert len(category) == 10

    def test_category_products_property(self):
        category = Category("Test Category", "Category Description")
        product = Product("Test Product", "Description", 100.0, 10)
        category.add_product(product)
        expected_output = "Test Product, 100.0 руб. Остаток: 10 шт."
        assert category.products == expected_output


class TestCategoryIterator:
    def test_iterator(self):
        category = Category("Test Category", "Category Description")
        product1 = Product("Product 1", "Description 1", 100.0, 10)
        product2 = Product("Product 2", "Description 2", 200.0, 5)
        category.add_product(product1)
        category.add_product(product2)

        iterator = CategoryIterator(category)
        products_list = list(iterator)

        assert products_list == [product1, product2]
        assert len(products_list) == 2
