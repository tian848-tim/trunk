'''
测试用例标题：发货确认测试
测试场景：发货确认业务流程测试——采购经理拒绝
创建者：Tim
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
from cgitb import text, handler
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest,configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import json
import random

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')


'''
测试用例
'''



class FlowOrderShippingApply(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_ShippingClass_ordershippingapply_FlowOrderShippingApply_reject.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_ShippingClass_ordershippingapply_FlowOrderShippingApply_reject.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '订单发货确认——采购经理拒绝'
        # 脚本标识－ID
        self.script_id = 'FlowOrderShippingApply_reject'
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






    def test_FlowOrderShippingApply(self):

        su = self.loadvendername()
        ad = self.loadvendernames()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('carla','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到船务类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        sleep(3)

        # 定位到订单发货确认
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '订单发货确认')]").click()

        sleep(2)

        # 定位到订单发货确认新建
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位添加订单信息按钮'''
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        if ad[0] != '':
            # 点击确认
             self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//input[contains(@name,'keywords')]").send_keys(ad[0])

             sleep(2)

            # 点击确认
             self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//span[contains(@class,'fa-search')]").click()

             _elementFiveth = (random.randint(0, 0))

             # 定位订单第一条记录
             _elementSecond = self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

             sleep(2)

             # 在此元素上双击
             ActionChains(self.driver).double_click(_elementSecond).perform()

        else:
            _elementFiveth = (random.randint(0, 10))

            # 定位订单第一条记录
            _elementSecond = self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//tr[@data-recordindex={}]".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class,'fa-play')]").click()

        self.driver.implicitly_wait(30)
        # 获取弹窗提示：
        self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(10)



        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        if self.is_alert_present():

         alert = self.driver.switch_to_alert()

         alert.accept()  # 退出页面

        else:
            pass


        sleep(5)

        self.login(su[1][0], su[1][1])

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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

        # 定位iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationMainTabsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        # 点击拒绝
        self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class, 'fa-window-close')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('是').click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        if self.is_alert_present():

         alert = self.driver.switch_to_alert()

         alert.accept()  # 退出

        else:
              pass

        sleep(5)

        if handler.lower()=='carla':

            self.login('Jack.L', '123')

            sleep(5)


            # 关闭弹出框
            self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

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

            # 定位iframe
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationMainTabsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

            sleep(2)

            # 输入内容
            self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

            sleep(2)

            # 退出iframe
            self.driver.switch_to.default_content()

            # 点击拒绝
            self.driver.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class, 'fa-window-close')]").click()

            sleep(3)

            self.driver.find_element_by_link_text('是').click()

            sleep(2)

        else:
            self.driver.quit()

    def isElementExist(self, link):
        flag = True

        try:
            self.driver.find_element_by_xpath(link)

            print('元素找到')
            return flag
        except:
            flag = False
            print('未找到')
            return flag



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
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

