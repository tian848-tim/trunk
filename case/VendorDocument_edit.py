'''
测试用例标题：供应商档案测试
测试场景：供应商档案业务流程测试——编辑
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
class VendorDocument(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")


    def loadvendername(self):

        global result
        file = open(rootPath + '/data/VendorDocument_edit.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '供应商档案——编辑'
        # 脚本标识－ID
        self.script_id = 'VendorDocument_edit'
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


    def test_VendorDocument(self):
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

        # 定位到供应商档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'供应商档案')]").click()

        sleep(3)

        # 定位到新建供应商按钮第一条
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentGridPanelID-body']//div[contains(text(),'1')]").click()

        sleep(3)


        # 定位到编辑供应商按钮
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(3)

        # 定位到供应商编码
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//span[contains(@class,'x-btn-icon-el')]").click()

        sleep(3)

        # 定位到供应商分类
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.categoryName']").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 10))

        sleep(2)

        # 定位到分类
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryDialogWinID']//tr[@data-recordindex={}]".format(_elementFiveth)).click()

        sleep(2)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='VendorCategoryDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)


        # 定位到中文名称
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.cnName']").clear()

        sleep(2)


        _elementFiveth = (random.randint(0, 100))

        sleep(2)

        # 定位到中文名称
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.cnName']").send_keys('test',_elementFiveth)

        sleep(2)

        # 定位到英文名称
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.enName']").clear()

        sleep(2)

        _T="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        _elementFiveth = (random.choice(_T))

        # 定位到英文名称
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.enName']").send_keys('test',_elementFiveth)

        sleep(2)


        # 定位到定金类型
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.depositType']").click()

        sleep(3)

        # 定位到定金类型
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'百分比')]").click()

        sleep(3)

        # 定位到定金类率
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.depositRate']").clear()

        sleep(3)

        _N =random.random()

        # 定位到定金类率
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID-body']//input[@name='main.depositRate']").send_keys(_N)

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(10)

        # 定位到档案修改历史
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentTabsPanelID']//span[contains(text(),'档案修改历史')]").click()

        sleep(3)

        # 定位到档案修改历史审核
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentGridPanelID-ArchivesHistoryTabGrid-body']//div[contains(@class,'btnRowConfirm')]").click()

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='VendorDocumentFormWinID']//span[contains(@class,'fa-check')]").click()

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

