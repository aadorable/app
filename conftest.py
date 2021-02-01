# *** coding: utf-8 ***
#@Time   : 2021/1/30 17:26
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : conftest.py

import pytest
import time
from base.baseDriver import BaseDriver

@pytest.fixture(scope='function')
def getdriver():
    driver = BaseDriver().start_driver('com.douban.frodo', '.activity.SplashActivity')
    yield driver
    time.sleep(3)
    driver.quit()
