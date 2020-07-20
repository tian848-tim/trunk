'''
测试用例标题：代运营产品测试
测试场景：代运营产品业务流程测试——编辑
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
class ProductCategory(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")


    def loadvendername(self):

        global result
        file = open(rootPath + '/data/ProductAgencyOperation_edit.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '代运营产品——编辑'
        # 脚本标识－ID
        self.script_id = 'ProductAgencyOperation_edit'
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


    def test_ProductCategory(self):
        su = self.loadvendername()
        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('admin','123')


        sleep(5)

        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(3)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(3)

        # 定位到代运营产品
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'代运营产品')]").click()

        sleep(3)

        # 定位到第一条
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)


        # 定位到产品证书档案编辑
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.sku']").clear()

        _elementFiveth = (random.randint(0, 1000))

        # 定位到产品编码
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.sku']").send_keys("SDF",_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.name']").clear()

        # 定位到产品名
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.name']").send_keys("SDF",_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.barcode']").clear()

        _elementFiveth = (random.randint(0, 1000))

        # 定位到条码
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.barcode']").send_keys("SDF",_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.ean']").clear()

        _elementFiveth = (random.randint(0, 1000))

        # 定位到EAN
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.ean']").send_keys("SDF",_elementFiveth)

        sleep(3)

        # 定位到分类
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.categoryName']").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 10))

        # 定位到分类
        _elementFirst =self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelID']//tr[@data-recordindex={}]".format(_elementFiveth))

        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.pcsPerCarton']").clear()

        _elementFiveth = (random.randint(1, 10))

        # 定位到件/箱
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.pcsPerCarton']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonL']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到内箱长
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonL']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonW']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到内箱宽
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonW']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonH']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到内箱高
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonH']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonGrossWeight']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到毛重
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonGrossWeight']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonCbm']").clear()


        _elementFiveth = (random.randint(1, 100))

        # 定位到体积
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonCbm']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonNetWeight']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到净重
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonNetWeight']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonCubicWeight']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到重量
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.innerCartonCubicWeight']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonL']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱长
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonL']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonW']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱宽
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonW']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonH']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱高
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonH']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonCbm']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱体积
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonCbm']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonGrossWeight']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱毛重
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonGrossWeight']").send_keys(_elementFiveth)

        sleep(3)

        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonCubicWeight']").clear()

        _elementFiveth = (random.randint(1, 100))

        # 定位到外箱重量
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormPanelID']//input[@name='main.prop.masterCartonCubicWeight']").send_keys(_elementFiveth)

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormWinID']//span[contains(@class,'fa-save')]").click()


        sleep(10)

        # 定位到第一条
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationTbsPanelId']//span[contains(text(),'档案修改历史')]").click()

        sleep(3)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationGridPanelID-ArchivesHistoryTabGrid-SubGridPanelId-body']//div[contains(@class,'btnRowConfirm')]").click()

        sleep(3)

        # 定位到审核
        self.driver.find_element_by_xpath("//*[@id='ProductAgencyOperationFormWinID']//span[contains(@class,'fa-check')]").click()

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



