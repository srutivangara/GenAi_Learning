import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Order Date.csv")

plt.hist(data["Sales"], bins=10)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()