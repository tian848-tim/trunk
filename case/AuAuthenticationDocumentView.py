'''
测试用例标题：澳洲认证档案测试
测试场景：澳洲认证档案业务流程测试
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
        file = open(rootPath + '/data/AuAuthenticationDocumentView.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '澳洲认证档案'
        # 脚本标识－ID
        self.script_id = 'AuAuthenticationDocumentView'
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

        #self.login('admin','123')

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

        # 定位到服务商
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'服务商')]").click()

        sleep(3)

        # 定位到服务商档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'澳洲认证档案')]").click()

        sleep(3)

        # 定位到服务商档案新建
        self.driver.find_element_by_xpath("//*[@id='AuAuthenticationDocumentView']//span[contains(@class,'fa-plus')]").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到服务商编码
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//input[@name='main.code']").send_keys("DFG",_elementFiveth)

        sleep(3)

       ## 定位到服务商类别
       #self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID-body']//input[@name='main.categoryName']").click()

       #sleep(3)

       #_T = (random.randint(0, 3))

       ## 定位到服务商类别
       #self.driver.find_element_by_xpath("//*[@id='ServiceProviderCategoryDialogWinTreePanelId-body']//tr[@data-recordindex={}]".format(_T)).click()

       #sleep(2)

       ## 定位确认
       #self.driver.find_element_by_xpath("//*[@id='ServiceProviderCategoryDialogWinID']//span[contains(@class,'fa-check')]").click()

       #sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到公司中文名
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//input[@name='main.cnName']").send_keys("测试",_elementFiveth)

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到公司英文名
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//input[@name='main.enName']").send_keys("DFXC",_elementFiveth)

        sleep(3)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到公司地址
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//input[@name='main.address']").send_keys("地址",_elementFiveth)

        sleep(3)

        # 定位到服务商来源
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//input[@name='main.source']").click()

        sleep(3)


        # 定位到服务商来源
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'互联网')]").click()

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ServiceProviderDocumentFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(8)



    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):#
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
