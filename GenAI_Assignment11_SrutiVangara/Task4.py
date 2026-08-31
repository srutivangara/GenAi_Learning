import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("diabetes.csv")

# Create age groups to compare the average glucose and BMI values
data["Age Group"] = pd.cut(data["Age"], bins=[20, 30, 40, 50, 100], labels=["21-30", "31-40", "41-50", "51+"])

# Calculate average glucose and BMI for each age group
grouped_data = data.groupby("Age Group", observed=False)[["Glucose", "BMI"]].mean()

# Create positions for the bars
x = np.arange(len(grouped_data))

# Set the width of each bar
width = 0.35

# Create the first set of bars
plt.bar(x - width / 2, grouped_data["Glucose"], width=width, align="center", label="Glucose")

# Create the second set of bars
plt.bar(x + width / 2, grouped_data["BMI"], width=width, align="center", label="BMI")

# Add title and axis labels
plt.title("Average Glucose and BMI by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Value")

# Add age group names to the x-axis
plt.xticks(x, grouped_data.index)

# Add a legend to identify the bars
plt.legend()

# Display the multiple bar chart
plt.show()