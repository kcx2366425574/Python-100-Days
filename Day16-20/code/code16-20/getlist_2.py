# -*- encoding : utf-8 -*-
"""
@File       : getlist_2.py
@Time       :2021/1/4 10:44
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""

names = ["tom", "xiaoming", "jim", "kaungcx"]

subjects = ["Math", "English", "Chinese"]

x, y = len(names), len(subjects)
# 初始化空列表
scores = [[None] * (1+len(subjects)) for _ in range(len(names)+1)]
for i, name in enumerate(names):
    scores[i+1][0] = name
    for j, subject in enumerate(subjects):
        scores[0][j+1] = subject
        scores[i+1][j+1] = float(input("请输入成绩:"))

for index in scores:
    print(index)
