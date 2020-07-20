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
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购计划——固定供应商'
        # 脚本标识－ID
        self.script_id = 'test_flow_purchase_contract'
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

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_PurchasePlan(self):
        self.login('Ken_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()

        sleep(2)

        # 定位到采购计划新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到供应商名称输入框
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.vendorName']").click()

        sleep(2)

        # 定位到供应商选择器关键字输入框
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys('汇信进出口集团股份有限公司')

        sleep(2)

        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        # 定位查询结果第一个元素
        _element=self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_element).perform()

        sleep(2)

        # 定位到订单类型
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.purchaseType']").click()

        sleep(2)

        #定位订单类型
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '国际订单')]").click()

        sleep(2)

        # 定位添加SKU按钮'''
        _elementThird=self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementThird).perform()

        sleep(2)

        # 定位到sku
        self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID-body']//input[@name='keywords']").send_keys("KPF-TABLE-60-BU")

        sleep(2)

        # 定位到sku
        self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID-body']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        # 定位第一个SKU
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 定位到确认按钮
        self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位生成周期输入框
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID-body']//input[@name='main.leadTime']").send_keys('2')

        sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-save')]").click()

        sleep(2)

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(3)

        # 定位到相关报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'相关报告')]").click()

        sleep(2)

        # 定位到产品分析报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品分析报告')]").click()

        sleep(2)

        # 定位到产品分析报告新建
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到申请单类型
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@value='新品开发申请']").click()

        sleep(2)

        # 采购计划申请
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains (text(),'采购计划申请')]").click()

        sleep(2)

        # 定位到应用ID
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main_businessId']").click()

        sleep(2)

        # 定位第采购计划申请器第一条记录
        _elementFourth = self.driver.find_element_by_xpath("//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)

        # 定位到报告文件输入框
        self.driver.find_element_by_xpath( "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='reportFileDocumentName']").click()

        sleep(2)

        # 定位文件选择器第一条记录
        _elementFiveth = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFiveth).perform()

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到报告标题
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.title']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到报告编号
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.serialNumber']").send_keys(_elementFiveth)

        sleep(2)

        # 报告时间
        #self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.reportTime']").send_keys('2018-06-02')

        #sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(2)

        # 定位到申请单据
        _elementSixth=self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSixth).perform()

        sleep(2)

        # 定位到采购计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()

        sleep(2)

        # 选择采购计划第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()


        sleep(2)

        # 定位到采购计划编辑
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-play')]").click()

        sleep(2)

        # 定位到采购计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()

        sleep(2)

        # 选择采购计划第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购计划编辑
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位到通过按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-check-square')]").click()

        sleep(2)


    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
