
'''
测试用例标题：收款账号变更测试
测试场景：收款账号变更流程测试
创建者：Tom
创建日期：2018-7-25
最后修改日期：2018-7-25
输入数据：供应商：搭瓦家具公司，审批流程各个角色账号
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
cfg.read('../../../../core/config.ini')

'''
测试用例
'''

class Refund(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '收款账号变更'
        # 脚本标识－ID
        self.script_id = 'test_flow_bank_account'
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


    def test_flow_balance_refund(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据
        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()  # 定位到财务类
        sleep(3)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '收款账号变更')]").click()  # 定位到收款账号变更

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountView']//span[contains(@class,'fa-plus')]").click()  # 定位到收款账号变更新建





        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-vendorContainer']//input[@name='main.vendorName']").click()  # 选择供应商


        self.dr.find_element_by_xpath(
            "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys('搭')  # 定位到关键字

        self.dr.find_element_by_xpath(
            "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()  # 点击搜索

        _elementFirst = self.dr.find_element_by_xpath(
            "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位供应商第一条记录

        ActionChains(self.dr).double_click(_elementFirst).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyCnName']").send_keys('中国')  # 公司中文名

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyEnName']").send_keys(
            'CHINA')  # 公司英文名

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyCnAddress']").send_keys(
            '广州')  # 公司中文地址

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.companyEnAddress']").send_keys(
            'GZ')  # 公司英文地址

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.beneficiaryBank']").send_keys(
            '工商银行')  # 开户银行

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.beneficiaryBankAddress']").send_keys(
            '广州')  # 开户银行地址

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.bankAccount']").send_keys(
            '6225211001112588')  # 账号

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='main.currency']").click()  # 结算币种

        self.dr.find_element_by_xpath(
            "//*[@class='x-list-plain']//li[contains(text(), 'USD')]").click()  # 选择USD

        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountViewFormPanelID-body']//input[@name='guaranteeLetterName']").click()  # 保函


        _elementSecond = self.dr.find_element_by_xpath(
            "//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位第一条记录

        ActionChains(self.dr).double_click(_elementSecond).perform()  # 在此元素上双击



        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountForm']//span[contains(@class,'fa-play')]").click()  # 定位到发启按钮

        sleep(2)




        self.dr.find_element_by_link_text('注销').click()  # 点击注销


        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面


        self.login('Vic_cn', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click() #定位到待办事项第一条记录

        self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click() # 点击马上处理





        self.dr.find_element_by_xpath(
            "//*[@id='FlowBankAccountForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面

        sleep(5)

        self.login('emma', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()  # 定位到待办事项第一条记录

        self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()  # 点击马上处理



        self.dr.find_element_by_xpath("//*[@id='FlowBankAccountForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过


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
