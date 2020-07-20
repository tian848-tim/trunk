'''
测试用例标题：样品付款测试
测试场景：样品付款业务流程测试
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
#用谷歌浏览器,下载chromedriver到python安装目录

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

class sample(unittest.TestCase):

    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values':
                {
                    'notifications': 2
                }
        }
        options.add_experimental_option('prefs', prefs)
        self.dr = webdriver.Chrome(chrome_options=options)
        # 脚本标识－标题
        self.script_name = '样品付款'
        # 脚本标识－ID
        self.script_id = 'test_flow_sample_payment'
        self.target_url = self.base_url + self.project_path

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


    def test_Sample(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据
        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '财务类')]").click()  # 定位到财务类
        sleep(3)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '样品付款')]").click()  # 定位到样品付款申请

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择样品付款申请第一条记录


        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentView']//span[contains(@class,'fa-pencil-square-o')]").click()  # 定位到付款申请编辑

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentForm']//span[contains(@class,'fa-play')]").click()  # 定位到发启按钮

        sleep(5)




        self.dr.find_element_by_link_text('注销').click()  # 点击注销


        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面





        sleep(5)

        self.login('Vic_cn', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click() #定位到待办事项第一条记录

        self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click() # 点击马上处理

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

        self.dr.find_element_by_xpath(
            "//*[@class='x-list-plain']//li[contains(text(), 'Hanne')]").click()  # 选择Hanne

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        sleep(2)

        alert.accept()  # 退出页面

        sleep(5)

        self.login('Hanne', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath(
            "//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()  # 定位到待办事项第一条记录

        self.dr.find_element_by_xpath(
            "//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()  # 点击马上处理

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentForm-body']//input[@name='main.paymentTotalSampleFeeRmb']").send_keys('26')  # 输入RMB

        self.dr.find_element_by_xpath(
            "//*[@id='FlowSamplePaymentForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过


        sleep(2)






    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
