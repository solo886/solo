# @Time : 2021/4/10 13:20 
# __author__ = 'zhangcheng'
# coding:utf-8
import allure
import pytest
import yaml
from Calculator import Calculator
@allure.feature("计算器模块")
class TestCalc:
    @allure.story("计算整型")
    def test_add_int(self,getdatas_int,fun_ini):
        assert getdatas_int[2] == fun_ini.add(getdatas_int[0], getdatas_int[1])

    @allure.story("计算浮点数")
    def test_add_float(self,getdatas_float,fun_ini):
        assert getdatas_float[2] == round(fun_ini.add(getdatas_float[0], getdatas_float[1]),2)

    @allure.story("计算除数")
    def test_div(self,getdatas_div,fun_ini):
        try:
            assert getdatas_div[2] == fun_ini.div(getdatas_div[0], getdatas_div[1])
        except ZeroDivisionError:
            print('除数为0')
