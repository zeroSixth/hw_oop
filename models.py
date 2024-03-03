class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно.")
        elif hasattr(self, '_price') and value < self._price:
            response = input("Понизить цену? y/n: ")
            if response == 'y':
                self._price = value
            else:
                print("Изменение цены отменено.")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list = None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self._products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self._products.append(product)
        Category.total_unique_products += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        return sum(product.quantity for product in self._products)

    @property
    def products(self):
        return '\n'.join([str(product) for product in self._products])


class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category._products):
            product = self._category._products[self._index]
            self._index += 1
            return product
        raise StopIteration
