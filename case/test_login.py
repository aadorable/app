# *** coding: utf-8 ***
#@Time   : 2021/1/30 17:26
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_login.py

from pageAction.login_action import Login

class TestLogin():

    def test_login(self, getdriver):
        driver = getdriver
        login = Login(driver)
        login.login_success()
        login.after_login_click_my()
        assert 'ster~' in driver.page_source

