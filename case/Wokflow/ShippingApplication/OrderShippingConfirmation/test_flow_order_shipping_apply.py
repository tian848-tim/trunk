'''
测试用例标题：发货确认测试
测试场景：发货确认业务流程测试
创建者：Tom
创建日期：2018-7-25
最后修改日期：2018-8-2
输入数据：审批流程各个角色账号
输出数据：无

'''
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
        self.script_name = '订单发货确认'
        # 脚本标识－ID
        self.script_id = 'test_flow_order_shipping_apply'
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






    def test_order_shipping_apply(self):
        self.login('carla','123')
        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath( "//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据

        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '船务类')]").click()  # 定位到船务类

        sleep(3)

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(), '订单发货确认')]").click()  # 定位到订单发货确认

        self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationView']//span[contains(@class,'fa-plus')]").click()  # 定位到订单发货确认新建

        _elementFirst = self.dr.find_element_by_xpath(
            "//*[@id='FlowOrderShippingConfirmationFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")  # 定位添加订单信息按钮'''

        ActionChains(self.dr).double_click(_elementFirst).perform()




        _elementSecond = self.dr.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位订单第一条记录

        ActionChains(self.dr).double_click(_elementSecond).perform()  # 在此元素上双击




        self.dr.find_element_by_xpath("//*[@id='OrderShippingPlanDialogWinID']//span[contains(@class,'fa-check')]").click() #点击确认


        self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class,'fa-play')]").click()  # 点击发启

        sleep(2)

        # 获取当前节点处理人

        handler = self.dr.find_element_by_xpath(
                "//div[@id='FlowOrderShippingConfirmationGridPanelID-body']/div/table/tbody/tr[1]/td[10]/div").text

        print(handler)


        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        if self.is_alert_present():

         alert = self.dr.switch_to_alert()

         alert.accept()  # 退出页面

        else:
            pass

        sleep(5)
        '''第一节点审核'''
        self.login(handler.lower(), '123')

        if OrderShippingApply.isElementExist(self,"//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]"):
            pass

        else:
         self.login(handler, '123')

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

        # 判断是否需要分配处理人



        if self.dr.find_element_by_xpath( "//*[@id='FlowOrderShippingConfirmationMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").is_displayed(): # 分配处理人

             self.dr.find_element_by_xpath( "//*[@id='FlowOrderShippingConfirmationMainTabsPanelID-win-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

             self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()  # 选择Jack.L

             self.dr.find_element_by_xpath("//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        else:
             self.dr.find_element_by_xpath(
                "//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        if self.is_alert_present():

         alert = self.dr.switch_to_alert()

         alert.accept()  # 退出

        else:
              pass

        sleep(5)

        if handler.lower()=='carla':

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
                "//*[@id='FlowOrderShippingConfirmationForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

            sleep(3)

        else:
            self.dr.quit()

    def isElementExist(self, link):
        flag = True

        try:
            self.dr.find_element_by_xpath(link)

            print('元素找到')
            return flag
        except:
            flag = False
            print('未找到')
            return flag



    def is_alert_present(self):
        try:
            self.dr.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.dr.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

