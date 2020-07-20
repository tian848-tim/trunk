'''
测试用例标题：新品开发测试
测试场景：新品开发申请业务流程测试
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


class NewProduct(unittest.TestCase):

    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新品开发'
        # 脚本标识－ID
        self.script_id = 'test_flow_new_product'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.dr = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.dr = webdriver.Firefox(log_path=self.log_path)

        self.dr.implicitly_wait(15)
        self.verificationErrors = []
        self.accept_next_alert = True

        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_NewProduct(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()  # 定位到新品开发

        self.dr.find_element_by_xpath("//*[@id='FlowNewProductView']//span[contains(@class,'fa-plus')]").click()#定位到样品申请新建

        self.dr.find_element_by_xpath( "//*[@id='FlowNewProductViewFormPanelID-body']//input[@name='main.vendorName']").click()  ## 选择供应商

        self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys('搭')  # 定位到关键字

        self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()  # 点击搜索





        _elementFirst = self.dr.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位供应商第一条记录

        ActionChains(self.dr).double_click(_elementFirst).perform()  # 在此元素上双击

        _elementSecond = self.dr.find_element_by_xpath("//*[@id='FlowNewProductFormGridPanelID']//img[contains(@class,'x-tool-plus')]")  # 定位添加产品按钮'''

        ActionChains(self.dr).double_click(_elementSecond).perform()

        _elementThird = self.dr.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位样品第一条记录

        ActionChains(self.dr).double_click(_elementThird).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click() #点击确认

        self.dr.find_element_by_xpath("//*[@id='FlowNewProductForm']//span[contains(@class,'fa-save')]").click()  # 点击保存



        self.dr.find_element_by_link_text('注销').click()  # 点击注销


        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)
        '''提交报告'''
        self.login('Vic_cn', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath(
            "//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        sleep(3)

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(),'相关报告')]").click()  # 定位到相关报告

        sleep(2)

        self.dr.find_element_by_xpath(
            "//*[@id='west-panel-targetEl']//span[contains(text(),'产品分析报告')]").click()  # 定位到产品分析报告

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisView']//span[contains(@class,'fa-plus')]").click()  # 定位到产品分析报告新建



        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main_businessId']").click()  # 定位到应用ID

        _elementFourth = self.dr.find_element_by_xpath(
            "//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位第新品开发申请器第一条记录

        ActionChains(self.dr).double_click(_elementFourth).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='reportFileDocumentName']").click()  # 定位到报告文件输入框

        _elementFiveth = self.dr.find_element_by_xpath(
            "//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位文件选择器第一条记录

        ActionChains(self.dr).double_click(_elementFiveth).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.title']").send_keys('测试2')  # 定位到报告标题

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.serialNumber']").send_keys(
            '5646')  # 定位到报告编号

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.reportTime']").send_keys(
            '2018-06-02')  # 报告时间

        self.dr.find_element_by_xpath(
            "//*[@id='ReportProductAnalysisFormWinID']//span[contains(@class,'fa-save')]").click()  # 定位到保存按钮

        sleep(2)


        '''发启。。。。。'''
    def test_new_product_plus(self):

        sleep(5)

        self.login('Vic_cn', '123')

        sleep(5)

        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()  # 关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '新品开发申请')]").click()  # 定位到新品开发申请

        self.dr.find_element_by_xpath(
            "//*[@id='FlowNewProductViewGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择新品开发第一条记录

        sleep(2)

        self.dr.find_element_by_xpath(
            "//*[@id='FlowNewProductView']//span[contains(@class,'fa-pencil-square-o')]").click()  # 定位到新品开发编辑

        self.dr.find_element_by_xpath(
            "//*[@id='FlowNewProductForm']//span[contains(@class,'fa-play')]").click()  # 定位到发启按钮


        '''第二节点审批'''

        self.dr.find_element_by_link_text('注销').click()  # 点击注销

        self.dr.find_element_by_link_text('是').click()

        alert = self.dr.switch_to_alert()

        alert.accept()  # 退出页面

        sleep(5)

        self.login('Vic_cn', '123')

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
            "//*[@id='FlowNewProductViewMainTabsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()  # 选择处理人

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), 'Jack')]").click()  # 选择Jack

        self.dr.find_element_by_xpath(
            "//*[@id='FlowNewProductForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(2)

        '''第三节点审批'''

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
            "//*[@id='FlowNewProductForm']//span[contains(@class, 'fa-check-square')]").click()  # 点击通过

        sleep(3)




    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
