import unittest
from cgitb import text
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


#未完任务:
        # 1. 上一个脚本对这个脚本的传值以及数值传送.
        # 2. 搜索确定的某个待审批任务.
        # 3. 利用print来写脚本运行日志,并且输出出错信息.
        # 4. 反审等功能需要再确定.
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
        self.login('carla','123')

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        sleep(1)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        self.dr.find_element_by_xpath("//*[@id='west-panel']//span[contains(text(), '发货确认')]").click()  # 定位到订单发货计划


        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='centerTabPanel']//span[contains(text(), '订单发货确认')]").click()  # 防止我的桌面跳出打断进程

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingConfirmationGridPanelID-body']//span[contains(text(), '审批中')]").click()  # 选择第一条的服务商名称

        self.dr.find_element_by_xpath("//*[@id='centerTabPanel-body']//span[contains(text(), '编辑')]").click()  # 确定

        self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(text(), '通过')]").click()  # 点击通过任务

        sleep(1)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        #船务审批流程结束,采购经理审批

        self.login('Jack.L', '123')

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据

        sleep(1)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()

        self.dr.find_element_by_xpath("//*[@id='west-panel']//span[contains(text(), '发货确认')]").click()  # 定位到订单发货计划

        sleep(1)
        self.dr.find_element_by_xpath(
            "//*[@id='centerTabPanel']//span[contains(text(), '订单发货确认')]").click()  # 防止我的桌面跳出打断进程

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingConfirmationGridPanelID-body']//span[contains(text(), '审批中')]").click()  # 选择第一条的服务商名称

        self.dr.find_element_by_xpath("//*[@id='centerTabPanel-body']//span[contains(text(), '编辑')]").click()  # 确定

        self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingConfirmationForm']//span[contains(text(), '通过')]").click()  # 点击通过任务

        sleep(1)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
