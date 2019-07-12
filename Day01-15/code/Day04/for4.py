"""
输入一个正整数判断它是不是素数
Version: 0.1
Author: haohj
Date: 2019-07-12
"""
import math

n = int(input('n = '))
end = int(math.sqrt(n) + 1)

is_prime = True
for x in range(2, end):
    if n % x == 0:
        is_prime = False
        break
if is_prime and n != 1:
    print('%d是素数' % n)
else:
    print('%d不是素数' % n)
