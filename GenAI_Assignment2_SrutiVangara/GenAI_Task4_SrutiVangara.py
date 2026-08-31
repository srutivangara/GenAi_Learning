daily = [200,150,0,400,50,-1,300]
total_sales = 0
for sale in daily:
    if sale == -1:
        break
    elif sale == 0:
        continue
    else:
        total_sales += sale
        print("Running total sale:",total_sales)
print("Total sales:",total_sales)