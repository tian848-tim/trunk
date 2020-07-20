'''
测试用例标题：新品档案测试
测试场景：新品档案业务流程测试
创建者：Tim
创建日期：2018-11-20
最后修改日期：2018-11-20
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
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

import random
import json

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''
class VendorCategory(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def loadvendername(self):

        global result
        file = open(rootPath + '/data/NewProductDocument.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        return result

    def purchaseType(self):

        global result
        file = open(rootPath + '/data/NewProductDocument.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['key']) for d in data['purchaseType']]

        return result


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '新品档案'
        # 脚本标识－ID
        self.script_id = 'NewProductDocument'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
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



    def test_NewProductDocument(self):

        su = self.loadvendername()
        we = self.purchaseType()

        for i in range(0, len(su)):
           print(su[i][0])
           print(su[i][1])
        self.login(su[0][0], su[0][1])
        #self.login('Vic_cn ','122')

        sleep(10)

        try:
             self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
             a = True
        except:
             a = False
        if a == True:
            print("元素存在")
        elif a == False:
            print("元素不存在")

        print(a)

        if a == True:

           # 关闭弹出框
           self.driver.find_element_by_xpath("//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").click()

        else:
            pass

        sleep(2)

        # 定位到资料档案
        self.driver.find_element_by_xpath("//*[@id='header-topnav']//span[contains(@class,'fa-file-o')]").click()

        sleep(2)

        # 定位到新品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'供应商产品线')]").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='VendorProductLineGridPanelID-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        _elementFiveth = (random.randint(1, len(lis)))

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='VendorProductLineGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        _G = self.driver.find_element_by_xpath("//*[@id='VendorProductLineGridPanelID-body']//tr[{}]/td[2]/div".format(_elementFiveth)).get_attribute("textContent")

        _H = self.driver.find_element_by_xpath("//*[@id='VendorProductLineGridPanelID-body']//tr[{}]/td[4]/div".format(_elementFiveth)).get_attribute("textContent")

        sleep(2)

        # 定位到产品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

        sleep(2)

        # 定位到新品档案
        self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'新品档案')]").click()

        sleep(2)

        # 定位到新品档案新建
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentView']//span[contains(@class,'fa-plus')]").click()

        sleep(2)

        _elementFiveth = (random.randint(0, 1000))

        # 定位到产品编码
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.sku']").send_keys("ASDF",_elementFiveth)

        sleep(2)

        # 定位到产品编码
        _T1 =self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.sku']").get_attribute("value")

        # 定位到产品名
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.name']").send_keys(_T1)

        sleep(2)

        # 定位到组合产品
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.combined']").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

        lis = ul.find_elements_by_xpath('li')

        first_category = lis[random.randint(0, len(lis) - 1)]

        sleep(2)

        first_category_name = first_category.text
        print("随机选择的是:{0}".format(first_category_name))
        first_category.click()

        sleep(2)

        # 定位到采购类型
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.purchaseType']").click()

        sleep(2)

        # 定位到采购类型
        self.driver.find_element_by_xpath("//*[@class='x-list-plain']//li[contains(text(),'{}')]".format(we[0])).click()

        sleep(2)

        # 定位到分类
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.categoryName']").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//input[@name='keywords']").send_keys(_H)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//span[contains(@class,'fa-search')]").click()

        sleep(1)

        ul = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        print(len(lis))

        while len(lis) > 1:

            # 定位到取消
            self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinID']//span[contains(@class,'fa-close')]").click()

            sleep(2)

            # 定位到取消
            self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormWinID']//span[contains(@class,'fa-close')]").click()

            sleep(2)

            # 定位到产品档案
            self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'供应商')]").click()

            sleep(2)

            # 定位到新品档案
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'供应商产品线')]").click()

            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@id='VendorProductLineGridPanelID-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            _elementFiveth = (random.randint(1, len(lis)))

            _elementFirst = self.driver.find_element_by_xpath(
                "//*[@id='VendorProductLineGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

            # 在此元素上双击
            ActionChains(self.driver).double_click(_elementFirst).perform()

            _G = self.driver.find_element_by_xpath(
                "//*[@id='VendorProductLineGridPanelID-body']//tr[{}]/td[2]/div".format(_elementFiveth)).get_attribute(
                "textContent")

            _H = self.driver.find_element_by_xpath(
                "//*[@id='VendorProductLineGridPanelID-body']//tr[{}]/td[4]/div".format(_elementFiveth)).get_attribute(
                "textContent")

            sleep(2)

            # 定位到产品档案
            self.driver.find_element_by_xpath("//*[@id='west-panel-body']//span[contains(text(),'产品资料')]").click()

            sleep(2)

            # 定位到新品档案
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[contains(text(),'新品档案')]").click()

            sleep(2)

            # 定位到新品档案新建
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentView']//span[contains(@class,'fa-plus')]").click()

            sleep(2)

            _elementFiveth = (random.randint(0, 1000))

            # 定位到产品编码
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.sku']").send_keys("ASDF",
                                                                                                    _elementFiveth)

            sleep(2)

            # 定位到产品编码
            _T1 = self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.sku']").get_attribute("value")

            # 定位到产品名
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.name']").send_keys(_T1)

            sleep(2)

            # 定位到组合产品
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.combined']").click()

            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@class='x-boundlist-list-ct x-unselectable']/ul")

            lis = ul.find_elements_by_xpath('li')

            first_category = lis[random.randint(0, len(lis) - 1)]

            sleep(2)

            first_category_name = first_category.text
            print("随机选择的是:{0}".format(first_category_name))
            first_category.click()

            sleep(2)

            # 定位到采购类型
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.purchaseType']").click()

            sleep(2)

            # 定位到采购类型
            self.driver.find_element_by_xpath(
                "//*[@class='x-list-plain']//li[contains(text(),'{}')]".format(we[0])).click()

            sleep(2)

            # 定位到分类
            self.driver.find_element_by_xpath(
                "//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.categoryName']").click()

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@id='ProductCategoryDialogWinID']//input[@name='keywords']").send_keys(_H)

            sleep(2)

            self.driver.find_element_by_xpath(
                "//*[@id='ProductCategoryDialogWinID']//span[contains(@class,'fa-search')]").click()

            sleep(1)

            ul = self.driver.find_element_by_xpath(
                "//*[@id='ProductCategoryDialogWinTreePanelId-body']/div/table/tbody")

            lis = ul.find_elements_by_xpath('tr')

            print(len(lis))

        else:
            pass

        self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']//img[contains(@class, 'x-tree-expander')]").click()

        sleep(2)

        ul = self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']/div/table/tbody")

        lis = ul.find_elements_by_xpath('tr')

        #print(lis)

        #category = lis[len(lis)]

        #category_name = category.text

        #print(category_name)

        for i in range(0,len(lis)-1):

            #print(lis[i].text)

            if _H == lis[i].text:

                break

            #return i

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='ProductCategoryDialogWinTreePanelId-body']//tr[@data-recordindex={}]".format(i))

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位到处理人
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='handlerName']").click()

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        sleep(2)

        # 定位到处理人
        self.driver.find_element_by_xpath("//*[@id='HandlerDialogGridPanelID-body']//div[text()={}]".format(_elementFiveth)).click()

        sleep(2)

        # 定位到确认
        self.driver.find_element_by_xpath("//*[@id='HandlerDialogWinID']//span[contains(@class,'fa-check')]").click()

        sleep(2)

        # 定位到供应商
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormPanelID-body']//input[@name='main.prop.vendorName']").click()

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID-body']//input[@name='keywords']").send_keys(_G)

        sleep(2)

        self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID-body']//span[contains(@class ,'fa-search')]").click()

        sleep(2)

        _elementFirst =self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID']//div[text()='1']")

        sleep(2)

        # 在此元素上双击
        ActionChains(self.driver).double_click(_elementFirst).perform()

        sleep(2)

        # 定位到确认
        #self.driver.find_element_by_xpath("//*[@id='VendorDialogWinID']//span[contains(@class,'fa-check')]").click()

        #sleep(2)

        _elementFiveth = (random.randint(1, 20))

        # 定位到起订量
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormWinID']//input[@name='main.prop.moq']").send_keys(_elementFiveth)

        sleep(2)

        _elementFiveth = (random.randint(1, 10))

        # 定位到件/箱
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormWinID']//input[@name='main.prop.pcsPerCarton']").send_keys(_elementFiveth)

        sleep(2)


        # 定位到保存
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentFormWinID']//span[contains(@class,'fa-save')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        #self.driver.implicitly_wait(10)
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)

        sleep(1)

        # 定位到第一条
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentGridPanelID-body']//div[contains(text(),'1')]").click()

        _W = self.driver.find_element_by_xpath("//*[@id='NewProductDocumentGridPanelID-locked-body']/div/table/tbody/tr[1]/td[3]/div").text

        sleep(1)

        # 写入json
        one = "{}".format(_W)
        two = "{}".format(_G)
        mess1 = [{"key": one},{"key": two}]
        three = {"variable": mess1}
        data = dict(three)
        jsonData = json.dumps(data)
        desktop_path = rootPath + '/data/'
        full_path = desktop_path + "test_NewProductDocument" + time.strftime("%Y-%m-%d") + '.json'
        fileObject = open(full_path, 'w')
        fileObject.write(jsonData)
        fileObject.close()

        sleep(2)

        # 定位到启用
        self.driver.find_element_by_xpath("//*[@id='NewProductDocumentView']//span[contains(@class,'fa-location-arrow')]").click()

        self.driver.implicitly_wait(60)
        # 获取弹窗提示：
        a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
        print(a)




    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

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

if __name__ == "__main__":
        unittest.main()