import sys
from collections import Counter

for line in sys.stdin:
    string_lst = line.split()
    for str_1 in string_lst:
        string_count = dict(Counter(str_1))
        res = sorted(zip(string_count.values(), string_count.keys()), key=lambda x: x[0])
        for index in range(len(res)):
            if len(res) == index:
                break
            if len(res) == 1:
                str_1.replace(res[index][1], '')
                break
            if index > 0 and res[index][0] != res[index - 1][0]:
                break
            str_1.replace(res[index][1], '')
        print(str_1)
