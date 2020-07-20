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
import json
import logging
import datetime

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')
logging.basicConfig(level=logging.INFO)

'''
测试用例
'''


class CustomClearance(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/test7.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/test7.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def Browser(self):

        global BrowserName
        file = open(rootPath + '/data/test7.json', encoding='utf-8')
        data = json.load(file)
        BrowserName = [(d["BrowserName"]) for d in data["Browser"]]

        return BrowserName

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '清关检查'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_customclearance_flowCustomClearance'
        self.target_url = self.base_url + self.project_path

        name = self.Browser()

        print(name)

        for i in range(0, len(name)):
            print(name[i])

        try:
            if name[0] == "firefox" or name[0] == "Firefox" or name[0] == "ff":
                print("start browser name :Firefox")
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(15)
                self.driver.maximize_window()
                return self.driver
            elif name[0] == "chrome" or name[0] == "Chrome":
                print("start browser name :Chrome")
                self.driver = webdriver.Chrome()
                self.driver.implicitly_wait(15)
                self.driver.maximize_window()
                return self.driver
            elif name[0] == "ie" or name[0] == "Ie":
                print("start browser name :Ie")
                self.driver = webdriver.Ie()
                self.driver.implicitly_wait(15)
                self.driver.maximize_window()
                return self.driver
            elif name[0] == "phantomjs" or name[0] == "Phantomjs":
                print("start browser name :phantomjs")
                self.driver = webdriver.PhantomJS()
                self.driver.implicitly_wait(15)
                self.driver.maximize_window()
                return self.driver
            else:
                print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
        except Exception as msg:
            print("启动浏览器出现异常：%s" % str(msg))

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()
        navigationStart4 = self.driver.execute_script("return window.performance.timing.fetchStart")
        loadEventEnd4 = self.driver.execute_script("return window.performance.timing.loadEventEnd")

        print(navigationStart4)
        print(loadEventEnd4)
        durtime4 = (loadEventEnd4 - navigationStart4)
        print("Login加载时间", str(durtime4 / 1000), ".s")
        logging.info("Login加载时间"+str(durtime4 / 1000)+".s")
        sleep(5)


    def test_CustomClearance(self):

        su = self.loadvendername()
        ad = self.loadvendernames()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)
        starttime = datetime.datetime.now()

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同申请')]").click()


        # 定位到All pending文件夹

        endtime = datetime.datetime.now()

        loadtime=(endtime-starttime)
        print(loadtime)
        print(starttime)
        print(endtime)



        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//input[contains(@class, 'x-form-text')]").send_keys('J19-0412')

        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-search')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[text()='{}']".format(1)).click()

        sleep(2)


        # 定位到清关申请编辑
        self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(@class,'fa-pencil-square-o')]").click()

        navigationStart2 = self.driver.execute_script("return window.performance.timing.requestStart")
        loadEventEnd2 = self.driver.execute_script("return window.performance.timing.responseEnd")
        loadEvent2 = self.driver.execute_script("return window.performance.timing")

        print(navigationStart2)
        print(loadEventEnd2)
        print(loadEvent2)
        durtime2 = (loadEventEnd2 - navigationStart2)
        print("编辑加载时间", str(durtime2 / 1000), ".s")
        logging.info("编辑加载时间"+ str(durtime2 / 1000)+".s")

        self.driver.implicitly_wait(30)

        sleep(5)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

        navigationStart3 = self.driver.execute_script("return window.performance.timing.fetchStart")
        loadEventEnd3 = self.driver.execute_script("return window.performance.timing.loadEventEnd")

        print(navigationStart3)
        print(loadEventEnd3)

        durtime3 = (loadEventEnd3 - navigationStart3)
        print("页面加载时间", str(durtime3 / 1000), ".s")
        logging.info("页面加载时间"+ str(durtime3 / 1000)+".s")

        sleep(5)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop ')]").click()

        sleep(2)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '统计分析')]").click()

        sleep(2)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '销售预测分析')]").click()

        navigationStart5 = self.driver.execute_script("return window.performance.timing.fetchStart")
        loadEventEnd5 = self.driver.execute_script("return window.performance.timing.loadEventEnd")

        durtime5 = (loadEventEnd5 - navigationStart5)
        print("页面加载时间", str(durtime5 / 1000), ".s")
        logging.info("页面加载时间"+ str(durtime5 / 1000)+".s")

        sleep(5)

    def tearDown(self):
        self.driver.quit()

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



if __name__ == "__main__":
    unittest.main()
