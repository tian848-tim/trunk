'''
测试用例标题：采购计划测试
测试场景：采购计划业务流程测试——复制
创建者：Tim
创建日期：2018-10-22
最后修改日期：2018-10-22
输入数据：审批流程各个角色账号
输出数据：无
产品分析报告会验证报表数据重复，每次发启要修改报表输入信息

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

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''


class NewProduct(unittest.TestCase):

    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan_copy.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan_copy.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def skuname(self):
        global sku
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan_copy.json', encoding='utf-8')
        data = json.load(file)
        sku = [(d['sku']) for d in data['skuname']]

        return sku

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购计划业务流程测试——复制'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_purchaseplan_flowPurchasePlan_copy'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_NewProduct(self):
        su = self.loadvendername()
        ad = self.loadvendernames()
        sku = self.skuname()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])

        #self.login('Ken_cn', '123')
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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        # 定位到采购计划申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划申请')]").click()

        sleep(2)

        # 定位采购计划第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()

        # 定位复制按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class, 'fa-copy')]").click()

        sleep(2)

        # 定位保存按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class, 'fa-save')]").click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        sleep(2)

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出

        sleep(2)

    def tearDown(self):
                self.driver.quit()

if __name__ == "__main__":
        unittest.main()




