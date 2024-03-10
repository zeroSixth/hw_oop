import pytest
from models import Product, Smartphone, LawnGrass, Category


def test_product_addition():
    phone1 = Smartphone("Phone1", "High-end smartphone", 50000, 10, "High", "ModelX", 128, "Black")
    phone2 = Smartphone("Phone2", "Budget smartphone", 20000, 20, "Medium", "ModelY", 64, "Blue")
    assert phone1 + phone2 == (50000 * 10) + (20000 * 20)

    grass1 = LawnGrass("Grass1", "High-quality lawn grass", 1000, 50, "Germany", 7, "Green")
    with pytest.raises(TypeError):
        _ = phone1 + grass1


def test_category_product_addition():
    electronics = Category("Electronics", "Gadgets and more")
    phone = Smartphone("Phone1", "High-end smartphone", 50000, 10, "High", "ModelX", 128, "Black")
    electronics.add_product(phone)
    assert len(electronics.products) == 1

    with pytest.raises(ValueError):
        electronics.add_product("Not a Product Object")
