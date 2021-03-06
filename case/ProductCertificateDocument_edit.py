'''
测试用例标题：产品证书测试
测试场景：产品证书业务流程测试——编辑
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
        file = open(rootPath + '/data/ProductCertificateDocument_edit.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/ProductCertificateDocument_edit.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '产品证书——编辑'
        # 脚本标识－ID
        self.script_id = 'ProductCertificateDocument_edit'
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
        ad = self.loadvendernames()
        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn','123')

        sleep(5)

        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(3)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(3)

        # 定位到产品证书档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品证书档案')]").click()

        sleep(3)


        # 定位到产品证书档案第一条记录
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到产品证书档案编辑
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(3)

        # 定位到供应商名称
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID']//input[contains(@class,'x-form-text')]").click()

        sleep(3)

        # 定位到搜索框
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID']//input[@name='keywords']").send_keys(ad[0])

        sleep(3)

        # 定位到供应商名称
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID']//span[contains(@class,'fa-search')]").click()

        sleep(3)

        # 定位到选择
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(3)


        # 定位到插入
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//img[contains(@class,'x-tool-plus')]")

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(3)

        _elementFiveth = (random.randint(0, 5))

        # 定位到选择
        _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_N).perform()

        sleep(3)

        _elementFiveth = (random.randint(0, 5))

        # 定位到选择
        _N = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_N).perform()

        sleep(3)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(3)

        # 定位到生效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//input[@name='effectiveDate']").clear()

        sleep(3)

        # 定位到生效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//input[@name='effectiveDate']").click()

        sleep(3)

        # 定位到失效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//input[@name='validUntil']").clear()

        sleep(3)

        # 定位到失效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//input[@name='validUntil']").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到认证编号
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//input[@name='certificateNumber']").send_keys("45785",_elementFiveth)

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到描述
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//textarea[@name='description']").send_keys("45785",_elementFiveth)

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到相关标准
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm-body']//textarea[@name='relevantStandard']").send_keys("45785",_elementFiveth)

        sleep(3)


        # 定位到插入
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='CertificateAttachmentMultiGrid']//img[contains(@class,'x-tool-plus')]")

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(3)

        _elementFiveth = (random.randint(0, 100))

        # 定位到选择
        _N = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_N).perform()

        sleep(3)

        _elementFiveth = (random.randint(0, 100))

        # 定位到选择
        _N = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_N).perform()

        sleep(3)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(5)


        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm']//span[contains(@class,'fa-save')]").click()

        sleep(5)


        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewMainTbsPanelID']//span[contains(text(),'档案修改历史')]").click()

        sleep(3)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewGridPanelID-ArchivesHistoryTabGrid-body']//div[contains(@class,'btnRowConfirm')]").click()

        sleep(3)

        # 定位到审核
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm']//span[contains(@class,'fa-check')]").click()

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



