import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("diabetes.csv")

# Create age groups for comparison
data["Age Group"] = pd.cut(data["Age"], bins=[20, 30, 40, 50, 100], labels=["21-30", "31-40", "41-50", "51+"])

# Count the number of diabetic and non-diabetic patients in each age group
grouped_data = data.groupby(["Age Group", "Outcome"], observed=False).size().unstack(fill_value=0)

# Create positions for the bars
x = np.arange(len(grouped_data))

# Get the number of patients with Outcome 0
not_diabetic = grouped_data[0]

# Get the number of patients with Outcome 1
diabetic = grouped_data[1]

# Set the width of the bars
width = 0.6

# Create the first part of the stacked bars
plt.bar(x, not_diabetic, width=width, align="center", label="Not Diabetic")

# Create the second part on top of the first bars using bottom
plt.bar(x, diabetic, width=width, align="center", bottom=not_diabetic, label="Diabetic")

# Add title and axis labels
plt.title("Diabetes Outcome by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")

# Add age group names to the x-axis
plt.xticks(x, grouped_data.index)

# Add a legend
plt.legend()

# Display the stacked bar chart
plt.show()