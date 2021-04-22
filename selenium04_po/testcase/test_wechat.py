# @Time : 2021/4/21 19:24 
# __author__ = 'zhangcheng'
# coding:utf-8
import pytest

from lesson04_selenium_po.page.main_page import MainPage

class TestWechat:
    def setup(self):
        self.main_page = MainPage()
    @pytest.mark.parametrize("name, accid, phone", [["亚瑟","10010","13899997777"]])
    def test_addmember(self,name, accid, phone):
        # 1.跳转到成员页面 2.添加成员 3.获取成员列表
        name_list = self.main_page.goto_add_info().add_member(name, accid, phone).get_member_list()
        assert name in name_list

    @pytest.mark.parametrize("name, accid, phone", [["亚瑟1", "100110", "13899997777"]])
    def test_addmember_fail(self, name, accid, phone):
        # 1.跳转到成员页面 2.添加成员 3.获取成员列表
        data_list = self.main_page.goto_add_info().add_member_fail(name, accid, phone).get_member_list()
        err = [i for i in data_list if i != ""]
        print(err)
        assert "亚瑟" in err[0]

    @pytest.mark.parametrize("apartname", [["产品部门"]])
    def test_add_apartment(self,apartname):
        # 1.跳转到成员页面 2.添加部门 3.获取部门列表
        apart_list = self.main_page.goto_add_info().add_apartment(apartname).get_apartment_list()
        assert apartname in apart_list



