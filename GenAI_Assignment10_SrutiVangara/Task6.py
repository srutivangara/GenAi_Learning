import pandas as pd
students = {
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
data_students = pd.DataFrame(students)
avg = data_students['Marks'].mean()
print(data_students[data_students['Marks']>75])
print(data_students[data_students['Subject']=='Math'])
print(data_students[data_students['Marks']<70])
print(data_students[data_students['Marks']>avg])