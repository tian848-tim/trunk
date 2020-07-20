"""
测试用例标题：采购询价测试
测试场景：采购询价业务流程测试—采购组长退回后——采购员重新发启流程
创建者：Tim
创建日期：2018-10-15
最后修改日期：2018-10-15
输入数据：供应商：福州瑞聚家居用品有限公司，审批流程各个角色账号
输出数据：无

"""
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time,unittest,configparser


'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')


class ProductQuotation(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")
    
    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购询价'
        # 脚本标识－ID
        self.script_id = 'test_flow_product_quotation'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)


        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_ProductQuotation(self):
        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(3)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

        sleep(2)

        # 定位到采购询价新建
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class,'fa-plus')]").click()

        sleep(3)

        ## 选择供应商
        self.driver.find_element_by_xpath( "//*[@id='FlowProductQuotationViewFormPanelID-body']//input[@name='main.vendorName']").click()

        sleep(2)

        ## 定位到关键字
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-body']//input[@name='keywords']").send_keys('瑞聚')

        sleep(2)

        # 点击搜索
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        # 定位采购第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加SKU按钮'''
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 定位SKU第一条记录
        _elementThird = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementThird).perform()

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位到aud框
        self.driver.find_element_by_xpath("//div[@id='FlowProductQuotationViewFormGridPanelID-normal-body']/div/table/tbody/tr/td[8]").click()

        sleep(2)

        ## 定位到AUD输入
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID']//input[@name='priceAud']").send_keys('10')

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-play')]").click()

        sleep(5)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        self.login('Vic_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(3)

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

        # 定位iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewMainTbsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入退回内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 点击退回
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class, 'x-btn-icon-el fa fa-fw fa-reply')]").click()

        sleep(3)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)

         #再发启流程

        self.login('Vic_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(3)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购询价申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价申请')]").click()

        sleep(2)

        # 选择采购询价第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(3)

        # 定位到采购询价编辑
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-pencil-square-o')]").click()

        sleep(5)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-check-square')]").click()

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        self.login('Vic_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(3)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购询价申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价申请')]").click()

        sleep(2)

        # 选择采购询价第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(3)

        # 定位到采购询价编辑
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-pencil-square-o')]").click()

        sleep(5)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-check-square')]").click()

        sleep(3)



        def is_element_present(self, how, what):
            try:                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

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
            self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
