import pandas as pd
marks = [78,85,60,66,72]
pd_marks = pd.Series(marks)
print(pd_marks.max())
print(pd_marks.min())
print(pd_marks.sum())
print(pd_marks.mean())
result = pd_marks.apply(lambda x: "Pass" if x>=70 else None)
print(result.count())