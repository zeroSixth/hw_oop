from abc import ABC, abstractmethod


class LoggingMixin:
    def __repr__(self):
        attributes = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ZeroQuantityError(Exception):
    """Исключение для товаров с нулевым или отрицательным количеством."""
    def __init__(self, message):
        super().__init__(message)


class Product(BaseProduct, LoggingMixin):
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ZeroQuantityError(
                f"Нельзя добавить товар '{name}' с нулевым или отрицательным количеством."
            )
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. В наличии: {self.quantity} шт."


class Smartphone(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            super().__str__() +
            f", Модель: {self.model}, Цвет: {self.color}, Память: {self.memory}GB"
        )


class LawnGrass(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, country, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return (
            super().__str__() +
            f", Страна: {self.country}, Время прорастания: {self.germination_time} дней, Цвет: {self.color}"
        )


class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только товары и их подклассы.")
        self.products.append(product)

    def average_price(self):
        if not self.products:
            return 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)

    def __str__(self):
        return f"{self.name}, всего товаров: {len(self.products)}"


class Order(LoggingMixin):
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть продуктом или его подклассом.")
        if quantity <= 0:
            raise ZeroQuantityError(
                "Нельзя оформить заказ на нулевое или отрицательное количество товара."
            )
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f"Заказ: {self.product.name}, Количество: {self.quantity}, "
            f"Общая стоимость: {self.total_cost} руб."
        )
