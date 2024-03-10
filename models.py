class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Нельзя складывать продукты разных классов")


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
        return super().__str__() + (f", Страна: {self.country}, Время прорастания: {self.germination_time} дней, Цвет:"
                                    f" {self.color}")


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
