class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(self.name)


class Laptop(Product):
    def get_info(self):
        print(f"Laptop -> {self.name}, {self.price}, {self.category}")


class Mobile(Product):
    def get_info(self):
        print(f"Mobile -> {self.name}, {self.price}, {self.category}")


products = [
    Laptop("HP Victus", 70000, "Electronics"),
    Mobile("Samsung S25", 80000, "Electronics")
]

for product in products:
    product.get_info()