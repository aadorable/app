# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:47
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : page_login.py

from base.baseApi import Base

class PageLogin(Base):
    # 点击账号密码登录
    def click_password_login(self):
        self.base_click(self.source.get_value('login.ini', 'Button', '帐号密码登录'))

    # 输入账号
    def input_username(self, username):
        self.base_input(self.source.get_value('login.ini', 'TextInput', '用户名'), username)

    # 输入密码
    def input_password(self, password):
        self.base_input(self.source.get_value('login.ini', 'TextInput', '密码'), password)

    # 点击登录
    def click_login_button(self):
        self.base_click(self.source.get_value('login.ini', 'Button', '登录按钮'))