# @Time : 2021/4/10 13:12 
# __author__ = 'zhangcheng'
# coding:utf-8
from decimal import Decimal

class Calculator:
    # 相加

    def add(self, a, b):
        return round(a+b, 1)

    # 相除
    def div(self, a, b):
        return a/b

