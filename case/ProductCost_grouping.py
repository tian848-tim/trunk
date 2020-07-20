'''
测试用例标题：成本计算测试
测试场景：成本计算业务流程测试
创建者：Tim
创建日期：2019-9-18
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

import json
import random

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class ProductCategory(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def variable(self):


        try:
            global ABC,variable
            file = open(rootPath + '/data/'+ "test_FlowFeePayment" + time.strftime("%Y-%m-%d") + '.json', encoding='utf-8')
            data = json.load(file)
            ABC = [(d['key']) for d in data['variable']]
            variable = True
            return ABC

        except IOError:

            variable = False

            print("test_FlowFeePayment" + time.strftime("%Y-%m-%d") + '.json'+"File not found")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/ProductCost_grouping.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/ProductCost_grouping.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '成本计算-组合'
        # 脚本标识－ID
        self.script_id = 'ProductCost_grouping'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_ProductCost_grouping(self):
        su = self.loadvendername()
        ad = self.loadvendernames()
        qw = self.variable()

        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('yvonne','123')

        sleep(5)

        try:
             self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        if a == True:

           # 关闭弹出框
           self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        else:
            pass

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(2)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(2)

        # 定位到成本计算
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'成本计算')]").click()

        sleep(2)


        # 定位到成本计算新建
        self.driver.find_element_by_xpath("//*[@id='ProductCostView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到发货计划编号
        self.driver.find_element_by_xpath("//*[@id='ProductCostViewFormPanelID']//input[contains(@name,'main_shippingPlanName')]").click()

        sleep(2)

        if  variable == True:

            # 定位到发货计划编号
            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID-body']//input[@name='keywords']").send_keys(qw[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID-body']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//div[contains(text(),'1')]").click()

        elif ad[0] != '':

            # 定位到发货计划编号
            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//div[@name='keywords']").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//div[contains(text(),'1')]").click()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            # 定位到发货计划
            self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//div[text()={}]".format(_elementFiveth)).click()

        sleep(2)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(5)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductCostForm']//span[contains(@class,'fa-save')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        # 定位到新品档案第一条
        self.driver.find_element_by_xpath("//*[@id='ProductCostViewGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(2)

        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='ProductCostViewTabsPanelId']//span[contains(text(),'档案修改历史')]").click()

        sleep(2)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='ProductCostViewGridPanelID-ArchivesHistoryTabGrid-locked-body']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位到审核
        self.driver.find_element_by_xpath("//*[@id='ProductCostForm']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 获取弹窗提示：
        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)


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



