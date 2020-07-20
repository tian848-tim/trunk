'''
测试用例标题：采购计划测试
测试场景：采购计划业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-19
输入数据：审批流程各个角色账号
输出数据：无
产品分析报告会验证报表数据重复，每次发启要修改报表输入信息
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


class purchasePlan(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def skuname(self):
        global skuname
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        skuname = [(d['sku']) for d in data['skuname']]

        return skuname

    def quotation(self):
        global quotation
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        quotation = [(d['key']) for d in data['quotation']]

        return quotation

    def keywords(self):
        global keywords
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        keywords = [(d['key']) for d in data['keywords']]

        return keywords


    def leadTime(self):
        global leadTime
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json', encoding='utf-8')
        data = json.load(file)
        leadTime = [(d['key']) for d in data['leadTime']]

        return leadTime

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_purchaseplan_flowPurchasePlan.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购计划'
        # 脚本标识－ID
        self.script_id = 'test_flow_purchaseplan'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(15)
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()

    # 判断当前语言
    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_PurchasePlan(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        sku = self.skuname()
        we = self.quotation()
        er = self.keywords()
        rt = self.leadTime()
        cn = self.CN()
        en = self.EN()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])

        #self.login('Ken_cn', '123')
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

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[0])).click()

        sleep(2)

        # 定位到采购计划新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        if we[0] != '':

            # 定位到采购询价
            self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'x-btn-icon-el  ')]").click()

            sleep(2)


            if  er[0] != '':

                       # 定位到供应商选择器关键字输入框
                       self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinID']//input[@name='keywords']").send_keys(er[0])

                       sleep(2)

                       # 定位到查询
                       self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinID']//span[contains(@class,'fa-search')]").click()

                       sleep(2)

                       # 定位查询结果第一个元素
                       _element = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                       sleep(2)

                       # 在此元素上双击
                       ActionChains(self.driver).double_click(_element).perform()

                       # 定位到确认
                       self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinID']//span[contains(@class,'fa-check')]").click()

            else:

                       _elementFiveth = (random.randint(1, 10))

                       sleep(2)

                       # 定位查询结果第一个元素
                       _element = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                       sleep(2)

                       # 在此元素上双击
                       ActionChains(self.driver).double_click(_element).perform()

                       # 定位到确认
                       self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationDialogWinID']//span[contains(@class,'fa-check')]").click()

        else:

               # 定位到供应商名称输入框
               self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.vendorName']").click()

               sleep(2)

               if  ad[0] != '':

                          # 定位到供应商选择器关键字输入框
                          self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                          sleep(2)

                          # 定位到查询
                          self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                          sleep(2)

                          # 定位查询结果第一个元素
                          _element = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                          sleep(2)

                          # 在此元素上双击
                          ActionChains(self.driver).double_click(_element).perform()

               else:

                          _elementFiveth = (random.randint(1, 10))

                          sleep(2)

                          # 定位查询结果第一个元素
                          _element = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                          sleep(2)

                          # 在此元素上双击
                          ActionChains(self.driver).double_click(_element).perform()


        sleep(3)

        # 定位到订单类型
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.purchaseType']").click()

        sleep(1)

        # 定位订单类型
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '国际订单')]").click()

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[0]

        first_category.click()

        sleep(1)

        try:
             self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//[@class='x-grid-view x-fit-item x-grid-view-default']//div[contains(text(),'{}')]".format(lg[2])).is_displayed()
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
                self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("冲销单据元素存在")
            elif a == False:
                print("冲销单据元素不存在")

            print(a)

            while (a == True):

                self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//img[@class = 'x-grid-checkcolumn']").click()

                try:
                    self.driver.find_element_by_xpath(
                        "//*[@id='FlowPurchasePlanFormPanelID']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                    a = True
                except:
                    a = False
                if a == True:
                    print("冲销单据元素存在")
                elif a == False:
                    print("冲销单据元素不存在")

                print(a)

        else:
            pass

        sleep(2)

        if we[0] == '':

            # 定位添加SKU按钮'''
            _elementThird = self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementThird).perform()

            sleep(2)

            _NoData = self.driver.find_element_by_xpath("//div[@id='OtherProductDialogWinGridPanelID-body']/div").text

            if _NoData == lg[2]:

            #try:
                 #self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                 a = True
            else:
                 a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

            print(a)

            sleep(2)

            while (a == True) :

                # 关闭窗口
                self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//img[contains(@class,'x-tool-close')]").click()

                sleep(2)

                # 在此元素上双击
                #ActionChains(self.driver).double_click(_elementFirst).perform()

                #sleep(2)

                # 定位到供应商名称输入框
                self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.vendorName']").click()

                sleep(2)

                if ad[0] != '':

                    # 定位到供应商选择器关键字输入框
                    self.driver.find_element_by_xpath(
                        "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                    sleep(2)

                    # 定位到查询
                    self.driver.find_element_by_xpath(
                        "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                    sleep(2)

                    # 定位查询结果第一个元素
                    _element = self.driver.find_element_by_xpath(
                        "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                    sleep(2)

                    # 在此元素上双击
                    ActionChains(self.driver).double_click(_element).perform()

                else:

                    _elementFiveth = (random.randint(1, 10))

                    sleep(2)

                    # 定位查询结果第一个元素
                    _element = self.driver.find_element_by_xpath(
                        "//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                    sleep(2)

                    # 在此元素上双击
                    ActionChains(self.driver).double_click(_element).perform()

                sleep(2)

                # 定位添加SKU按钮'''
                _elementThird = self.driver.find_element_by_xpath(
                    "//*[@id='FlowPurchasePlanFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementThird).perform()

                sleep(2)

                _NoData = self.driver.find_element_by_xpath(
                    "//div[@id='OtherProductDialogWinGridPanelID-body']/div").text

                if _NoData == lg[2]:

                    # try:
                    # self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                    a = True
                else:
                    a = False
                if a == True:
                    print("元素存在")
                elif a == False:
                    print("元素不存在")

                print(a)

                sleep(2)



            if sku[0] != '':

                    # 定位到sku
                    self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID-body']//input[@name='keywords']").send_keys(sku[0])

                    sleep(2)

                    # 定位到sku
                    self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID-body']//span[contains(@class,'fa-search')]").click()

                    sleep(2)

                    # 定位第一个SKU
                    _elementSecond = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                    sleep(2)

                    # 在此元素上双击
                    ActionChains(self.driver).double_click(_elementSecond).perform()

            else:

                ul = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']/div/table/tbody")

                lis = ul.find_elements_by_xpath('tr')

                print(len(lis))

                sleep(2)

                _elementFiveth = (random.randint(1, len(lis)))

                # 定位第一个SKU
                _elementSecond = self.driver.find_element_by_xpath(
                    "//*[@id='OtherProductDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementSecond).perform()

            sleep(2)

            # 定位到确认按钮
            self.driver.find_element_by_xpath(
                "//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click()

            sleep(2)

        else:
            pass

        # 定位生成周期输入框
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID-body']//input[@name='main.leadTime']").send_keys(rt[0])

        sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-save')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')

        for i in range(0,len(lis)):

            if  su[0][0]  in lis[i].text:

                print(i+1)

                column=i+1

                break

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(3)

        # 定位到相关报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[3])).click()

        sleep(2)

        # 定位到产品分析报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()='{}']".format(lg[4])).click()

        sleep(2)

        # 定位到产品分析报告新建
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到申请单类型
        self.driver.find_elements_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.businessType']")[1].click()

        sleep(2)

        # 采购计划申请
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains (text(),'采购计划申请')]").click()

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[1]

        first_category.click()

        sleep(2)

        # 定位到应用ID
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main_businessId']").click()

        sleep(2)

        # 定位第采购计划申请器第一条记录
        _elementFourth = self.driver.find_element_by_xpath(
            "//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)

        # 定位到报告文件输入框
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='reportFileDocumentName']").click()

        sleep(2)

        # 定位文件选择器第一条记录
        _elementFiveth = self.driver.find_element_by_xpath(
            "//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFiveth).perform()

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到报告标题
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.title']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到报告编号
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.serialNumber']").send_keys(_elementFiveth)

        # 报告时间
        # self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.reportTime']").send_keys('2018-06-02')

        # sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(2)

        # 定位到申请单据
        _elementSixth = self.driver.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSixth).perform()

        sleep(2)

        # 定位到采购计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

        sleep(2)

        # 选择采购计划第一条记录
        self.driver.find_element_by_xpath(
            "//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购计划编辑
        self.driver.find_element_by_xpath(
            "//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(2)

        _handler = self.driver.find_element_by_xpath(
            "//*[@id='FlowPurchasePlanGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                column)).get_attribute('textContent')

        print(_handler)

        for i in range(1, len(su)):

            if su[i][0] == _handler:
                _value = su[i][0]

                break

        self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

        sleep(2)

        self.driver.find_element_by_link_text(lg[8]).click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        # 强制等待
        sleep(5)

        '''审批'''
        if _value == su[1][0]:

            self.login(su[1][0], su[1][1])

            # self.login('Vic_cn', '123')

            # 强制等待
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
                print("元素存在")
            elif a == False:
                print("元素不存在")

            print(a)

            if a == True:

               # 关闭弹出框
               self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            else:
                pass

            # 强制等待
            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(1)

            # 定位到采购计划
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

            sleep(1)
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchasePlanGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[1][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            # 强制等待
            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            # 强制等待
            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            # 强制等待
            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 强制等待
            sleep(2)

            # 定位到通过按钮
            self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-check-square')]").click()

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
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购计划
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

            sleep(1)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchasePlanGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(2, len(su)):

                if su[i][0] == _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text(lg[7]).click()  # 点击注销

            sleep(2)

            self.driver.find_element_by_link_text(lg[8]).click()

            alert = self.driver.switch_to_alert()

            # 退出页面
            alert.accept()

            # 强制等待
            sleep(5)

        '''审批'''
        if _value == su[2][0]:

            self.login(su[2][0], su[2][1])

            # self.login('Vic_cn', '123')

            # 强制等待
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
                print("元素存在")
            elif a == False:
                print("元素不存在")

            print(a)

            if a == True:

               # 关闭弹出框
               self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            else:
                pass

            # 强制等待
            sleep(2)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            # 强制等待
            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            # 强制等待
            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            # 强制等待
            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 强制等待
            sleep(2)

            # 定位到通过按钮
            self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-check-square')]").click()

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



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
