'''
测试用例标题：新品开发测试
测试场景：新品开发申请业务流程测试——采购经理返审
创建者：Tim
创建日期：2018-7-25
最后修改日期：2018-7-25
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

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''


class NewProduct(unittest.TestCase):

    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_newproduct_flowNewProduct_Review_GM.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def loadvendernames(self):

        global result
        file = open(rootPath + '/data/workflow_PurchasingClass_newproduct_flowNewProduct_Review_GM.json', encoding='utf-8')
        data = json.load(file)
        results = [(d['name']) for d in data['use_vendorname']]

        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新品开发'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_newproduct_flowNewProduct_Review_GM'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)

        self.driver.implicitly_wait(15)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_NewProduct(self):

        su = self.loadvendername()
        ad = self.loadvendernames()

        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
        self.login(su[0][0],su[0][1])
        #self.login('Vic_cn', '123')

        # 强制等待
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

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到新品开发
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()

        sleep(2)

        # 定位到样品申请新建
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        ## 选择供应商
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewFormPanelID-body']//input[@name='main.vendorName']").click()

        sleep(2)

        if ad[0] != '':

                 # 定位到关键字
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
                sleep(2)

                _elementFiveth = (random.randint(1, 10))

             # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                sleep(2)

            # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位添加产品按钮
        _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowNewProductFormGridPanelID']//img[contains(@class,'x-tool-plus')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementSecond).perform()

        sleep(2)

        try:
             self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[text()='{}']".format('没有数据！')).is_displayed()
             a = True
        except:
            a = False
        if a == True:
            print("经理元素存在")
        elif a == False:
            print("经理元素不存在")

        while a == True:

            # 关闭
            self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//img[contains(@class, 'x-tool-close')]").click()

            sleep(2)

            ## 选择供应商
            self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewFormPanelID-body']//input[@name='main.vendorName']").click()

            sleep(2)

            if ad[0] != '':

                # 定位到关键字
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
                sleep(2)

                _elementFiveth = (random.randint(1, 10))

                # 定位供应商第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

            sleep(2)

            # 定位添加产品按钮
            _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowNewProductFormGridPanelID']//img[contains(@class,'x-tool-plus')]")

            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

            sleep(2)

            try:
                self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[text()='{}']".format('没有数据！')).is_displayed()
                a = True
            except:
                a = False
            if a == True:
                print("元素存在")
            elif a == False:
                print("元素不存在")

        else:
            pass



        # 定位样品第一条记录
        _elementThird = self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementThird).perform()

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 点击保存
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class,'fa-save')]").click()

        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        # 强制等待
        sleep(5)

        '''提交报告'''

        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn', '123')

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

        # 定位到工作面板
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

        sleep(3)

        # 定位到相关报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'相关报告')]").click()

        sleep(2)

        # 定位到产品分析报告
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品分析报告')]").click()

        sleep(2)

        # 定位到产品分析报告新建
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到应用ID
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main_businessId']").click()

        sleep(2)

        # 定位第新品开发申请器第一条记录
        _elementFourth = self.driver.find_element_by_xpath("//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFourth).perform()

        sleep(2)

        # 定位到报告文件输入框
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='reportFileDocumentName']").click()

        sleep(2)

        # 定位文件选择器第一条记录
        _elementFiveth = self.driver.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFiveth).perform()

        sleep(2)

        _elementFiveth = (random.randint(1, 1000))

        sleep(2)

        # 定位到报告标题
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.title']").send_keys('test',_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(1, 1000))

        sleep(2)

        # 定位到报告编号
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.serialNumber']").send_keys('test',_elementFiveth)

        sleep(2)

        # 报告时间
        #self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.reportTime']").send_keys('2018-06-02')

        #sleep(2)

        # 定位到保存按钮
        self.driver.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID']//span[contains(@class,'fa-save')]").click()

        # 强制等待
        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        sleep(5)

        '''发启。。。。。'''
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn', '123')

        # 强制等待
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

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到新品开发申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()

        sleep(2)

        # 选择新品开发第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewGridPanelID-body']//div[contains(text(), '1')]").click()

        # 强制等待
        sleep(2)

        # 定位到新品开发编辑
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位到发启按钮
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class,'fa-play')]").click()

        # 获取弹窗提示：
        self.driver.implicitly_wait(30)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        # 强制等待
        sleep(5)

        try:
            self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewGridPanelID-body']/div/table/tbody/tr[1]//span[contains(text(), '{}')]".format('调整申请')).is_displayed()
            a = True
        except:
            a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        sleep(2)

        if a == True:

             # 选择新品开发第一条记录
             self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewGridPanelID-body']//div[contains(text(), '1')]").click()

             # 强制等待
             sleep(2)

             # 定位到新品开发编辑
             self.driver.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class,'fa-pencil-square-o')]").click()

             sleep(2)

             self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()

             sleep(2)

             self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'{}')]".format(su[1][0])).click()

             sleep(2)

             # 定位到发启按钮
             self.driver.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class,'fa-check-square')]").click()

             # 获取弹窗提示：
             self.driver.implicitly_wait(30)
             a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
             print(a)

             # 强制等待
             sleep(5)

        else:
            pass



        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        sleep(5)

        '''第二节点审批'''

        self.login(su[1][0], su[1][1])
        #self.login('Vic_cn', '123')

        # 强制等待
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

        # 选择处理人
        #self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewMainTabsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()

        #sleep(2)

        # 选择Jack
        #self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(5)



        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        # 退出页面
        alert.accept()

        sleep(5)

        '''第三节点审批'''

        self.login(su[2][0], su[2][1])

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

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到新品开发申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()

        sleep(2)

        # 选择新品开发第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到新品开发编辑
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 定位iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowNewProductViewMainTabsPanelID-win-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入返审内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 点击返审
        self.driver.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class, 'fa-step-backward')]").click()

        sleep(3)


        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面




    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
