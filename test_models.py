import pytest
from models import Category, Product

@pytest.fixture(autouse=True)
def setup():
    Category.total_categories = 0
    Category.total_unique_products = set()

def test_product_initialization():
    product = Product("TestProduct", "A product for testing", 10.99, 100)
    assert product.name == "TestProduct"
    assert product.description == "A product for testing"
    assert product.price == 10.99
    assert product.quantity == 100

def test_category_initialization():
    product = Product("TestProduct", "A product for testing", 10.99, 100)
    category = Category("TestCategory", "A category for testing", [product])
    assert category.name == "TestCategory"
    assert category.description == "A category for testing"
    assert len(category.products) == 1
    assert Category.total_categories == 1
    assert "TestProduct" in Category.total_unique_products

def test_unique_product_addition():
    product1 = Product("TestProduct1", "First product for testing", 20.99, 50)
    product2 = Product("TestProduct2", "Second product for testing", 15.99, 75)
    category = Category("TestCategory", "A category for testing", [product1, product2])
    assert len(Category.total_unique_products) == 2

def test_duplicate_product_addition():
    product1 = Product("TestProduct", "A product for testing", 10.99, 100)
    Category("TestCategory1", "First category for testing", [product1])
    Category("TestCategory2", "Second category for testing", [product1])
    assert len(Category.total_unique_products) == 1
    assert Category.total_categories == 2

def test_category_without_products():
    category = Category("EmptyCategory", "A category without products", [])
    assert len(category.products) == 0
    assert Category.total_categories == 1

def test_adding_product_updates_unique_products():
    product = Product("NewProduct", "A new product", 25.50, 30)
    new_category = Category("NewCategory", "A new category", [product])
    assert "NewProduct" in Category.total_unique_products
