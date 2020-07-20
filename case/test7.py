'''
测试用例标题：清关测试
测试场景：清关申请业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-22
输入数据：审批流程各个角色账号
输出数据：无

'''

# -*- coding: utf-8 -*-
import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
#sys.path.append(rootPath)

import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest,configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import random




'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')


'''
测试用例
'''


class CustomClearance(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '文件上传'
        # 脚本标识－ID
        self.script_id = 'test_flow_custom_clearance'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_CustomClearance(self):
        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '文件管理')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '我的文件')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='MyDocumentView']//span[contains(text(), '选取文件')]").click()

        sleep(2)

        file_path = "C:\\Users\Administrator\Desktop\修改内箱净重20190607.sql"

        sleep(2)

        os.system(rootPath +"\\autoit\\import1.exe %s " % file_path)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='MyDocumentView']//div[contains(text(), '请选择')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='MyDocumentView']//input[@name='category']").click()

        sleep(2)
        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable' and @style='overflow: auto; height: 299px;']/ul")

        lis = ul.find_elements_by_xpath('li')

        print(lis)

        first_category = lis[random.randint(0, len(lis) - 1)]

        print(len(lis))

        print(first_category)

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()


        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='MyDocumentView']//span[contains(@class,'fa-refresh')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='MyDocumentView']//span[contains(@class,'fa-save')]").click()

        sleep(5)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面



    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
