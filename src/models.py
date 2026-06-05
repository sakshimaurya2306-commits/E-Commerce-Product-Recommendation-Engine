class Product:
    def __init__(self, product_id, name, category, brand, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = brand
        self.price = float(price)

    def __str__(self):
        return f"{self.product_id} | {self.name} | {self.category} | {self.brand} | Rs.{self.price}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"{self.user_id} | {self.name}"