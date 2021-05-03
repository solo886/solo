from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from lesson05_appium.page.add_member import AddMember
from lesson05_appium.page.basepage import BasePage
from lesson05_appium.page.manager_member import ManagerMember


class Contact(BasePage):
    def goto_add_member(self):
        # 滑动查找添加成员按钮
        self.swipe_fun('添加成员').click()
        return AddMember(self.driver)

    def goto_manager_member(self):
        __eme = (MobileBy.XPATH, "//*[contains(@text,'信息时代')]/"
                         "../../../../../android.widget.LinearLayout[2]"
                         "/android.widget.RelativeLayout[2]")

        # 进入通讯录，点击右上角的编辑按钮,进入管理通讯录页面
        # self.driver.find_element(*__eme).click()
        BasePage.find_element(*__eme).click()
        return  ManagerMember(self.driver)