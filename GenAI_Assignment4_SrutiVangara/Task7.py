prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
discount = float(input("Enter discount percentage: "))
total_discounted = 0
with open("discount_report.txt", "w") as f:
    f.write("Product | Original Price | Discounted Price\n")
    f.write("-" * 45 + "\n")
    for product, price in prices.items():
        discounted_price = price - (price * discount / 100)
        total_discounted += discounted_price
        f.write(f"{product.ljust(15)} | {str(price).ljust(6)} | {discounted_price:.2f}\n")
# Read and print the file
with open("discount_report.txt", "r") as f:
    print("\n------------Discount Report------------\n")
    print(f.read())
