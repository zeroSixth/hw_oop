from abc import ABC, abstractmethod


class LoggingMixin:
    def __repr__(self):
        attributes = ', '.join(f"{k}={v}" for k, v in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"


class AbstractProduct(ABC, LoggingMixin):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(repr(self))

    @abstractmethod
    def __str__(self):
        pass


class Product(AbstractProduct):
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_time = germination_time
        self.color = color


class AbstractEntity(ABC, LoggingMixin):
    @abstractmethod
    def summary(self):
        pass


class Order(AbstractEntity):
    def __init__(self, product, quantity):
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
        print(repr(self))

    def summary(self):
        return (f"Заказ: {self.product.name}, Количество: {self.quantity}, "
                f"Итог: {self.total_cost} руб.")


class Category(AbstractEntity):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.products = []
        print(repr(self))

    def add_product(self, product):
        if not isinstance(product, AbstractProduct):
            raise ValueError("Можно добавлять только продукты и их наследников")
        self.products.append(product)

    def summary(self):
        return f"Категория: {self.name}, Всего продуктов: {len(self.products)}"
