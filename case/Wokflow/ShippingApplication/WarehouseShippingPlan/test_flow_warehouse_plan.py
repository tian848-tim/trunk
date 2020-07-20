'''
测试用例标题：送仓计划测试
测试场景：送仓计划业务流程测试
创建者：Tom
创建日期：2018-7-25
最后修改日期：2018-7-25
输入数据：审批流程各个角色账号
输出数据：无

'''
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

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read('../../../../core/config.ini')

'''
测试用例
'''



class OrderShippingApply(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '送仓计划'
        # 脚本标识－ID
        self.script_id = 'test_flow_warehouse_plan'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.dr = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.dr = webdriver.Firefox(log_path=self.log_path)

        self.dr.implicitly_wait(15)
        self.dr.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_flow_warehouse_plan(self):
        self.login('carla','123')
        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据

        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()  # 定位到船务类

        sleep(3)

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(), '送仓计划')]").click()  # 定位到送仓计划

        self.dr.find_element_by_xpath("//*[@id='FlowWarehousePlanningView']//span[contains(@class,'fa-plus')]").click()  # 定位到送仓计划新建

        _elementFirst = self.dr.find_element_by_xpath(
            "//*[@id='FlowWarehousePlanningFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")  # 定位添加货柜信息按钮'''

        ActionChains(self.dr).double_click(_elementFirst).perform()




        _elementSecond = self.dr.find_element_by_xpath("//*[@id='PackingListDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位订单第一条记录

        ActionChains(self.dr).double_click(_elementSecond).perform()  # 在此元素上双击




        self.dr.find_element_by_xpath("//*[@id='PackingListDialogWinID']//span[contains(@class,'fa-check')]").click() #点击确认

        self.dr.find_element_by_xpath( "//*[@id='FlowWarehousePlanningFormPanelID']//input[@name='warehouse']").click() ## 定位货仓

        _elementThird = self.dr.find_element_by_xpath(
            "//*[@id='WarehouseDialogWinGridPanelID-center']//div[contains(text(), '1')]")  # 定位订单第一条记录

        ActionChains(self.dr).double_click(_elementThird).perform()  # 在此元素上双击



        self.dr.find_element_by_xpath("//*[@id='FlowWarehousePlanningForm']//span[contains(@class,'fa-play')]").click()  # 点击发启



        self.dr.find_element_by_link_text('注销').click()  # 点击注销


        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)
        '''第一节点审核'''
        self.login('carla', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click() #定位到待办事项第一条记录

        self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click() # 点击马上处理

        self.dr.find_element_by_xpath(
            "//*[@id='FlowWarehousePlanningMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

        self.dr.find_element_by_xpath(
            "//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()  # 选择Jack.L

        self.dr.find_element_by_xpath("//*[@id='FlowWarehousePlanningForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)

        '''第二点审核'''

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        self.login('Jack.L', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath(
            "//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()  # 定位到待办事项第一条记录

        self.dr.find_element_by_xpath(
            "//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()  # 点击马上处理


        self.dr.find_element_by_xpath(
            "//*[@id='FlowWarehousePlanningForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)


    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
