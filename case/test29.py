'''
测试用例标题：采购合同测试
测试场景：采购合同业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-18
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

    #用户名
    def account(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    #供应商
    def vendorname(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['vendorname']]

        return results

    #货柜类型
    def container(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['container']]

        return results

    #出货港口
    def originPort(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['originPort']]

        return results

    #尾款条款
    def balancePayment(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['key']) for d in data['balancePayment']]

        return results

    #其他费用
    def itemId(self):

        global value
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['itemId']]

        return value

    #数量
    def price(self):

        global value
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['price']]

        return value

    #结算类型
    def settlement(self):

        global value
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['settlement']]

        return value

    #冲销方法
    def writeoffMethod(self):

        global value
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        value = [(d['key']) for d in data['writeoffMethod']]

        return value

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购合同'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_purchasecontract_flowPurchaseContract'
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


    def test_PurchaseContract(self):

        su = self.account()
        ad = self.vendorname()
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

        #判断系统提示
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

        sleep(2)

        # 定位到采购计划列表新建
        self.driver.find_element_by_xpath("//*[@class='x-panel gb-blank x-tabpanel-child x-panel-default x-closable x-panel-closable x-panel-default-closable']//span[contains(text(), '采购计划列表')]").click()

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="PurchasePlanDialogWinID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        #判读供应商

        if ad[0] != '':

              self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID-body']//input[@name='keywords']").send_keys(ad[0])

              sleep(2)

              self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID-body']//span[contains(@class,'fa-search')]").click()

              try:

                  WebDriverWait(self.driver, 120).until(
                      EC.invisibility_of_element_located(
                          (By.XPATH, '//*[@style="right: auto; left: 839px; top: 539px; z-index: 19003; display: none;"]'))
                  )

              except IOError as a:
                  print("找不元素 " + a)

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

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(5)

        #判断关联供应商
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

            i = 0

            # 选择分类
            #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

            #first_categorie = self.driver.find_elements_by_css_selector('div.x-boundlist-list-ct')[0]

            #first_categories = first_categorie.find_elements_by_css_selector('ul.x-list-plain')

            ul = self.driver.find_element_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]/ul")
            lis = ul.find_elements_by_xpath('li')

            first_category = lis[i]

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()

        sleep(2)

        if (a == False) :

              # 定位联系人名称
              _T=self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

              print(_T)

              sleep(2)

              if  _T.strip() =='' :

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

                    i += 1

                    if i > len(lis)-1:

                        print("产品线不存在联系人")
                        self.driver.quit()

                    # 定位供应商产品分类
                    self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

                    sleep(3)

                    # 选择分类
                    # self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

                    # first_categorie = self.driver.find_elements_by_css_selector('div.x-boundlist-list-ct')[0]

                    # first_categories = first_categorie.find_elements_by_css_selector('ul.x-list-plain')

                    ul = self.driver.find_element_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]/ul")
                    lis = ul.find_elements_by_xpath('li')

                    first_category = lis[i]

                    first_category_name = first_category.text
                    print("随机选择的是:{0}".format(first_category_name))
                    first_category.click()

                    # 定位联系人名称
                    _T = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

                    print(_T)


        sleep(3)

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

        # 货柜类型
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(we[0])).click()

        sleep(2)

        originPortId = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.originPortId']").get_attribute('value')

        if originPortId == '':

            # 出货港口
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.originPortId']").click()

            sleep(2)

            # 宁波
            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(er[0])).click()

        # 尾款条
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.balancePaymentTerm']").click()

        sleep(2)

        # 开船前
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(rt[0])).click()

        sleep(2)

        #判断其他费用
        if ty[0] != '':

            # 定位添加按钮'''
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

        #判断冲销单据
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

        # 点击保存
        self.driver.find_elements_by_xpath("//*[@id='centerTabPanel-body']//span[contains(@class,'fa-save ')]")[1].click()

        self.driver.implicitly_wait(60)

        # 点击刷新
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractSearchFormPanelID']//span[contains(@class,'fa-search')]").click()

        sleep(1)

        # 定位关键字位置
        ul = self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')

        for i in range(0, len(lis)):

            if su[0][0] in lis[i].text:
                print(i + 1)

                column = i + 1

                break

        # 定位第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购合同编辑
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-pencil-square-o')]").click()

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="centerTabPanel-body"]//input[@name = "main.balanceUsd"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        sleep(1)

        #结算币种
        e = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.currency']").get_attribute('value')

        _F = e.capitalize()

        print(_F)

        #总货值
        totalValue = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalValue{}']".format(_F)).get_attribute('value')

        print(totalValue)

        #冲销金额
        writeOff = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.writeOff{}']".format(_F)).get_attribute('value')

        print(writeOff)

        #其他总费用
        totalOther = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalOther{}']".format(_F)).get_attribute('value')

        print(totalOther)

        print(float(totalValue) - float(writeOff) + float(totalOther))

        totalAmount = float(totalValue) - float(writeOff) + float(totalOther)

        #货值订金
        deposit = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.deposit{}']".format(_F)).get_attribute('value')

        print(deposit)

        #货值尾款
        balance = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.balance{}']".format(_F)).get_attribute('value')

        print(balance)

        #其他订金
        totalOtherDeposit = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.totalOtherDeposit{}']".format(_F)).get_attribute('value')

        print(totalOtherDeposit)

        print(float(deposit) + float(balance) + float(totalOtherDeposit))

        contractAmount = float(deposit) + float(balance) + float(totalOtherDeposit)

        amount = round(totalAmount,2) - round(contractAmount,2)

        print(amount)

        if amount == 0.00 :

            print("合同金额正确")

        else:

            print("合同金额有误，错误金额：",amount)

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        #self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = '操作提示流程已启动'

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(1)

        # 点击刷新
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractSearchFormPanelID']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        _handler = self.driver.find_element_by_xpath(
            "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                column)).get_attribute('textContent')

        print(_handler)

        for i in range(1, len(su)):

            if su[i][0] in _handler:
                _value = su[i][0]

                break

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        if _value == su[1][0]:

            self.login(su[1][0], su[1][1])
            #self.login('Vic_cn', '123')
            sleep(2)

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
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            self.driver.implicitly_wait(60)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[1][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(1)

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

            sleep(5)

            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = '操作提示操作成功！'

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(2, len(su)):

                if su[i][0] in _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面


            sleep(3)


        if  _value == su[2][0] :

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

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            self.driver.implicitly_wait(60)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]")

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
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = '操作提示操作成功！'

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(1)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            # 获取当前节点处理人
            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(3, len(su)):

                if su[i][0] in _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(3)


        if  _value == su[3][0] :

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

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            self.driver.implicitly_wait(60)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[3][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(1)

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
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = '操作提示操作成功！'

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()


            sleep(1)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            # 获取当前节点处理人
            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(4, len(su)):

                if su[i][0] in _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)

        if _value == su[4][0]:
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

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            self.driver.implicitly_wait(60)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[4][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(1)

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
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = '操作提示操作成功！'

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(1)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

            # 获取当前节点处理人
            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(5, len(su)):

                if su[i][0] in _handler:
                    _value = su[i][0]

                    break

            # 点击注销
            self.driver.find_element_by_link_text('注销').click()

            self.driver.find_element_by_link_text('是').click()

            if self.is_alert_present():

                alert = self.driver.switch_to_alert()

                alert.accept()  # 退出

            else:
                pass

            sleep(2)

        if _value == su[5][0]:

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
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = '操作提示操作成功！'

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

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
