# -*- encoding : utf-8 -*-
"""
@File       : itertools_module.py
@Time       :2021/1/4 13:47
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : 迭代工具模块

"""
import collections
import itertools

# 产生ABCD的全排列
a = itertools.permutations('ABCD')
print(set(a))
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))
