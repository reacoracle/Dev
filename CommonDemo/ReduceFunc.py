from functools import reduce

list01 = [
    [True, False],
    [False, False]
]

res = reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), list01)
print(res[0], res[1])