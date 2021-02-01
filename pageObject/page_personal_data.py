# *** coding: utf-8 ***
#@Time   : 2021/1/19 15:37
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : page_personal_data.py

import pageObject
from base.baseApi import Base
from base.baseSwipe import Swipe

class PagePersonalData(Base):
    # 输入昵称
    def input_nickname(self):
        self.base_input(pageObject.data_nickname, 'ster~')

    # 选择性别
    def click_gender(self):
        self.base_click(pageObject.data_gender)

    def input_introduction(self):
        self.base_input(pageObject.data_introduction, '这里是简介')

    # 选择城市
    def choose_city(self):
        self.base_click(pageObject.data_choose_city)
        # 滑动页面，找到对应省份
        el_province = Swipe(self.driver).swipe_and_find_element(pageObject.data_province)
        # 点击省份
        el_province.click()
        # 滑动页面，找到对应城市
        el_city = Swipe(self.driver).swipe_and_find_element(pageObject.data_city)
        # 点击城市
        el_city.click()

    # # 选择生日
    def choose_birthday(self):
        # 点击生日
        self.base_click(pageObject.data_birthday_text)
        # 选择年
        year = self.base_find_elements(pageObject.data_birthday)[0]
        Swipe(self.driver).el_swipe(year, 2, 'up')
        # 选择月
        month = self.base_find_elements(pageObject.data_birthday)[1]
        Swipe(self.driver).el_swipe(month, 2, 'up')
        # 选择日
        day = self.base_find_elements(pageObject.data_birthday)[2]
        Swipe(self.driver).el_swipe(day, 2, 'down')
        # 点击确定
        self.base_click(pageObject.data_birthday_confirm)

    def click_save(self):
        self.base_click(pageObject.data_save)








