# *** coding: utf-8 ***
#@Time   : 2021/1/25 11:33
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_personal_data.py

import time
import case
from pageAction.login_action import Login
from pageAction.personal_data_action import PersonalData
from base.baseDriver import BaseDriver
from base.baseApi import Base

class TestPersonalData():

    def setup_class(self):
        # 创建driver对象
        self.driver = BaseDriver().start_driver(case.appPackage, case.appActivity)
        # 登录系统
        Login(self.driver).login_success()
        self.personaldata = PersonalData(self.driver)
        self.base = Base(self.driver)

    def test_personal_data(self):
        self.personaldata.personal_data_business()
        time.sleep(1)
        assert '修改成功' in self.base.base_page_source