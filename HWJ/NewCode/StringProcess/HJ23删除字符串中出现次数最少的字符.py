import sys
from collections import Counter  # noqa

for line in sys.stdin:
    string_lst = line.split()

    """
        思路一:
            1. 对字符串的每个元素进行计数，得到计数字典{元素: 出现次数}
            2. 按照元素出现次数的大小进行排序，次数最少的在最前面
            3. 删除出现的频率最少且出现频率相同的所有元素
        通过全部用例 运行时间 45ms 占用内存 4648KB
    """
    # for str_1 in string_lst:
    #     string_count = dict(Counter(str_1))
    #     res = sorted(zip(string_count.values(), string_count.keys()), key=lambda x: x[0])
    #     for index in range(len(res)):
    #         if len(res) == index:
    #             break
    #         if len(res) == 1:
    #             str_1 = str_1.replace(res[index][1], '')
    #             break
    #         if index > 0 and res[index][0] != res[index - 1][0]:
    #             break
    #         str_1 = str_1.replace(res[index][1], '')
    #     print(str_1)

    """
        思路二:
            1. 对字符串的每个元素进行计数，得到计数字典{元素: 出现次数}
            2. 求取最小出现频率
            3. 删除与最小出现频率一致的所有元素
        通过全部用例 运行时间 27ms 占用内存 4543KB
    """
    for str_1 in string_lst:
        dic = {}
        for ele in str_1:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        min_count = min(dic.values())
        for k, v in dic.items():
            if v != min_count:
                continue
            str_1 = str_1.replace(k, '')
        print(str_1)
