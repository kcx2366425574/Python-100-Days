# -*- encoding : utf-8 -*-
"""
@File       : getdict.py
@Time       :2021/1/4 10:41
@Author     :kuang congxian
@Contact    :kuangcx@inspur.com
@Description : null
"""
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

price = {key: value for key, value in prices.items() if value < 200}
print(price)