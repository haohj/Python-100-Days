"""
输入半径计算圆的周长和面积
Version: 0.1
Author: haohj
Date: 2019-07-11
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('圆的周长为：%.2f' % perimeter)
print('圆的面积为：%.2f' % area)
