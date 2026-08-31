products = ["Books","Laptop","Headphones","Mobile","Pen Set","Ear Phones"]
# Sample product tuple (Product Name, Price, Category)
sample_product = ("Notebook", 120.25, "Stationery")

print("Original Tuple:")
print(sample_product)

# Convert tuple to list
product_list = list(sample_product)

# Change the price
product_list[1] = 150.00

# Convert back to tuple
sample_product = tuple(product_list)

print("\nUpdated Tuple:")
print(sample_product)