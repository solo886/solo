# @Time : 2021/4/21 19:25 
# __author__ = 'zhangcheng'
# coding:utf-8
# from add_info import AddInfo
from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson04_selenium_po.page.add_info import AddInfo
from lesson04_selenium_po.page.base_page import BasePage
from lesson04_selenium_po.page.contact import Contact


class MainPage(BasePage):
    def goto_contact(self):
        """跳转到通讯录页面"""
        return AddInfo()

    def goto_add_info(self):
        """跳转到添加成员，添加部门页面"""

        self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
        return AddInfo(self.driver)
