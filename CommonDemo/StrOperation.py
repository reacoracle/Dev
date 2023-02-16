import itertools

# 字符串拼接
list_1 = ["h", "e", "l", "l", "o"]
s = "".join(itertools.chain(*list_1))

