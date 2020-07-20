'''
测试用例标题：订单发货计划测试
测试场景：订单发货计划业务流程测试
创建者：Tim
创建日期：2018-11-8
最后修改日期：2018-11-8
输入数据：审批流程各个角色账号
输出数据：无

'''

# -*- coding: utf-8 -*-
import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, configparser
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


class CustomClearance(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '订单发货计划—固定供应商'
        # 脚本标识－ID
        self.script_id = 'test_flow_custom_clearance'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get('http://192.168.1.109:880/')  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_CustomClearance(self):
        self.login('carla', '123')


        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)
        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到订单发货计划
        self.driver.find_element_by_xpath( "//*[@id='west-panel-targetEl']//span[contains(text(), '订单发货计划')]").click()

        sleep(2)

        # 定位到订单发货计划新建
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位插入按钮
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanFormGridPanelID-f-body']//img[contains(@class, 'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)


        # 定位到供应商
        self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID-body']//input[@name='keywords']").send_keys("清远市瑞强五金制品有限公司")

        sleep(2)

        # 定位到供应商
        self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID-body']//span[contains(@class,'fa-search')]").click()



        sleep(2)

        # 定位第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位到服务商名称
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanForm-body']//input[@name='serviceProviderName']").click()

        sleep(2)

        _elementFiveth = (random.randint(0, 1))


        # 定位第一条记录
        #_elementFirst = self.driver.find_element_by_xpath("//*[@id='ServiceProviderQuotationDialogWinID']//div[contains(text(), 'K&N')]")
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='ServiceProviderQuotationDialogWinID']//tr[@data-recordindex={}]".format(_elementFiveth))
        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位到发启
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanForm']//span[contains(@class,'fa-play')]").click()

        sleep(8)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第一节点审核'''

        self.login('carla', '123')

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

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlaMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择第一项
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(5)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点审核'''

        self.login('Jack.L', '123')

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

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingPlanForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(5)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面


    def isElementExist(self, link):
        s=self.driver.find_elements_by_xpath(link)

        if s.click():

            return True
        else:

            return False


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



if __name__ == "__main__":
    unittest.main()

