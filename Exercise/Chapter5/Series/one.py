import numpy as np
from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])

# 最简单的 Series
# print(obj)
# 通过 Series 的 values 和 index 属性获取其数组表示形式和索引对象
# print('values', obj.values, 'index', obj.index)

# 通常，我们希望所创建的 Series 带有一个可以对各个数据点进行标记的索引：
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

# 与普通的Numpy数组相比，可以通过索引的方式选取Series中的一个或一组值
# print(obj2['a'])

# 赋值
obj2['d'] = 6
# 取值
# print(obj2[['c', 'a', 'd']])

# 数组运算都会保留索引和值之间的链接
print(obj2)
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# 可以把Series 是一个定长的有序字典，因为他是索引值到数据值的一个映射。
print('b' in obj2)
print('e' in obj2)

# 如果数据被存放在一个 Python 字典中，也可以直接通过这个字典来创建 Series
# 如果只传入一个字典，则结果 Series 的索引就是原字典的键（有序排列）
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = Series(sdata, index=states)
print(obj4)

# pandas 的 isnull 函数和 notnull 函数可用于检测确实数据
print(pd.isnull(obj4), pd.notnull(obj4))

# Series 也有类似的实例方法
print(obj4.isnull())

# Series 的一个重要的功能是：它在算术运算中会自动对齐不同索引的数据
print(obj3, '\n', obj4, '\n', obj3+obj4)

# Series 对象本身及其索引都有一个name属性，该属性跟 pandas 其他的关键功能关系非常密切
obj4.name = 'population'
obj4.index.name = 'state'

print(obj4)

# Series 索引可以通过赋值的方式就地修改：
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
