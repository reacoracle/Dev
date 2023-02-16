"""

"""


class Foo:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


res = Foo.__new__(Foo)

print(isinstance(res, Foo))


# def foo(arg_1, arg_2=None, arg_3=None):
#     return arg_1 * (arg_2 + arg_3)
#
#
# #
# # def bar(*args, args_1, args_2):
# #     return args[0], args[1]
#
#
# # a, b = bar(1, 2, args_1=3, args_2=4)
#
#
# def bar(arg_1, *args, arg_2=None):
#     print(f"arg_1: {arg_1}")
#     print(f"args: {args}")
#     print(f"arg_2: {arg_2}")
#
#
# def foo(*args, arg_1, arg_2=None):
#     print(f"args: {args}")
#     print(f"arg_1: {arg_1}")
#     print(f"arg_2: {arg_2}")
#
#
# bar(1, 2, 3, arg_2=4)
# foo(1, 2, arg_1=3, arg_2=4)




def foo(**kwargs):
    """

    :param kwargs:
    :return:
    """
    return [key for key, value in kwargs.items() if value]


# filter_lst = foo(**{'Tom': True, 'Rose': False, 'Jack': True, 'Jerry': True})
filter_lst = foo(Tom=True, Rose=False, Jack=True, Jerry=True)
print(filter_lst)


def bar(*args):
    pass


bar((1, 2, 3))
bar(*(1, 2, 3))
