import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

data_students = pd.DataFrame(students)
data_students.plot(x = 'Name',y = 'Marks',kind='bar')
data_students['Marks'].plot(kind='line')
data_students['Marks'].plot(kind='hist')