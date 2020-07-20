'''
测试用例标题：采购合同测试
测试场景：采购合同业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-18
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
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import random
import datetime


'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')
'''
测试用例
'''

class purchaseContract(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购合同'
        # 脚本标识－ID
        self.script_id = 'test_flow_purchase_contract'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(15)
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get('http://192.168.1.109:880/')  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_PurchaseContract(self):
        self.login('Sophia','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)



        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        sleep(2)


        ul = self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID']/div[2]/div/div/div")

        lis = ul.find_elements_by_xpath('div')

        sleep(2)

        print(type(lis))

        print(lis)


        for  i in  lis :

            #u = i.unicode('utf-8')

            if i == '当前处理人':

               print (i)

        sleep(2)

        print('123')



        first_category = lis[random.randint(0, len(lis) - 1)]

        print(len(lis))

        print(first_category)

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        print(datetime.datetime.now())


        print(time.strftime("%Y-%m-%d %H:%M:%S"))

        try:
            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]//span[contains(text(), '{}')]".format('调整申请')).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("经理元素存在")
        elif a == False:
            print("经理元素不存在")

        print(a)



        sleep(2)

    def isElementExist(self):

        try:

            sleep(10)

            self.driver.find_element_by_link_text('Vic_cn')

            return True

        except:

                return False

    #print(isElementExist(self))



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
