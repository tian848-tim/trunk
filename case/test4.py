# _._ coding:utf-8 _._

"""
:author: gz_tester
:time: 2017.05.04
:content: 随机选择同一类型下的某一个元素
"""

from selenium import webdriver
import random
import time

class Course:

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.kgc.cn/list')
        self.driver.maximize_window()

    def get_first_category(self):
        """
        随机筛选课程方向

        :return:
        """
        first_categories = self.driver.find_elements_by_css_selector('dl.new-courseTag dd')[0]
        first_categories = first_categories.find_elements_by_css_selector('div.new-courseHref a')
        first_category = first_categories[random.randint(1, len(first_categories) - 1)]
        time.sleep(1)

        print(first_categories)

        print(len(first_categories))

        print(first_category)


        return first_category



    def run(self):
        """
        调用课程的筛选方向，并随机筛选方向

        :return:
        """
        first_category = self.get_first_category()
        first_category_name = first_category.text
        print("随机选择的课程方向是:{0}".format(first_category_name))
        first_category.click()
        time.sleep(1)

        self.driver.quit()
        print('测试通过')

if __name__ == '__main__':
    course = Course()
    course.run()