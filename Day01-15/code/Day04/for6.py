"""
打印各种三角形图案
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
Version: 0.1
Author: haohj
Date: 2019-07-12
"""

row = int(input('请输入行数：'))

for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
