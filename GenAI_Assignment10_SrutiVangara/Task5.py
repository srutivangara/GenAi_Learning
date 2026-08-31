import pandas as pd
students = {
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
data_students = pd.DataFrame(students)
print(data_students.info())
print(data_students.describe())
print(data_students.head())
print(data_students.tail())
print(data_students.sort_values(by = 'Marks',ascending =False))
print(data_students.sort_values(by = 'Marks',ascending =False).reset_index(drop=True))