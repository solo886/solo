# @Time : 2021/4/17 19:55 
# __author__ = 'zhangcheng'
# coding:utf-8
import pytest
import yaml
from selenium import webdriver


class TestWechat():
    def test_getcookies(self):
        # 复用浏览器
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        # 获取cookie，并存入yaml中
        cookies = self.driver.get_cookies()
        with open('cookies.yaml', 'w', encoding='UTF-8') as f:
            yaml.dump(cookies, f)

    # @pytest.mark.skip
    def test_wechat(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 获取当前页cookie后，并使用cookie登录
        with open('cookies.yaml', encoding='UTF-8') as f:
            data_cookie = yaml.safe_load(f)
            for cookie in data_cookie:
                self.driver.add_cookie(cookie)
        # 进行添加成员操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.find_element_by_xpath('//*[@class="ww_operationBar"]/a[1]').click()
        self.driver.find_element_by_id('username').send_keys('张三')
        self.driver.find_element_by_id('memberAdd_english_name').send_keys('zhangsan')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('123456')
        self.driver.find_element_by_name('gender').click()
        self.driver.find_element_by_id('memberAdd_phone').send_keys('15811112222')
        self.driver.find_element_by_id('memberAdd_telephone').send_keys('075512345678')
        self.driver.find_element_by_id('memberAdd_mail').send_keys('123@qq.com')
        self.driver.find_element_by_id('memberEdit_address').send_keys('我的老家就在这个屯')
        self.driver.find_element_by_id('memberAdd_title').send_keys("工程师")
        self.driver.find_element_by_xpath('//*[@class="js_member_editor_form"]/div[3]/a[1]').click()