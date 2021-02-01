# *** coding: utf-8 ***
#@Time   : 2021/2/1 8:20 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : run.py

'''
subprocess.call()
os.system(命令行命令)：不能收集返回值，只能运行命令
多进程实现多任务
'''

import pytest
import os
import time
import multiprocessing
import subprocess

def start_appium_server():
    os.system('appium')

def main():
    '''
    启动各种服务
    1. appium服务
    2. pytest运行脚本
    3. 启动allure服务
    :return:
    '''
    # 用多进程启动appium服务，
    p = multiprocessing.Process(target=start_appium_server)
    p.start()
    time.sleep(2)
    pytest.main(['-sv', './case/test_login.py', '--alluredir=./reports/douban', '--clean-alluredir'])
    # 启动allure服务
    subprocess.call('allure generate ./reports/douban -o ./reports/html --clean', shell=True)
    # 等待其他进程
    p.join()
    # 进程退出
    p.terminate()


if __name__ == '__main__':
    main()