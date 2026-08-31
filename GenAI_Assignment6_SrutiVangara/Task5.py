cart = []

while True:
    value = input("Enter price (or 'q' to quit): ")

    if value.lower() == "q":
        break

    try:
        price = float(value)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

print("Total Items:", len(cart))
print("Total Bill:", sum(cart))