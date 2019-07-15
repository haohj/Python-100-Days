"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: haohj
Date: 2019-07-15
"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError
    fruits[1] = 'apple'
    print(fruits)
    # 添加元素
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)
    # 删除元素
    del fruits[1]
    #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    fruits.pop()
    fruits.pop(0)
    fruits.remove('apple')
    print(fruits)


if __name__ == '__main__':
    main()
