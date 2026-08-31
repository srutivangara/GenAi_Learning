class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(Name={self.name}, Price={self.price}, Category={self.category})"

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Laptop", 60000, "Electronics")
product2 = Product("Phone", 30000, "Electronics")

print(product1)
print(product2)

print("Total Price:", product1 + product2)