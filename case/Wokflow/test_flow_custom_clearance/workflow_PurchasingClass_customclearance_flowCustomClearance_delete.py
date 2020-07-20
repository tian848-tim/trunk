'''
测试用例标题：清关测试
测试场景：清关申请业务流程测试——删除
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


class CustomClearance(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_customclearance_flowCustomClearance_delete.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_PurchasingClass_customclearance_flowCustomClearance_delete.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '清关检查——删除'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_customclearance_flowCustomClearance_delete'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_CustomClearance(self):
        su = self.loadvendername()
        ad = self.loadvendernames()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0], su[0][1])
        # self.login('Vic_cn','123')
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
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '清关&发运申请')]").click()

        sleep(2)

        # 定位到清关申请新建
        self.driver.find_element_by_xpath(
            "//*[@id='FlowCustomClearanceView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择采购订单号
        self.driver.find_element_by_xpath(
            "//*[@id='FlowCustomClearanceViewFormPanelID-body']//input[@name='orderNumber']").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        sleep(2)

        _elementFiveth = (random.randint(1, len(lis)))

        _elementSecond = self.driver.find_element_by_xpath(
            "//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody/tr[{}]/td[18]/div".format(
                _elementFiveth)).get_attribute('textContent')

        print(_elementSecond)

        sleep(1)

        # 定位订单号第二条记录
        _elementFirst = self.driver.find_element_by_xpath(
            "//*[@id='OrderDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        _T = self.driver.find_element_by_xpath(
            "//*[@class='x-form-trigger-input-cell']//input[@name='main.containerQty']").get_attribute("value")

        sleep(2)

        while (_T != '1'):
            ## 选择采购订单号
            self.driver.find_element_by_xpath(
                "//*[@id='FlowCustomClearanceViewFormPanelID-body']//input[@name='orderNumber']").click()

            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            print(len(lis))

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            _elementSecond = self.driver.find_element_by_xpath(
                "//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody/tr[{}]/td[18]/div".format(
                    _elementFiveth)).get_attribute('textContent')

            print(_elementSecond)

            sleep(1)

            # 定位订单号第二条记录
            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='OrderDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            _T = self.driver.find_element_by_xpath(
                "//*[@class='x-form-trigger-input-cell']//input[@name='main.containerQty']").get_attribute("value")

            sleep(2)


        else:

            _elementFiveth = (random.randint(0, 1000))

            ## 定位到船名
            self.driver.find_element_by_xpath(
                "//*[@id='FlowCustomClearanceViewFormPanelID-body']//input[@name='main.vessel']").send_keys(
                _elementFiveth)

            sleep(2)

            _elementFiveth = (random.randint(0, 1000))

            ## 定位到航次
            self.driver.find_element_by_xpath(
                "//*[@id='FlowCustomClearanceViewFormPanelID-body']//input[@name='main.voy']").send_keys(_elementFiveth)

            sleep(2)

            _elementFiveth = (random.randint(0, 1000))

            ## 定位到集装箱编码
            self.driver.find_element_by_xpath(
                "//*[@id='packingListContainer-innerCt']//input[@name='containerNumber']").send_keys(_elementFiveth)

            sleep(2)

            _elementFiveth = (random.randint(0, 1000))

            ## 定位到封印编码
            self.driver.find_element_by_xpath(
                "//*[@id='packingListContainer-innerCt']//input[@name='sealsNumber']").send_keys(_elementFiveth)

            sleep(2)

            # 点击发启
            self.driver.find_element_by_xpath(
                "//*[@id='FlowCustomClearanceForm']//span[contains(@class,'fa-play')]").click()

            self.driver.implicitly_wait(30)
            # 获取弹窗提示：
            self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            sleep(5)

            # 点击注销
            self.driver.find_element_by_link_text('注销').click()

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

        sleep(5)

        '''审核'''

        self.login(su[0][0], su[0][1])

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
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到清关&发运申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '清关&发运申请')]").click()

        sleep(2)

        # 定位到第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowCustomClearanceViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击删除按钮
        self.driver.find_element_by_xpath("//*[@id='FlowCustomClearanceView']//span[contains(@class, 'fa-trash')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()