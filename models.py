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

    @property
    def products(self):
        return '\n'.join([f"{product.name}, {product.price} руб. Остаток: "
                          f"{product.quantity} шт." for product in self._products])


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

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products_list=None):
        if products_list is not None:
            for product in products_list:
                if product.name == name:
                    if price > product.price:
                        product.price = price
                    product.quantity += quantity
                    return product
        return cls(name, description, price, quantity)
