# *** coding: utf-8 ***
#@Time   : 2021/1/23 16:26
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : baseApi.py

from tools.inihelper import IniHelper
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.source = IniHelper()

    def base_window_size(self):
        return self.driver.get_window_size()

    @property
    def base_page_source(self):
        return self.driver.page_source

    def base_find_element(self, loc):
        '''
        :param loc: loc = xpath=>//android.widget.TextView[@text='我的'] 字符串的类型
        :return: 定位到的元素
        '''
        element = ''
        ele_type = loc.split('=>')[0]
        ele_value = loc.split('=>')[1]
        if ele_type == '' or ele_value == '':
            logger.error('grammatical error, eg:"id=>name"')
            raise NameError('grammatical error, eg:"id=>name"')
        if ele_type == 'id':
            try:
                element = self.driver.find_element_by_id(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' %e)
        elif ele_type == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' %e)
        elif ele_type == 'name':
            try:
                element = self.driver.find_element_by_name(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'link':
            try:
                element = self.driver.find_element_by_link_text(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'class':
            try:
                element = self.driver.find_element_by_class_name(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'p_link':
            try:
                element = self.driver.find_element_by_partial_link_text(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'android_uiautomator':
            try:
                element = self.driver.find_element_by_android_uiautomator(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        else:
            logger.error('NoSuchElementTypeException:%s' %ele_type)
            raise NameError('please enter correct type: id, name, class, link, p_link, xpath, android_uiautomator')

        return element

    def base_find_elements(self, loc):
        '''
                :param loc: loc = xpath=>//android.widget.TextView[@text='我的'] 字符串的类型
                :return: 定位到的元素
                '''
        element = ''
        ele_type = loc.split('=>')[0]
        ele_value = loc.split('=>')[1]
        if ele_type == '' or ele_value == '':
            logger.error('grammatical error, eg:"id=>name"')
            raise NameError('grammatical error, eg:"id=>name"')
        if ele_type == 'id':
            try:
                element = self.driver.find_elements_by_id(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'xpath':
            try:
                element = self.driver.find_elements_by_xpath(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'name':
            try:
                element = self.driver.find_elements_by_name(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'link':
            try:
                element = self.driver.find_elements_by_link_text(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'class':
            try:
                element = self.driver.find_elements_by_class_name(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'p_link':
            try:
                element = self.driver.find_elements_by_partial_link_text(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        elif ele_type == 'android_uiautomator':
            try:
                element = self.driver.find_elements_by_android_uiautomator(ele_value)
                logger.info('had find element{}, by {} via value{}'.format(element.text, ele_type, ele_value))
            except Exception as e:
                logger.error('定位方式有误：%s' % e)
        else:
            logger.error('NoSuchElementTypeException:%s' % ele_type)
            raise NameError('please enter correct type: id, name, class, link, p_link, xpath, android_uiautomator')

        return element

    def base_click(self, loc):
        el = self.base_find_element(loc)
        el.click()

    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text