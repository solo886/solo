# @Time : 2021/4/21 20:57 
# __author__ = 'zhangcheng'
# coding:utf-8
import yaml
from selenium import webdriver


class BasePage:
    """如下是构造函数，当其他类继承此函数后，每次都会先执行此构造函数"""
    def __init__(self,base_driver=None):
        if base_driver==None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            # 获取当前页cookie后，并使用cookie登录
            with open('cookies3.yaml', encoding='UTF-8') as f:
                data_cookie = yaml.safe_load(f)
                for cookie in data_cookie:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = base_driver