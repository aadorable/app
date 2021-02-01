# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:48
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : page_index.py

import pageObject
from base.baseApi import Base

class PageIndex(Base):
    # 点击我的
    def click_my(self):
        self.base_click(self.source.get_value('index.ini', 'Button', '我的'))

    # 点击个人主页
    def click_person_homepage(self):
        self.base_click(pageObject.index_person_homepage)
