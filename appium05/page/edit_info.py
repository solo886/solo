# @Time :  22:52
# __authou__= 'zhangcheng'
# conding = utf-8
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lesson05_appium.page.basepage import BasePage


class EditInfo(BasePage):
    def delete_member(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'删除')]").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        # 点击删除按钮，并点击确定
        __del_eme = (MobileBy.XPATH, "//*[contains(@text,'删除')]")
        __sure_eme = (MobileBy.XPATH, "//*[contains(@text,'确定')]")
        BasePage.find_element(*__del_eme).click()
        BasePage.find_element(*__sure_eme).click()
        # sleep(3)  # 返回到成员列表页时，成员还没有立即消失，需要有一个等待时间
        # 显示等待，当name这个元素不可见时，再往下执行
        __emel = (MobileBy.XPATH, f"//*[@text='{name}']")
        WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located(__emel))
        from lesson05_appium.page.manager_member import ManagerMember
        return ManagerMember(self.dirver)