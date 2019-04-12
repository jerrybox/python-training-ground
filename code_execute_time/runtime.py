# -*- coding: UTF-8 -*-
"""
# reference: https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module
# reference: https://blog.csdn.net/hqzxsc2006/article/details/50337865
    Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变）。
    为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
    写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。
    func.__name__, example.__doc__
"""


import time
from functools import wraps


def execute_time(fn):
    @wraps(fn)
    def fn_wrap(*args, **kwargs):
        start_time = time.time()

        result = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time
        print('Execution time: %.3f .' % elapsed_time)
        return result
    return fn_wrap


@execute_time
def test():
    for i in range(10):
        time.sleep(1)
        pass


'''
D:\PycharmProject\DemoTest>python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from code_execute_time import runtime
>>> runtime.test()
Execution time: 10.002 .
>>>
'''
