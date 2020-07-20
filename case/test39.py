



#! user/bin/python
#----------------------------------
'''
代码说明：
编写日期：
设计  者：
'''
#----------------------------------
from BeautifulReport import BeautifulReport
import unittest
import time
if __name__ == '__main__':
     currTime = time.strftime('%Y-%m-%d %H_%M_%S')
     filename = currTime+'.html'
     test_suite = unittest.defaultTestLoader.discover(r'F:/trunk/case', pattern='login_test.py')
     result = BeautifulReport(test_suite)
     result.report(filename=filename, description='测试deafult报告', log_path='.')