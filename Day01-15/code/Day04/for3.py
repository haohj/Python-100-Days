"""
输入非负整数n计算n!
Version: 0.1
Author: haohj
Date: 2019-07-12
"""

n = int(input('n = '))

result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
