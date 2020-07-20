'''
测试用例标题：样品申请测试
测试场景：样品申请业务流程测试
创建者：Tom
创建日期：2018-7-25
最后修改日期：2018-7-25
输入数据：审批流程各个角色账号
输出数据：无

'''
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
            file = open(rootPath + '/data/test_flowsample_json.json', encoding='utf-8')
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

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '样品申请'
        # 脚本标识－ID
        self.script_id = 'test_flowsample_json'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.dr = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.dr = webdriver.Firefox(log_path=self.log_path)

        self.verificationErrors = []
        self.accept_next_alert = True

        self.dr.implicitly_wait(15)
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get(self.target_url)  # 登录页面
        self.dr.find_element_by_id('account-inputEl').send_keys(username)
        self.dr.find_element_by_id('password-inputEl').send_keys(password)
        self.dr.find_element_by_id('button-1013-btnIconEl').click()


    def test_flowsample_json(self):

        su = self.loadvendername()
        for i in range(0, len(su)):
            print(su[i][0])
            print(su[i][1])
            self.login(su[i][0],su[i][1])
            sleep(5)

            # 关闭弹出框
            self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()
            # 定位到申请单据
            self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()
            # 定位到样品申请
            self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '样品申请')]").click()
            # 定位到样品申请新建
            self.dr.find_element_by_xpath("//*[@id='FlowSampleView']//span[contains(@class,'fa-plus')]").click()
            ## 选择供应商
            self.dr.find_element_by_xpath( "//*[@id='FlowSampleViewFormPanelID-body']//input[@name='main.vendorName']").click()
            ## 定位到关键字
            self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//input[@name='keywords']").send_keys("")
            # 点击搜索
            self.dr.find_element_by_xpath("//*[@id='VendorDialogWinSearchPanelID-innerCt']//span[contains(@class,'fa-search')]").click()
            sleep(3)
            # 定位供应商第一条记录

            _elementFirst = self.dr.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[contains(text(), '1')]")

            # 在此元素上双击
            ActionChains(self.dr).double_click(_elementFirst).perform()
            # 定位添加样品按钮'''
            _elementSecond = self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID_header-body']//img[contains(@class,'x-tool-plus')]")

            ActionChains(self.dr).double_click(_elementSecond).perform()
            # 定位样品第一条记录
            _elementThird = self.dr.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[contains(text(), '1')]")
            # 在此元素上双击
            ActionChains(self.dr).double_click(_elementThird).perform()
            # 点击确认
            self.dr.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()
            # 点击aud
            self.dr.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[5]").click()
            # 清除输入框
            self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeAud']").clear()
            ## 定位到AUD输入
            self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeAud']").send_keys('10')
            # 点击样品件数
            self.dr.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[8]").click()
            ## 清除样品件数
            self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='qty']").clear()
            ## 定位到样品件数
            self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='qty']").send_keys(test_flowsample_json.qty)
            # 定位到费用可退
            self.dr.find_element_by_xpath( "//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[12]").click()
            # 清除输入框
            self.dr.find_element_by_xpath( "//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeRefund']").clear()
            # 定位费用可退
            # 定位到费用可退
            self.dr.find_element_by_xpath("//*[@id='FlowSampleFormGridPanelID-f-body']//input[@name='sampleFeeRefund']").send_keys(test_flowsample_json.sampleFeeRefund)

            self.dr.find_element_by_xpath("//div[@id='FlowSampleFormGridPanelID-normal-body']/div/table/tbody/tr/td[12]").click()
            # 点击发启
            self.dr.find_element_by_xpath("//*[@id='FlowSampleForm']//span[contains(@class,'fa-play')]").click()

            # 点击注销
            self.dr.find_element_by_link_text('注销').click()


            self.dr.find_element_by_link_text('是').click()

            if self.is_alert_present():

                alert = self.dr.switch_to_alert()

                alert.accept()

            else:
                pass

            sleep(2)

            self.login(su[i][0],su[i][1])
            sleep(7)
            # 关闭弹出框
            self.dr.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()
            # 定位到工作面板
            self.dr.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()
            # 定位到待办事项
            self.dr.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(), '待办事项')]").click()
            # 定位到待办事项第一条记录
            self.dr.find_element_by_xpath("//*[@id='EventsGridPanelID-body']//div[contains(text(), '1')]").click()
            # 点击马上处理
            self.dr.find_element_by_xpath("//*[@id='EventsFormPanelID-body']//span[contains(@class, 'x-btn-icon-el')]").click()
            # 点击通过

            self.dr.find_element_by_xpath("//*[@id='FlowSampleForm']//span[contains(@class, 'fa-check-square')]").click()
            sleep(3)
            self.dr.find_element_by_link_text('注销').click()

            self.dr.find_element_by_link_text('是').click()

            if self.is_alert_present():
                alert = self.dr.switch_to_alert()

                alert.accept()
            sleep(2)


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
