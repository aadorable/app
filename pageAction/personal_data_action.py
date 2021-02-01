# *** coding: utf-8 ***
#@Time   : 2021/1/25 10:59
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : personal_data_action.py

import time
from pageAction.action_manager import ActionManager

class PersonalData(ActionManager):

    def personal_data_business(self):
        self.pageindex.click_my()
        time.sleep(1)
        self.pageindex.click_person_homepage()
        time.sleep(1)
        self.pagepersonalhome.click_personal_data()
        time.sleep(1)
        self.pagepersonaldata.input_nickname()
        time.sleep(1)
        # self.pagepersonaldata.click_gender()
        # time.sleep(1)
        self.pagepersonaldata.input_introduction()
        time.sleep(1)
        self.pagepersonaldata.choose_city()
        time.sleep(1)
        self.pagepersonaldata.choose_birthday()
        time.sleep(1)
        self.pagepersonaldata.click_save()
        time.sleep(1)
