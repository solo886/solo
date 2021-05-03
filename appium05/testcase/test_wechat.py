from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException


class Testdemo:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "solo"
        caps['udid'] = '127.0.0.1:7555'
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["setting[waitForIdleTimeout]"] = 0
        caps["skipDeviceInitialization"] = True
        # 客户端和服务端远程建立连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.faker = Faker('zh-CN')

    def setup(self):
        # 初始化，启动app
        self.driver.launch_app()
    def teardown(self):
        # 关闭app，类似于退到后台
        self.driver.close_app()
    def teardown_class(self):
        # 资源销毁，类似于kill应用进程
        self.driver.quit()

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
    @pytest.mark.parametrize('a',[["aa"],["bb"],["c"],["d"],['e'],['f'],['g'],['h']])
    def test_case(self,a):
        name = self.faker.name()
        phone_num = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.swipe_fun('添加成员').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../"
                                                 "android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//"
                                                 "android.widget.EditText").send_keys(phone_num)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
    def test_delete_member(self):
        # 进入通讯录页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 遍历获取通讯录名单
        emle = self.driver.find_elements(MobileBy.XPATH,
                                         "//*[contains(@text,'张诚')]/../../../../../..//android.widget.TextView")
        eme_num = []
        for i in emle:
            eme_num.append(i.text)
        print(eme_num)
        name = eme_num[4]
        print(name)

        # 进入通讯录，点击右上角的编辑按钮,进入管理通讯录页面
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'信息时代')]/"
                                                 "../../../../../android.widget.LinearLayout[2]"
                                                 "/android.widget.RelativeLayout[2]").click()

        # 点击通讯名单的某一个人，进入到个人信息编辑页面
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']").click()
        # 点击删除按钮，然后再点确定按钮进行删除
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'删除')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        sleep(3)  # 返回到成员列表页时，成员还没有立即消失，需要有一个等待时间
        # 获取通讯录列表，检查删除的不在通讯录中
        emle1 = self.driver.find_elements(MobileBy.XPATH,
                                         "//*[contains(@text,'张诚')]/../../../../../..//android.widget.TextView")
        eme_list = []
        for i in emle1:
            eme_list.append(i.text)
        print(eme_list)
        assert name not in eme_list





