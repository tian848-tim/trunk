'''
测试用例标题：产品组合关系测试
测试场景：产品组合关系业务流程测试
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
        file = open(rootPath + '/data/ProductCombination_BatchEditing.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def importFile(self):

        global results
        file = open(rootPath + '/data/ProductCombination_BatchEditing.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['importFile']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '产品组合关系—批量编辑'
        # 脚本标识－ID
        self.script_id = 'ProductCombination_BatchEditing'
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
        qw = self.importFile()

        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
       # self.login('Vic_cn','123')

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

        sleep(3)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(3)

        # 定位到产品组合关系
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品组合关系')]").click()

        sleep(3)

        # 定位到产品组合关系批量编辑
        self.driver.find_element_by_xpath("//*[@id='ProductCombinationView']//span[@class='x-btn-icon-el fa fa-fw fa-pencil-square ']").click()

        sleep(3)

        # 定位到数据文件
        self.driver.find_element_by_xpath("//*[@id='ProductSpecialityNotifiedFormWinID-body']//input[@name='main.importFile']").click()

        sleep(3)

        # 定位到文件选择器
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID-body']//input[@name='keywords']").send_keys(qw[0])

        sleep(3)

        # 定位到查询
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID-body']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        _elementFirst = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(1)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(3)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='ProductSpecialityNotifiedFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='DataImportGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='DataImportView']//span[contains(@class, 'fa-file-text-o')]").click()

        sleep(2)

        self.driver.find_element_by_link_text('是').click()

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.x-box-mc'))
            )

        except IOError as a:
            print("找不元素 " + a)

        # 获取弹窗提示：
        # self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='DataImportGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        ul = self.driver.find_elements_by_xpath("//*[@id='DataImportFormPanelID-v-body']//td[contains(@class, 'x-form-display-field-body')]")[9]

        print(ul.text)

        sleep(3)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面


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