sales = [1200,450,980,1500,3000]
with open("sales_data.txt","w") as f:
    for sale in sales:
        f.write(f"{str(sale)}\n")
with open("sales_data.txt","r") as f:
    data = f.read()
    print(data)