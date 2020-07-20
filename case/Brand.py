'''
测试用例标题：品牌管理
测试场景：品牌管理流程测试
创建者：Tim
创建日期：2019-9-17
最后修改日期：2019-9-17
输入数据：
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time, unittest, configparser
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


class Refund(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/Brand.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '品牌管理'
        # 脚本标识－ID
        self.script_id = 'Brand'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_flow_balance_refund(self):

        su = self.loadvendername()

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
            print("系统提示元素存在")
        elif a == False:
            print("系统提示元素不存在")

        print(a)

        if a == True:

           # 关闭弹出框
           self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        else:
            pass

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-file-o')]").click()

        sleep(2)

        # 定位到产品资料
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '产品资料')]").click()

        sleep(3)

        # 定位到品牌管理
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '品牌管理')]").click()

        sleep(2)

        # 定位到新建
        self.driver.find_element_by_xpath("//*[@id='BrandView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        #随机英文
        _T = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        _elementFirst = (random.choice(_T))

        #随机数字
        _elementFiveth = (random.randint(0, 1000))

        # 选择品牌名
        self.driver.find_element_by_xpath("//*[@id='BrandForm-body']//input[@name='main.brandName']").send_keys(_elementFirst,_elementFirst,_elementFiveth)

        sleep(2)

        #代理
        self.driver.find_element_by_xpath("//*[@id='BrandForm-body']//input[@name='main.isAgency']").click()

        sleep(2)

        #随机选择
        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(0, len(lis) - 1)]

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        sleep(2)

        # 定位添加订单信息按钮'''
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='BrandViewFormPanelID-body']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        ActionChains(self.driver).double_click(_elementFirst).perform()

        #搜索框获取当前条数，随机选择
        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        _elementFiveth = (random.randint(1, len(lis)))

        _elementFirst = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']//tr[@data-recordindex='{}']".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        #确定
        self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        #保存
        self.driver.find_element_by_xpath("//*[@id='BrandForm']//span[contains(@class,'fa-save')]").click()


        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
