"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: 骆昊
Date: 2019-07-12
"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for x in range(1,n + 1):
        result *= x
    return result
print(factorial(7) // factorial(3) // factorial(4))
