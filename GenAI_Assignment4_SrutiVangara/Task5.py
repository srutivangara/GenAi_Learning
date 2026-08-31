with open("products.txt","w") as f:
    for i in range(3):
        pro_name , price = input("Enter Product name and price(with space in between): ").split()
        f.write(f"{pro_name.ljust(15)} | {price.ljust(6)}\n")

with open("products.txt","r") as f:
    print(f.read())
