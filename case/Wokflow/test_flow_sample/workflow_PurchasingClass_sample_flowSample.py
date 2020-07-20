'''
测试用例标题：样品申请测试
测试场景：样品申请业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-15
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


class sample(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def variable(self):


        try:
            global ABC,variable
            file = open(rootPath + '/data/'+ "test_NewProductDocument" + time.strftime("%Y-%m-%d") + '.json', encoding='utf-8')
            data = json.load(file)
            ABC = [(d['key']) for d in data['variable']]
            variable = True
            return ABC

        except IOError:
            variable = False

            print("test_NewProductDocument" + time.strftime("%Y-%m-%d") + '.json'+"File not found")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_sample_flowSample.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_sample_flowSample.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_PurchasingClass_sample_flowSample.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_sample_flowSample.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '样品申请'
        # 脚本标识－ID
        self.script_id = 'test_flow_sample'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.verificationErrors = []
        self.accept_next_alert = True

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    # 判断当前语言
    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

    def test_Sample(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        qw = self.variable()
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

        # 定位到样品申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

        sleep(2)

        # 定位到样品申请新建
        self.driver.find_element_by_xpath("//*[@id='FlowSampleView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择供应商
        self.driver.find_element_by_xpath( "//*[@id='FlowSampleViewFormPanelID-body']//input[@name='main.vendorName']").click()

        sleep(2)

        if variable == True:

                 ## 定位到关键字
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(qw[1])

                 sleep(2)

                 # 点击搜索
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                 sleep(2)

                 # 定位供应商第一条记录
                 _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                 # 在此元素上双击
                 ActionChains(self.driver).double_click(_elementFirst).perform()

        elif ad[0] != '':

                 ## 定位到关键字
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                 sleep(2)

                 # 点击搜索
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                 sleep(2)

                 # 定位供应商第一条记录
                 _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                 # 在此元素上双击
                 ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            _elementFiveth = (random.randint(1, len(lis)))

            # 定位供应商第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加样品按钮'''
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID_header-body']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(1)

        _NoData = self.driver.find_element_by_xpath("//div[@id='ProductDialogWinGridPanelID-body']/div").text

        if _NoData == lg[2]:

        #try:
             #self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
             a = True
        else:
             a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        sleep(1)

        while (a == True):

            # 关闭
            self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//img[contains(@class, 'x-tool-close')]").click()

            sleep(2)

            ## 选择供应商
            self.driver.find_element_by_xpath("//*[@id='FlowSampleViewFormPanelID-body']//input[@name='main.vendorName']").click()

            sleep(2)

            if variable == True:

                ## 定位到关键字
                self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(qw[1])

                sleep(2)

                # 点击搜索
                self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                sleep(2)

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            elif ad[0] != '':

                ## 定位到关键字
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

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            else:

                ul = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']/div/table/tbody")

                lis = ul.find_elements_by_xpath('tr')

                _elementFiveth = (random.randint(1, len(lis)))

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath(
                    "//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            # 定位添加样品按钮'''
            _elementSecond = self.driver.find_element_by_xpath(
                "//*[@id='FlowSampleFormGridPanelID_header-body']//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

            _NoData = self.driver.find_element_by_xpath("//div[@id='ProductDialogWinGridPanelID-body']/div").text

            if _NoData == lg[2]:

                # try:
                # self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                a = True
            else:
                a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

            print(a)

            sleep(1)

        else:
            pass

        if variable == True:
            ## 定位到关键字
            self.driver.find_element_by_xpath(
                "//*[@id='ProductDialogWinID-body']//input[@name='keywords']").send_keys(qw[0])

            sleep(2)

            # 点击搜索
            self.driver.find_element_by_xpath(
                "//*[@id='ProductDialogWinID-body']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            # 定位供应商第一条记录
            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            _elementFiveth = (random.randint(1, len(lis)))

            # 定位样品第一条记录
            _elementThird = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementThird).perform()

            sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 点击aud
        self.driver.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[5]").click()

        sleep(2)

        # 清除输入框
        self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeAud']").clear()

        sleep(2)

        _E = random.randint(1,100)

        ## 定位到AUD输入
        self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeAud']").send_keys(_E)

        sleep(2)

        # 点击样品件数
        self.driver.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[8]").click()

        sleep(2)

        ## 清除样品件数
        self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='qty']").clear()

        sleep(2)

        _F = random.randint(1,100)

        ## 定位到样品件数
        self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='qty']").send_keys(_F)

        sleep(2)

        # 定位到费用可退
        self.driver.find_element_by_xpath( "//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[12]").click()

        sleep(2)

        # 清除输入框
        self.driver.find_element_by_xpath( "//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeRefund']").clear()

        sleep(2)

        _G = random.randint(1,2)

        ## 定位费用可退
        self.driver.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeRefund']").send_keys(_G)

        sleep(2)

        # 定位到费用可退
        self.driver.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[12]").click()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowSampleForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[3]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        try:

            self.driver.find_element_by_xpath(
                "//*[@id='FlowSampleViewGridPanelID-body']/div/table/tbody/tr[1]//span[contains(text(),'{}')]".format(
                    '审批中')).is_displayed()

            process = True
        except:
            process = False

        if process == True:
            print("审批中")
        elif process == False:
            print("流程通过")


        self.driver.find_element_by_link_text(lg[5]).click()  # 点击注销


        self.driver.find_element_by_link_text(lg[6]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(2)

        if process == True:

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

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@id='FlowSampleForm']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[4]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(2)

    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
