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

class purchaseContract(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results


    def container(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['container']]

        return results

    def originPort(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['originPort']]

        return results

    def balancePayment(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['balancePayment']]

        return results

    def itemId(self):

        global value
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['itemId']]

        return value

    def price(self):

        global value
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['price']]

        return value

    def settlement(self):

        global value
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['settlement']]

        return value

    def writeoffMethod(self):

        global value
        file = open(rootPath + '/data/workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['writeoffMethod']]

        return value


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购合同定金'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_purchasecontractdeposit_FlowPurchaseContractDeposit'
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
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_FlowPurchaseContractDeposit(self):
        su = self.loadvendername()
        ad = self.loadvendernames()
        we = self.container()
        er = self.originPort()
        rt = self.balancePayment()
        ty = self.itemId()
        yu = self.price()
        ui = self.settlement()
        qw = self.writeoffMethod()

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

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        sleep(2)

        # 定位到采购合同新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-plus')]").click()

        self.driver.implicitly_wait(60)

        # 定位到采购计划列表新建
        self.driver.find_element_by_xpath("//*[@class='x-btn-button']//span[contains(text(), '采购计划列表')]").click()

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="PurchasePlanDialogWinID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        if ad[0] != '':

              self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID-body']//input[@name='keywords']").send_keys(ad[0])

              sleep(5)

              self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID-body']//span[contains(@class,'fa-search')]").click()

              sleep(5)

              _elementFirst = self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinGridPanelID-body']//div[contains(text(), '1')]")

              sleep(2)

              # 在此元素上双击
              ActionChains(self.driver).double_click(_elementFirst).perform()

        else:


              _elementFiveth = (random.randint(0, 10))

        # 定位采购计划第一条记录
              _elementFirst = self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

              sleep(2)

        # 在此元素上双击
              ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(5)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(5)

        try:
             #EC.visibility_of_element_located("//*[@class='x-form-layout-table']//input[@name='main.relateCompanyName']")
             self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//table[@class='x-field col-2 x-table-plain x-form-item x-form-type-text x-field-default x-autocontainer-form-item' and  @style='width: 150px; display: none;']").is_displayed()

             #self.driver.find_element_by_css_selector("table[class$='x-autocontainer-form-item'][style='width: 150px; display: none;']").is_displayed()

             a = True
        except:
             a = False
        if a == True:
            print("关联公司元素不存在")
        elif a == False:
            print("关联公司元素存在")


        sleep(2)

        if (a == False) :


             self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.relateCompanyName']").click()

             sleep(2)

             self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()  # 123

        else:
            pass

        sleep(2)

        if (a == False) :

            # 定位供应商产品分类
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()  # 456

        else:

            # 定位供应商产品分类
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

            sleep(3)

            # 选择分类
            #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

            #first_categorie = self.driver.find_elements_by_css_selector('div.x-boundlist-list-ct')[0]

            #first_categories = first_categorie.find_elements_by_css_selector('ul.x-list-plain')

            ul = self.driver.find_element_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]/ul")
            lis = ul.find_elements_by_xpath('li')

            first_category = lis[random.randint(0, len(lis)-1)]

            print(len(lis))

            sleep(2)

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()

        # 实例化一个Select类的对象
        #selector = Select(self.driver.find_element_by_css_selector('ul.x-list-plain'))

        # 下面三种方法用于选择"篮球运动员"
        #selector.select_by_index("2")  # 通过index进行选择,index从0开始

        sleep(2)

        if (a == False) :

              # 定位联系人名称
              _T=self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

              print(_T)

              sleep(2)

              if  _T.strip() =='' :


                  sleep(2)

              # 定位联系人
                  self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").click()

                  sleep(2)

                  try:
                      self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li").is_displayed()
                      b = True
                  except:
                      b = False

                  if b == True:
                      print("联系人元素存在")
                  elif b == False:
                      print("联系人元素不存在")


                  if b == True:
                     # 定位联系人
                     #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()

                     # 定位联系人
                     self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li[1]").click()

                  sleep(2)

        else:

            # 定位联系人名称
            _T = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

            print(_T)

            while _T.strip() == '':

                # 定位联系人
                self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").click()

                sleep(2)

                try:
                    self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li").is_displayed()
                    b = True
                except:
                    b = False

                if b == True:
                    print("联系人元素存在")
                elif b == False:
                    print("联系人元素不存在")

                if b == True:
                    # 定位联系人
                    #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()

                    # 定位联系人
                    self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li[1]").click()

                    # 定位联系人名称
                    _T = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

                    print(_T)

                else:

                    # 定位供应商产品分类
                    self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

                    sleep(3)

                    # 选择分类
                    # self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

                    # first_categorie = self.driver.find_elements_by_css_selector('div.x-boundlist-list-ct')[0]

                    # first_categories = first_categorie.find_elements_by_css_selector('ul.x-list-plain')

                    ul = self.driver.find_element_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]/ul")
                    lis = ul.find_elements_by_xpath('li')

                    first_category = lis[random.randint(0, len(lis) - 1)]

                    print(len(lis))

                    sleep(2)

                    first_category_name = first_category.text
                    print("随机选择的是:{0}".format(first_category_name))
                    first_category.click()

                    # 定位联系人名称
                    _T = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

                    print(_T)


        sleep(2)

        _Y = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.depositType']").get_attribute("value")

        print(_Y)

        if _Y != '百分比':

             # 订金类型
             self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.depositType']").click()

             sleep(1)

             # 订金类型
             self.driver.find_element_by_xpath( "//*[@class='x-list-plain']//li[contains(text(),'百分比')]").click()

             sleep(2)

             # 订金率
             self.driver.find_element_by_xpath( "//*[@class='x-form-layout-table']//input[@name='main.depositRate']").clear()

             sleep(2)

             _N =random.random()

             # 订金率
             self.driver.find_element_by_xpath( "//*[@class='x-form-layout-table']//input[@name='main.depositRate']").send_keys(_N)

        else:
            pass

        # 完货日期
        self.driver.find_element_by_xpath( "//*[@class='x-form-layout-table']//input[@name='main.readyDate']").click()

        sleep(2)

        # 订单日期
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.orderDate']").click()

        sleep(2)

        b = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.etd']").get_attribute('value')

        if b == '':

        # 预计发货时间
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.etd']").click()

        else:
            pass

        sleep(2)

        # 预计发货时间
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.eta']").click()

        sleep(2)

        # 货柜类型
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.containerType']").click()

        sleep(2)

        # 开船前#20GP
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(we[0])).click()

        sleep(2)

        # 出货港口
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.originPortId']").click()

        sleep(2)

        # 宁波
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(er[0])).click()

        sleep(2)

        # 尾款条
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.balancePaymentTerm']").click()

        sleep(2)

        # 开船前
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(rt[0])).click()

        sleep(2)

        if ty[0] != '':

            # 定位添加SKU按钮'''
            _elementThird = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']/tbody[29]//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementThird).perform()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//div[contains(text(), '熏蒸费')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='itemId']").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(ty[0])).click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@style='width: 1140px;']/tbody/tr/td[5]/div").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-item-body x-form-trigger-wrap-focus']//input[@name='priceAud']").send_keys(yu[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//div[contains(text(), '合同订金内')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='settlementType']").click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(ui[0])).click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.eta']").click()

        try:
             self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
             c = True
        except:
             c = False
        if c == True:
            print("可冲销单据元素不存在")
        elif c == False:
            print("可冲销单据元素存在")

        #print(c)

        if (c == False):

            try:
                self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                d = True
            except:
                d = False
            if d == True:
                print("元素存在")
            elif d == False:
                print("元素不存在")

            #print(d)

            while (d == True):

                self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//img[@class = 'x-grid-checkcolumn']").click()

                sleep(2)

                if qw[0] != '':

                    self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//div[contains(text(), '合同尾款内')]").click()

                    sleep(2)

                    self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//input[@name='writeoffMethod']").click()

                    sleep(2)

                    self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(qw[0])).click()

                    sleep(2)

                    # 完货日期
                    self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.readyDate']").click()

                    sleep(2)

                else:
                    pass

                try:
                    self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//img[@class = 'x-grid-checkcolumn']").is_displayed()
                    d = True
                except:
                    d = False
                if d == True:
                    print("元素存在")
                elif d == False:
                    print("元素不存在")

                print(d)

                if (d == True):

                    if (qw[1] != ''):

                        qw[0] = qw[1]

            else:
                pass

        else:
            pass

        e = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.currency']").get_attribute('value')

        _F = e.capitalize()

        print(_F)

        sleep(2)

        totalValue = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalValue{}']".format(_F)).get_attribute('value')

        print(totalValue)

        sleep(2)

        writeOff = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.writeOff{}']".format(_F)).get_attribute('value')

        print(writeOff)

        sleep(2)

        totalOther = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalOther{}']".format(_F)).get_attribute('value')

        print(totalOther)

        sleep(2)

        print(float(totalValue) - float(writeOff) + float(totalOther))

        totalAmount = float(totalValue) - float(writeOff) + float(totalOther)

        sleep(2)

        deposit = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.deposit{}']".format(_F)).get_attribute('value')

        print(deposit)

        sleep(2)

        balance = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.balance{}']".format(_F)).get_attribute('value')

        print(balance)

        sleep(2)

        totalOtherDeposit = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalOtherDeposit{}']".format(_F)).get_attribute('value')

        print(totalOtherDeposit)

        sleep(2)

        print(float(deposit) + float(balance) + float(totalOtherDeposit))

        contractAmount = float(deposit) + float(balance) + float(totalOtherDeposit)

        sleep(2)

        amount = totalAmount - contractAmount

        print('%.1f' % amount)

        if amount == 0.0:

            print("合同金额正确")

        else:

            print("合同金额有误，错误金额：",amount)

        sleep(2)

        if deposit == 0 :

            print("合同订金为0，请重新操作脚本")

            self.driver.quit()

        # 点击发启
        self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        #self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(8)
        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        try:
            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]//span[contains(text(), '{}')]".format('调整申请')).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("调整申请元素存在")
        elif a == False:
            print("调整申请元素不存在")

        print(a)

        sleep(5)

        if a == True:

            # 选择新品开发第一条记录
            self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()

            # 强制等待
            sleep(2)

            # 定位到新品开发编辑
            self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-pencil-square-o')]").click()

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@class='x-form-layout-table']//input[@name='flowNextHandlerAccount']").click()

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@class='x-list-plain']//li[contains(text(),'{}')]".format(su[1][0])).click()

            sleep(2)

            # 定位到发启按钮
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class,'fa-check-square')]").click()

            # 获取弹窗提示：
            self.driver.implicitly_wait(60)
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



        self.login(su[1][0], su[1][1])
        #self.login('Vic_cn', '123')

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

        self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)


        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        # 获取当前节点处理人
        try:
             self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID']//div[@text()={}]".format(su[2][0])).is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("经理元素存在")
        elif a == False:
            print("经理元素不存在")

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)

        print(a)


        if  a == True :

            self.login(su[2][0], su[2][1])
            #self.login('Jack.L', '123')

            try:
                self.driver.find_element_by_xpath(
                    "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)


            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            # 获取当前节点处理人
            try:
                 self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID']//div[@text()={}]".format(su[3][0])).is_displayed()
                 a = True
            except:
                 a = False
            if a == True:
                print("总监元素存在")
            elif a == False:
                print("总监元素不存在")

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

        else:
            pass


        sleep(3)

        print(a)


        if  a == True :

            self.login(su[3][0], su[3][1])
            #self.login('Jack.L', '123')

            try:
                self.driver.find_element_by_xpath(
                    "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)

        else:
            pass



        #会计审核

        self.login(su[4][0],su[4][1])
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

        # 分配处理人
        #self.driver.find_element_by_xpath("//*[@class='x-form-trigger-input-cell']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择dickson
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'dickson')]").click()

        #sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        if self.is_alert_present():

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出

        else:
            pass

        sleep(2)

        # dickson审批
        self.login(su[5][0], su[5][1])
        #self.login('dickson', '123')

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
        self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(2)

        '''合同订金审批'''

        self.login(su[4][0], su[4][1])
        #self.login('emma','123')

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

        # 定位到币种
        _R = self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.currency']").get_attribute('value')

        _U = _R.capitalize()

        print(_U)

        # 定位到应付款
        payable = self.driver.find_element_by_xpath("//*[@id='FlowDepositContractForm']//input[@name = 'main.payable{}']".format(_U)).get_attribute('value')

        _P = float(deposit) + float(totalOtherDeposit) - float(payable)

        if  _P == 0.0:

            print("合同支付订金正确")

        else:

            print("合同支付订金错误：",_P)

            self.driver.quit()

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


        self.login(su[4][0], su[4][1])
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
