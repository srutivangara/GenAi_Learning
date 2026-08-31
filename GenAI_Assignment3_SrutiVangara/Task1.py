def apply_discount(price,discount_percent=5):
    price = price - (discount_percent/100)
    print("Amount after dicount:",price)
apply_discount(1000,10)
apply_discount(500)
