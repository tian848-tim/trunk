'''
测试用例标题：产品认证测试
测试场景：产品认证申请业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-11-5
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



class OrderQc(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '产品认证申请检查'
        # 脚本标识－ID
        self.script_id = 'test_flow_product_certifition'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_Order_Qc(self):
        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '检验类')]").click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '产品认证')]").click()

        sleep(2)

        # 定位到产品认证申请新建
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择供应商
        self.driver.find_element_by_xpath( "//*[@id='FlowProductCertificationFormPanelID']//input[@name='main.vendorName']").click()

        sleep(2)

        ## 定位到关键字
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys('搭')

        sleep(2)

        # 点击搜索
        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

        sleep(2)

        # 定位供应商第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加产品按钮'''
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationFormGridPanelID']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        # 定位样品第一条记录
        _elementThird = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-center']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementThird).perform()

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationForm']//span[contains(@class,'fa-play')]").click()

        sleep(10)




        self.driver.find_element_by_link_text('注销').click()  # 点击注销


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

#        '''第二节点'''
#
#        self.login('Vic_cn', '123')
#
#        sleep(5)
#
#        # 关闭弹出框
#        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()
#
#        sleep(2)
#
#        # 定位到工作面板
#        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()
#
#        sleep(2)
#
#        # 定位到待办事项
#        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()
#
#        sleep(2)
#
#        # 定位到待办事项第一条记录
#        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()
#
#        sleep(2)
#
#        # 点击马上处理
#        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()
#
#        sleep(2)
#
#        # 分配处理人
#        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()
#
#        sleep(2)
#
#        # 选择
#        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'barrycoutinho')]").click()
#
#        sleep(2)
#
#        # 点击通过
#        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationForm']//span[contains(@class, 'fa-check-square')]").click()
#
#        sleep(8)
#
#
#
#        self.driver.find_element_by_link_text('注销').click()  # 点击注销
#
#        self.driver.find_element_by_link_text('是').click()
#
#        alert = self.driver.switch_to_alert()
#
#        alert.accept()  # 退出页面
#
#        sleep(5)
#

        '''第三节点'''

        self.login('barrycoutinho', '123')

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

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择Linda
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Linda_cn')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(8)



        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第四节点提交档案'''

        self.login('Linda_cn', '123')

        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-file-o')]").click()

        sleep(2)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '产品档案')]").click()

        sleep(3)

        # 定位到产品证书档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '产品证书档案')]").click()

        sleep(2)

        # 定位到产品证书档案新建
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到应用ID
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//input[@name='main_businessId']").click()

        sleep(2)

        # 定位第申请器第一条记录
        _elementeight = self.driver.find_element_by_xpath("//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementeight).perform()

        sleep(2)

        # 定位到证书文件输入框
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//input[@name='main.fileName']").click()

        sleep(2)

        # 定位文件选择器第一条记录
        _elementseven = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementseven).perform()

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到描述
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//textarea[@name='description']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到相关标准
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//textarea[@name='relevantStandard']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到认证编号
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID']//input[@name='certificateNumber']").send_keys(_elementFiveth)

        sleep(2)

        # 生效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//input[@name='effectiveDate']").send_keys('2018-01-02')

        sleep(2)

        # 失效日期
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentViewFormPanelID-body']//input[@name='validUntil']").send_keys('2018-12-02')

        sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='ProductCertificateDocumentForm']//span[contains(@class,'fa-save')]").click()

        sleep(5)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第四节点通过'''

        self.login('Linda_cn', '123')

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

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择Vic
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'barrycoutinho')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(8)




        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第五节点'''

        self.login('barrycoutinho', '123')

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

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowProductCertificationForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(3)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面




    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
