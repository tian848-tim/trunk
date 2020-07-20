'''
测试用例标题：订单质检测试
测试场景：订单质检业务流程测试——删除
创建者：Tim
创建日期：2018-11-5
最后修改日期：2018-11-5
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

import time,unittest,configparser
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

class OrderQc(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC_delete.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC_delete.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '订单质检——删除'
        # 脚本标识－ID
        self.script_id = 'workflow_CheakClass_orderqc_flowOrderQC_delete'
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


    def test_Order_Qc(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
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
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '检验类')]").click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '订单质检申请')]").click()

        sleep(2)

        # 定位第一条记录
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionGridPanelID-body']//div[contains(text(), '1')]").click()

        #sleep(2)

        # 定位到订单质检申请新建
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class,'fa-pencil-square-o')]").click()

        # 定位到订单质检申请新建
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择供应商
        self.driver.find_element_by_xpath( "//*[@id='FlowOrderQualityInspectionFormPanelID']//input[@name='main.vendorName']").click()

        sleep(2)

        print(ad[0])

        if ad[0] != '' :

               ## 定位到关键字
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

               sleep(2)

               # 点击搜索
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

               sleep(2)

               # 定位供应商第一条记录
               _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

               sleep(2)

               # 在此元素上双击
               ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            _elementFiveth = (random.randint(1, 10))

            # 定位供应商第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        ## 选择订单列表
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionFormPanelID-body']//input[@name='main.orderNumber']").click()

        sleep(2)

        # 定位订单列表第一条'
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class,'fa-play')]").click()

        # 点击发启
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class,'fa-check-square')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(10)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点'''

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
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '检验类')]").click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '订单质检申请')]").click()

        sleep(2)

        # 定位到订单质检申请第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到删除按钮
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class, 'fa-trash')]").click()

        sleep(2)


        self.driver.find_element_by_link_text('是').click()


        # 点击注销
        self.driver.find_element_by_link_text('注销').click()


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()


