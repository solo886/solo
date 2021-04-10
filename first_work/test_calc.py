# @Time : 2021/4/10 13:20 
# __author__ = 'zhangcheng'
# coding:utf-8

import pytest
import yaml
from Calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expan", yaml.safe_load(open("./data_add.yaml")))
    def test_add(self,a,b,expan):
        assert expan == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expan", yaml.safe_load(open("data_div.yaml")))
    def test_div(self,a,b,expan):
        if b == 0:
            return 0
        else:
            assert expan == self.calc.div(a, b)
# if __name__=="__main__":
#     pytest.main(['test_calc.py','-vs'])