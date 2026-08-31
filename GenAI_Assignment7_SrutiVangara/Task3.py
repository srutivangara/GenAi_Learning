class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product Name : {self.name}")
        print(f"Price        : {self.price}")
        print(f"Category     : {self.category}")


class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        super().get_info()
        print(f"Warranty     : {self.warranty_years} Years")


electronic = ElectronicProduct("Laptop", 65000, "Electronics", 2)

electronic.get_info()