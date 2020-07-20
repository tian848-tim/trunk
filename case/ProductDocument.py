'''
测试用例标题：产品档案测试
测试场景：产品档案业务流程测试
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
        file = open(rootPath + '/data/ProductDocument.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '产品档案'
        # 脚本标识－ID
        self.script_id = 'ProductDocument'
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
        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn ','123')

        sleep(5)

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

        sleep(2)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(2)

        # 定位到新品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品档案')]").click()

        sleep(2)

        # 定位到新品档案第一条
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(2)

        # 定位到新品档案第一条
        sku = self.driver.find_element_by_xpath("//*[@id='ProductDocumentGridPanelID-locked-body']/div/table/tbody/tr/td[3]/div").text

        sleep(2)

        # 定位到新品档案编辑
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(1)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonL']").clear()

        sleep(1)

        _elementFiveth = (random.randint(0, 100))

        # 定位到内箱长
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonL']").send_keys(_elementFiveth)

        sleep(1)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonW']").clear()

        sleep(1)

        _elementFiveth_1 = (random.randint(0, 100))

        # 定位到内箱宽
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonW']").send_keys(_elementFiveth_1)

        sleep(1)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonH']").clear()

        sleep(1)

        _elementFiveth_2 = (random.randint(0, 100))

        # 定位到内箱高
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonH']").send_keys(_elementFiveth_2)

        sleep(1)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonGrossWeight']").clear()

        sleep(1)


        _elementFiveth_3 = (random.randint(0, 100))

        # 定位到内箱毛重
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonGrossWeight']").send_keys(_elementFiveth_3)

        sleep(1)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonNetWeight']").clear()

        sleep(2)

        _elementFiveth = (random.randint(0, 100))

        # 定位到内箱净重
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.innerCartonNetWeight']").send_keys(_elementFiveth)

        sleep(1)

        _T = self.driver.find_element_by_xpath(
            "//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.pcsPerCarton']").get_attribute(
            "value")

        sleep(2)

        if _T > '1':

            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonL']").clear()

            sleep(1)

            _elementFiveth = (random.randint(_elementFiveth_1, 100))

            # 定位到外箱长
            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonL']").send_keys(_elementFiveth)

            sleep(1)

            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonW']").clear()

            sleep(1)

            _elementFiveth = (random.randint(_elementFiveth_2, 100))

            # 定位到外箱宽
            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonW']").send_keys(_elementFiveth)

            sleep(1)

            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonH']").clear()

            sleep(1)

            _elementFiveth = (random.randint(_elementFiveth_3, 100))

            # 定位到外箱高
            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonH']").send_keys(_elementFiveth)

        sleep(2)


        # 定位到外箱纸箱规格
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonStructure']").click()

        sleep(2)

        # 定位到外箱纸箱规格
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'A=A')]").click()

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(0, len(lis) - 1)]

        print(len(lis))

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonGrossWeight']").clear()

        sleep(2)

        _elementFiveth = (random.randint(0, 100))

        # 定位到外箱毛重
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonGrossWeight']").send_keys(_elementFiveth)

        sleep(2)

        # 定位到外箱毛重
        _T=self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.prop.masterCartonGrossWeight']").get_attribute("value")

        sleep(2)

        if _T >= '60':

            self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID-body']//input[@name='main.palletized']").click()

            sleep(2)

            #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item x-boundlist-item-over')]").click()

            ul = self.driver.find_elements_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']")[1]
            ul = ul.find_element_by_xpath('ul')
            lis = ul.find_elements_by_xpath('li')

            first_category = lis[random.randint(1, len(lis) - 1)]

            print(len(lis))

            sleep(2)

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()

        else:

            pass

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID']//span[contains(@class,'fa-save')]").click()

        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)


        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        # 强制等待
        sleep(5)

        self.login(su[1][0], su[1][1])
        #self.login('Vic_cn ','122')

        sleep(5)

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

        sleep(2)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(2)

        # 定位到新品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品档案')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentView']//input[@name='keywords']").send_keys(sku)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ProductDocumentView']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        # 定位到新品档案第一条
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(2)

        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentTbsPanelId']//span[contains(text(),'档案修改历史')]").click()

        sleep(2)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentTbsPanelId-body']//div[contains(@class,'btnRowConfirm')]").click()

        sleep(2)

        # 定位到审核
        self.driver.find_element_by_xpath("//*[@id='ProductDocumentFormWinID']//span[contains(@class,'fa-check')]").click()

        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

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