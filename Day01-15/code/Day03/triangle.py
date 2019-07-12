"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
Version: 0.1
Author: haohj
Date: 2019-07-12
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# 两边之和大于第三边
if a + b > c and a + c > b and b + c > a:
    print('三角形的周长是：%.2f' % (a + b + c))
    # 海伦公式 p=(a+b+c)/2,S=sqrt[p(p-a)(p-b)(p-c)]
    p = (a + b + c) / 2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print('三角形的面积是：%.2f' % s)
else:
    print('不能构成三角形')
