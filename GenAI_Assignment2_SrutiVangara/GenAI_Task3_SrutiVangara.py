orders = []

while True:
    print("\n===== MENU =====")
    print("1. Add order amount\n2. Show all orders and totals after discounts\nq. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        order = int(input("Enter order amount: "))
        orders.append(order)
        print("Order added successfully!")

    elif choice == "2":
        if len(orders) == 0:
            print("No orders available.")
        else:
            total = 0

            print("\nOrder\tDiscount\tFinal Amount")

            for order in orders:
                if order >= 2000:
                    discount = order * 0.15
                elif order >= 1500:
                    discount = order * 0.10
                elif order >= 1000:
                    discount = order * 0.07
                else:
                    discount = 0

                final_amount = order - discount
                total += final_amount
                print(f"{order}\t{discount}\t\t%{final_amount}")
            print("\nTotal Revenue After Discounts:", total)

    elif choice.lower() == "q":
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")
        continue