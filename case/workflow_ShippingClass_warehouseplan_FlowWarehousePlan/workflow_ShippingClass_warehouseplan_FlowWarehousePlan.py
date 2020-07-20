'''
测试用例标题：送仓计划测试
测试场景：送仓计划业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-11-12
最后修改日期：2018-11-12
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

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''



class FlowWarehousePlan(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_ShippingClass_warehouseplan_FlowWarehousePlan.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_ShippingClass_warehouseplan_FlowWarehousePlan.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '送仓计划'
        # 脚本标识－ID
        self.script_id = 'workflow_ShippingClass_warehouseplan_FlowWarehousePlan'
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


    def test_FlowWarehousePlan(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('carla','123')
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

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到送仓计划
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '送仓计划')]").click()

        sleep(2)

        # 定位到送仓计划新建
        self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位添加货柜信息按钮'''
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        if ad[0] != '':

            # 点击确认
             self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinID']//input[contains(@name,'keywords')]").send_keys(ad[0])

             sleep(2)

            # 点击确认
             self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinID']//span[contains(@calss,'fa-search')]").click()

             _elementFiveth = (random.randint(0, 0))

             sleep(2)

             # 定位订单第一条记录
             _elementSecond = self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

             sleep(2)

             # 在此元素上双击
             ActionChains(self.driver).double_click(_elementSecond).perform()

        else:

            ul = self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            print(len(lis))

            sleep(2)

            _elementFiveth = (random.randint(1, len(lis)))

            sleep(2)

            _elementFirst = self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinGridPanelID']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()


        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='PackingListDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        ## 定位货仓
        self.driver.find_element_by_xpath( "//*[@id='FlowWarehousePlanningFormPanelID']//input[@name='warehouse']").click()

        try:
            WebDriverWait(self.driver,120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="WarehouseDialogWinGridPanelID-body"]//div[contains(text(), "1")]'))
            )

        except IOError as a:
            print("找不元素 " + a)

        ul = self.driver.find_element_by_xpath("//*[@id='WarehouseDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        _elementFiveth = (random.randint(1, len(lis)))

        sleep(2)

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='WarehouseDialogWinID']//div[text()='{}']".format(_elementFiveth))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        # 输入起始
        self.driver.find_element_by_xpath("//*[@class='x-form-trigger-input-cell']//input[@name='main.receiveStartDate']").click()

        sleep(2)

        # 输入结束
        self.driver.find_element_by_xpath("//*[@class='x-form-trigger-input-cell']//input[@name='main.receiveEndDate']").click()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 判断流程
        _prompt = '操作提示流程已启动'

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第一节点审核'''

        self.login(su[1][0],su[1][1])
        #self.login('carla', '123')

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        #self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择Jack.L
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()

        #sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowWarehousePlanningForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = '操作提示操作成功！'

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面




    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
