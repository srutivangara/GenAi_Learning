import numpy as np
sales = ([1200,1500,900,2000,1800,1700,1600])
print("Total weekly sales:",np.sum(sales))
avg = np.mean(sales)
print("Average daily sales:",avg)
print(f"Highest sales day:{np.max(sales)},Lowest sales day{np.min(sales)}")
print("Standard deviation:",np.std(sales))
print("Sales above average:")
for i in sales:
    if i>avg:
        print(i,end =" | ")
