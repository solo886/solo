# @Time :  22:51
# __authou__= 'zhangcheng'
# conding = utf-8
from appium.webdriver.common.mobileby import MobileBy

from lesson05_appium.page.basepage import BasePage


class ManagerMember(BasePage):
    def get_member_list(self):
        # 获取成员列表，选取第五个成员进行删除
        # emle = self.driver.find_elements(MobileBy.XPATH,
        #                                  "//*[contains(@text,'张诚')]/../../../../../..//android.widget.TextView")

        __emel = (MobileBy.XPATH, "//*[contains(@text,'张诚')]/../../../../../..//android.widget.TextView")
        eme_list = BasePage.find_element(*__emel)
        self.eme_num = []
        for i in eme_list:
            self.eme_num.append(i.text)
        # print(eme_num)
        return self.eme_num

    def goto_edit_info(self, name):
        # 点击通讯名单的某一个人，进入到个人信息编辑页面
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']").click()

        __emel = (MobileBy.XPATH, f"//*[@text='{name}']")
        BasePage.find_element(*__emel).click()
        from lesson05_appium.page.edit_info import EditInfo

        return EditInfo(self.dirver)
