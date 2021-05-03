from appium.webdriver.common.mobileby import MobileBy
from lesson05_appium.page.basepage import BasePage
from lesson05_appium.page.contact import Contact


class MainPage(BasePage):
      def goto_contact(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        __contact_eme = (MobileBy.XPATH, "//*[@text='通讯录']")
        BasePage.find_element(*__contact_eme).click()
        return Contact(self.driver)