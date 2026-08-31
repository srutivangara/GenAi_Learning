# Healthcare Diabetes Data Visualization

## Introduction

This project is based on a Healthcare Diabetes dataset downloaded from Kaggle.

The main objective of this project is to use Python and Matplotlib to create different types of visualizations. These visualizations help us understand the data, identify relationships between numerical values, compare different groups, and study the distribution of healthcare-related information.

## Dataset

The dataset used in this project is a Healthcare Diabetes dataset obtained from Kaggle.

The dataset contains patient-related information that can be used to analyze diabetes and other health-related factors.

Some of the important columns used in the project include:

- Age
- BMI
- Glucose
- BloodPressure
- Outcome

The `Outcome` column represents the diabetes result, where:

- `0` represents a patient who is not diabetic
- `1` represents a patient who is diabetic

## Technologies Used

- Python
- Pandas
- Matplotlib
- NumPy
- Kaggle

## Python Libraries

The following Python libraries are used in this project:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
````

## Project Structure

The project can be organized as follows:

```text
Healthcare-Diabetes-Visualization/
│
├── diabetes.csv
├── task1_line_plot.py
├── task2_scatter_plot.py
├── task3_bar_plot.py
├── task4_multiple_bar_plot.py
├── task5_stacked_bar_chart.py
├── task6_histogram.py
├── task7_pie_chart.py
└── README.md
```

## Conclusion

This project demonstrates how Python, Pandas, NumPy, and Matplotlib can be used to visualize healthcare diabetes data.

Different types of plots provide different ways of understanding the dataset. Line plots help show trends, scatter plots show relationships, bar charts compare groups, stacked bar charts show the composition of groups, histograms show numerical distributions, and pie charts show category proportions.

The project also demonstrates the direct use of Matplotlib functions such as `plt.bar()` for multiple and stacked bar charts, including bar width, alignment, legends, and the `bottom` parameter.
