from abc import ABC, abstractmethod


class LoggingMixin:
    """Mixin для добавления возможности представления объекта через __repr__."""
    def __repr__(self):
        attributes = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"


class BaseProduct(ABC):
    """Базовый абстрактный класс продукта."""
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(BaseProduct, LoggingMixin):
    """Класс продукта с основными атрибутами."""
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством!")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. В наличии: {self.quantity} шт."


class Smartphone(Product, LoggingMixin):
    """Класс смартфона, расширяющий класс продукта."""
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (super().__str__() +
                f", Модель: {self.model}, Цвет: {self.color}, Память: {self.memory}GB")


class LawnGrass(Product, LoggingMixin):
    """Класс газонной травы, расширяющий класс продукта."""
    def __init__(self, name, description, price, quantity, country, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return (super().__str__() +
                f", Страна: {self.country}, Время прорастания: {self.germination_time} дней, Цвет: {self.color}")


class Category:
    """Класс категории для группировки товаров."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        """Добавление продукта в категорию с проверкой типа."""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только товары и их подклассы.")
        self.products.append(product)

    def average_price(self):
        """Расчет средней цены товаров в категории."""
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0  # Возврат 0, если в категории нет товаров

    def __str__(self):
        return f"{self.name}, всего товаров: {len(self.products)}"


class Order(LoggingMixin):
    """Класс заказа, содержащий продукт и его количество."""
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть продуктом или его подклассом.")
        if quantity <= 0:
            raise ValueError("Нельзя оформить заказ на нулевое или отрицательное количество товара.")
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        """Расчет общей стоимости заказа."""
        return self.product.price * self.quantity

    def __str__(self):
        return (f"Заказ: {self.product.name}, Количество: {self.quantity}, "
                f"Общая стоимость: {self.total_cost} руб.")
