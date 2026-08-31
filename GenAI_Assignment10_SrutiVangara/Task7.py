import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
data_students = pd.DataFrame(students)
print(data_students.groupby('Subject')['Marks'].mean())
print(data_students.groupby('Subject')['Name'].count())
print(data_students.groupby('Subject')['Marks'].max())