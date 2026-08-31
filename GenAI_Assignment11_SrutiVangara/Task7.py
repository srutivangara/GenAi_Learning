import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Order Date.csv")

sales = data.groupby("Category")["Sales"].sum()

plt.pie(sales, labels=sales.index, autopct="%1.1f%%")

plt.title("Market Share by Category")

plt.show()