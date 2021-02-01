# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:11
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : baseDriver.py

from appium import webdriver

class BaseDriver():
    @staticmethod
    def start_driver(appPackage, appActivity):
        # 1.启动项
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7'
        desired_caps['deviceName'] = '10.0.0.1:5555'
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['udid'] = '127.0.0.1:62001'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['newCommandTimeout'] = 6000
        # 链接远程appium服务
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    driver = BaseDriver().start_driver('com.douban.frodo', '.activity.SplashActivity')
