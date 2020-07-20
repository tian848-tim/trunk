'''
测试用例标题：问题记录测试
测试场景：问题记录业务流程测试
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

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '问题记录'
        # 脚本标识－ID
        self.script_id = 'ProductProblem'
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
        self.login('admin','123')

        sleep(5)

        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(3)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(3)

        # 定位到产品分类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'问题记录')]").click()

        sleep(3)


        # 定位到产品分类新建
        self.driver.find_element_by_xpath("//*[@id='ProductProblemView']//span[contains(@class,'fa-plus')]").click()

        sleep(3)


        # 定位到OMS订单
        self.driver.find_element_by_xpath("//*[@id='ProductProblemFormPanelID-body']//input[@name='omsOrderIdName']").click()

        sleep(3)

        # 定位到OMS订单
        self.driver.find_element_by_xpath("//*[@id='ProductProblemFormPanelID-body']//input[@name='omsOrderIdName']").click()

        sleep(3)

        _elementFiveth = (random.randint(0, 10))

        # 定位到选择
        _N = self.driver.find_element_by_xpath("//*[@id='OmsOrderDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

        sleep(3)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='OmsOrderDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(3)

        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='ProductCategoryFormWinID']//span[contains(@class,'fa-save')]").click()

        sleep(10)



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



