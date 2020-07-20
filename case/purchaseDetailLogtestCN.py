'''
测试用例标题：采购系统申请单据加载时间
测试场景：采购系统申请单据加载时间
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import json
import csv

import datetime
import paramiko


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
        file = open(rootPath + '/data/purchaseDetailLogtestCN.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购系统申请单据加载时间'
        # 脚本标识－ID
        self.script_id = 'purchaseDetailLogtestCN'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(12)
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Chrome(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_purchaseDetailLogtestCN(self):

        data = []
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 现在
        nowTime_second = datetime.datetime.now().strftime('%H:%M:%S')
        data.append(nowTime)
        data.append(nowTime_second)

        su = self.loadvendername()

        #for i in range(0, len(su)):
            #print(su[i][0])
            #print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Vic_cn','123')


        navigationStart = self.driver.execute_script("return window.performance.timing.fetchStart")
        loadEventEnd = self.driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime = (loadEventEnd - navigationStart)
        print("Login加载时间", str(durtime / 1000), ".s")
        data.append((round(durtime / 1000, 2)))

        sleep(5)

        try:
             self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
             a = True
        except:
             a = False

        if a == True:

           # 关闭弹出框
           self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        else:
            pass

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)
        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

        self.driver.implicitly_wait(120)

        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowProductQuotationForm"]//div[@id="FlowProductQuotationViewFormGridPanelID-body"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime1 = (End - Start)

        print("采购询价加载时间", str(durtime1 / 1000),".s")
        data.append((round(durtime1 / 1000, 2)))

        sleep(2)

        # 定位到新品开发申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()

        self.driver.implicitly_wait(120)

        # 定位到新品开发申请
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到新品开发申请
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowNewProductForm"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime2 = (End - Start)

        print("新品开发申请加载时间", str(durtime2/1000),".s")
        data.append((round(durtime2 / 1000, 2)))

        sleep(2)

        # 定位到样品申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '样品申请')]").click()

        self.driver.implicitly_wait(120)

        # 定位到样品申请
        self.driver.find_element_by_xpath("//*[@id='FlowSampleViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到样品申请
        self.driver.find_element_by_xpath("//*[@id='FlowSampleView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowSampleFormGridPanelID"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime3 = (End - Start)

        print("样品申请加载时间", str(durtime3/1000),".s")
        data.append((round(durtime3 / 1000, 2)))

        sleep(2)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()

        self.driver.implicitly_wait(120)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowPurchasePlanFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime4 = (End - Start)

        print("采购计划加载时间", str(durtime4/1000),".s")
        data.append((round(durtime4 / 1000, 2)))

        sleep(2)


        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        self.driver.implicitly_wait(120)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")


        #try:
        #    first_categories = self.driver.find_elements_by_xpath("//div[@class='x-panel-body x-grid-body x-panel-body-default x-box-layout-ct x-panel-body-default x-docked-noborder-right x-docked-noborder-bottom x-docked-noborder-left']")[4]
#
        #    first_categories.find_element_by_xpath("//div[contains(text(), '1')]").is_displayed()
        #    a = True
        #except:
        #    a = False

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="centerTabPanel-body"]//input[@name = "main.balanceUsd"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + "s")

        durtime5 = (End - Start)

        print("采购合同加载时间", str(durtime5/1000),".s")
        data.append((round(durtime5 / 1000, 2)))

        sleep(2)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '清关')]").click()

        self.driver.implicitly_wait(120)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='FlowCustomClearanceViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到清关申请
        self.driver.find_element_by_xpath("//*[@id='FlowCustomClearanceView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")


        #try:
        #    first_categories = self.driver.find_elements_by_xpath("//div[@class='x-panel grid-panel x-grid-with-col-lines x-grid-with-row-lines x-panel-default x-grid']")[2]
#
        #    first_categories.find_element_by_xpath("//div[contains(text(), '1')]").is_displayed()
#
        #except IOError as a:
        #    print("找不元素 " + a)



        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowCustomClearanceForm"]//input[@name = "containerNumber"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime6 = (End - Start)

        print("清关申请加载时间", str(durtime6/1000),".s")
        data.append((round(durtime6 / 1000, 2)))

        sleep(2)

        # 定位到归属权变更
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '归属权变更')]").click()

        self.driver.implicitly_wait(120)

        # 定位到归属权变更
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到归属权变更
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="ParentProductFormGrid-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime7 = (End - Start)

        print("归属权变更加载时间", str(durtime7/1000),".s")
        data.append((round(durtime7 / 1000, 2)))

        sleep(2)


        # 定位到开设产品线
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '开设产品线')]").click()

        self.driver.implicitly_wait(120)

        # 定位到开设产品线
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到开设产品线
        self.driver.find_element_by_xpath("//*[@id='FlowProductLineView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowProductLineViewGridPanelID-VendorMultiGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("开设产品线加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)


        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '检验类')]").click()

        sleep(2)

        # 定位到安检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '安检申请')]").click()

        self.driver.implicitly_wait(120)

        # 定位到安检申请
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到安检申请
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowComplianceArrangementFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("安检申请加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)


        # 定位到样品检验
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '样品检验')]").click()

        self.driver.implicitly_wait(120)

        # 定位到样品检验
        self.driver.find_element_by_xpath("//*[@id='FlowSampleQcGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到样品检验
        self.driver.find_element_by_xpath("//*[@id='FlowSampleQcView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowSampleQcFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("样品检验加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到订单质检
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '订单质检')]").click()

        self.driver.implicitly_wait(120)

        # 定位到订单质检
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到订单质检
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowOrderQualityInspectionForm"]//input[@name="main.orderNumber"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("订单质检加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到拓展安检
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '拓展安检')]").click()

        self.driver.implicitly_wait(120)

        # 定位到拓展安检
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementExtendGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到拓展安检
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementExtendView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowComplianceArrangementExtendFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("拓展安检加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到风控级别
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '风控级别')]").click()

        self.driver.implicitly_wait(120)

        # 定位到风控级别
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到风控级别
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowComplianceArrangementQuickForm"]//div[@id="FlowComplianceArrangementQuickFormGridPanelID-body"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("风控级别加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(2)

        # 定位到货代报价
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '货代报价')]").click()

        self.driver.implicitly_wait(120)

        # 定位到货代报价
        self.driver.find_element_by_xpath("//*[@id='FlowServiceInquiryViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到货代报价
        self.driver.find_element_by_xpath("//*[@id='FlowServiceInquiryView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowServiceInquiryViewFormPanelID-FlowServiceInquiryFreightMultiGrid-FlowServiceInquiryFreightMultiGridPanelID-locked-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("货代报价加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到订单港口变更
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '订单港口变更')]").click()

        self.driver.implicitly_wait(120)

        # 定位到订单港口变更
        self.driver.find_element_by_xpath("//*[@id='FlowOrderChangePortViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到订单港口变更
        self.driver.find_element_by_xpath("//*[@id='FlowOrderChangePortView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowOrderChangePortForm"]//input[@name="orderNumber"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("订单港口变更加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)


        # 定位到发货计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '发货计划')]").click()

        self.driver.implicitly_wait(120)

        # 定位到发货计划
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到发货计划
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowOrderShippingPlanFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("发货计划加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到发货确认
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '发货确认')]").click()

        self.driver.implicitly_wait(120)

        # 定位到发货确认
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到发货确认
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowOrderShippingConfirmationFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("发货确认加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到送仓计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '送仓计划')]").click()

        self.driver.implicitly_wait(120)

        # 定位到送仓计划
        self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到送仓计划
        self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowWarehousePlanningFormGridPanelID"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("送仓计划加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到收货通知
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收货通知')]").click()

        self.driver.implicitly_wait(120)

        # 定位到收货通知
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到收货通知
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowOrderReceivingNoticeForm"]//input[@name="main.orderNumber"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("收货通知加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(2)

        # 定位到样品付款
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '样品付款')]").click()

        self.driver.implicitly_wait(120)

        # 定位到样品付款
        self.driver.find_element_by_xpath("//*[@id='FlowSamplePaymentGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到样品付款
        self.driver.find_element_by_xpath("//*[@id='FlowSamplePaymentView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowSamplePaymentFormGridPanelID"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("样品付款加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到合同订金
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '合同订金')]").click()

        self.driver.implicitly_wait(120)

        # 定位到合同订金
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到合同订金
        self.driver.find_element_by_xpath("//*[@id='FlowDepositContractView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowDepositContractFormGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("合同订金加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到费用登记
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用登记')]").click()

        self.driver.implicitly_wait(120)

        # 定位到费用登记
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到费用登记
        self.driver.find_element_by_xpath("//*[@id='FlowFeeRegistrationView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowFeeRegistrationSubGridPanelID-purchaseContractProduct-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("费用登记加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到费用支付
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用支付')]").click()

        self.driver.implicitly_wait(120)

        # 定位到费用支付
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到费用支付
        self.driver.find_element_by_xpath("//*[@id='FlowFeePaymentView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowFeeRegistrationSubGridPanelID-project-normal-body"]//div[contains(text(), "其它费用尾款")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("费用支付加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到差额退款
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '差额退款')]").click()

        self.driver.implicitly_wait(120)

        # 定位到差额退款
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到差额退款
        self.driver.find_element_by_xpath("//*[@id='FlowBalanceRefundView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowBalanceRefundForm"]//input[@name="main.vendorName"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("差额退款加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 定位到收款账号
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收款账号')]").click()

        self.driver.implicitly_wait(120)

        # 定位到收款账号
        self.driver.find_element_by_xpath("//*[@id='FlowBankAccountViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到收款账号
        self.driver.find_element_by_xpath("//*[@id='FlowBankAccountView']//span[contains(@class, 'fa-pencil-square-o')]").click()

        Start = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(Start/1000) + ".s")

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="FlowBankAccountForm"]//input[@name="main.companyCnName"]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        finally:
            End = self.driver.execute_script("return window.performance.now()")
        print("加载时间",str(End/1000) + ".s")

        durtime8 = (End - Start)

        print("收款账号加载时间", str(durtime8/1000),".s")
        data.append((round(durtime8 / 1000, 2)))

        sleep(2)

        # 系统当前时间年份
        year = time.strftime('%Y', time.localtime(time.time()))
        # 月份
        month = time.strftime('%m', time.localtime(time.time()))
        # 日期
        day = time.strftime('%d', time.localtime(time.time()))
        # 具体时间 小时分钟毫秒
        mdhms = time.strftime('%m%d%H%M%S', time.localtime(time.time()))
        filetestyear = year
        filetestmonth = month
        filetestday = day
        fileYear = 'C:/purchase_test/' + year
        fileMonth = fileYear + month
        fileDay = fileMonth + day
        fileurl = filetestyear + filetestmonth + filetestday

        # if not os.path.exists(fileYear):
        #     os.mkdir(fileYear)
        #     os.mkdir(fileMonth)
        #     os.mkdir(fileDay)
        # else:
        #     if not os.path.exists(fileMonth):
        #         os.mkdir(fileMonth)
        #         os.mkdir(fileDay)
        #     else:
        #         if not os.path.exists(fileDay):
        #             os.mkdir(fileDay)

        # 创建一个文件，以‘timeFile_’+具体时间为文件名称
        fileDir = fileDay +'CN'+ '.csv'
        filetesturl = fileurl+ 'CN'+ '.csv'

        # 在该文件中写入当前系统时间字符串


        print(fileDir)
        endurl = '/var/www/pc/log/' + filetesturl
        print(endurl)

        try:
            f = open(fileDir, 'r')
            f.close()
        except IOError:
            f = open(fileDir, 'w')
            f.close()

        with open(fileDir, 'r+', newline='') as csvFile:
            try:
                # reader = csv.reader(csvFile)
                # reader.next(csvFile)
                writer = csv.writer(csvFile)

                reader = csv.reader(csvFile)
                rows = [row for row in reader]
                # print(rows)
                # print(type(rows))
                # print(len(rows))

                with open(fileDir, 'a+', newline='') as csvFile:
                    if len(rows) < 2:

                        headers = ['Date', 'Time', 'Login', '采购询价', '新品开发申请', '样品申请 ','采购计划', '采购合同', '清关申请', '归属权变更', '开设产品线','安检申请',
                                   '样品检验','订单质检','拓展安检','风控级别变更','货代报价','订单港口变更','发货计划','发货确认','送仓计划','收货通知','样品付款','合同订金',
                                   '费用登记','费用支付','差额退款','收款账号变更']
                        writer.writerow(headers)
                        writer.writerow(data)

                    else:
                        writer.writerow(data)






                        # if reader:
                        #     headers = ['脚本运行时间', 'Login时间', 'AllPending']
                        #     writer.writerow(headers)
                        #     writer.writerow(data)
                        #
                        # else:
                        #     writer.writerow(data)


            finally:
                csvFile.close()

        transport = paramiko.Transport(('192.168.1.224', 22))
        transport.connect(username='root', password='2019#newaim')

        sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

        sftp.put(fileDir, endurl)  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt

        transport.close()  # 关闭连接

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




























