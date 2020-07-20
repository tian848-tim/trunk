'''
测试用例标题：采购合同测试
测试场景：采购合同业务流程测试——采购组长退回——采购员重新发启
创建者：Tim
创建日期：2018-10-18
最后修改日期：2018-10-18
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
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''

class purchaseContract(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")
    
    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购合同'
        # 脚本标识－ID
        self.script_id = 'test_flow_purchase_contract'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(15)
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


    def test_PurchaseContract(self):
        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购合同
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        sleep(2)

        # 定位到采购合同新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        # 定位到采购计划列表新建
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//span[contains(text(), '采购计划列表')]").click()

        sleep(2)

        # 定位采购计划第一条记录
        _elementFirst = self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinGridPanelID-body']//div[contains(text(), '1')]")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 点击确认
        self.driver.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位供应商产品分类
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-formTable']//input[@name='main.vendorProductCategoryAlias']").click()

        sleep(2)

        # 选择分类
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

        sleep(2)

        # 定位联系人名称
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-formTable']//input[@name='main.sellerContactCnName']").click()

        sleep(2)

        # 选择联系人
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class,'x-boundlist-item-over')]").click()

        sleep(3)

        # 完货日期
        self.driver.find_element_by_xpath( "//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.readyDate']").click()

        sleep(2)

        # 订单日期
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.orderDate']").click()

        sleep(2)

        # 预计发货时间
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.etd']").click()

        sleep(2)

        # 预计发货时间
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.eta']").click()

        sleep(2)

        # 货柜类型
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.containerType']").click()

        sleep(2)

        # 开船前#20GP
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '20')]").click()

        sleep(2)

        # 出货港口
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.originPortId']").click()

        sleep(2)

        # 宁波
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '宁波')]").click()

        sleep(2)

        # 尾款条
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.balancePaymentTerm']").click()

        sleep(2)

        # 开船前
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '开船前')]").click()

        sleep(2)

        # 点击发启
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class,'fa-play')]").click()

        sleep(8)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)


        self.login('Vic_cn', '123')

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
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//iframe[contains(@class,'cke_wysiwyg_frame cke_reset')]"))

        sleep(2)

        # 输入退回内容
        self.driver.find_element_by_class_name("cke_show_borders").send_keys('test')

        sleep(2)

        # 退出iframe
        self.driver.switch_to.default_content()

        sleep(2)

        # 定位到退回按钮
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class,'fa-reply')]").click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        sleep(2)


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出


        sleep(2)

        '''重新发启'''

        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购合同申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        sleep(2)

        # 选择采购计划第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购计划编辑
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(2)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        sleep(2)


        self.driver.find_element_by_link_text('是').click()

        alert = self.driver.switch_to_alert()

        alert.accept()  # 退出


        sleep(2)

        '''采购组长审核'''

        self.login('Vic_cn','123')
        sleep(5)

        # 关闭弹出框
        self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        sleep(2)

        # 定位到申请单据
        self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

        sleep(2)

        # 定位到采购合同申请
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()

        sleep(2)

        # 选择采购计划第一条记录
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()

        sleep(2)

        # 定位到采购计划编辑
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-pencil-square-o')]").click()

        sleep(2)

        # 判断是否需要分配处理人

        if self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").is_displayed():  # 分配处理人

            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

            self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()  # 选择Jack.L

            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        else:

            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)

        # 获取当前节点处理人

        handler = self.driver.find_element_by_xpath("//div[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[34]/div").text

        print(handler)

        self.driver.find_element_by_link_text('注销').click()  # 点击注销

        self.driver.find_element_by_link_text('是').click()

        if self.is_alert_present():

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出

        else:
            pass

        sleep(2)

        if handler == 'Jack.L':

            self.login('Jack.L', '123')

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
            self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()

            sleep(5)

        else:
            pass

        #会计审核

        self.login('emma', '123')

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
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()

        sleep(2)

        # 选择dickson
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'dickson')]").click()

        sleep(2)

        # 点击通过
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(2)

        # 点击注销
        self.driver.find_element_by_link_text('注销').click()

        sleep(2)

        self.driver.find_element_by_link_text('是').click()

        if self.is_alert_present():

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出

        else:
            pass

        sleep(2)

        # dickson审批

        self.login('dickson', '123')

        sleep(8)

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
        self.driver.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()

        sleep(5)

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

    if __name__ == "__main__":
        unittest.main()
