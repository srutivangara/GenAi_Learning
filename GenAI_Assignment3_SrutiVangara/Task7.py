def add_prices(prices_list,price):
    return prices_list.append(price)
def get_average_price(prices_list):
    avg_price = sum(prices_list)/len(prices_list)
    return avg_price
def get_max_price(prices_list):
    return max(prices_list)
price=[100,200,450,360,480]
while True:
    print(price)
    print("-------MENU------")
    print("1.Add Price\n2.Show average price\n3.Show highest price\nq.Quit")
    choice = input("Enter your choice:")
    if choice == 1:
        p = int(input("Enter price to add:"))
        print("List after adding the price",add_prices(price,p))
    elif choice == 2:
        print("Average price:",get_average_price(price))
    elif choice == 3:
        print("Highest price:",get_max_price(price))
    else:
        break
    