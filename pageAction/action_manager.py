# *** coding: utf-8 ***
#@Time   : 2021/1/25 11:00
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : action_manager.py

from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
from pageObject.page_personal_data import PagePersonalData
from pageObject.page_personal_home import PagePersonalHome

class ActionManager():
    def __init__(self, driver):
        self.pageindex = PageIndex(driver)
        self.pagelogin = PageLogin(driver)
        self.pagepersonaldata = PagePersonalData(driver)
        self.pagepersonalhome = PagePersonalHome(driver)