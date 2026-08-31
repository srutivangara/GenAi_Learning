sales = [5000,2500,1700]
with open("sales_data.txt","a") as f:
    for sale in sales:
        f.write(f"{sale}\n")
with open("sales_data.txt","r") as f:
    print(f.read())