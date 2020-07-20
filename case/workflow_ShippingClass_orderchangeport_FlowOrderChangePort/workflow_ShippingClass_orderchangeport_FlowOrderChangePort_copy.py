'''
测试用例标题：订单港口变更
测试场景：订单港口变更业务流程测试——复制
创建者：Tim
创建日期：2018-11-8
最后修改日期：2018-11-8
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
from selenium.webdriver.common.action_chains import ActionChains
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
        file = open(rootPath + '/data/workflow_ShippingClass_orderchangeport_FlowOrderChangePort_copy.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_ShippingClass_orderchangeport_FlowOrderChangePort_copy.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '订单港口变更业务流程测试——复制'
        # 脚本标识－ID
        self.script_id = 'workflow_ShippingClass_orderchangeport_FlowOrderChangePort_copy'
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


    def test_CustomClearance(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        print(ad)
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn','123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到订单港口变更
        self.driver.find_element_by_xpath( "//*[@id='west-panel-targetEl']//span[contains(text(), '订单港口变更')]").click()

        sleep(2)

        # 定位到订单港口变更第一条
        self.driver.find_element_by_xpath( "//*[@id='FlowOrderChangePortViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到复制
        self.driver.find_element_by_xpath( "//*[@id='FlowOrderChangePortView']//span[contains(@class, 'fa-copy')]").click()

        sleep(2)

        # 定位到保存
        self.driver.find_element_by_xpath( "//*[@id='FlowOrderChangePortForm']//span[contains(@class, 'fa-save')]").click()

        sleep(5)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)

    def isElementExist(self, link):
        s = self.driver.find_elements_by_xpath(link)

        if s.click():

            return True
        else:

            return False

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

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
        unittest.main()
