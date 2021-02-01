# *** coding: utf-8 ***
#@Time   : 2021/1/27 21:49
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : inihelper.py

import configparser
from item_path import DIR_NAME

class IniHelper(object):
    def __init__(self):
        '''
        具体的配置文件在哪个文件夹里面
        '''
        self.source_folder = 'pageElement'

    def get_source_file(self, filename):
        '''
        获取ini文件的config配置信息
        :param filename: ini文件的名字
        :return: 
        '''
        # 创建config这个类
        try:
            config = configparser.ConfigParser()
            filepath = DIR_NAME + '/' + self.source_folder + '/' + filename
            # 通过这个文件路径读取的内容就会保存到config中
            config.read(filepath, encoding='utf-8')
            return config
        except Exception as e:
            print('read config file error:' + str(e))

    def get_value(self, filename, section, key):
        '''
        获取key对应的值。即定位方法和值
        :param filename: 
        :param section: 
        :param key: 
        :return: 
        '''
        try:
            config = self.get_source_file(filename)
            value = config.get(section, key)
            return value
        except Exception as e:
            print('get value fail:', str(e))


if __name__ == '__main__':
    str = IniHelper().get_value('index.ini', 'Button', '我的')
    li = str.split('=>')
    print(li)

