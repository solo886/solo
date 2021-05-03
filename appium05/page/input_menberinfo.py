from appium.webdriver.common.mobileby import MobileBy
from lesson05_appium.page.basepage import BasePage
from lesson05_appium.util.util_info import Utilinfo


class InputMemberInfo(BasePage):

    def input_member_info(self,name,phone_num):

        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../"
        #                                          "android.widget.EditText").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//"
        #                                          "android.widget.EditText").send_keys(phone_num)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        __name_eme = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        __phone_eme =(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText")
        __save_eme = (MobileBy.XPATH, "//*[@text='保存']")
        BasePage.find_element(*__name_eme).send_keys(name)
        BasePage.find_element(*__phone_eme).send_keys(phone_num)
        BasePage.find_element(*__save_eme).click()
        from lesson05_appium.page.add_member import AddMember
        return AddMember(self.driver)