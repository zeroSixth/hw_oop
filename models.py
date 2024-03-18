from abc import ABC, abstractmethod


# Миксин для представления объектов с выводом всех их атрибутов
class LoggingMixin:
    def __repr__(self):
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"


# Базовый абстрактный класс продукта
class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Исключение для ситуации добавления товара с нулевым количеством
class ZeroQuantityError(Exception):
    def __init__(self, message):
        super().__init__(message)


# Класс продукта, включающий в себя основные свойства и методы
class Product(BaseProduct, LoggingMixin):
    def __init__(self, name, description, price, quantity):
        # Проверка на нулевое или отрицательное количество товара при его добавлении
        if quantity <= 0:
            raise ZeroQuantityError(f"Нельзя добавить товар '{name}' с нулевым или отрицательным количеством.")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. В наличии: {self.quantity} шт."


# Класс смартфона, наследующий свойства и методы от Product
class Smartphone(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return super().__str__() + f", Модель: {self.model}, Цвет: {self.color}, Память: {self.memory}GB"


# Класс газонной травы, также наследует от Product
class LawnGrass(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, country, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return super().__str__() + (f", Страна: {self.country}, "
                                    f"Время прорастания: {self.germination_time} дней, Цвет: {self.color}")


# Класс категории для группировки товаров
class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []

    # Добавление продукта в категорию с проверкой его типа
    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только товары и их подклассы.")
        self.products.append(product)

    # Расчет средней цены товаров в категории
    def average_price(self):
        if not self.products:
            return 0  # Возвращаем 0, если товаров нет, избегая деления на ноль
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)

    def __str__(self):
        return f"{self.name}, всего товаров: {len(self.products)}"


# Класс заказа, включающий в себя продукт и его количество
class Order(LoggingMixin):
    def __init__(self, product, quantity):
        # Проверка типа продукта и количества при создании заказа
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть продуктом или его подклассом.")
        if quantity <= 0:
            raise ZeroQuantityError("Нельзя оформить заказ на нулевое или отрицательное количество товара.")
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total_cost()

    # Расчет общей стоимости заказа
    def calculate_total_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Общая стоимость: {self.total_cost} руб."
