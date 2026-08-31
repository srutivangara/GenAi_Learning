import pandas as pd
marks = [78,85,90,66,72]
pd_marks = pd.Series(marks)
print(pd_marks.values)
print(pd_marks.index)
print(pd_marks.dtype)
print(pd_marks.head(1))
print(pd_marks.tail(2))