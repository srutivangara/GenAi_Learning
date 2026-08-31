from GenAI_Task1_SrutiVangara import products

price_dict = {
    "Laptop": 69000,
    "Headphones": 2000,
    "Mobile": 25000,
    "Hair Serum": 370.45,
    "Ear Phones": 1200,
    "Notebook": 120.25
}

def add_product(name, price):
    price_dict[name] = price
    print(f"{name} added successfully.")

def update_price(name, new_price):
    if name in price_dict:
        price_dict[name] = new_price
        print(f"{name} price updated.")
    else:
        print("Product not found.")

def remove_product(name):
    try:
        del price_dict[name]
        print(f"{name} removed successfully.")
    except KeyError:
        print(f"{name} does not exist.")

add_product("Keyboard", 1200)
update_price("Notebook", 150)
remove_product("Hair Serum")

average = sum(price_dict.values()) / len(price_dict)
print("Average Price:", average)
