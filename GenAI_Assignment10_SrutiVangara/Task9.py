import pandas as pd

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

data_sales = pd.DataFrame(sales)
print(data_sales['Revenue'].sum())
print(data_sales['Revenue'].mean())
print(data_sales.loc[data_sales['Revenue'].idxmax()])
avg = data_sales['Revenue'].mean()
print(data_sales[data_sales['Revenue'] > avg])
data_sales.plot(x='Day', y='Revenue', kind='line')