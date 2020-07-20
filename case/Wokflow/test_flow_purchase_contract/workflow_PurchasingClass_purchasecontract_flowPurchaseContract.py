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

        global account
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        account = [(d['username'], d['password']) for d in data['login']]

        return account

    #供应商
    def vendorname(self):

        global vendorname
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        vendorname = [(d['name']) for d in data['vendorname']]

        return vendorname

    #出货港口
    def originPort(self):

        global originPort
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        originPort = [(d['key']) for d in data['originPort']]

        return originPort

    #其他费用
    def itemId(self):

        global itemId
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        itemId = [(d['key']) for d in data['itemId']]

        return itemId

    #数量
    def price(self):

        global price
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        price = [(d['key']) for d in data['price']]

        return price


    #冲销方法
    def writeoffMethod(self):

        global writeoffMethod
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json', encoding='utf-8')
        data = json.load(file)
        writeoffMethod = [(d['key']) for d in data['writeoffMethod']]

        return writeoffMethod

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_purchasecontract_flowPurchaseContract.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en

    # 判断当前语言
    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

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
        er = self.originPort()
        ty = self.itemId()
        yu = self.price()
        qw = self.writeoffMethod()
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
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

        sleep(2)

        # 定位到采购合同新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到采购计划列表新建
        self.driver.find_element_by_xpath("//*[contains(@id , 'FlowPurchaseContractFormext')]//span[contains(@class, 'x-btn-icon-el  ')]").click()

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

              ad = self.driver.find_element_by_xpath(
                  "//*[@id='PurchasePlanDialogWinGridPanelID-body']/div/table/tbody/tr[{}]/td[3]".format(_elementFiveth)).text

            # 定位采购计划第一条记录
              _elementFirst = self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

              sleep(2)

            # 在此元素上双击
              ActionChains(self.driver).double_click(_elementFirst).perform()

        if ad[0] != '':
            ad = ad[0]

        else:
            ad = ad

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        #元素等待
        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[contains(@id,"FlowPurchaseContractFormext")]//div[contains(text(), "{}")]'.format(ad)))
            )

        except IOError as a:
            print("找不元素 " + a)

        #判断关联供应商
        try:
             #EC.visibility_of_element_located("//*[@class='x-form-layout-table']//input[@name='main.relateCompanyName']")
             #self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//table[@class='x-field col-2 x-table-plain x-form-item x-form-type-text x-field-default x-autocontainer-form-item' and  @style='width: 150px; display: none;']").is_displayed()

             #self.driver.find_element_by_css_selector("table[class$='x-autocontainer-form-item'][style='width: 150px; display: none;']").is_displayed()

             WebDriverWait(self.driver, 20).until(
                 EC.invisibility_of_element_located(
                     (By.XPATH, '//*[@name="main.relateCompanyName"]'))
             )
             a = True
        except:
             a = False
        if a == True:
            print("关联公司元素不存在")
        elif a == False:
            print("关联公司元素存在")


        if (a == False) :
             sleep(1)

             self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.relateCompanyName']").click()

             sleep(1)

             self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()  # 123

        else:
            pass


        if (a == False) :

            sleep(1)

            # 定位供应商产品分类
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

            sleep(1)

            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()  # 456

        else:

            sleep(1)

            # 定位供应商产品分类
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

            sleep(1)

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


        if (a == False) :

              # 定位联系人名称
              _T=self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

              print(_T)

              # 定位联系人
              self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").click()

              if  _T.strip() =='' :

                  try:
                      #self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li").is_displayed()

                      ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct x-unselectable')]")[1]
                      ul = ul.find_element_by_xpath('ul')
                      ul.find_element_by_xpath('li').is_displayed()

                      b = True
                  except:
                      b = False

                  if b == True:
                      print("联系人元素存在")
                  elif b == False:
                      print("联系人元素不存在")



        else:

            # 定位联系人名称
            _T = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute("value")

            print(_T)

            # 定位联系人
            self.driver.find_element_by_xpath(
                "//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").click()

            while _T.strip() == '':

                try:
                    #self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li").is_displayed()

                    ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct x-unselectable')]")[1]
                    ul = ul.find_element_by_xpath('ul')
                    ul.find_element_by_xpath('li').is_displayed()

                    b = True

                except:
                    b = False

                if b == True:
                    print("联系人元素存在")
                elif b == False:
                    print("联系人元素不存在")

                if b == True:
                    # 定位联系人
                    #self.driver.find_element_by_xpath("//*[@style='right: auto; left: 381px; top: 440px; height: auto; width: 680px; z-index: 19001;']/div/ul/li[1]").click()

                    ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct x-unselectable')]")[1]
                    ul = ul.find_element_by_xpath('ul')
                    ul.find_elements_by_xpath('li')[0].click()

                    # 定位联系人名称
                    _T = self.driver.find_element_by_xpath(
                        "//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").get_attribute(
                        "value")

                    print(_T)

                else:

                    i += 1

                    if i > len(lis)-1:

                        print("产品线不存在联系人")
                        self.driver.quit()

                    # 定位供应商产品分类
                    self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.vendorProductCategoryAlias']").click()

                    sleep(1)

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

                    # 定位联系人
                    self.driver.find_element_by_xpath(
                        "//*[@class='x-form-layout-table']//input[@name='main.sellerContactCnName']").click()


        sleep(1)

        # 完货日期
        self.driver.find_element_by_xpath( "//*[@class='x-form-layout-table']//input[@name='main.readyDate']").click()

        sleep(1)

        # 订单日期
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.orderDate']").click()

        sleep(1)

        b = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.etd']").get_attribute('value')

        if b == '':

        # 预计发货时间
            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.etd']").click()

        else:
            pass

        sleep(1)

        # 预计发货时间
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.eta']").click()

        sleep(1)

        # 货柜类型
        self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.containerType']").click()

        sleep(1)

        # 货柜类型
        ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct x-unselectable')]")[2]
        ul = ul.find_element_by_xpath('ul')
        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(0, len(lis) - 1)]

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()


        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(we[0])).click()

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
        ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]")[3]
        ul = ul.find_element_by_xpath('ul')
        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(0, len(lis) - 1)]

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(rt[0])).click()

        sleep(2)

        #判断其他费用
        if ty[0] != '':

            # 定位添加按钮'''
            _elementThird = self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']/tbody[29]//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementThird).perform()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//div[text()= '{}']".format(lg[8])).click()

            sleep(2)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='itemId']").click()

            sleep(2)

            ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]")[4]
            ul = ul.find_element_by_xpath('ul')
            lis = ul.find_elements_by_xpath('li')

            first_category = lis[random.randint(0, len(lis) - 1)]

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()

            #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(ty[0])).click()

            sleep(1)

            self.driver.find_element_by_xpath("//*[@style='width: 1140px;']/tbody/tr/td[5]/div").click()

            sleep(1)

            self.driver.find_element_by_xpath("//*[@class='x-form-item-body x-form-trigger-wrap-focus']//input[@name='priceAud']").send_keys(yu[0])

            sleep(1)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//div[text()= '{}']".format(lg[9])).click()

            sleep(1)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='settlementType']").click()

            sleep(1)

            ul = self.driver.find_elements_by_xpath("//*[contains(@class,'x-boundlist-list-ct')]")[5]
            ul = ul.find_element_by_xpath('ul')
            lis = ul.find_elements_by_xpath('li')

            first_category = lis[random.randint(0, len(lis) - 1)]

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()
            #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(ui[0])).click()

            sleep(1)

            self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.eta']").click()

        #判断冲销单据
        try:
             self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//div[contains(text(),'{}')]".format(lg[2])).is_displayed()

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


            #
            while (d == True):

                self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//img[@class = 'x-grid-checkcolumn']").click()

                sleep(1)

                if qw[0] != '':

                    self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//div[text()='{}']".format(lg[3])).click()

                    sleep(1)

                    self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//input[@name='writeoffMethod']").click()

                    sleep(1)

                    self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(qw[0])).click()

                    sleep(1)

                    # 完货日期
                    self.driver.find_element_by_xpath("//*[@class='x-form-layout-table']//input[@name='main.readyDate']").click()

                    sleep(1)

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

        sleep(2)

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

        if float(deposit) == 0.00 :

            deposit = True

        else:

            deposit = False

        print(deposit)

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

        _prompt = lg[4]

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

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        if _value == su[1][0]:

            self.login(su[1][0], su[1][1])
            #self.login('Vic_cn', '123')
            sleep(2)

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
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到采购合同
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

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
                                                      '//*[contains(@id,"FlowPurchaseContractForm")]//div[contains(text(), "{}")]'.format(
                                                          ad)))
                )

            except IOError as a:
                print("找不元素 " + a)

            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[5]

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(2, len(su)):

                if su[i][0] in _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[7]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面


            sleep(3)


        if  _value == su[2][0] :

            self.login(su[2][0], su[2][1])
            #self.login('Jack.L', '123')

            sleep(2)

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

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
                                                      '//*[contains(@id,"FlowPurchaseContractForm")]//div[contains(text(), "{}")]'.format(
                                                          ad)))
                )

            except IOError as a:
                print("找不元素 " + a)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[5]

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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

            self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[7]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(3)


        if  _value == su[3][0] :

            self.login(su[3][0], su[3][1])
            #self.login('Jack.L', '123')

            sleep(2)

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

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
                                                      '//*[contains(@id,"FlowPurchaseContractForm")]//div[contains(text(), "{}")]'.format(
                                                          ad)))
                )

            except IOError as a:
                print("找不元素 " + a)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[5]

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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

            self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[7]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)

        if _value == su[4][0]:
            #会计审核

            self.login(su[4][0],su[4][1])
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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

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
                                                      '//*[contains(@id,"FlowPurchaseContractForm")]//div[contains(text(), "{}")]'.format(
                                                          ad)))
                )

            except IOError as a:
                print("找不元素 " + a)

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

            _prompt = lg[5]

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
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
            self.driver.find_element_by_link_text(lg[6]).click()

            self.driver.find_element_by_link_text(lg[7]).click()

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

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            sleep(2)

            if deposit == False:

                _elementFirst = 2

                # 定位到待办事项第一条记录
                self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[text()= '{}']".format(_elementFirst)).click()

            else:

                _elementFirst = 1

                # 定位到待办事项第一条记录
                self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[text()= '{}']".format(_elementFirst)).click()

            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 元素等待
            try:
                WebDriverWait(self.driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      '//*[contains(@id,"FlowPurchaseContractForm")]//div[contains(text(), "{}")]'.format(
                                                          ad)))
                )

            except IOError as a:
                print("找不元素 " + a)

            # 点击通过
            self.driver.find_element_by_xpath("//*[@role='presentation']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[5]

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
