# from operator import attrgetter
from itertools import groupby

iter_object = [
    {'Name': 'Jerry', 'Score': 98},
    {'Name': 'Tom', 'Score': 60},
    {'Name': 'Jack', 'Score': 34},
    {'Name': 'Rose', 'Score': 75}
]

# 按照是否大于60分把字典分组(按照现有字典顺序进行分组 True: [98], False: [60, 34], True: [75])
group_iters = groupby(iterable=iter_object, key=lambda ele: ele['Score'] > 60)
# for item in res:
#     for i in item:
#         print('='*20)
#         if type(i) == bool:
#             print(i)
#             continue
#         for j in i:
#             print(j)

# 一般来说是先对迭代对象按照某个属性排序，再利用groupby进行分组
sorted_iter = sorted(iter_object, key=lambda ele: ele['Score'])

# for item in map(lambda element: setattr(element, ('Name', 'Score'), (None, None)), iter_object):
#     print(item)
