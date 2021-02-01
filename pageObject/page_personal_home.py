# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:50
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : page_personal_home.py

import pageObject
from base.baseApi import Base

class PagePersonalHome(Base):
    # 点击编辑个人资料
    def click_personal_data(self):
        self.base_click(pageObject.personal_data)
