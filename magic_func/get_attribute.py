# -*- encoding : utf-8 -*-
"""
@File       : get_attribute.py
@Time       :2021/7/4 10:43
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""


class ClassA:

    x = 'a'
    count = 0

    def __getattribute__(self, item):
        print("__getattribute__")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("__getattr__")
        return super().__dict__[item]


if __name__ == '__main__':
    a = ClassA()
    print(a.x)
    print(a.z)
