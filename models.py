from abc import ABC, abstractmethod


class LoggingMixin:
    def __repr__(self):
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"


class BaseProduct(ABC, LoggingMixin):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass


class Product(BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return super().__str__() + f", Модель: {self.model}, Цвет: {self.color}, Память: {self.memory}GB"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return super().__str__() + (f", Страна: {self.country}, "
                                    f"Время прорастания: {self.germination_time} дней, Цвет: {self.color}")


class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только продукты и их наследников")
        self.products.append(product)

    def __str__(self):
        return f"{self.name}, {len(self.products)} продукт(ов)"


class Order(LoggingMixin):
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть продуктом или его наследником")
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_cost} руб."
