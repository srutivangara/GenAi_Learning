import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Order Date.csv")

plt.scatter(data["Sales"], data["Profit"])

plt.title("Relationship Between Sales and Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()