# GenAI Assignment 12 – Seaborn Data Visualization

## 📌 Overview

This assignment focuses on data visualization using **Python, Pandas, Matplotlib, and Seaborn**.

The objective is to explore a sales dataset and create different types of visualizations to understand relationships, distributions, categorical comparisons, and correlations within the data.

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📂 Dataset

The project uses a sales dataset containing information such as:

- Product ID
- Product Category
- Region
- Quantity Sold
- Unit Price
- Unit Cost
- Sales Amount
- Discount

## 📊 Tasks Covered

### Task 1 – Relational Plot
- Created a relational plot using numerical variables.
- Used a categorical variable with `hue` to differentiate groups.

### Task 2 – Line Plot, Scatter Plot & Facet
- Created a line plot using `sns.lineplot()`.
- Created a scatter plot using `sns.scatterplot()`.
- Used faceting to split the visualization based on a categorical column.

### Task 3 – Univariate Distribution
Created different visualizations for a numerical variable:
- Histogram using `sns.histplot()`
- KDE plot
- Rug plot
- Histogram combined with KDE

### Task 4 – Bivariate Distribution
Used two numerical variables to create:
- Bivariate histogram
- Bivariate KDE plot

### Task 5 – Pair Plot & Correlation Heatmap
- Created a pair plot using `sns.pairplot()`.
- Created a correlation matrix using Pandas.
- Visualized the correlation matrix using `sns.heatmap()`.

### Task 6 – Categorical Plots
Created:
- Bar plot
- Box plot
- Violin plot
- Count plot

These plots were used to analyze numerical variables across categorical groups.

### Task 7 – Regression Plot
- Created a regression plot using `sns.regplot()`.
- Created an `lmplot()` with a categorical variable using `hue`.

### Task 8 – Multi-Plot & Figure-Level Plots
- Created a `FacetGrid` using numerical variables on the X and Y axes.
- Used a categorical variable for faceting.
- Created visualizations using:
  - `sns.relplot()`
  - `sns.catplot()`
  - `sns.displot()`

## 📁 Project Structure

```text
GenAI_Assignment12/
│
├── sales_data.csv
├── Task1.ipynb
├── Task2.ipynb
├── Task3.ipynb
├── Task4.ipynb
├── Task5.ipynb
├── Task6.ipynb
├── Task7.ipynb
├── Task8.ipynb
└── README.md