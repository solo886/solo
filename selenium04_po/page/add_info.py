# @Time : 2021/4/21 19:25 
# __author__ = 'zhangcheng'
# coding:utf-8
# from contact import Contact
from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson04_selenium_po.page.base_page import BasePage
from lesson04_selenium_po.page.contact import Contact


class AddInfo(BasePage):
    # 设定为元祖，*用于解包元祖，使其变成
    __username = (By.ID, 'username')
    __ele_accid = (By.ID, 'memberAdd_acctid')
    __mobile = (By.ID, 'memberAdd_phone')
    def add_member(self, name, accid, phone):
        """添加成员，"""
        # *用于解包元祖，使其变成两个参数
        self.driver.find_element(*self.__username).send_keys(name)
        self.driver.find_element(*self.__ele_accid ).send_keys(accid)
        self.driver.find_element(*self.__mobile).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)

    def add_member_fail(self, name, accid, phone):
        """添加成员"""
        self.driver.find_element(*self.__username).send_keys(name)
        self.driver.find_element(*self.__ele_accid).send_keys(accid)
        self.driver.find_element(*self.__mobile).send_keys(phone)
        ele = self.driver.find_element(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for list in ele:
            error_list.append(list.text)
        return error_list




    def add_apartment(self,apartname):
        """添加部门"""
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_inputText:nth-child(2)").send_keys(apartname)
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body[id='1688850853022845_anchor']").click()
        self.driver.find_element(By.XPATH, '//*[@id="1688850853022845_anchor"]').click()
        self.driver.find_element(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
        return Contact()