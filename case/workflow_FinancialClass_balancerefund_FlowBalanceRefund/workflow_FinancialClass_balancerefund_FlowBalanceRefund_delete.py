'''
测试用例标题：差额退款测试
测试场景：差额退款业务流程测试——删除
创建者：Tim
创建日期：2018-11-15
最后修改日期：2018-11-15
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
# -*- coding: utf-8 -*-
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



class Refund(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")


    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_FinancialClass_balancerefund_FlowBalanceRefund_delete.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_balancerefund_FlowBalanceRefund_delete.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):

        # 脚本标识－标题
        self.script_name = '差额退款——删除'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_balancerefund_FlowBalanceRefund_delete'
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


    def test_flow_balance_refund(self):

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

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(3)

        # 定位到差额退款申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '差额退款')]").click()

        sleep(2)

        # 定位到额退款新建
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 退款类型
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormPanelID-body']//input[@name='main.type']").click()

        sleep(2)

        # 选择样品采购费
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '供应商')]").click()

        sleep(2)

        # 选择供应商
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormPanelID']//input[@name='main.vendorName']").click()

        sleep(2)

        if ad[0] != '':

               # 定位到关键字
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

               sleep(2)

               # 点击搜索
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

               sleep(2)

               # 定位供应商第一条记录
               _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

               sleep(2)

               # 在此元素上双击
               ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            _elementFiveth = (random.randint(1, 10))

            # 定位供应商第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 订单编号
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundForm']//input[@name='main.orderNumber']").click()

        try:
             self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        sleep(2)

        while (a == True) :

            # 订单编号
            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//img[contains(@class,'x-tool-close')]").click()

            sleep(2)

            # 在此元素上双击
            #ActionChains(self.driver).double_click(_elementFirst).perform()

            #sleep(2)

            # 选择供应商
            self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormPanelID']//input[@name='main.vendorName']").click()

            sleep(2)

            if ad[0] != '':

                # 定位到关键字
                self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                sleep(2)

                # 点击搜索
                self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                sleep(2)

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            else:

                _elementFiveth = (random.randint(1, 10))

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            # 订单编号
            self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundForm']//input[@name='main.orderNumber']").click()

            sleep(2)


            try:
                self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

                sleep(2)

        else:
            pass

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        sleep(2)

        _elementFiveth = (random.randint(1, len(lis)))

        sleep(2)

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 选择单号
        _elementFirst =self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormPanelID-asnContainer']//img[@role='presentation']")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        try:
             self.driver.find_element_by_xpath("//*[@id='AsnDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        sleep(2)

        while (a == True) :

            # 订单编号
            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']////img[contains(@class,'x-tool-close')]").click()

            sleep(2)

            # 在此元素上双击
            #ActionChains(self.driver).double_click(_elementFirst).perform()

            #sleep(2)

            # 订单编号
            self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundForm']//input[@name='main.orderNumber']").click()

            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            print(len(lis))

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            sleep(2)

            _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            # 选择单号
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormPanelID-asnContainer']//img[@role='presentation']")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            try:
                self.driver.find_element_by_xpath("//*[@id='AsnDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

            sleep(2)

        else:
            pass


        ul = self.driver.find_element_by_xpath("//*[@id='AsnDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        sleep(2)

        _elementFiveth = (random.randint(1, len(lis)))

        sleep(2)

        # 定位第一条记录
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='AsnDialogWinID']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='AsnDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 选择单号
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundSubGridPanelID-product-normal-body']/div/table/tbody/tr[1]/td[11]").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 100))

        # 选择单号
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundFormGridPanelID-f-body']//input[@name='diffAud']").send_keys(_elementFiveth)

        sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundForm']//span[contains(@class,'fa-save')]").click()

        sleep(8)




        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面

        sleep(5)

        '''删除'''

        self.login(su[0][0],su[0][1])
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(3)

        # 定位到差额退款申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '差额退款')]").click()

        sleep(2)

        # 定位到差额退款申请第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到差额退款申请删除按钮
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundView']//span[contains(@class, 'fa-trash')]").click()

        sleep(2)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面

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

if __name__ == "__main__":
        unittest.main()