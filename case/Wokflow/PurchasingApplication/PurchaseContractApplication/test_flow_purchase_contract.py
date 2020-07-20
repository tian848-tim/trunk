'''
测试用例标题：采购合同测试
测试场景：采购合同业务流程测试
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
from time import sleep
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

class purchaseContract(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购合同'
        # 脚本标识－ID
        self.script_id = 'test_flow_purchase_contract'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.dr = webdriver.Firefox()
            self.dr.implicitly_wait(15)
        else:
            # 如果使用最新firefox需要使用下面这句
            self.dr = webdriver.Firefox(log_path=self.log_path)
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_PurchaseContract(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购合同')]").click()  # 定位到采购合同

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-plus')]").click()#定位到采购合同新建

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//span[contains(text(), '采购计划列表')]").click()  # 定位到采购计划列表新建

        _elementFirst = self.dr.find_element_by_xpath("//*[@id='PurchasePlanDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位采购计划第一条记录

        ActionChains(self.dr).double_click(_elementFirst).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='PurchasePlanDialogWinID']//span[contains(@class,'fa-check')]").click() #点击确认

        self.dr.find_element_by_xpath(
            "//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.buyerInfoName']").click()  # 定位买方信息

        _elementSecond = self.dr.find_element_by_xpath(
            "//*[@id='BuyerDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位查询结果第一个元素

        ActionChains(self.dr).double_click(_elementSecond).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath( "//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.readyDate']").send_keys('2018-06-05')  # 完货日期

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.orderDate']").send_keys('2018-06-03')  # 订单日期

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.etd']").send_keys('2018-06-10') #预计发货时间

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.containerType']").click() # 货柜类型

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '20')]").click()  # 开船前#20GP

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.originPortId']").click()  # 出货港口

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '宁波')]").click()  # 宁波

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractFormPanelID-body']//input[@name='main.balancePaymentTerm']").click()  # 尾款条

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '开船前')]").click()   # 开船前

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class,'fa-play')]").click()  # 点击发启

        sleep(3)

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractGridPanelID-body']//div[contains(text(), '1')]").click()#选择第一条采购合同

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractView']//span[contains(@class,'fa-pencil-square-o')]").click()  # 点击编辑





        # 判断是否需要分配处理人

        if self.dr.find_element_by_xpath( "//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").is_displayed(): # 分配处理人

             self.dr.find_element_by_xpath( "//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

             self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack.L')]").click()  # 选择Jack.L

             self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        else:

         self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)



        # 获取当前节点处理人

        handler = self.dr.find_element_by_xpath(
            "//div[@id='FlowPurchaseContractGridPanelID-body']/div/table/tbody/tr[1]/td[34]/div").text

        print(handler)

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        if self.is_alert_present():

            alert = self.dr.switch_to_alert()

            alert.accept()  # 退出

        else:
            pass

        sleep(2)


        if handler=='Jack.L':

         self.login('Jack.L', '123')
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
             "//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

         sleep(5)

        else:
            pass

        self.login('emma', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()  # 定位到待办事项

        self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click() #定位到待办事项第一条记录

        self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click() # 点击马上处理

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()  # 分配处理人

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'dickson')]").click()  # 选择dickson

        self.dr.find_element_by_xpath("//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        if self.is_alert_present():

            alert = self.dr.switch_to_alert()

            alert.accept()  # 退出

        else:
            pass

        sleep(2)

        self.login('dickson', '123')#dickson审批

        sleep(8)

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
        "//*[@id='FlowPurchaseContractForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(5)

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


if __name__ == "__main__":
    unittest.main()
