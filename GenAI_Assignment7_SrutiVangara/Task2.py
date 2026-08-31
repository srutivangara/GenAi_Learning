class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully.")
        else:
            print("Invalid price! Price should be greater than 0.")

    def get_info(self):
        print(f"Product Name : {self.name}")
        print(f"Price        : {self.__price}")
        print(f"Category     : {self.category}")


product = Product("Laptop", 60000, "Electronics")

product.get_info()

print("\nCurrent Price:", product.get_price())

product.set_price(55000)

print("Updated Price:", product.get_price())

product.get_info()