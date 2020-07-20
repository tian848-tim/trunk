import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
import time


# 待执行用例的目录
def allcase():
    # 引入执行用例集的根目录
    case_dir = r"F:\trunk\case"
    # 创建用例集函数testsuite
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='test38.py',
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase


# 执行用例，并放入到执行的html测试report中。
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    sopp = open(r"D:\res.html", "wb")
    runner = HTMLTestRunner(stream=sopp, title="sss", description="asd")
    runner.run(allcase())


#if __name__ == '__main__':
#     currTime = time.strftime('%Y-%m-%d %H_%M_%S')
#     filename = currTime+'.html'
#     test_suite = unittest.defaultTestLoader.discover(r'F:/trunk/var/report', pattern='login_test.py')
#     result = BeautifulReport(test_suite)
#     result.report(filename=filename, description='测试deafult报告', log_path='.')