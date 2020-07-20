'''
测试用例标题：采购定金申请测试
测试场景：采购定金申请业务流程测试
创建者：Tim
创建日期：2018-11-19
最后修改日期：2018-11-19
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
from time import sleep
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

class purchaseContract(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def variable(self):


        try:
            global ABC,variable
            file = open(rootPath + '/data/'+ "test_PurchaseContract" + time.strftime("%Y-%m-%d") + '.json', encoding='utf-8')
            data = json.load(file)
            ABC = [(d['key']) for d in data['variable']]
            variable = True
            return ABC

        except IOError:
            variable = False

            print("test_PurchaseContract" + time.strftime("%Y-%m-%d") + '.json'+"File not found")



    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit_grouping.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit_grouping.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购合同定金-组合'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit_grouping'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(15)
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get('http://192.168.1.112:880/')  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_FlowPurchaseContractDeposit(self):
        su = self.loadvendername()
        ad = self.loadvendernames()
        we = self.variable()


        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Vic_cn','123')
        sleep(5)

        try:
             self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("系统提示元素存在")
        elif a == False:
            print("系统提示元素不存在")

        print(a)

        if a == True:

           # 关闭弹出框
           self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        else:
            pass

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(2)

        # 定位到合同订金
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '合同订金申请')]").click()

        sleep(2)

        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractView-body']//input[@name='keywords']").send_keys(we[0])

        sleep(2)

        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractView-body']//span[contains(@class, 'fa-search')]").click()

        try:
             self.driver.find_element_by_xpath("//*[@id='FlowDepositContractGridPanelID-body']//div[contains(test(),'没有数据！')]").is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("合同订金不存在")
        elif a == False:
            print("合同订金存在")


        print(a)

        sleep(2)

        if a == True:

            self.driver.quit()

        else:

            pass

        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位到币种
        _R = self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.currency']").get_attribute('value')

        _U = _R.capitalize()

        print(_U)

        # 定位到应付款
        payable = self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.payable{}']".format(_U)).get_attribute('value')

        sleep(2)

        # 定位到实付款
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.payment{}']".format(_U)).clear()

        sleep(2)

        # 定位到实付款
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.payment{}']".format(_U)).send_keys(payable)

        sleep(2)

        # 定位到通过
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//span[contains(@class,'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(2)


        self.login(su[0][0], su[0][1])
        #self.login('emma', '123')

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

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面

        sleep(5)


    def isElementExist(self, link):
        flag = True

        try:
            self.driver.find_element_by_xpath(link)

            print('元素找到')
            return flag
        except:
            flag = False
            print('未找到')
            return flag



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


if __name__ == "__main__":
    unittest.main()
