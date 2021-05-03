from lesson05_appium.page.app import App
from lesson05_appium.util.util_info import Utilinfo


class TestWechatPo:
    def setup_class(self):
        self.app = App()
        self.info = Utilinfo()
        self.name = self.info.get_name()
        self.phone_num = self.info.get_phone_num()
    def set_up(self):
        # 启动app
        self.main = self.app.start()
    def teardown_class(self):
        self.app.stop()

    def test_add_member(self):
        self.main.goto_mainpage().goto_contact().goto_add_member().goto_input_memberinfo().input_member_info(self.name,self.phone_num).get_toast()

    def test_del_member(self):
        name_list = self.main.goto_mainpage().goto_contact().goto_manager_member().get_member_list()
        member_list = self.main.goto_mainpage().goto_contact().goto_manager_member().\
            goto_edit_info(name_list[5]).delete_member(name_list[5]).get_member_list()
        assert name_list[5] not in member_list