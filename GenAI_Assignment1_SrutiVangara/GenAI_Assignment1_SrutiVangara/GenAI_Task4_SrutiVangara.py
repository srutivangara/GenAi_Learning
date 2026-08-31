from GenAI_Task1_SrutiVangara import products
from GenAI_Task2_SrutiVangara import categories
from GenAI_Task3_SrutiVangara import price_dict

# Create catalog
catalog = []

for product, category in zip(products, categories):
    if product in price_dict:
        catalog.append((product, price_dict[product], category))

print("Catalog:")
for item in catalog:
    print(item)

# Create category_to_products dictionary
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("\nCategory to Products:")
print(category_to_products)

# Print products in category with maximum products
max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("\nCategory with Maximum Products:", max_category)
print("Products:")

for product in category_to_products[max_category]:
    print(product)