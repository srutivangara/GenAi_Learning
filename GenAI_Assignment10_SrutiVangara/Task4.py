import pandas as pd
students = {
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
data_students = pd.DataFrame(students)
print(data_students.head(3))
print(data_students.tail(2))
print(data_students.shape)
print(data_students.columns)