from appium import webdriver

from lesson05_appium.page.mainpage import MainPage


class App:
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "solo"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["setting[waitForIdleTimeout]"] = 0
            caps["skipDeviceInitialization"] = True
            # 客户端和服务端远程建立连接
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.launch_app() # 服用driver
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        self.driver.quit()
    def goto_mainpage(self):

        return MainPage(self.driver)