'''
测试用例标题：SKU风控级别变更
测试场景：SKU风控级别变更业务流程测试——安检组长拒绝
创建者：Tim
创建日期：2018-11-6
最后修改日期：2018-11-6
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

import json
import random

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''

class ComplianceExtend(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_CheckClass_complianceapplyquick_FlowComplianceApplyQuick_securityleadr_reject.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_CheckClass_complianceapplyquick_FlowComplianceApplyQuick_securityleadr_reject.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = 'SKU风控级别变更业务流程测试——安检组长拒绝'
        # 脚本标识－ID
        self.script_id = 'workflow_CheckClass_complianceapplyquick_FlowComplianceApplyQuick_securityleadr_reject'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_Compliance_Extend(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Linda_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '检验类')]").click()

        sleep(3)

        # 定位到SKU风控级别变更
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), 'SKU风控级别变更')]").click()

        sleep(2)

        # 定位到新建
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickView']//span[contains(@class, 'fa-plus')]").click()

        sleep(2)


        # 定位到供应商名称
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickViewFormPanelID-body']//input[@name='main.vendorName']").click()

        sleep(2)

        if ad[0] != '':

              # 定位到关键字
              self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-body']//input[contains(@class, 'x-form-text')]").send_keys(ad[0])

              sleep(2)

              # 定位到查询
              self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-body']//span[contains(@class, 'fa-search')]").click()

              sleep(2)


              # 定位到第一项
              _elementFourth = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

              sleep(2)

              # 在此元素上双击
              ActionChains(self.driver).double_click(_elementFourth).perform()

        else:
            _elementFiveth = (random.randint(1, 10))

            # 定位到第一项
            _elementFourth = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)


        # 定位到插入
        _elementFourth = self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickFormGridPanelID_header-body']//img[contains(@class, 'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)

        # 定位样品第二条记录
        _elementFourth = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)


        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)


        # 定位到风控级别
        self.driver.find_element_by_xpath("//div[@id='FlowComplianceArrangementQuickFormGridPanelID-normal-body']/div/table/tbody/tr/td[3]").click()

        sleep(2)

        # 点击
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickFormGridPanelID-f-body']//input[contains(@class, 'x-field-default-form-focus')]").click()

        sleep(2)

        # 定位到级别
        self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']//li[contains(text(), '黄（五抽一）')]").click()

        sleep(2)

        # 退出定位到级别
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickFormGridPanelID-normal-body']//div[contains(@class, 'x-grid-view-default')]").click()

        sleep(2)


        # 定位到发启
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickForm']//span[contains(@class, 'fa-play')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(5)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点'''

        self.login(su[0][0],su[0][1])
        #self.login('Linda_cn','123')


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
        if   self.driver.find_element_by_xpath( "//*[@id='FlowComplianceArrangementQuickViewMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").is_displayed():

             sleep(2)

            # 分配处理人
             self.driver.find_element_by_xpath( "//*[@id='FlowComplianceArrangementQuickViewMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

             sleep(2)

             # 选择
             self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(su[0][0])).click()

            # 点击通过
             self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickForm']//span[contains(@class, 'fa-check-square')]").click()

        else:

            # 点击通过
             self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(5)



        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第三节点'''

        self.login(su[0][0],su[0][1])

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
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickViewMainTbsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 点击拒绝
        self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementQuickForm']//span[contains(@class, 'fa-window-close')]").click()

        sleep(5)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面


    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
