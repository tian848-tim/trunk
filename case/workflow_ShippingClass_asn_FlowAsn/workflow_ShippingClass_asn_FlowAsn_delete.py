'''
测试用例标题：收货通知测试
测试场景：收货通知业务流程测试——删除
创建者：：Tim
创建日期：2018-11-12
最后修改日期：2018-11-12
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



class FlowAsn(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_ShippingClass_asn_FlowAsn_delete.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_ShippingClass_asn_FlowAsn_delete.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '收货通知——删除'
        # 脚本标识－ID
        self.script_id = 'FlowAsn_delete'
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


    def test_FlowAsn(self):
        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('rachel','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到收货通知
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收货通知')]").click()

        sleep(2)

        # 定位到收货通知新建
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到采购订单编号
        self.driver.find_element_by_xpath("//*[@class='x-form-trigger-input-cell']//input[@name='main.orderNumber']").click()

        sleep(2)

        if ad[0] != '':

            # 点击发启
            self.driver.find_element_by_xpath("//*[@id='WarehousePlanningDialogWinID']//input[contains(@name,'keywords')]").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='WarehousePlanningDialogWinID']//span[contains(@class,'fa-search')]").click()

            _elementFiveth = (random.randint(0, 0))

            sleep(2)

            # 定位订单记录
            _elementSecond = self.driver.find_element_by_xpath("//*[@id='WarehousePlanningDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))


            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

        else:
            _elementFiveth = (random.randint(0, 5))

            sleep(2)

            # 定位订单记录
            _elementSecond = self.driver.find_element_by_xpath("//*[@id='WarehousePlanningDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)


        # 输入接收时间
        #self.driver.find_element_by_xpath("//*[@class='x-form-trigger-input-cell']//input[@name='main.receiveDate']").send_keys('2018-10-23')

        #sleep(2)

        #_elementFiveth = (random.randint(0, 1000))

        # 输入ASN
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeFormPanelID-body']//input[@name='main.asnNumber']").send_keys("ASD",_elementFiveth)

        #sleep(2)

        # 点击保存
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeForm']//span[contains(@class,'fa-sav')]").click()

        sleep(10)



        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''删除'''

        self.login(su[0][0],su[0][1])
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到收货通知
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收货通知')]").click()

        sleep(2)

        # 定位到收货通知第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeView-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到收货通知删除
        self.driver.find_element_by_xpath("//*[@id='FlowOrderReceivingNoticeView']//span[contains(@class, 'fa-trash')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(2)



    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()