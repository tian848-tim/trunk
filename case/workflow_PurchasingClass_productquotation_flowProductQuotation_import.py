"""
测试用例标题：采购询价测试
测试场景：采购询价业务流程测试——导入
创建者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-23
输入数据：供应商：瑞聚家具公司，审批流程各个角色账号
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
        self.script_name = '新建供应商分类'
        # 脚本标识－ID
        self.script_id = 'test_flow_product_quotation_import'
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


    def test_productquotation(self):
        self.login('Vic_cn','123')

        # 强制等待
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

        # 强制等待
        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        # 强制等待
        sleep(2)

        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

        sleep(3)

        # 定位到导入
        self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class,'fa-file-text-o')]").click()

        sleep(3)


        # 定位到数据文件
        self.driver.find_element_by_xpath("//*[@id='DataImportFormPanelID-body']//input[@name='main.importFile']").click()

        sleep(3)

        # 定位到搜索框
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinSearchPanelID']//input[@name='keywords']").send_keys("productquotation_import_for_newaim.csv")

        sleep(3)


        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinSearchPanelID']//span[contains(@class,'fa-search')]").click()

        sleep(3)


        # 定位到第一条记录
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)


        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductSpecialityNotifiedFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(3)

        # 定位到第一条
        self.driver.find_element_by_xpath("//*[@id='DataImportGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到执行
        self.driver.find_element_by_xpath("//*[@id='DataImportView']//span[contains(@class,'fa-file-text-o')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(10)

        # 定位到第一条
        self.driver.find_element_by_xpath("//*[@id='DataImportGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(10)


        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        # 强制等待
        sleep(2)

        # 定位到采购询价
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

        sleep(10)





        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        sleep(2)

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()



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
