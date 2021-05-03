import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def swipe_fun(self, name, num=3):
        # 设置查找次数，通过外部传入
        for i in range(0, num):
            try:
                print(i)
                self.driver.implicitly_wait(1)
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']")
                return element
            except NoSuchElementException:
                print("未找到添加成员按钮，将滑动查找")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                start_x = width/2
                start_y = height*0.8
                end_x = start_x
                end_y = height*0.3
                duration = 2000    # ms
                # 开始进行滑动查找
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num-1:
                # 如果num-1次没有找到，则报出下面的异常
                raise NoSuchElementException(f"找了{i}此，未找到")

    def find_element(self, by, value):
        logging.info(by)
        logging.info(value)
        element = self.driver.find_element(by, value)
        return element