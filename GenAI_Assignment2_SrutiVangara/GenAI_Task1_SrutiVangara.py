try:
    order_amount = int(input("Enter amount:"))
    if order_amount>=2000:
        final_amount = order_amount - int(0.15*order_amount)
    elif order_amount>=1500:
        final_amount = order_amount - int(0.10*order_amount)
    elif order_amount>=1000:
        final_amount = order_amount - int(0.07*order_amount)
    else :
        final_amount = order_amount
    print("Amount:",final_amount)
except ValueError:
    print("Error! Please enter an integer value")