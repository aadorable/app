# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:59
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : baseSwipe.py

import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.baseApi import Base
from base.baseDriver import BaseDriver

class Swipe(Base):
    def swipe_page(self, dir='up', duration=3000):
        '''
        页面滑动
        :param dir: 滑动方向
        :param duration: 持续时间
        :return: 
        '''
        screen = self.base_window_size()
        screen_width = screen['width']
        screen_height = screen['height']
        x = screen_width * 0.5
        y = screen_height * 0.5
        top_y  = screen_height * 0.25
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        right_x = screen_width * 0.75
        if dir == 'up':
            self.driver.swipe(x, bottom_y, x, top_y, duration)
        elif dir == 'down':
            self.driver.swipe(x, top_y, x, bottom_y, duration)
        elif dir == 'left':
            self.driver.swipe(right_x, y, left_x, y, duration)
        elif dir == 'right':
            self.driver.swipe(left_x, y, right_x, y, duration)
        else:
            raise Exception('请输入正确的滑动方向，如up/down/left/right')

    def swipe_and_find_element(self, loc, dir='up'):
        while True:
            try:
                return self.base_find_element(loc)
            except:
                old_page_source = self.base_page_source
                self.swipe_page(dir)
                if old_page_source == self.base_page_source:
                    raise Exception('滑到了底部，请检查元素定位方式')

    def el_swipe(self, el, n ,dir):
        '''
        单元素滑动 location  size  获取滑动点的x,y值
        :param el: 对哪个元素进行操作
        :param n: 目标-当前值=n次
        :param dir: 方向
        :return: 
        '''
        # 1.获取元素的宽高
        el_size = el.size
        el_width = el_size['width']
        el_height = el_size['height']
        # 2.获取元素的x,y轴坐标
        el_location = el.location
        el_x = el_location['x']
        el_y = el_location['y']
        # 3.定位滑动点
        swipe_x = int(el_x + el_width * 0.5)
        swipe_up_top = int(el_y * 0.8)
        swipe_up_bottom = int(el_y + el_height * 0.9)
        swipe_down_top = int(el_y + el_height * 0.3)
        swipe_down_bottom = int(el_y * 1.3 )
        if dir == 'up':
            for i in range(n):
                self.driver.swipe(swipe_x, swipe_up_bottom, swipe_x, swipe_up_top, 10000)
                time.sleep(2)
        elif dir == 'down':
            for i in range(n):
                self.driver.swipe(swipe_x, swipe_down_top, swipe_x, swipe_down_bottom, 10000)
                time.sleep(2)
        else:
            raise Exception



if __name__ == '__main__':
    driver = BaseDriver().start_driver('com.android.settings', '.ChooseLockPattern')
    # loc = By.XPATH, '//*[@text="关于平板电脑"]'
    # el = Swipe(driver).swipe_and_find_element(loc)
    # el.click()
