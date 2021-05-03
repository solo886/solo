from appium.webdriver.common.mobileby import MobileBy

from lesson05_appium.page.basepage import BasePage


class AddMember(BasePage):
    def goto_input_memberinfo(self):

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        __text_eme = (MobileBy.XPATH, "//*[@text='手动输入添加']")
        BasePage.find_element(*__text_eme).click()
        from lesson05_appium.page.input_menberinfo import InputMemberInfo
        return InputMemberInfo(self.driver)

    def get_toast(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")