'''
测试用例
'''
'''
测试用例标题：Magento_Email_Compose
测试用例场景：新建Email
创建者：Seven
创建日期：2019-01-08
最后修改日期：2019-01-16
输入参数：
输出参数：
路径：G:\svnFile\trunk\case
'''
# -*- coding: utf-8 -*-
import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
#sys.path.append(rootPath)
import time,unittest,configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import unittest, time, re
import datetime

from time import sleep

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

class seventest(unittest.TestCase):
    base_url = cfg.get("projects", "base_url")
    project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = 'seventest'
        # 脚本标识－ID
        self.script_id = 'seventest'
        self.target_url = self.base_url + self.project_path
        if (cfg.get("webdriver", "enabled") == "off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Chrome()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Chrome(log_path=self.log_path)
        self.driver.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.driver.get('http://cs.newaim.com.au/login')  # 登录页面
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('loginsubmit').click()
        navigationStart4 = self.driver.execute_script("return window.performance.timing.fetchStart")
        loadEventEnd4 = self.driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime4 = (loadEventEnd4 - navigationStart4)
        print("Login加载时间", str(durtime4 / 1000), ".s")
        sleep(5)



    def test_seventestdetail(self):
        self.login('seven','123456')
        self.driver.implicitly_wait(5)
        driver = self.driver # this is add
        # 定位到eBay模块
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, './/*[@id=\'col-main\']/div[1]/div[3]/ul/li[2]/a'))).send_keys(Keys.ENTER)
        except Exception as e:
            print("找不 id为 create_link " + e)
        # 定位到Email菜单
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID,'menu_email'))).send_keys(Keys.ENTER)
        except Exception as e:
            print("找不 id为 create_link " + e)
        driver.implicitly_wait(30)
        # iframe_email层
        driver.switch_to.frame("iframe_email")
        sleep(5)
        #driver.switch_to.parent_frame()
        sleep(5)
        #starttime = datetime.datetime.now()
        navigationStart1 = driver.execute_script("return window.performance.timing.fetchStart")
        # 定位到All pending文件夹
        driver.find_element_by_xpath(".//*[@id='email_todo']/a").click()
        #endtime = datetime.datetime.now()
        loadEventEnd1 = driver.execute_script("return window.performance.timing.loadEventEnd")
        #loadtime=(endtime-starttime)
        #print(loadtime)
        durtime1 = (loadEventEnd1 - navigationStart1)
        print("Email All pending加载时间", str(durtime1 / 1000), ".s")
        sleep(5)
        # 顶层
        driver.switch_to.default_content()
        # iframe_email层
        driver.switch_to.frame("iframe_email")
        # 定位到Sent Report文件夹
        driver.find_element_by_xpath(".//*[@id='col_sub']/div[4]/ul/li[3]/a").click()
        sleep(5)
        # ctn-iframe层
        driver.switch_to.frame("ctn-iframe")
        navigationStart6= driver.execute_script("return window.performance.timing.fetchStart")
        driver.find_element_by_xpath(".//*[@id='listDiv']//td[contains(text(),'medw03@bigpond.com')]").click()
        loadEventEnd6 = driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime6 = (loadEventEnd6 - navigationStart6)
        print("Email无附件详情页面加载时间", str(durtime6 / 1000), ".s")
        sleep(5)
        #顶层
        driver.switch_to.default_content()
        # iframe_email层
        driver.switch_to.frame("iframe_email")
        # 定位到Sent Report文件夹
        driver.find_element_by_xpath(".//*[@id='col_sub']/div[4]/ul/li[3]/a").click()
        sleep(5)
        # ctn-iframe层
        driver.switch_to.frame("ctn-iframe")
        navigationStart5 = driver.execute_script("return window.performance.timing.fetchStart")
        driver.find_element_by_xpath(".//*[@id='listDiv']//td[contains(text(),'Kate Williams')]").click()
        loadEventEnd5 = driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime5 = (loadEventEnd5 - navigationStart5)
        print("Email有附件详情页面加载时间", str(durtime5 / 1000), ".s")
        sleep(5)
        # 顶层
        driver.switch_to.default_content()
        # 定位到Message菜单
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.ID, 'menu_messsage'))).send_keys(Keys.ENTER)
        except Exception as e:
            print("找不 id为 create_link " + e)
        driver.implicitly_wait(30)
        # iframe_message层
        driver.switch_to.frame("iframe_message")
        sleep(5)
        navigationStart2 = driver.execute_script("return window.performance.timing.fetchStart")
        # 定位到All pending文件夹
        driver.find_element_by_xpath(".//*[@id='msg_todo']/a").click()
        # endtime = datetime.datetime.now()
        loadEventEnd2 = driver.execute_script("return window.performance.timing.loadEventEnd")
        # loadtime=(endtime-starttime)
        # print(loadtime)
        durtime2 = (loadEventEnd2 - navigationStart2)
        print("Message All pending加载时间", str(durtime2 / 1000), ".s")
        sleep(10)
        # 定位到Starred文件夹
        driver.find_element_by_xpath(".//*[@id='col_sub']/div[3]/ul/li[8]/a").click()
        sleep(5)
        # ctn-iframe层
        driver.switch_to.frame("message-list")
        sleep(5)
        # 定位到关键字搜索框
        driver.find_element_by_xpath(".//*[@id='keyword']").send_keys("adeveci")
        sleep(5)
        # 定位到Search 按钮
        driver.find_element_by_xpath(".//*[@id='btn-search']").click()
        sleep(20)
        navigationStart8 = driver.execute_script("return window.performance.timing.fetchStart")
        driver.find_element_by_xpath(".//*[@id='listDiv']//td[contains(text(),'adeveci')]").click()
        loadEventEnd8 = driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime8 = (loadEventEnd8 - navigationStart8)
        print("Message无附件详情页面加载时间", str(durtime8 / 1000), ".s")
        sleep(5)
        # 顶层
        driver.switch_to.default_content()
        # iframe_message层
        driver.switch_to.frame("iframe_message")
        # 定位到Starred文件夹
        driver.find_element_by_xpath(".//*[@id='col_sub']/div[3]/ul/li[8]/a").click()
        sleep(5)
        # ctn-iframe层
        driver.switch_to.frame("message-list")
        sleep(5)
        # 定位到关键字搜索框
        driver.find_element_by_xpath(".//*[@id='keyword']").send_keys("envixr")
        sleep(5)
        # 定位到Search 按钮
        driver.find_element_by_xpath(".//*[@id='btn-search']").click()
        sleep(20)
        navigationStart8 = driver.execute_script("return window.performance.timing.fetchStart")
        driver.find_element_by_xpath(".//*[@id='listDiv']//td[contains(text(),'envixr')]").click()
        loadEventEnd8 = driver.execute_script("return window.performance.timing.loadEventEnd")
        durtime8 = (loadEventEnd8 - navigationStart8)
        print("Message有附件详情页面加载时间", str(durtime8 / 1000), ".s")
        sleep(5)
        #顶层
        driver.switch_to.default_content()
        # 定位到Ticket模块
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, './/*[@id=\'col-main\']/div[1]/div[3]/ul/li[5]/a'))).send_keys(Keys.ENTER)
        except Exception as e:
            print("找不 id为 create_link " + e)
        driver.implicitly_wait(30)
        navigationStart3 = driver.execute_script("return window.performance.timing.fetchStart")
        # 定位到All pending文件夹
        driver.find_element_by_xpath(".//*[@id='col_sub']/div[3]/ul/li[1]/a").click()
        # endtime = datetime.datetime.now()
        loadEventEnd3 = driver.execute_script("return window.performance.timing.loadEventEnd")
        # loadtime=(endtime-starttime)
        # print(loadtime)
        durtime3 = (loadEventEnd3 - navigationStart3)
        print("Ticket All加载时间", str(durtime3 / 1000), ".s")
        sleep(5)


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

