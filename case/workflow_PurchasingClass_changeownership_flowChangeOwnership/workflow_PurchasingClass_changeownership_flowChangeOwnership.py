'''
测试用例标题：归属权变更
测试场景：归属权变更业务流程测试
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


class ChangeOwnership(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_changeownership_flowChangeOwnership.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

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
        file = open(rootPath + '/data/workflow_PurchasingClass_changeownership_flowChangeOwnership.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_changeownership_flowChangeOwnership.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '归属权变更'
        # 脚本标识－ID
        self.script_id = 'test_flow_custom_clearance'
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

    def test_ChangeOwnership(self):

        su = self.loadvendername()
        cn = self.CN()
        en = self.EN()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0], su[0][1])
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

        # 定位到归属权变更申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

        sleep(2)

        #定位新建按钮
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipView']//span[contains(@class, 'fa-plus')]").click()

        sleep(2)

        #定位供应商名称
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.vendorName')]").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        #定位第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        print(_elementFiveth)

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        #self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID']//span[contains(@class, 'fa-check')]").click()



        sleep(2)

        #定位变更供应商变更
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@class, 'x-form-cb')]").click()

        sleep(2)

        #定位新归属人
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.newOwnerName')]").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        _elementFiveth = (random.randint(1, len(lis)))

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()


        sleep(2)

        #定位新sku操作人
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.newOperatorName')]").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        _elementFiveth = (random.randint(1, len(lis)))

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        #定位变更产品线归属
        self.driver.find_elements_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@class, 'x-form-cb')]")[1].click()

        sleep(2)

        #定位变更产品线归属
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[@name='main.productLine']").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(1, len(lis) - 1)]

        print(len(lis))

        print(first_category)

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        sleep(2)

        #定位发启
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipForm']//span[contains(@class, 'fa-play')]").click()

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

        # 点击注销
        self.driver.find_element_by_link_text(lg[4]).click()


        self.driver.find_element_by_link_text(lg[5]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''经理审核'''

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

        #定位通过
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipForm']//span[contains(@class, 'fa-check-square')]").click()

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





