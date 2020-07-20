'''
测试用例标题：收款账号变更测试
测试场景：收款账号变更流程测试——采购组长拒绝
创建者：Tim
创建日期：2018-11-15
最后修改日期：2018-11-15
输入数据：供应商：搭瓦家具公司，审批流程各个角色账号
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
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

class Refund(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_FinancialClass_bankaccount_FlowBankAccount_purchaseleader_reject.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_FinancialClass_bankaccount_FlowBankAccount_purchaseleader_reject.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '收款账号变更——采购组长拒绝'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_bankaccount_FlowBankAccount_purchaseleader_reject'
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


    def test_flow_balance_refund(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0], su[0][1])
        # self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到财务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()

        sleep(3)

        # 定位到收款账号变更
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收款账号变更')]").click()

        sleep(2)

        # 定位到收款账号变更新建
        self.driver.find_element_by_xpath("//*[@id='FlowBankAccountView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 选择供应商
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-vendorContainer']//input[@name='main.vendorName']").click()

        sleep(2)

        if ad[0] != '':

            # 定位到关键字
            self.driver.find_element_by_xpath(
                "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

            sleep(2)

            # 点击搜索
            self.driver.find_element_by_xpath(
                "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            _elementFiveth = (random.randint(1, 10))

            # 定位供应商
            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(),'{}')]".format(_elementFiveth))

            print(_elementFirst)

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            _elementFiveth = (random.randint(1, 10))

            # 定位供应商
            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(),'{}')]".format(_elementFiveth))

            print(_elementFirst)

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 公司中文名
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyCnName']").send_keys('中国')

        sleep(2)

        # 公司英文名
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyEnName']").send_keys('CHINA')

        sleep(2)

        # 公司中文地址
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyCnAddress']").send_keys('广州')

        sleep(2)

        # 公司英文地址
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyEnAddress']").send_keys('GZ')

        sleep(2)

        # 开户银行
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.beneficiaryBank']").send_keys('工商银行')

        sleep(2)

        # 开户银行地址
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.beneficiaryBankAddress']").send_keys(
            '广州')

        sleep(2)

        # 账号
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.bankAccount']").send_keys(
            '6225211001112588')

        sleep(2)

        # 结算币种
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.currency']").click()

        sleep(2)

        # 选择USD
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'USD')]").click()

        sleep(2)

        # 保函
        self.driver.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='guaranteeLetterName']").click()

        sleep(2)

        # 定位第一条记录
        _elementSecond = self.driver.find_element_by_xpath(
            "//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowBankAccountForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(8)



        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第一节点'''

        self.login(su[1][0], su[1][1])
        # self.login('Vic_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

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
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowBankAccountViewMainTbsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 点击拒绝
        self.driver.find_element_by_xpath("//*[@id='FlowBankAccountForm']//span[contains(@class, 'fa-window-close')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)



        def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
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
