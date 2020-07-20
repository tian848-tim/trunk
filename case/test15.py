"""
测试用例标题：采购询价测试
测试场景：采购询价业务流程测试
创建者：Tom
修改者：Tim
创建日期：2018-7-25
最后修改日期：2018-10-23
输入数据：供应商：瑞聚家具公司，审批流程各个角色账号
输出数据：无

"""



from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest,configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import  json
import  random

import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')


class test_flowsample_json(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime(
        "%Y-%m-%d %H_%M_%S")
    # #定义供应商名
    # vendorName = '搭'
    # 1为费用可退，2为不可退
    sampleFeeRefund = '1'
    #定义数量
    qty = '10'

    def loadvendername(self):
        try:
            file = open(rootPath + '/data/test.json', encoding='utf-8')
            data = json.load(file)
            result = [(d['username'], d['password']) for d in data['login']]
        except Exception as e:
            print(e)

        # i = random.randint(0, 1)
        #
        # print(i)
        # str_as = "['login'][" + str(i) + ']["username"]'
        # print(str_as)
        # vender = setting["use_vendorname"][1]["name"]
        # return vender
        # result = [(item['username'],item['password']) for item in setting['login']]
        # print(result)
        return result


    def loadvendernames(self):
        try:
            file = open(rootPath + '/data/test.json', encoding='utf-8')
            data = json.load(file)
            result = [(d['username'], d['password']) for d in data['login']]

            results = [(d['name']) for d in data ['use_vendorname']]
        except Exception as e:
            print(e)

        # i = random.randint(0, 1)
        #
        # print(i)
        # str_as = "['login'][" + str(i) + ']["username"]'
        # print(str_as)
        # vender = setting["use_vendorname"][1]["name"]
        # return vender
        # result = [(item['username'],item['password']) for item in setting['login']]
        # print(result)
        return results


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新建供应商分类'
        # 脚本标识－ID
        self.script_id = 'test_flow_product_quotation'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)


        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 定义登录方法
    def login(self, username, password):
        self.driver.get('http://192.168.1.112:880/')  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()


    def test_productquotation(self):

            su = self.loadvendername()
            ad = self.loadvendernames()
            for i in range(0, len(su)):
                print(su[i][0])
                print(su[i][1])
            print(ad)
            self.login(su[0][0],su[0][1])
            #self.login('Vic_cn','123')

            # 强制等待
            sleep(5)

            # 关闭弹出框
            self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            # 强制等待
            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            # 强制等待
            sleep(2)

            # 定位到采购询价
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '采购询价')]").click()

            # 强制等待
            sleep(2)

            # 定位到采购询价新建
            self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationView']//span[contains(@class,'fa-plus')]").click()

            # 强制等待
            sleep(2)

            # 选择供应商
            self.driver.find_element_by_xpath( "//*[@id='FlowProductQuotationViewFormPanelID-body']//input[@name='main.vendorName']").click()

            # 强制等待
            sleep(2)

            print(ad[0])

            if ad[0] != '':

                # 定位到关键字
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-body']//input[@name='keywords']").send_keys(ad[0])

            # 强制等待
                 sleep(2)

            # 点击搜索
                 self.driver.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()

            # 强制等待
                 sleep(2)

            # 定位采购第一条记录
                 _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

            # 强制等待
                 sleep(2)

            # 在此元素上双击
                 ActionChains(self.driver).double_click(_elementFirst).perform()

            # 强制等待
                 sleep(2)

            else:
                # 定位采购第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

                # 强制等待
                sleep(2)

                # 在此元素上双击
                ActionChains(self.driver).double_click(_elementFirst).perform()

                # 强制等待
                sleep(2)


            # 定位添加SKU按钮
            _elementSecond = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID_header-targetEl']//img[contains(@class,'x-tool-plus')]")

            # 强制等待
            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementSecond).perform()

            # 强制等待
            sleep(2)

            # 定位SKU第一条记录
            _elementThird = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")

            # 强制等待
            sleep(2)

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementThird).perform()

            # 强制等待
            sleep(2)

            # 点击确认
            self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

            # 强制等待
            sleep(2)

            # 定位到aud框
            self.driver.find_element_by_xpath("//div[@id='FlowProductQuotationViewFormGridPanelID-normal-body']/div/table/tbody/tr/td[8]").click()

            # 强制等待
            sleep(2)

            ## 定位到AUD输入
            self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID']//input[@name='priceAud']").send_keys('100')

            # 强制等待
            sleep(2)

            # 点击发启
            self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-play')]").click()

            # 强制等待
            sleep(10)

            self.driver.find_element_by_link_text('注销').click()  # 点击注销

            sleep(2)

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            # 退出页面
            alert.accept()

            # 强制等待
            sleep(5)

            '''审批'''

            self.login(su[1][0], su[1][1])

            #self.login('Vic_cn', '123')

            # 强制等待
            sleep(5)

            # 关闭弹出框
            self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

            # 强制等待
            sleep(2)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            # 强制等待
            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()

            # 强制等待
            sleep(2)

            # 定位到待办事项第一条记录
            self.driver.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()

            # 强制等待
            sleep(2)

            # 点击马上处理
            self.driver.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()

            # 强制等待
            sleep(2)

            # 判断是否需要分配处理人

            # 分配处理人
            if   self.driver.find_element_by_xpath( "//*[@id='FlowProductQuotationViewMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").is_displayed():

                # 分配处理人
                 self.driver.find_element_by_xpath( "//*[@id='FlowProductQuotationViewMainTbsPanelID-win-0-body']//input[@name='flowNextHandlerAccount']").click()

                 # 选择第一项
                 self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(@class, 'x-boundlist-item-over')]").click()

                # 点击通过
                 self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class, 'fa-check-square')]").click()

            else:

                # 点击通过
                 self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class, 'fa-check-square')]").click()

            sleep(2)

            # 点击注销
            self.driver.find_element_by_link_text('注销').click()

            self.driver.find_element_by_link_text('是').click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

