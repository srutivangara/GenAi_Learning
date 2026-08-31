with open("sales_data.txt","r") as f:
    first_line = f.readline().strip()
    sale_list = [int(line.strip()) for line in f.readlines() if line.strip()]
total_sales = sum(sale_list)
highest_sales = max(sale_list)
lowest_sales = min(sale_list)
average_sales = (highest_sales+lowest_sales)/len(sale_list)
print(f"Total sales : {total_sales} \nHighest sales : {highest_sales} \nLowest sale: {lowest_sales} \nAverage sale : {average_sales}")