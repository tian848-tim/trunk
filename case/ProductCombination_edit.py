'''
测试用例标题：产品组合关系测试
测试场景：产品组合关系业务流程测试——编辑
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

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class VendorCategory(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/ProductCombination_edit.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/ProductCombination_edit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '产品组合关系——编辑'
        # 脚本标识－ID
        self.script_id = 'ProductCombination_edit'
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



    def test_vendorcategory(self):
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

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(3)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(3)

        # 定位到产品组合关系
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品组合关系')]").click()

        sleep(3)

        # 定位到产品组合关系第一条
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormGridGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到产品组合关系编辑
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到组合产品编码
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID-body']//input[@name='main.combinedSku']").send_keys("SDFGH",_elementFiveth)

        sleep(3)

        # 定位到组合产品编码
        _T = self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID-body']//input[@name='main.combinedSku']").get_attribute("value")

        sleep(3)


        # 定位到组合产品名
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID-body']//input[@name='main.combinedName']").send_keys(_T)

        sleep(3)

        # 定位到EAN
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID-body']//span[contains(@class,'x-btn-icon-el')]").click()


        sleep(3)

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormGridPanelID-f-body']//img[contains(@class, 'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()


        sleep(3)

        if ad[0] != '':


            # 定位到关键字
            self.driver.find_element_by_xpath("//*[@id='ProductDialogWinSearchPanelID-body']//input[@name='keywords']").send_keys(ad[0])

            sleep(3)

            # 定位到查询
            self.driver.find_element_by_xpath("//*[@id='ProductDialogWinSearchPanelID-body']//span[contains(@class,'fa-search')]").click()

            sleep(3)

            _elementFiveth = (random.randint(0, 20))

            # 定位到选择
            _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_N).perform()

            sleep(3)

            _elementFiveth = (random.randint(0, 20))

            # 定位到选择
            _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_N).perform()

            sleep(3)

        else:

            _elementFiveth = (random.randint(0, 20))

            # 定位到选择
            _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_N).perform()

            sleep(3)

            _elementFiveth = (random.randint(0, 20))

            # 定位到选择
            _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_N).perform()

            sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID']//span[contains(@class,'fa-save')]").click()


        sleep(3)


        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormGridMainTbsPanelID']//span[contains(text(),'档案修改历史')]").click()

        sleep(3)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormGridGridPanelID-ArchivesHistoryTabGrid-body']//div[contains(@class,'btnRowConfirm')]").click()

        sleep(3)

        # 定位到审核
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationFormWinID']//span[contains(@class,'fa-check')]").click()

        sleep(8)

    def tearDown(self):
        self.driver.quit()

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

if __name__ == "__main__":
        unittest.main()