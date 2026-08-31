with open("sales_data.txt","r") as f:
    print(f.read())
    f.seek(0)
    first_line = f.readline().strip()
    sale_list = [int(line.strip()) for line in f.readlines() if line.strip()]
print(sale_list)
print("First line:",first_line)