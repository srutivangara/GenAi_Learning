class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product Name : {self.name}")
        print(f"Price        : {self.price}")
        print(f"Category     : {self.category}")

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        return self.price - discount
product1 = Product("Laptop", 60000, "Electronics")
product2 = Product("Shoes", 2500, "Fashion")
product1.get_info()
print()
product2.get_info()
print()
print("Discounted Price:", product1.apply_discount(10))