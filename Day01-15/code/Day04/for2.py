"""
用for循环实现1~100之间的偶数求和
Version: 0.1
Author: haohj
Date: 2019-07-12
"""
sum = 0
for x in range(2, 101, 2):
    print(x)
    sum += x
print(sum)
