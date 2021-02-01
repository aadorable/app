# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:22
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : __init__.py.py
from selenium.webdriver.common.by import By

'''首页配置'''
index_click_my = By.XPATH, '//*[@text="我的"]'
index_person_homepage = By.XPATH, '//*[@text="个人主页"]'

'''个人主页配置'''
personal_data = By.XPATH, '//*[@text="编辑个人资料"]'

'''个人资料页配置'''
data_nickname = By.ID, 'com.douban.frodo:id/input_name'
data_gender = By.ID, 'com.douban.frodo:id/female'
data_choose_city = By.ID, 'com.douban.frodo:id/select_city_action'
data_introduction = By.ID, 'com.douban.frodo:id/input_intro'
data_province = By.XPATH, '//*[@text="湖北"]'
data_city = By.XPATH, '//*[@text="武汉"]'
data_birthday_text = By.ID, 'com.douban.frodo:id/birthday'
data_birthday = By.ID, 'android:id/numberpicker_input'
data_birthday_confirm = By.XPATH, '//*[@text="确定"]'
data_save = By.XPATH, '//*[@text="保存"]'