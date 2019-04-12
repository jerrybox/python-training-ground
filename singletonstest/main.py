import logging

from singletonstest import source
# from singletonstest import other  # 只有模块被导入这个模块内部代码才会被执行一遍

print(source.FILENAME)
# NewSource.py

source.get_num()
# I am in change.py
