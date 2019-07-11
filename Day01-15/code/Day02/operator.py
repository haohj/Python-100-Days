"""
运算符的使用
Version: 0.1
Author: haohj
Date: 2019-07-11
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print(" a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1

print('flag1 = ', flag1)  # ture
print('flag2 = ', flag2)  # false
print('flag3 = ', flag3)  # false
print('flag4 = ', flag4)  # true
print('flag5 = ', flag5)  # false
print(flag1 is True)  # true
print(flag1 is not False)  # true
