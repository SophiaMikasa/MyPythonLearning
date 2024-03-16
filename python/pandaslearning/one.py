import pandas as pd
import string

t = pd.Series([1, 2, 31, 12, 3, 4])
print(t)

t2 = pd.Series([1, 23, 2, 2, 1, 2, 3, 4, 2, 3], index=list('abcdefghij'))
print(t2)

temp_dict = {'name': 'xiaohong', 'age': 30, 'tel': 10086}
t3 = pd.Series(temp_dict)
print(t3)

a = {string.ascii_uppercase[i]: i for i in range(10)}
t4 = pd.Series(a)
print(t4)

print(t2[t2>10])