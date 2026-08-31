import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Order Date.csv")

sales = data.groupby("Category")["Sales"].sum()

plt.bar(sales.index, sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

data = pd.read_csv("Order Date.csv")

sales = data.groupby("Category")["Sales"].sum()

plt.barh(sales.index, sales.values)

plt.title("Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Category")

plt.show()