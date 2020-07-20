'''
测试用例标题：送仓时间变更测试
测试场景：送仓时间变更业务流程测试
创建者：Tim
创建日期：2018-11-20
最后修改日期：2018-11-20
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
import datetime

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class ChangeOrderQty(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def variable(self):


        try:
            global ABC,variable
            file = open(rootPath + '/data/'+ "test_FlowFeePayment" + time.strftime("%Y-%m-%d") + '.json', encoding='utf-8')
            data = json.load(file)
            ABC = [(d['key']) for d in data['variable']]
            variable = True
            return ABC

        except IOError:

            variable = False

            print("test_FlowFeePayment" + time.strftime("%Y-%m-%d") + '.json'+"File not found")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/ChangeOrderQty.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/ChangeOrderQty.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['keywords']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '下单量变更单--组合'
        # 脚本标识－ID
        self.script_id = 'ChangeOrderQty_grouping'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()



    def test_ChangeOrderQty(self):

        su = self.loadvendername()
        ad = self.variable()
        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn ','123')

        sleep(10)

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

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(3)

        # 定位到订单资料
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'订单资料')]").click()

        sleep(3)

        # 定位到下单量变更单
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'下单量变更单')]").click()

        sleep(3)

        # 定位到新建
        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyView']//span[contains(@class,'fa-plus')]").click()

        sleep(3)

        # 定位到订单编号
        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormWinID-body']//input[@name = 'main.orderNumber']").click()

        sleep(5)

        if ad[0] !='':

            self.driver.find_element_by_xpath(
                "//*[@id='OrderDialogWinID-body']//input[@name = 'keywords']").send_keys(ad[0])

            sleep(2)

            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID-body']//span[contains(@class,'fa-search')]").click()

            sleep(2)

            _elementFirst =self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[text()='1']")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')


            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            sleep(2)

            _elementFirst =self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加订单信息按钮'''
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-f-body']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        ActionChains(self.driver).double_click(_elementFirst).perform()


        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        sleep(2)

        _elementFiveth = (random.randint(1, len(lis)))

        sleep(2)

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        target = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        sleep(3)

        # 定位到关键字
        self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-normal-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        sleep(2)

        _elementFiveth = (random.randint(1, len(lis)))

        _elementThird = self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[4]/div[contains(@class,'x-grid-cell-inner ')]".format(_elementFiveth)).text

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[7]/div[contains(@class,'x-grid-cell-inner ')]".format(_elementFiveth)).click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-f-body']//input[@name = 'changeOrderQty']").clear()

        sleep(2)

        _elementThird = (random.randint(1, int(_elementThird)))

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-f-body']//input[@name = 'changeOrderQty']").send_keys(_elementThird)

        sleep(2)

        _elementFourth= self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[4]/div[contains(@class,'x-grid-cell-inner ')]".format(len(lis))).text

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[7]/div[contains(@class,'x-grid-cell-inner ')]".format(len(lis))).click()

        sleep(2)

        _elementFourth = (random.randint(1, int(_elementFourth)))

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormGridPanelID-f-body']//input[@name = 'changeOrderQty']").send_keys(_elementFourth)

        sleep(2)

        target = self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormWinID']//span[contains(@class,'fa-save ')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormWinID']//span[contains(@class,'fa-save ')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(120)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyGridPanelID-body']//div[text()='1']").click()

        sleep(5)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyTbsPanelId-body']//span[contains(@class,'fa-check')]").click()

        sleep(5)

        self.driver.find_element_by_xpath("//*[@id='ChangeOrderQtyFormWinID']//span[contains(@class,'fa-check')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(120)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()















