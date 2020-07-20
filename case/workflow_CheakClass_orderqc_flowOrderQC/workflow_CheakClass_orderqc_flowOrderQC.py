'''
测试用例标题：订单质检测试
测试场景：订单质检业务流程测试
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

import  json

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

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global results
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results

    # 判断当前语言
    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC.json',
                    encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_CheakClass_orderqc_flowOrderQC.json',
                    encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '订单质检'
        # 脚本标识－ID
        self.script_id = 'workflow_CheakClass_orderqc_flowOrderQC'
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

        su = self.loadvendername()
        ad = self.loadvendernames()
        cn = self.CN()
        en = self.EN()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])

        #self.login('Vic_cn','123')
        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[0])).click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[1])).click()

        sleep(2)

        # 定位第一条记录
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionGridPanelID-body']//div[contains(text(), '1')]").click()

        #sleep(2)

        # 定位到订单质检申请新建
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class,'fa-pencil-square-o')]").click()

        # 定位到订单质检申请新建
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择供应商
        self.driver.find_element_by_xpath( "//*[@id='FlowOrderQualityInspectionFormPanelID']//input[@name='main.vendorName']").click()

        sleep(2)

        print(ad[0])

        if ad[0] != '' :

               ## 定位到关键字
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

               sleep(2)

               # 点击搜索
               self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

               sleep(2)

               # 定位供应商第一条记录
               _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

               sleep(2)

               # 在此元素上双击
               ActionChains(self.driver).double_click(_elementFirst).perform()

        else:

            _elementFiveth = (random.randint(1, 20))

            # 定位供应商第一条记录
            _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        ## 选择订单列表
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionFormPanelID-body']//input[@name='main.orderNumber']").click()

        sleep(2)

        # 检查元素是否存在
        _NoData = self.driver.find_element_by_xpath("//div[@id='OrderDialogWinGridPanelID-body']/div").text

        if _NoData == lg[3]:

        #try:
            #self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
            a = True
        else:
            a = False

        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        sleep(2)

        while (a == True) :

            # 订单编号
            self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//img[contains(@class,'x-tool-close')]").click()

            sleep(2)

            ## 选择供应商
            self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionFormPanelID']//input[@name='main.vendorName']").click()

            sleep(2)

            print(ad[0])

            if ad[0] != '':

                ## 定位到关键字
                self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys(ad[0])

                sleep(2)

                # 点击搜索
                self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

                sleep(2)

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            else:

                _elementFiveth = (random.randint(1, 20))

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            ## 选择订单列表
            self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionFormPanelID-body']//input[@name='main.orderNumber']").click()

            sleep(2)

            # 检查元素是否存在
            _NoData = self.driver.find_element_by_xpath("//div[@id='OrderDialogWinGridPanelID-body']/div").text

            if _NoData == lg[3]:

                # try:
                # self.driver.find_element_by_xpath("//*[@id='OrderDialogWinID']//div[contains(text(),'{}')]".format('没有数据！')).is_displayed()
                a = True
            else:
                a = False

            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")


        ul = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        _elementFiveth = (random.randint(1, len(lis)))

        _elementFirst = self.driver.find_element_by_xpath("//*[@id='OrderDialogWinGridPanelID']//div[text()='{}']".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(3)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class,'fa-play')]").click()

        # 点击发启
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class,'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[4]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        # 点击注销
        self.driver.find_element_by_link_text(lg[6]).click()


        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第二节点'''

        self.login(su[0][0], su[0][1])
        #self.login('sunny_cn', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择Vic
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '{}')]".format(su[0][0])).click()

        sleep(2)


        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)



        '''第三节点'''

        self.login(su[1][0], su[1][1])
        #self.login('sunny_cn', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择Vic
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Yuri')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第四节点提交报告'''
        self.login(su[2][0], su[2][1])
        #self.login('Yuri', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到相关报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[8])).click()

        sleep(2)

        # 定位订单检验报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[9])).click()

        sleep(2)

        # 定位订单检验报告新建
        self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到应用ID
        self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionFormPanelID-body']//input[@name='main_businessId']").click()

        sleep(2)

        # 定位第申请器第一条记录
        _elementFourth = self.driver.find_element_by_xpath("//*[@id='FlowOtherDialogWinGridPanelID']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)

        # 定位到报告标题
        self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionFormPanelID-body']//input[@name='main.title']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        sleep(2)


        # 定位到报告编号
        self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionFormPanelID-body']//input[@name='main.serialNumber']").send_keys(_elementFiveth)

        sleep(2)

        # 定位到报告文件
        _element =self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionFormPanelID-body']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_element).perform()

        sleep(2)

        # 定位第文件选择申请器第一条记录
        _elementFivth = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFivth).perform()

        sleep(2)

        # 定位到确认按钮
        self.driver.find_element_by_xpath("//*[@id='FilesDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='ReportOrderInspectionFormWinID']//span[contains(@class,'fa-save')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)


        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        '''第四节点通过'''
        self.login(su[2][0], su[2][1])
        #self.login('Yuri', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择Vic
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'sunny')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第五节点'''
        self.login(su[1][0], su[1][1])
        #self.login('sunny_cn', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择Vic
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Vic')]").click()

        #sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第六节点'''
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn', '123')

        sleep(5)

        lg = self.CheckLanguage()

        if lg == True:

            lg = cn

        else:

            lg = en

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

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[0])).click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[1])).click()

        sleep(2)

        # 定位关键字位置
        ul = self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionGridPanelID-body']/div/table/tbody/tr[1]")

        lis = ul.find_elements_by_xpath('td')

        for i in range(0, len(lis)):

            if su[0][0] in lis[i].text:
                print(i + 1)

                column = i + 1

                break

        sleep(2)

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(2)

        # 定位到待办事项
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

        sleep(2)

        # 定位到待办事项第一条记录
        self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 点击马上处理
        self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

        sleep(2)

        # 分配处理人
        #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择Jack
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()

        #sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        _prompt = lg[5]

        if _prompt in a:

            pass

        else:

            print("流程错误")

            self.driver.quit()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到检验类
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[0])).click()

        sleep(3)

        # 定位到订单质检申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[1])).click()

        sleep(2)

        _handler = self.driver.find_element_by_xpath(
            "//*[@id='FlowOrderQualityInspectionGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                column)).get_attribute('textContent')

        print(_handler)

        for i in range(3, len(su)):

            if su[i][0] == _handler:
                _value = su[i][0]

                break

        self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

        self.driver.find_element_by_link_text(lg[7]).click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        '''第七节点'''

        if _value == su[3][0] :

            self.login(su[3][0], su[3][1])
            #self.login('Jack.L', '123')

            sleep(5)

            lg = self.CheckLanguage()

            if lg == True:

                lg = cn

            else:

                lg = en

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

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到检验类
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[0])).click()

            sleep(3)

            # 定位到订单质检申请
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[1])).click()

            sleep(2)

            # 定位关键字位置
            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowOrderQualityInspectionGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            for i in range(0, len(lis)):

                if su[3][0] in lis[i].text:
                    print(i + 1)

                    column = i + 1

                    break

            sleep(2)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            sleep(2)

            # 判断是否需要分配处理人

            # 分配处理人
            if self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").is_displayed():

                # 分配处理人
                self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionMainTbsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

                # 选择第一项
                self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class, 'x-boundlist-item-over')]").click()

                sleep(2)

                # 点击通过
                self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

            else:

                # 点击通过
                self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

            # 点击通过
            #self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[5]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath(
                "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            sleep(2)

            # 定位到检验类
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[0])).click()

            sleep(3)

            # 定位到订单质检申请
            self.driver.find_element_by_xpath(
                "//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[1])).click()

            sleep(2)

            _handler = self.driver.find_element_by_xpath(
                "//*[@id='FlowOrderQualityInspectionGridPanelID-body']/div/table/tbody/tr[1]/td[{0}]/div".format(
                    column)).get_attribute('textContent')

            print(_handler)

            for i in range(4, len(su)):

                if su[i][0] == _handler:
                    _value = su[i][0]

                    break

            self.driver.find_element_by_link_text(lg[6]).click()  # 点击注销

            self.driver.find_element_by_link_text(lg[7]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

            sleep(5)

        if  _value == su[4][0] :


                 '''第七节点'''

                 self.login(su[4][0], su[4][1])
                 #self.login('Jack.L', '123')

                 sleep(5)

                 lg = self.CheckLanguage()

                 if lg == True:

                     lg = cn

                 else:

                     lg = en

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

                 # 定位到工作面板
                 self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

                 sleep(2)

                 # 定位到待办事项
                 self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text() = '{}']".format(lg[2])).click()

                 sleep(2)

                 # 定位到待办事项第一条记录
                 self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

                 sleep(2)

                 # 点击马上处理
                 self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

                 sleep(2)

                 # 点击通过
                 self.driver.find_element_by_xpath("//*[@id='FlowOrderQualityInspectionForm']//span[contains(@class, 'fa-check-square')]").click()

                 self.driver.implicitly_wait(60)
                 # 获取弹窗提示：
                 a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
                 print(a)

                 _prompt = lg[5]

                 if _prompt in a:

                     pass

                 else:

                     print("流程错误")

                     self.driver.quit()





    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
