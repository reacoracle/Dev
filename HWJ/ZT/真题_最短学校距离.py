"""
    如果有一个数轴，数轴上有若干个点。要在数轴上找一点，使得它到各个点的距离之和最短。
    实际在考察中位数，中位数就是最优解。中位数有这样的性质: 所有数与中位数的绝对差之和最小。中位数是数列中间的那个数，或者是中间的那两个数之一。
"""
family_num = int(input())
position_lst = [int(i) for i in input().split()]

print(family_num)
print(position_lst)

position_lst.sort()
if len(position_lst) % 2:
    print(len(position_lst) // 2)
else:
    print(len(position_lst) // 2 - 1)
