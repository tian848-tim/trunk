'''
测试用例标题：费用登记测试
测试场景：费用登记测试
创建者：Tom
创建日期：2018-7-25
最后修改日期：2018-7-25
输入数据：审批流程各个角色账号
输出数据：无

'''
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

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read('../core/config.ini')

'''
测试用例
'''

class FeeRegister(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):

        # 脚本标识－标题
        self.script_name = '费用登记'
        # 脚本标识－ID
        self.script_id = 'test_flow_fee_register'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.dr = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.dr = webdriver.Firefox(log_path=self.log_path)

        self.dr.implicitly_wait(15)
        self.dr.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_flow_fee_register(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据
        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()  # 定位到财务类
        sleep(3)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '费用登记')]").click()  # 定位到费用登记申请

        self.dr.find_element_by_xpath(
            "//*[@id='FlowFeeRegistrationView']//span[contains(@class,'fa-plus')]").click()  # 定位到费用登记新建

        self.dr.find_element_by_xpath(
            "//*[@id='FlowFeeRegistrationFormPanelID-body']//input[@name='main.feeType']").click()  ## 选择费用类型

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '合同尾款')]").click()  # 合同尾款



        self.dr.find_element_by_xpath(
            "//*[@id='FlowFeeRegistrationFormPanelID-orderContainer-innerCt']//input[@name='main.orderNumber']").click()  ## 选择订单编号

        _elementFirst = self.dr.find_element_by_xpath(
            "//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位采购第一条记录

        ActionChains(self.dr).double_click(_elementFirst).perform()  # 在此元素上双击

        sleep(2)

        self.dr.find_element_by_xpath(
            "//*[@id='FlowFeeRegistrationForm']//span[contains(@class,'fa-play')]").click()  # 定位到发启按钮

        sleep(2)


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
            self.dr.quit()
            self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
