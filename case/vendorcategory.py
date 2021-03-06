'''
测试用例标题：供应商分类测试
测试场景：供应商分类业务流程测试
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

import time,unittest,configparser
from time import sleep
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
        file = open(rootPath + '/data/vendorcategory.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建供应商分类'
        # 脚本标识－ID
        self.script_id = 'vendorcategory'
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

        # 定位到供应商分类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(@class,'node-text')]").click()

        sleep(3)

        # 定位到供应商分类第一条记录
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewTreePanelId-body']//div[contains(text(),'1')]").click()

        sleep(3)

        # 定位到新建供应商按钮
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewPanelID']//span[contains(@class,'fa-plus')]").click()

        sleep(3)

        # 定位到中文名称
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId-body']//input[@name='main.cnName']").clear()

        sleep(3)

        _elementFiveth = (random.randint(0, 100))

        sleep(2)

        # 定位到中文名称测试
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId-body']//input[@name='main.cnName']").send_keys('测试',_elementFiveth)

        sleep(2)

        # 定位到英文名称测试
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId-body']//input[@name='main.enName']").clear()

        sleep(2)

        _T="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        _elementFiveth = (random.choice(_T))

        _S = (random.choice(_T))

        sleep(2)

        # 定位到英文名称测试
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId-body']//input[@name='main.enName']").send_keys(_elementFiveth,_S)

        sleep(2)

        # 定位到选择叶子
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId']//input[@id='main.status-1-inputEl']").click()

        sleep(6)

        # 定位到选择叶子
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryViewFormPanelId']//input[@id='main.leaf-1-inputEl']").click()

        sleep(6)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryFormWinID']//span[contains(@class,'fa-save')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(60)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(3)


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

