# Cython: language_level=3

# 找出可迭代对象中最大的元素
from functools import reduce

print(reduce(lambda x, y: x if x > y else y, [2, 1, 4, 3]))

print(reduce(lambda x, y: x if int(x.split('-')[-1]) > int(y.split('-')[-1]) else y,
             ['M01-01', 'M01-04', 'M01-02', 'M01-03']))


