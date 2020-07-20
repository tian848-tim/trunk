import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains



class purchasePlan(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(15)
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_PurchaseContract(self):
        self.login('admin','123')


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        sleep(1)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        self.dr.find_element_by_xpath("//*[@id='west-panel']//span[contains(text(), '订单发货')]").click()  # 定位到订单发货计划

        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '发货计划申请')]").click()  # 防止我的桌面跳出打断进程
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '发货计划申请')]").click()  # 防止我的桌面跳出打断进程

        self.dr.find_element_by_xpath("//*[@id='centerTabPanel-body']//span[contains(text(), '新建')]").click()  # 定位到订单发货计划

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanFormGridPanelID_header-body']//div[contains(@data-qtip, '插入')]").click()  # 定位到插入案件

        _doubleClickInsert = self.dr.find_element_by_xpath(
            "//*[@id='OrderDialogWinGridPanelID-body']//div[contains(text(), '1')]")# 定位订单发货计划第一条记录

        ActionChains(self.dr).double_click(_doubleClickInsert).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='OrderDialogWinID']//span[contains(text(), '确认')]").click()  # 确定

        self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingPlanFormPanelID-formTable']//input[@name='serviceProviderName']").click() #选择服务商名称

        self.dr.find_element_by_xpath("//*[@id='ServiceProviderQuotationDialogWinGridPanelID-body']//div[contains(text(), '1')]").click()   # 选择第一条的服务商名称

        self.dr.find_element_by_xpath("//*[@id='ServiceProviderQuotationDialogWinID']//span[contains(text(), '确认')]").click()  # 确定

        #self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingPlanGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择第一条的服务商名称

        self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingPlanForm']//span[contains(text(), '发启')]").click()  # 点击发启按钮

        sleep(1)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面







        sleep(3)

        self.login('carla', '123')  # Carla审批

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据

        sleep(1)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        self.dr.find_element_by_xpath("//*[@id='west-panel']//span[contains(text(), '订单发货')]").click()  # 定位到订单发货计划
        sleep(1)
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '发货计划申请')]").click()  # 防止我的桌面跳出打断进程
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '发货计划申请')]").click()  # 防止我的桌面跳出打断进程

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择第一单申请单

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanView']//span[contains(text(), '编辑')]").click()  # 定位到编辑按键

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanForm']//span[contains(text(), '通过')]").click()  # 定位到通过按键

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(3)





        self.login('Jack.L', '123')  # Jack审批

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据

        sleep(1)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        self.dr.find_element_by_xpath("//*[@id='west-panel']//span[contains(text(), '订单发货')]").click()  # 定位到订单发货计划

        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '发货计划申请')]").click()  # 防止我的桌面跳出打断进程

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择第一单申请单

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanView']//span[contains(text(), '编辑')]").click()  # 定位到编辑按键

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingPlanForm']//span[contains(text(), '通过')]").click()  # 定位到通过按键

        sleep(3)

    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
