'''
测试用例标题：安检申请流程
测试场景：安检申请流程正常审批——安检经理退回
创建者：Tim
创建日期：2018-10-30
最后修改日期：2018-10-29
输入数据：审批流程各个角色账号
输出数据：无

'''


# -*- coding: utf-8 -*-
import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, configparser
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
class complianceApply(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_QCGM_return.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_QCGM_return.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    def skuname(self):
        global name
        file = open(rootPath + '/data/workflow_CheckClass_complianceApply_FlowComplianceApply_QCGM_return.json', encoding='utf-8')
        data = json.load(file)
        name = [(d['name']) for d in data['skuname']]

        return name

    def setUp(self):
        #脚本标识-标题
        self.script_name ='安检申请流程正常审批——安检经理退回'
        #脚本标识-ID
        self.script_id ='workflow_CheckClass_complianceApply_FlowComplianceApply_QCGM_return'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            #如果使用最新的foxfire 需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
                # 如果使用最新firefox需要使用下面这句
                self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        #定义登录方法
    def login(self, username, password):
            self.driver.get(self.target_url)#d登录页面
            self.driver.find_element_by_id("account-inputEl").send_keys(username)
            self.driver.find_element_by_id("password-inputEl").send_keys(password)
            self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

    def test_flow_compliance_apply(self):

            su = self.loadvendername()
            ad = self.loadvendernames()
            sku = self.skuname()
            for i in range(0, len(su)):
                    print(su[0][0])
                    print(su[0][1])
            self.login(su[0][0], su[0][1])

            # self.login('Vic_cn','123')

            sleep(5)

            '''点击新增安检申请流程'''

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
                    self.driver.find_element_by_xpath(
                            "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            else:
                    pass

            sleep(2)

            # 点击申请单据
            self.driver.find_element_by_xpath(
                    "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(3)

            # 点击检验类
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'检验类')]").click()

            sleep(3)

            # 点击安检申请
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'安检申请')]").click()

            sleep(2)

            # 点击安检申请新建按钮
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            '''选择供应商'''

            # 点击供应商名称输入框
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementViewFormPanelID']//input[@name='main.vendorName']").click()

            sleep(2)

            print(ad[0])

            if ad[0] != '':

                    print(1)

                    # 在关键字输入框录入‘飞亚家具有限公司’
                    self.driver.find_element_by_xpath(
                            "//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                    sleep(2)

                    # 点击查询按钮
                    self.driver.find_element_by_xpath(
                            "//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                    sleep(2)

                    # 定位到查询结果第一个元素
                    _elementFrist = self.driver.find_element_by_xpath(
                            "//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(),'1')]")

                    sleep(2)

                    # 点击双击
                    ActionChains(self.driver).double_click(_elementFrist).perform()

            else:
                    _elementFiveth = (random.randint(1, 10))

                    # 定位到查询结果第一个元素
                    _elementFrist = self.driver.find_element_by_xpath(
                            "//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                    sleep(2)

                    # 点击双击
                    ActionChains(self.driver).double_click(_elementFrist).perform()

            '''添加SKU'''

            sleep(2)

            # 点击添加产品‘+’按钮
            _elementSecond = self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 点击双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

            sleep(2)

            if sku[0] != '':

                    # 在关键字输入框录入‘BFRAME-E-TRUN’
                    self.driver.find_element_by_xpath(
                            "//*[@id='ProductDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(
                            sku[0])

                    sleep(2)

                    # 点击查询按钮
                    self.driver.find_element_by_xpath(
                            "//*[@id='ProductDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                    sleep(2)

                    # 点击选择第一条记录
                    _elementThird = self.driver.find_element_by_xpath(
                            "//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                    sleep(2)

                    # 点击双击
                    ActionChains(self.driver).double_click(_elementThird).perform()

                    sleep(2)

            else:
                    sleep(2)

                    # 点击选择第一条记录
                    _elementThird = self.driver.find_element_by_xpath(
                            "//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                    sleep(2)

                    # 点击双击
                    ActionChains(self.driver).double_click(_elementThird).perform()

                    sleep(2)

            # 点击确认
            self.driver.find_element_by_xpath(
                    "//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

            '''添加附件'''

            sleep(2)

            # 顶级添加附件# ‘+’按钮
            _elementFifth = self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementViewGridPanelID-MyDocumentMultiGridPanelID_header-targetEl']//img[contains(@class,' x-tool-plus')]")

            sleep(2)

            # 点击双击
            ActionChains(self.driver).double_click(_elementFifth).perform()

            sleep(2)

            # 点击选择第一条记录
            _elementSixth = self.driver.find_element_by_xpath(
                    "//*[@id='FilesDialogWinGridPanelID']//div[contains(text(),'1')]")

            sleep(2)

            # 点击双击
            ActionChains(self.driver).double_click(_elementSixth).perform()

            sleep(2)

            # 定位到确认按钮
            self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID']//span[contains(@class,'fa-check')]").click()

            sleep(3)

            # 定位到发启按钮
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementForm']//span[contains(@class,'fa-play')]").click()

            self.driver.implicitly_wait(30)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            sleep(5)

            '''退出系统'''
            # 点击注销退出系统
            self.driver.find_element_by_link_text("注销").click()

            # 点击退出提示的‘是’
            self.driver.find_element_by_link_text("是").click()

            alert = self.driver.switch_to_alert()
            # 退出页面
            alert.accept()
            sleep(5)

            '''第二节点审批'''

            self.login(su[1][0], su[1][1])
            # self.login('becky', '123')

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
                    self.driver.find_element_by_xpath(
                            "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            else:
                    pass

            sleep(2)

            # 点击工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

            sleep(2)

            # 点击第一条记录（如果有多条待办任务时，这种定位方法是不行的）
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(),'1')]").click()

            sleep(2)

            # 点击马上处理1
            self.driver.find_element_by_xpath(
                    "//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            # 点击分配处理人
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementViewMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()

            sleep(2)

            # 点击选择处理人‘Linda_cn’
            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'Linda_cn')]").click()

            sleep(2)

            # 点击领取
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementForm']//span[contains(@class,'fa-eye')]").click()

            sleep(5)

            # 点击领取弹出框的‘是’
            self.driver.find_element_by_link_text("是").click()

            # self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementForm']//span[contains(text(), '是')]").click() #点击确认领取
            sleep(5)

            '''第三个节点审批：添加安检报告'''

            # 点击工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到相关报告
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'相关报告')]").click()

            sleep(2)

            # 点击产品安检报告
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品安检报告')]").click()

            sleep(2)

            # 点击新建产品安检报告
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            # 点击应用ID
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceFormPanelID-body']//input[@name='main_businessId']").click()

            sleep(2)

            # 点击选择第一条记录
            _elementSeventh = self.driver.find_element_by_xpath(
                    "//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(),'1')]")

            sleep(2)

            # 点击双击选中第一条记录
            ActionChains(self.driver).double_click(_elementSeventh).perform()

            sleep(2)

            # _elementFiveth = (random.randint(0, 10000))

            # sleep(2)

            # 定位到报告标题
            # self.driver.find_element_by_xpath("//*[@id='ReportProductComplianceFormWinID']//input[@name='main.title']").send_keys(_elementFiveth)

            # sleep(2)

            # _elementFiveth = (random.randint(0, 10000))

            # sleep(2)

            # 定位到报告标题
            # self.driver.find_element_by_xpath("//*[@id='ReportProductComplianceFormWinID']//input[@name='main.serialNumber']").send_keys(_elementFiveth)

            sleep(2)

            # 点击生成标题
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceFormPanelID-body']//span[contains(text(),'生成标题')]").click()

            # sleep(2)
            # self.driver.find_element_by_xpath("//*[@id='ReportProductComplianceFormPanelID-body']//div[contains(@class,'x-form-trigger-first')]").click()#点击选择报告报告日期
            # 点击选择报告时间
            # self.driver.find_element_by_xpath("//*[@id='ReportProductComplianceFormPanelID-body']//input[@name='main.reportTime']").send_keys('2018-07-31')

            sleep(2)

            # 点击第一个sku
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceFormPanelID-body']//div[contains(text(),'1')]").click()

            sleep(2)

            # 点击风控级别
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceFormPanelID-body']//input[@name='products[0].cplRiskRating']").click()

            sleep(2)

            # 选择五抽一
            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'黄')]").click()

            sleep(5)

            # 点击保存
            self.driver.find_element_by_xpath(
                    "//*[@id='ReportProductComplianceFormWinID']//span[contains(@class,'fa-save')]").click()

            self.driver.implicitly_wait(30)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            sleep(5)

            '''第三个节点审批'''

            # 点击工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到我的消息
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'我的消息')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

            sleep(2)

            # 点击第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(),'1')]").click()

            sleep(2)

            # 点击马上处理2
            self.driver.find_element_by_xpath(
                    "//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            # 点击通过
            self.driver.find_element_by_xpath(
                    "//*[@id='FlowComplianceArrangementForm']//span[contains(@class,'fa-check-square')]").click()

            self.driver.implicitly_wait(30)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            sleep(5)

            # 点击注销退出系统
            self.driver.find_element_by_link_text("注销").click()

            # 点击退出提示的‘是’
            self.driver.find_element_by_link_text("是").click()

            alert = self.driver.switch_to_alert()
            # 退出页面
            alert.accept()
            sleep(5)

            '''第四个节点审批'''

            self.login(su[2][0], su[2][1])

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
                    self.driver.find_element_by_xpath(
                            "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            else:
                    pass

            sleep(2)

            # 点击工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)
            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

            sleep(2)

            #$self.driver.find_element_by_xpath("//*[@id='EventsView']//span[contains(text(),'fa-refresh')]").click()#点击刷新按钮
            # 点击第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(),'1')]").click()

            sleep(2)

            # 点击马上处理3
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            # 定位iframe
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementViewMainTbsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

            sleep(2)

            # 输入退回内容
            self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

            sleep(2)

            # 退出iframe
            self.driver.switch_to.default_content()

            sleep(2)

            #定位退回按钮
            self.driver.find_element_by_xpath("//*[@id='FlowComplianceArrangementForm']//span[contains(@class, 'fa-reply')]").click()


            sleep(5)

            # 点击注销
            self.driver.find_element_by_link_text('注销').click()

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面


    def tearDown(self):
            self.driver.quit()


if __name__== '__main__':
        # complianceApply.base_url='http://192.168.1.118:880'
        unittest.main()