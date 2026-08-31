import pandas as pd
marks = [78,85,60,66,72]
pd_marks = pd.Series(marks)
add = pd_marks+5
sub = pd_marks-2
mul = pd_marks*1.05
div = pd_marks/2
print("Add 5 grace marks:\n",add,"\nSubtract 2 marks:\n",sub,"\nMultiply all marks:\n",mul,"\nDivide all marks:\n",div)