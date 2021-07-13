# -*- encoding : utf-8 -*-
"""
@File       : orm_demo.py
@Time       :2021/6/21 14:50
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : ORM映射
"""


# 一、首先定义Field类，它负责保存数据库表的字段名和字段类型
class field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<{}:{}>".format(self.name, self.column_type)


class stringField(field):

    def __init__(self, name):
        super().__init__(name, "varchar(1000)")


class intField(field):

    def __init__(self, name):
        super().__init__(name, "Integer")


# 二、定义元类，控制Model对象的创建
class modelMetaclass(type):

    def __new__(cls, name, bases, attrs):

        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        mapping = dict()
        for key, value in attrs.items():
            if isinstance(value, field):
                print("found apping:{}===>{}".format(key, value))
                mapping[key] = value

        for key in mapping.keys():
            attrs.pop(key)

        attrs["__table__"] = name.lower()
        attrs["__mapping__"] = mapping

        return super().__new__(cls, name, bases, attrs)


# 三、Model基类
class Model(dict, metaclass=modelMetaclass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            AttributeError("'Model' object has no attribute {}".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for key, value in self.__mapping__.items():
            fields.append(value.name)
            params.append('?')
            args.append(getattr(self, key, None))

        sql = "insert into {}({}) values {}".format(self.__table__, ",".join(fields), ",".join(params))
        print("SQL:{}".format(sql))
        print("ARGS:{}".format(args))


class User(Model):
    id = intField("id")
    name = stringField("username")
    email = stringField("email")
    password = stringField("password")


user = User(id=1, name="Job", email="job@test.com", password="pw")
user.save()
