'''
测试用例标题：费用支付测试
测试场景：费用支付流程测试——出纳作废
创建者：Tim
创建日期：2018-11-14
最后修改日期：2018-11-14
输入数据：供应商：搭瓦家具公司，审批流程各个角色账号
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

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment_AccountPayable_invalid.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment_AccountPayable_invalid.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '费用支付——出纳作废'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_feepayment_FlowFeePayment_AccountPayable_invalid'
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


    def test_flow_fee_register(self):

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

        sleep(2)

        # 定位到费用支付申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用支付')]").click()

        sleep(2)

        # 定位到费用支付新建
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择费用ID
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentFormPanelID-body']//input[@name='main.feeRegistrationName']").click()

        sleep(1)

        try:
            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
            a = True
        except:
            a = False

        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        if  a == True:

            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//img[contains(@class,'x-tool-close')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class,'close')]").click()

            sleep(2)

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用登记')]").click()

            sleep(2)

            # 定位到费用登记新建
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            ## 选择费用类型
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-body']//input[@name='main.feeType']").click()

            sleep(2)

            # 合同尾款
            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '预付合同尾款')]").click()

            sleep(2)

            ## 选择订单编号
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-orderContainer-innerCt']//input[@name='main.orderNumber']").click()

            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            print(len(lis))

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            # 定位采购第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            # 定位到发启按钮
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//span[contains(@class,'fa-play')]").click()

            sleep(3)

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用支付')]").click()

            sleep(2)

            # 定位到费用支付新建
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            ## 选择费用ID
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentFormPanelID-body']//input[@name='main.feeRegistrationName']").click()

        sleep(2)

        if ad[0] != '':


            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//input[@name='keywords]").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//span[contains(@class, 'fa-search')]")

            sleep(2)

             # 定位采购第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinGridPanelID']//div[contains(text(), '1')]")

            sleep(2)

             # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:
             # 定位采购第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinGridPanelID']//div[contains(text(), '1')]")

            sleep(2)

             # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(8)

        try:
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]//span[contains(text(), '{}')]".format('调整申请')).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        sleep(2)

        if a == True:

            # 选择新品开发第一条记录
            self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentGridPanelID-body']//div[contains(text(), '1')]").click()

            # 强制等待
            sleep(2)

            # 定位到新品开发编辑
            self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-pencil-square-o')]").click()

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@class='x-list-plain']//li[contains(text(),'{}')]".format(su[1][0])).click()

            sleep(2)

            # 定位到发启按钮
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class,'fa-check-square')]").click()

            # 获取弹窗提示：
            self.driver.implicitly_wait(30)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            # 强制等待
            sleep(5)

        else:
            pass

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点'''

        self.login(su[1][0],su[1][1])
        #self.login('Vic_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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

        # 选择处理人
        #self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentMainTabsPanelID-win-0']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择JACK
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack')]").click()

        #sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(3)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第三点'''

        self.login(su[2][0],su[2][1])
        #self.login('Jack.L', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(3)

        # 定位到费用支付申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用支付')]").click()

        sleep(3)

        # 获取当前节点处理人
        try:
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]//div[text()='{}']".format(su[3][0])).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("总监元素存在")
        elif a == False:
            print("总监元素不存在")

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        print(a)


        if  a == True :


             '''第四节点'''

             self.login(su[3][0], su[3][1])
             #self.login('emma', '123')

             sleep(5)

             # 关闭弹出框
             self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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

             # 选择处理人
             #self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentMainTabsPanelID-win-0']//input[@name='flowNextHandlerAccount']").click()

             #sleep(2)

             # 选择JACK
             #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'dickson')]").click()

             #sleep(2)


             # 点击通过
             self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

             self.driver.implicitly_wait(30)
             # 获取弹窗提示：
             self.driver.implicitly_wait(10)
             a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
             print(a)

             sleep(3)



             self.driver.find_element_by_link_text('注销').click()  # 点击注销

             self.driver.find_element_by_link_text('是').click()

             alert = self.driver.switch_to_alert()

             alert.accept()  # 退出页面

             sleep(5)

        else:
            pass


        '''第五节点'''

        self.login(su[4][0], su[4][1])
        #self.login('dickson', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(30)

        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(3)



        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第六节点'''

        self.login(su[5][0], su[5][1])
        #self.login('emma', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(30)

        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(3)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''最后节点'''

        self.login(su[4][0], su[4][1])
        #self.login('emma', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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

        # 定位iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            "//*[@id='FlowFeePaymentMainTabsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 点击作废
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'flowcancel')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

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
