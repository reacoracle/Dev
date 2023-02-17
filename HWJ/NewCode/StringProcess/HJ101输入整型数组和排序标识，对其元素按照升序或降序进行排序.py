import sys

ele_num = int(input())
lst = [int(i) for i in list(input().split())]
sort_rule = int(input())

lst.sort(reverse=sort_rule)

for i in range(len(lst)):
    if i != len(lst) - 1:
        print(lst[i], end=' ')
    else:
        print(lst[i])
