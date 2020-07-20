'''
测试用例标题：清关测试
测试场景：归属权变更业务流程测试——经理拒绝
创建者：Tim
创建日期：2018-10-26
最后修改日期：2018-10-26
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


class ChangeOwnership(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_changeownership_flowChangeOwnership_reject.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '归属权变更业务流程测试——经理拒绝'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_changeownership_flowChangeOwnership_reject'
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
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_ChangeOwnership(self):

        su = self.loadvendername()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('Richard_cn', '123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到归属权变更申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '归属权变更申请')]").click()

        sleep(2)

        #定位新建按钮
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipView']//span[contains(@class, 'fa-plus')]").click()

        sleep(2)

        #定位供应商名称
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.vendorName')]").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        #定位第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        print(_elementFiveth)

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        #self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID']//span[contains(@class, 'fa-check')]").click()



        sleep(2)

        #定位变更供应商变更
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@class, 'x-form-cb')]").click()

        sleep(2)

        #定位新归属人
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.newOwnerName')]").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        #定位第一条记录
        _elementFirst =self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        #定位新sku操作人
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[contains(@name, 'main.newOperatorName')]").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        #定位第一条记录
        _elementFirst =self.driver.find_element_by_xpath("//*[@id='UserDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        #定位变更产品线归属
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//label[contains(text(), '是否变更产品线归属')]").click()

        sleep(2)

        #定位变更产品线归属
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewFormPanelID-body']//input[@name='main.productLine']").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        print(lis)

        first_category = lis[random.randint(1, len(lis) - 1)]

        print(len(lis))

        print(first_category)

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        sleep(2)

        #定位发启
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipForm']//span[contains(@class, 'fa-play')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''经理审核'''

        self.login(su[1][0], su[1][1])
        #self.login('Jack.L', '123')

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
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipViewMainTbsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        #定位拒绝
        self.driver.find_element_by_xpath("//*[@id='FlowChangeOwnershipForm']//span[contains(@class, 'fa-window-close')]").click()

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





