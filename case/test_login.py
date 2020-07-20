# -*- coding: utf-8 -*-
import time,unittest,configparser
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read('../core/config.ini')

'''
测试用例
'''
class login(unittest.TestCase):
    base_url = cfg.get("project", "base_url")
    project_path = cfg.get("project", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '用户登录检查'
        # 脚本标识－ID
        self.script_id = 'test_login'
        self.target_url = self.base_url + self.project_path
        if(cfg.get("webdriver", "enabled")=="off"):
            # 如果使用最新firefox需要屏蔽下面这句
            self.driver = webdriver.Firefox()
        else:
            # 如果使用最新firefox需要使用下面这句
            self.driver = webdriver.Firefox(log_path=self.log_path)
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_(self):
        driver = self.driver
        driver.get(self.target_url)
        driver.find_element_by_id("account-inputEl").clear()
        driver.find_element_by_id("account-inputEl").send_keys("admin")
        driver.find_element_by_id("password-inputEl").clear()
        driver.find_element_by_id("password-inputEl").send_keys("123")
        driver.find_element_by_id('button-1013-btnIconEl').click()
        time.sleep(5)
        driver.find_element_by_css_selector("div.x-tool-img.x-tool-close").click()

        driver.find_element_by_link_text(u"我的消息").click()
        time.sleep(5)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

'''
Main 函数
'''
if __name__ == "__main__":
    unittest.main()

