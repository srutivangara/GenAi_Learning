import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Order Date.csv")

data["Order Date"] = pd.to_datetime(data["Order Date"])

data["Month"] = data["Order Date"].dt.month

sales = data.groupby("Month")["Sales"].sum()

plt.plot(sales.index, sales.values, marker="o")

plt.title("Sales Trend Over Months")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()