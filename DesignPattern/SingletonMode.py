# Cython: language_level=3
"""

"""

import os
import time
import threading


class Foo:
    def __new__(cls, *args, **kwargs):
        # if not Foo.__instance:
        if not hasattr(Foo, '_instance'):
            Foo._instance = object.__new__(cls)
        return Foo._instance

    def __init__(self, name_: str = None):
        self.name = name_


foo_1 = 'A'


def foo():
    for _ in range(2):
        time.sleep(3)
        print(
            f"Branch thread is running... Thread number is {os.getpid()} and native thread id is {threading.get_native_id()} and thread ident is {threading.get_ident()}.")  # noqa
        global foo_1
    foo_1 = Foo('A')


thread_1 = threading.Thread(target=foo)
thread_1.start()

res = threading.enumerate()
for _ in range(2):
    time.sleep(2)
    print(
        f"Main thread is running... Thread number is {os.getpid()} and native thread id is {threading.get_native_id()} and thread ident is {threading.get_ident()}.")  # noqa
foo_2 = Foo('B')

thread_1.join()

# import multiprocessing
#
# res = multiprocessing.cpu_count()


#
#
# foo_1 = Foo(name_='Tom')
# foo_2 = Foo(name_='Jerry')
#
print(id(foo_1))
print(id(foo_2))

print(foo_1.name)
print(foo_2.name)
