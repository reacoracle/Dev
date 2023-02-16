"""
    已知一个列表和字典, 获取字典的键不在列表中的所有键值对.
    example:
        list01 = ['Tom', 'Jerry', 'Rose', 'Jack']
        dict01 = {'Jerry': 18, 'Rose': 16, 'Timmy': 24}
    output:

"""

# 1. 过滤列表指定元素
# 过滤掉列表中为空的元素
dict_1 = {'Tom': 97, 'Jerry': 95, 'Rose': None}
# 可以使用filter函数
res_1 = filter(lambda element: element[1] is not None, dict_1.items())
# 也可使用推导式
res_2 = {key: value for key, value in dict_1.items() if value is not None}

from functools import reduce
import itertools

list01 = ['Tom', 'Jerry', 'Rose', 'Jack']
dict01 = {'Jerry': 18, 'Rose': 16, 'Timmy': 24}
dict01 = filter(lambda person_obj_: person_obj_ not in list01, dict01)
