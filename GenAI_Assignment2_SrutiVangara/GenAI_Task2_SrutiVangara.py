orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders = 0
print("Order\tDiscount\tFinal Amount")
print("--------------------------------------")

for order_amount in orders:

    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500:
        discount = 10
    elif order_amount >= 1000:
        discount = 7
    else:
        discount = 0

    discount_amount = (discount / 100) * order_amount
    final_amount = order_amount - discount_amount
    print(f"{str(order_amount).ljust(15)}{str(discount).ljust(6)}%{final_amount}")
    total_revenue += final_amount
   
print("--------------------------------------")
print("Total Revenue After Discounts:", total_revenue)
