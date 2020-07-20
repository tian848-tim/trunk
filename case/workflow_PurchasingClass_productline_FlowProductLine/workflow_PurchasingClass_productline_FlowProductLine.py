'''
测试用例标题：开设产品线测试
测试场景：开设产品线业务流程测试
创建者：Tim
创建日期：2018-10-26
最后修改日期：2018-10-26
输入数据：审批流程各个角色账号
输出数据：无

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


class ProductLine(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_productline_FlowProductLine.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_productline_FlowProductLine.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    # 判断当前语言
    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_PurchasingClass_productline_FlowProductLine.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_productline_FlowProductLine.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '开设产品线'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_productline_FlowProductLine'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_ProductLine(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        cn = self.CN()
        en = self.EN()


        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Richard_cn', '123')
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

        # 定位到开设产品线申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

        sleep(2)

        #定位新建
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineView']//span[contains(@class, 'fa-plus')]").click()

        sleep(2)

        #定位供应商名称
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineViewFormPanelID-body']//input[contains(@name, 'main.vendorName')]").click()

        sleep(2)

        if ad[0] !='':

            self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID-body']//input[@name='keywords']").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID-body']//span[contains(@class,'fa-search')]").click()

            # 定位第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='1']")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:
            #随机选择
            _elementFiveth = (random.randint(1, 10))

            #定位第一条记录
            _elementFirst =self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加产品按钮
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowProductLineViewFormPanelID']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        _elementFiveth = (random.randint(0, len(lis))-1)

        # 定位订单号记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//tr[@data-recordindex={}]".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        #定位确认
        self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//span[contains(@class, 'fa-check')]").click()

        sleep(2)

        #定位保存
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineForm']//span[contains(@class, 'fa-save')]").click()

        self.driver.implicitly_wait(60)

        self.driver.find_element_by_xpath("//*[@id='FlowProductLineView-body']//span[contains(@class, 'fa-search')]").click()

        sleep(2)

        # 定位关键字位置
        ul = self.driver.find_element_by_xpath("//*[@id='FlowProductLineViewGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')



        for i in range(0, len(lis)):

            if su[0][0] in lis[i].text:
                print(i + 1)

                column = i + 1

                break

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='FlowProductLineViewGridPanelID-body']//div[text()='1']").click()

        sleep(1)

        #定位编辑
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        sleep(2)

        #定位发启
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineForm']//span[contains(@class, 'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 判断流程
        _prompt = lg[2]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(2)

        _handler = self.driver.find_element_by_xpath(
            "//*[@id='FlowProductLineViewGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                column)).get_attribute('textContent')

        print(_handler)

        for i in range(1, len(su)):

            if su[i][0] == _handler:
                _value = su[i][0]

                break
        sleep(1)

        # 点击注销
        self.driver.find_element_by_link_text(lg[4]).click()

        self.driver.find_element_by_link_text(lg[5]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)

        if _value == su[1][0]:

            self.login(su[1][0], su[1][1])
            #self.login('Jack.L', '123')

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

            # 定位到开设产品线申请
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowProductLineViewGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[1][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到开设产品线申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            sleep(2)

            #定位第一条
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()


            #定位马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            #定位通过
            self.driver.find_element_by_xpath("//*[@id='FlowProductLineForm']//span[contains(@class, 'fa-check-square')]").click()

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

            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到开设产品线申请
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

            sleep(1)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowProductLineViewGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(2, len(su)):

                if su[i][0] == _handler:
                    _value = su[i][0]

                    break


            # 点击注销
            self.driver.find_element_by_link_text(lg[4]).click()

            self.driver.find_element_by_link_text(lg[5]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面


            sleep(3)

        if _value == su[2][0]:

            self.login(su[2][0], su[2][1])
            #self.login('Jack.L', '123')

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
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到开设产品线申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

            sleep(2)

            #定位第一条
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()


            #定位马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            #定位通过
            self.driver.find_element_by_xpath("//*[@id='FlowProductLineForm']//span[contains(@class, 'fa-check-square')]").click()

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

            # 点击注销
            self.driver.find_element_by_link_text(lg[4]).click()

            self.driver.find_element_by_link_text(lg[5]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()

