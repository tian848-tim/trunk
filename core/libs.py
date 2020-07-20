# -*- coding: utf-8 -*-
import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

import time, unittest
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from core.logger import Log

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class MainTestCase(unittest.TestCase):
    # 运行时代码输出日志对象
    logger = Log(level='info', log_path=cfg.get("logs", "path"), file_pre='script_')

    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("logs", "path") + '/' + cfg.get("logs", "pre") + '%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")
    webdriver_log = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")
    # 脚本标识－标题
    script_name = '脚本标题'
    # 脚本标识－ID
    script_id = '脚本ID'


    '''设置浏览器驱动类型'''
    def init(self, driver='firefox', time_to_wait=10 ):
        self.target_url = self.base_url + self.project_path
        self.verificationErrors = []

        # 以下变量可以在脚本中重写 ============
        self.accept_next_alert = True
        # 以上变量可以在脚本中重写 ============

        if driver == 'firefox':
            if (cfg.get("webdriver", "enabled") == "off"):
                # 如果使用最新firefox需要屏蔽下面这句
                self.driver = webdriver.Firefox()
            else:
                # 如果使用最新firefox需要使用下面这句
                self.driver = webdriver.Firefox(log_path=self.webdriver_log)
        elif driver == 'chrome':
            # chrome
            options = webdriver.ChromeOptions()
            prefs = {
                'profile.default_content_setting_values':
                    {'notifications': 2}
            }
            options.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(chrome_options=options)

        # 等待响应时长
        self.driver.implicitly_wait(time_to_wait)



    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
