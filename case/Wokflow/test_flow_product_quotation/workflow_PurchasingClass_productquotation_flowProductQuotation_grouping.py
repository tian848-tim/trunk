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

    def loadvendername(self):

        global result

        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation_grouping.json', encoding='utf-8')
        data = json.load(file)

        result = [(d['username'], d['password']) for d in data['login']]

        return result


    def loadvendernames(self):

        global results

        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation_grouping.json', encoding='utf-8')
        data = json.load(file)
        result = [(d['username'], d['password']) for d in data['login']]

        results = [(d['name']) for d in data ['use_vendorname']]

        return results

    def price(self):

        global price

        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation_grouping.json', encoding='utf-8')
        data = json.load(file)

        price = [(d['key']) for d in data ['price']]

        return price


    def moq(self):

        global moq

        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation_grouping.json', encoding='utf-8')
        data = json.load(file)

        moq = [(d['key']) for d in data ['moq']]

        return moq

    def qty(self):

        global qty

        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation_grouping.json', encoding='utf-8')
        data = json.load(file)

        qty = [(d['key']) for d in data ['qty']]

        return qty

    def CN(self):

        global cn
        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation.json', encoding='utf-8')
        data = json.load(file)
        cn = [(d['key']) for d in data['cnLanguage']]

        return cn

    def EN(self):

        global en
        file = open(rootPath + '/data/workflow_PurchasingClass_productquotation_flowProductQuotation.json', encoding='utf-8')
        data = json.load(file)
        en = [(d['key']) for d in data['enLanguage']]

        return en


    def setUp(self):
        # 脚本标识－标题
        self.script_name = '采购询价测试-组合'
        # 脚本标识－ID
        self.script_id = 'workflow_PurchasingClass_productquotation_flowProductQuotation_grouping'
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
        self.driver.get(self.target_url)  # 登录页面
        self.driver.find_element_by_id('account-inputEl').send_keys(username)
        self.driver.find_element_by_id('password-inputEl').send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='LoginWin']//span[contains(@class,'x-btn-icon-el')]").click()

        # 判断当前语言

    def CheckLanguage(self):
        global _Language
        _Language = self.driver.find_element_by_xpath("//div[@id='header-right']/div/span[1]").text

        if _Language in "欢迎您":
            _Language = True

        else:
            _Language = False

        return _Language


    def test_productquotation(self):

            su = self.loadvendername()
            ad = self.loadvendernames()
            we = self.price()
            er = self.moq()
            rt = self.qty()
            cn = self.CN()
            en = self.EN()

            for i in range(0, len(su)):
                print(su[i][0])
                print(su[i][1])
            print(ad)
            self.login(su[0][0],su[0][1])
            #self.login('Vic_cn','123')

            # 强制等待
            sleep(5)

            lg = self.CheckLanguage()

            if lg == True:

                lg = cn

            else:

                lg = en

            try:
                self.driver.find_element_by_xpath(
                    "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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

            # 强制等待
            sleep(2)

            # 定位到申请单据
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-code-fork')]").click()

            # 强制等待
            sleep(2)

            # 定位到采购询价
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[0])).click()

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
                _elementFiveth = (random.randint(1, 10))


                # 定位采购第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

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

            sleep(2)

            _NoData = self.driver.find_element_by_xpath("//div[@id='ProductDialogWinGridPanelID-body']/div").text

            if _NoData == lg[2]:

            #try:

                #self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[text()='{}']".format('没有数据！')).is_displayed()
                name = True
            else:
                name = False

            if name == True:
                print("元素存在")
            elif name == False:
                print("元素不存在")

            sleep(2)

            while  name == True:

                # 关闭
                self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//img[contains(@class, 'x-tool-close')]").click()

                # 强制等待
                sleep(2)

                # 选择供应商
                self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormPanelID-body']//input[@name='main.vendorName']").click()

                # 强制等待
                sleep(2)

                _elementFiveth = (random.randint(1, 10))


                # 定位采购第一条记录
                _elementFirst = self.driver.find_element_by_xpath("//*[@id='VendorDialogWinGridPanelID-body']//div[text()='{}']".format(_elementFiveth))

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

                sleep(2)

                _NoData = self.driver.find_element_by_xpath("//div[@id='ProductDialogWinGridPanelID-body']/div").text

                if _NoData == lg[2]:

                    # try:

                    # self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[text()='{}']".format('没有数据！')).is_displayed()
                    name = True
                else:
                    name = False

                if name == True:
                    print("元素存在")
                elif name == False:
                    print("元素不存在")

            else:
                pass

            ul = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']/div/table/tbody")
            lis = ul.find_elements_by_xpath('tr')
            print(len(lis))

            if int(rt[0]) > len(lis):
                print("选择条数大于sku数量")

                self.driver.quit()

            qty = 1

            while  qty <= int(rt[0]):

                 # 定位SKU第一条记录
                 _elementThird = self.driver.find_element_by_xpath("//*[@id='ProductDialogWinGridPanelID-body']//div[text()= '{}']".format(qty))

                 # 强制等待
                 sleep(2)

                 # 在此元素上双击
                 ActionChains(self.driver).double_click(_elementThird).perform()

                 # 强制等待
                 sleep(2)

                 qty += 1

            # 点击确认
            self.driver.find_element_by_xpath("//*[@id='ProductDialogWinID']//span[contains(@class,'fa-check')]").click()

            # 强制等待
            sleep(2)

            ul = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID-locked-body']/div/table/tbody")
            lis = ul.find_elements_by_xpath('tr')
            print(len(lis))

            qty = 1

            while  qty <= len(lis):

                 # 定位到aud框
                 self.driver.find_element_by_xpath("//div[@id='FlowProductQuotationViewFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[8]".format(qty)).click()

                 # 强制等待
                 sleep(2)

                 ## 定位到AUD输入
                 self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID']//input[@name='priceAud']").send_keys(we[0])

                 # 强制等待
                 sleep(2)

                 # 定位到采购件数框
                 self.driver.find_element_by_xpath("//div[@id='FlowProductQuotationViewFormGridPanelID-normal-body']/div/table/tbody/tr[{}]/td[14]".format(qty)).click()

                 # 强制等待
                 sleep(2)

                 ## 定位到采购件数输入
                 self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID']//input[@name='moq']").clear()

                 sleep(2)

                 ## 定位到采购件数输入
                 self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewFormGridPanelID']//input[@name='moq']").send_keys(er[0])

                 qty += 1

            # 强制等待
            sleep(2)

            # 点击发启
            self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationForm']//span[contains(@class,'x-btn-icon-el fa fa-fw fa-play')]").click()

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[3]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(1)

            #_W = self.driver.find_element_by_xpath("//*[@id='FlowProductQuotationViewGridPanelID-body']/div/table/tbody/tr[1]/td[2]/div").text

            ul = self.driver.find_element_by_xpath(
                "//*[@id='FlowProductQuotationViewGridPanelID-body']/div/table/tbody/tr[1]")

            lis = ul.find_elements_by_xpath('td')

            _W = 'FPQ'

            for i in range(0, len(lis)):

                if _W in lis[i].text:
                    _W = lis[i].text

                    break

            print(_W)

            # 写入json
            one = "{}".format(_W)
            mess1 = [{"key": one}]
            two = {"variable": mess1}
            data = dict(two)
            jsonData = json.dumps(data)
            desktop_path = rootPath + '/data/'
            full_path = desktop_path + "test_productquotation" + time.strftime("%Y-%m-%d") + '.json'
            fileObject = open(full_path, 'w')
            fileObject.write(jsonData)
            fileObject.close()

            self.driver.find_element_by_link_text(lg[5]).click()  # 点击注销

            sleep(2)

            self.driver.find_element_by_link_text(lg[6]).click()

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

            try:
                self.driver.find_element_by_xpath(
                    "//*[@id='msgwin-div']//div[contains(@class,'x-tool-close')]").is_displayed()
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

            # 强制等待
            sleep(2)

            # 定位到工作面板
            self.driver.find_element_by_xpath("//*[@id='appNavTabPanel']//span[contains(@class,'fa-desktop')]").click()

            # 强制等待
            sleep(2)

            # 定位到待办事项
            self.driver.find_element_by_xpath("//*[@id='west-panel-targetEl']//span[text()= '{}']".format(lg[1])).click()

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

            self.driver.implicitly_wait(60)
            # 获取弹窗提示：
            #self.driver.implicitly_wait(10)
            a = self.driver.find_element_by_css_selector('.x-box-mc').get_attribute('textContent')
            print(a)

            _prompt = lg[4]

            if _prompt in a:

                pass

            else:

                print("流程错误")

                self.driver.quit()

            sleep(2)

            # 点击注销
            self.driver.find_element_by_link_text(lg[5]).click()

            self.driver.find_element_by_link_text(lg[6]).click()

            alert = self.driver.switch_to_alert()

            alert.accept()  # 退出页面

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

