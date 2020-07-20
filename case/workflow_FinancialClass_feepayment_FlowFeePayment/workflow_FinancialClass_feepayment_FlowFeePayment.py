'''
测试用例标题：费用支付测试
测试场景：费用支付流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
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

import json
import random

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment.json', encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_FinancialClass_feepayment_FlowFeePayment.json', encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '费用支付'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_feepayment_FlowFeePayment'
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

    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

    def test_flow_fee_register(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        cn = self.CN()
        en = self.EN()


        for i in range(0, len(su)):
          print(su[i][0])
          print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Vic_cn','123')
        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

        sleep(2)

        # 定位到费用支付申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[1])).click()

        sleep(2)

        # 定位到费用支付新建
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-plus')]").click()

        self.driver.implicitly_wait(60)

        ## 选择费用ID
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentFormPanelID-body']//input[@name='main.feeRegistrationName']").click()

        sleep(1)

        # 检查元素是否存在
        _NoData = self.driver.find_element_by_xpath("//div[@id='FeeRegistrationDialogWinGridPanelID-body']/div").text

        if _NoData in lg[4]:

        #try:
            #self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
            a = True
        else:
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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[2])).click()

            sleep(2)

            # 定位到费用登记新建
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            ## 选择费用类型
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-body']//input[@name='main.feeType']").click()

            sleep(2)

            # 合同尾款
            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[text()='{}']".format(lg[9])).click()

            sleep(2)

            ## 选择订单编号
            self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationFormPanelID-orderContainer-innerCt']//input[@name='main.orderNumber']").click()

            # 元素等待
            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(), '1')]"))
                )

            except IOError as a:
                print("找不元素 " + a)

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

            # 元素等待
            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//*[@id='FlowFeeRegistrationSubGridPanelID-price-body']//div[contains(text(), '1')]"))
                )

            except IOError as a:
                print("找不元素 " + a)

            e = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.currency']").get_attribute('value')

            _F = e.capitalize()

            sleep(2)

            totalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.totalPrice{}']".format(_F)).get_attribute('value')



            try:
                self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//div[contains(text(),'{}')]".format(lg[4])).is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("冲销金额元素不存在")
            elif a == False:
                print("冲销金额元素存在")

            print(a)

            if (a == False):

                try:
                    self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                    a = True
                except:
                    a = False
                if a == True:
                    print("冲销金额元素存在")
                elif a == False:
                    print("冲销金额元素不存在")

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
                        print("冲销金额元素存在")
                    elif a == False:
                        print("冲销金额元素不存在")

                    print(a)

                else:
                    pass

            else:
                pass

            sleep(2)

            writeOff = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.writeOff{}']".format(_F)).get_attribute('value')

            total = float(totalPrice) - float(writeOff)

            totalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationForm']//input[@name='main.totalPrice{}']".format(_F)).get_attribute('value')

            amount = round(total,2) - round(float(totalPrice),2)

            print(amount)

            if amount == 0.00 :

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
            _prompt = lg[5]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[1])).click()

            sleep(2)

            # 定位到费用支付新建
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            ## 选择费用ID
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentFormPanelID-body']//input[@name='main.feeRegistrationName']").click()

        if ad[0] != '':


            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//input[@name='keywords]").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinID']//span[contains(@class, 'fa-search')]")

            sleep(2)

            _er = self.driver.find_element_by_xpath(
                "//*[@id='FeeRegistrationDialogWinGridPanelID-body']/div/table/tbody/tr[1]/td[6]/div").text

             # 定位采购第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinGridPanelID']//div[contains(text(), '1')]")

            sleep(2)

             # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            sleep(1)

            _er = self.driver.find_element_by_xpath(
                "//*[@id='FeeRegistrationDialogWinGridPanelID-body']/div/table/tbody/tr[1]/td[6]/div").text

             # 定位采购第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='FeeRegistrationDialogWinGridPanelID']//div[contains(text(), '1')]")

            sleep(2)

             # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        e = self.driver.find_element_by_xpath("//div[@class='x-form-display-field' and @aria-invalid='false']/span").text

        print(e)

        _F = e.capitalize()

        sleep(2)

        totalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//input[@name='main.totalPrice{}']".format(_F)).get_attribute('value')

        sleep(2)

        paymentTotalPrice = self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//input[@name='main.paymentTotalPrice{}']".format(_F)).get_attribute('value')

        sleep(2)

        amount = round(float(totalPrice),2) - round(float(paymentTotalPrice),2)

        print(amount)

        if amount == 0.00 :

            print("支付金额正确")

        else:

            print("支付金额有误，错误金额：",amount)

        sleep(2)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class,'fa-save')]").click()

        self.driver.implicitly_wait(60)

        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView-body']//span[contains(@class,'fa-search')]").click()

        sleep(1)

        # 定位关键字位置
        ul = self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')

        for i in range(0, len(lis)):

            if su[0][0] in lis[i].text:
                print(i + 1)

                column = i + 1

                break

        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(3)

        # 定位到编辑
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class,'fa-pencil-square-o')]").click()

        #元素等待
        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(_er)))
            )

        except IOError as a:
            print("找不元素 " + a)


        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 判断流程
        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(1)

        _handler = self.driver.find_element_by_xpath(
            "//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                column)).get_attribute('textContent')

        print(_handler)

        for i in range(1, len(su)):

            if su[i][0] == _handler:
                _value = su[i][0]

                break

        self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[8]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点'''

        if _value == su[1][0]:

            self.login(su[1][0],su[1][1])
            #self.login('Vic_cn', '123')

            sleep(5)

            lg = self.CheckLanguage()

            if lg == True:

                lg = cn

            else:

                lg = en

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
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到财务类
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

            sleep(2)

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            sleep(2)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[1][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(2)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[3])).click()

            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 元素等待
            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(
                                                          _er)))
                )

            except IOError as a:
                print("找不元素 " + a)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square ')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[6]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(1)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(2, len(su)):

                if su[i][0] == _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[8]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)


        '''第三点'''

        if _value == su[2][0]:

            self.login(su[2][0],su[2][1])
            #self.login('Jack.L', '123')

            lg = self.CheckLanguage()

            if lg == True:

                lg = cn

            else:

                lg = en

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
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到财务类
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

            sleep(2)

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[1])).click()

            sleep(2)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[2][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(1)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[3])).click()

            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 元素等待
            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(
                                                          _er)))
                )

            except IOError as a:
                print("找不元素 " + a)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[6]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到财务类
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

            sleep(3)

            # 定位到费用支付申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[1])).click()

            sleep(1)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(3, len(su)):

                if su[i][0] == _handler:
                    _value = su[i][0]

                    break


            self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[8]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)

        if _value == su[3][0]:
             '''第四节点'''

             self.login(su[3][0], su[3][1])
             #self.login('emma', '123')

             sleep(5)

             lg = self.CheckLanguage()

             if lg == True:

                 lg = cn

             else:

                 lg = en

             try:
                 self.driver.find_element_by_xpath(
                     "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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
                 self.driver.find_element_by_xpath(
                     "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

             else:
                 pass

             sleep(2)

             # 定位到工作面板
             self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

             sleep(2)

             # 定位到待办事项
             self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[3])).click()

             sleep(2)

             # 定位到待办事项第一条记录
             self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

             sleep(2)

             # 点击马上处理
             self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

             # 元素等待
             try:
                 WebDriverWait(self.driver, 120).until(
                     EC.visibility_of_element_located((By.XPATH,
                                                       "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(
                                                           _er)))
                 )

             except IOError as a:
                 print("找不元素 " + a)


             # 点击通过
             self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

             self.driver.implicitly_wait(60)
             # 获取弹窗提示：
             a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
             print(a)

             _prompt = lg[6]

             if _prompt in a:

                 pass

             else:

                 print("流程错误")

                 self.driver.quit()

             sleep(2)

             self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

             self.driver.find_element_by_link_text(lg[8]).click()

             alert = self.driver.switch_to_alert()

             alert.accept()  # 退出页面

             sleep(5)


        '''第六节点'''

        self.login(su[4][0], su[4][1])
        #self.login('dickson', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[3])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        #元素等待
        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(_er)))
            )

        except IOError as a:
            print("找不元素 " + a)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[6]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

        sleep(3)

        # 定位到费用支付申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[1])).click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')

        for i in range(0, len(lis)):

            if lg[8] in lis[i].text:

                a = True

                break

            else:
                a = False

        self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[8]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        if a == True:

                '''第七节点'''

                self.login(su[4][0], su[4][1])
                #self.login('dickson', '123')

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

                # 定位到工作面板
                self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

                sleep(2)

                # 定位到待办事项
                self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[3])).click()

                sleep(2)

                # 定位到待办事项第一条记录
                self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

                sleep(4)

                # 点击马上处理
                self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

                # 元素等待
                try:
                    WebDriverWait(self.driver, 120).until(
                        EC.visibility_of_element_located((By.XPATH,
                                                          "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(
                                                              _er)))
                    )

                except IOError as a:
                    print("找不元素 " + a)

                # 点击通过
                self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

                self.driver.implicitly_wait(60)
                a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
                print(a)

                _prompt = lg[6]

                if _prompt in a:

                    pass

                else:

                    print("流程错误")

                    self.driver.quit()

                self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

                self.driver.find_element_by_link_text(lg[8]).click()

                alert = self.driver.switch_to_alert()

                alert.accept()  # 退出页面

                sleep(5)

        else:

            pass



        '''最后节点'''

        self.login(su[4][0], su[4][1])
        #self.login('emma', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[3])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        #元素等待
        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='FlowFeePaymentFormPanelID-body']//div[contains(text(), '{}')]".format(_er)))
            )

        except IOError as a:
            print("找不元素 " + a)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[6]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[8]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面



    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
