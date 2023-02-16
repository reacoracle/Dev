# 返回一个上下文管理器，如果它们发生在 with 语句的主体中，则抑制任何指定的异常，然后使用 with 语句结束后的第一条语句继续执行。
#
# 与任何其他完全抑制异常的机制一样，此上下文管理器应仅用于覆盖非常具体的错误，其中已知静默继续执行程序是正确的做法。
import contextlib


def foo():
    return 1 / 0


with contextlib.suppress(NameError, ZeroDivisionError):
    foo()
    print('b')
print('a')

# 等同于
try:
    foo()
except ZeroDivisionError:
    pass
