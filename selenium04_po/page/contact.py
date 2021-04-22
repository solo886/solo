# @Time : 2021/4/21 19:25 
# __author__ = 'zhangcheng'
# coding:utf-8
from selenium.webdriver.common.by import By

from lesson04_selenium_po.page.base_page import BasePage


class Contact(BasePage):
    def get_member_list(self):
        """获取成员列表，并返回所有成员，用于断言"""
        member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print('member_list')
        name_list = []
        for list in member_list:
            name_list.append(list.text)
        print(name_list)

        return name_list

    def get_apartment_list(self):
        """获取部门列表，并返回所有部门，用于断言"""
        # 获取部门列表
        ele = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-children")
        apart_list = []
        for apart in ele:
            apart_list.append(apart.text)
        print(apart_list)
        return apart_list

    def add_apartment_fail(self):
        """添加部门"""
