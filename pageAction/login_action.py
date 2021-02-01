# *** coding: utf-8 ***
#@Time   : 2021/1/25 11:04
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : login_action.py

import time
from pageAction.action_manager import ActionManager

class Login(ActionManager):

    # 成功登录
    def login_success(self):
        self.pagelogin.click_password_login()
        self.pagelogin.input_username('18240887426')
        self.pagelogin.input_password('19971218')
        self.pagelogin.click_login_button()
        time.sleep(1)

    # 登录业务-测试功能
    def login_business(self, username, password):
        self.pagelogin.click_password_login()
        self.pagelogin.input_username(username)
        self.pagelogin.input_password(password)
        self.pagelogin.click_login_button()
        time.sleep(1)

    # 断言 点击我的 判断昵称是否在页面源码中
    def after_login_click_my(self):
        self.pageindex.click_my()
        time.sleep(1)