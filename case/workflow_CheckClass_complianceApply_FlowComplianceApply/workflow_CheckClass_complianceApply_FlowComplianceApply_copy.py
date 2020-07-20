'''
测试用例标题：安检申请流程
测试场景：安检申请流程正常审批——复制
创建者：Tim
创建日期：2018-10-29
最后修改日期：2018-10-29
输入数据：审批流程各个角色账号
输出数据：无

'''


# -*- coding: utf-8 -*-
import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import json
'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class complianceApply(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_copy.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_copy.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def skuname(self):
        global name
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_copy.json', encoding='utf-8')
        data = json.load(file)
        name = [(d['name']) for d in data['skuname']]

        return name


    def setUp(self):
        #脚本标识-标题
        self.script_name ='安检申请流程正常审批——复制'
        #脚本标识-ID
        self.script_id ='workflow_CheckClass_complianceApply_FlowComplianceApply_copy'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            #如果使用最新的foxfire 需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
                # 如果使用最新firefox需要使用下面这句
                self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        #定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)#d登录页面
        self.driver.find_element_by_id("account-inputEl").send_keys(username)
        self.driver.find_element_by_id("password-inputEl").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_flow_compliance_apply(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        sku = self.skuname()
        for i in range(0, len(su)):
          print(su[0][0])
          print(su[0][1])
        self.login(su[0][0],su[0][1])

        #self.login('Vic_cn','123')

        sleep(5)

        '''点击新增安检申请流程'''

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

        # 点击申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(3)

        # 点击检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'检验类')]").click()

        sleep(3)

        # 点击安检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'安检申请')]").click()

        sleep(2)

        # 定位第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementViewGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(2)

        # 定位复制按钮
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementView']//span[contains(@class,'fa-copy')]").click()

        sleep(2)

        # 定位保存按钮
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementForm']//span[contains(@class,'fa-save')]").click()

        sleep(5)

        # 点击注销

        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()