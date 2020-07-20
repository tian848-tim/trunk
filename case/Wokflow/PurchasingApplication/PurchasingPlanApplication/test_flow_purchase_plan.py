'''
测试用例标题：采购计划测试
测试场景：采购计划业务流程测试
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



class purchasePlan(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建采购计划'
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

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('http://192.168.1.108:880/')  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_PurchasePlan(self):
        self.login('Vic_cn','123')
        sleep(5)


        self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()#关闭弹出框

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()#定位到申请单据

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()  # 定位到采购计划

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-plus')]").click()#定位到采购计划新建

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.vendorName']").click()  # 定位到供应商名称输入框


        self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys('搭')  # 定位到供应商选择器关键字输入框

        self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click() # 定位到查询

        _element=self.dr.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")#定位查询结果第一个元素

        ActionChains(self.dr).double_click(_element).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID']//input[@name='main.purchaseType']").click()#定位到订单类型

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(), '国际订单')]").click()

        _elementThird=self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")  # 定位添加SKU按钮'''

        ActionChains(self.dr).double_click(_elementThird).perform()

        _elementSecond = self.dr.find_element_by_xpath("//*[@id='OtherProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位第一个SKU

        ActionChains(self.dr).double_click(_elementSecond).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='OtherProductDialogWinID']//span[contains(@class,'fa-check')]").click()  # 定位到确认按钮

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanFormPanelID-body']//input[@name='main.leadTime']").send_keys('2')  # 定位生成周期输入框

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-save')]").click()  # 定位到保存按钮

        self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()  # 定位到工作面板

        sleep(3)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'相关报告')]").click()  # 定位到相关报告

        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'产品分析报告')]").click()  # 定位到产品分析报告

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisView']//span[contains(@class,'fa-plus')]").click()  # 定位到产品分析报告新建

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@value='新品开发申请']").click()  # 定位到申请单类型

        self.dr.find_element_by_xpath("//*[@class='x-list-plain']//li[contains (text(),'采购计划申请')]").click()# 采购计划申请

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main_businessId']").click()  # 定位到应用ID

        _elementFourth = self.dr.find_element_by_xpath("//*[@id='FlowOtherDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位第采购计划申请器第一条记录

        ActionChains(self.dr).double_click(_elementFourth).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath( "//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='reportFileDocumentName']").click() #定位到报告文件输入框

        _elementFiveth = self.dr.find_element_by_xpath("//*[@id='FilesDialogWinGridPanelID-body']//div[contains(text(), '1')]")  # 定位文件选择器第一条记录

        ActionChains(self.dr).double_click(_elementFiveth).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.title']").send_keys('测试2')  # 定位到报告标题

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.serialNumber']").send_keys('5646')  # 定位到报告编号

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID-body']//input[@name='main.reportTime']").send_keys('2018-06-02') #报告时间

        self.dr.find_element_by_xpath("//*[@id='ReportProductAnalysisFormWinID']//span[contains(@class,'fa-save')]").click()  # 定位到保存按钮



        _elementSixth=self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()  # 定位到申请单据
        ActionChains(self.dr).double_click(_elementSixth).perform()  # 在此元素上双击

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()  # 定位到采购计划

        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()#选择采购计划第一条记录


        sleep(2)

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-pencil-square-o')]").click()  # 定位到采购计划编辑

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-play')]").click()  # 定位到发启按钮

        self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购计划')]").click()  # 定位到采购计划

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanGridPanelID-body']//div[contains(text(), '1')]").click()  # 选择采购计划第一条记录

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanView']//span[contains(@class,'fa-pencil-square-o')]").click()  # 定位到采购计划编辑

        self.dr.find_element_by_xpath("//*[@id='FlowPurchasePlanForm']//span[contains(@class,'fa-check-square')]").click()  # 定位到通过按钮

        sleep(2)


    def tearDown(self):
            self.dr.quit()


if __name__ == "__main__":
    unittest.main()
