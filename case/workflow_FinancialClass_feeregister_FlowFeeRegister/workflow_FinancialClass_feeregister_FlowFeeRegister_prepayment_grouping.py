'''
测试用例标题：费用登记测试
测试场景：费用登记测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-11-13
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

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

class FeeRegister(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

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
        file = open(rootPath + '/data/workflow_FinancialClass_feeregister_FlowFeeRegister_grouping.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):

        # 脚本标识－标题
        self.script_name = '费用登记-预付尾款-组合'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_feeregister_FlowFeeRegister_prepayment_grouping'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_flowFeeRegister(self):

        su = self.loadvendername()
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

        sleep(3)

        # 定位到费用登记申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用登记')]").click()

        sleep(2)

        # 定位到费用登记新建
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到费用登记费用类型
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-body']//input[@name = 'main.feeType']").click()

        sleep(2)

        # 定位到费用登记费用类型
        self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']//li[contains(text(),'预付合同尾款')]").click()

        sleep(2)

        # 定位到费用登记订单编号
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-body']//input[@name = 'main.orderNumber']").click()

        sleep(2)

        if we[0] != '':

            # 定位到费用登记订单编号
            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinSearchPanelID-body']//input[@name = 'keywords']").send_keys(we[0])

            sleep(2)

            # 定位到费用登记查询
            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinSearchPanelID-body']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            # 定位到费用登记查询
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(),'1')]")

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            sleep(2)

            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='OrderDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        e = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.currency']").get_attribute('value')

        _F = e.capitalize()

        sleep(2)

        totalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.totalPrice{}']".format(_F)).get_attribute('value')

        try:
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        if (a == False):

            try:
                self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

            print(a)

            while (a == True):

                self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//img[@class =  'x-grid-checkcolumn']").click()

                sleep(2)

                try:
                    self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                    a = True
                except:
                    a = False
                if a == True:
                    print("元素存在")
                elif a == False:
                    print("元素不存在")

                print(a)

            else:
                pass

        else:
            pass

        sleep(2)

        writeOff = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.writeOff{}']".format(_F)).get_attribute('value')

        total = float(totalPrice) - float(writeOff)

        totalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.totalPrice{}']".format(_F)).get_attribute('value')

        amount = total - float(totalPrice)

        print('%.1f' % amount)

        if amount == 0.0:

            print("金额正确")

        else:

            print("金额有误，错误金额：", amount)

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//span[contains(@class,'fa-play')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 判断流程
        _prompt = '操作提示流程已启动'

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(2)

        _W = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationGridPanelID-body']/div/table/tbody/tr[1]/td[7]/div").text

        # 写入json
        one = "{}".format(_W)
        mess1 = [{"key": one}]
        two = {"variable": mess1}
        data = dict(two)
        jsonData = json.dumps(data)
        desktop_path = rootPath + '/data/'
        full_path = desktop_path + "test_flowFeeRegister" + time.strftime("%Y-%m-%d") + '.json'
        fileObject = open(full_path, 'w')
        fileObject.write(jsonData)
        fileObject.close()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面



    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
