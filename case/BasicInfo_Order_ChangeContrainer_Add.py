'''
测试用例标题：新增装柜信息变更
测试场景：新增装柜信息变更
创建者：Tim
创建日期：2018-11-26
最后修改日期：2
输入数据：
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
from selenium.webdriver.common.action_chains import ActionChains
import  random
import linecache
import json
'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class ADD(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/BasicInfo_Order_ChangeContrainer_Add.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '装柜信息变更'
        # 脚本标识－ID
        self.script_id = 'BasicInfo_Order_ChangeContrainer_Add'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_BasicInfo_Order_ChangeContrainer_Add(self):
        try:
            su = self.loadvendername()
            for i in range(0, len(su)):
                print(su[i][0])
                print(su[i][1])
            self.login(su[0][0], su[0][1])
            #self.login('carla','123')
            sleep(5)
            try:
                self.driver.find_element_by_xpath(
                    "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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
            #定位到资料档案
            self.driver.find_element_by_xpath("//*[@id='__nortPanel-innerCt']//span[contains(text(),'资料档案')]").click()
            sleep(2)
            # 定位到订单资料
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'订单资料')]").click()
            sleep(2)
            # 定位到装柜变更
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'装柜信息变更')]").click()
            sleep(2)
            # 定位到新建
            self.driver.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(@class,'fa-plus')]").click()
            sleep(2)
            #定位到订单号
            self.driver.find_element_by_xpath("//*[@id='ChangeContrainerViewFormPanelID']//input[@name='orderNumber']").click()
            sleep(2)

            _elementFiveth = (random.randint(1, 10))
            #定位到第一条订单
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-center-body']//div[text()='{}']".format(_elementFiveth))



            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            # 输入新装柜编号
            self.driver.find_element_by_xpath("//*[@id='ChangeContrainerForm-body']//input[@name='main.newContainerNumber']").send_keys('636')

            sleep(2)

            # 输入新装柜编码
            self.driver.find_element_by_xpath("//*[@id='ChangeContrainerViewFormPanelID-body']//input[@name='main.newSealsNumber']").send_keys('WWQ')

            sleep(2)
            # 定位到保存按钮
            self.driver.find_element_by_xpath("//*[@id='ChangeContrainerForm']//span[contains(@class,'fa-save')]").click()
            sleep(2)
        except NoSuchElementException as e:
            raise
            print(e)
            return False


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