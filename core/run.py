# -*- coding: utf-8 -*-
import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest,time,json,datetime
from  HTMLTestRunner import HTMLTestRunner
from core.config import Config
from core.dbModels import Na_Script_Result, DbRunLogs



#定义测试用例路径
cfg = Config().cfg
log = Config().log

class Report:
    def __init__(self):
        if (sys.argv.__len__()>1):
            self.script = sys.argv[1]
        else:
            # self.script = "test_login.py"
            self.script = ""

        self.script = sys.argv[0]

        self.test_dir = cfg.get("path", "script")
        self.report_dir = cfg.get("path", "report")
        log.info(rootPath)

    def runs(self, script):
        log.info("-------测试用例开始---------")
        self.script = script
        # if(test_dir): self.test_dir = test_dir
        # if(report_dir): self.report_dir = report_dir


        discover = unittest.defaultTestLoader.discover(self.test_dir, pattern=self.script)
        beginDate = time.time()
        beginDateTime = datetime.datetime.now()

        # 创建报告文件夹
        dir1 = time.strftime("%Y%m")
        dir2 = time.strftime("%d")
        if (not os.path.exists(self.report_dir + '/' + dir1)):
            os.mkdir(self.report_dir + '/' + dir1, 777)
        if (not os.path.exists(self.report_dir + '/' + dir1 + '/' + dir2)):
            os.mkdir(self.report_dir + '/' + dir1 + '/' + dir2, 777)

        # 报告文件完整路径
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        report_name = self.report_dir + '/' + dir1 + '/' + dir2 + '/' + now + '_result.html'

        # 打开文件在报告文件写入测试结果
        with open(report_name, 'wb') as f:
            log.info("报告文件：" + report_name)
            try:
                runer = HTMLTestRunner(stream=f, title="Test Report [{0}]".format(self.script), description='Test case result')
                result = runer.run(discover)
                # attrs = runer.getReportAttributes(result)

                #插入数据库
                ent = Na_Script_Result()
                # 读取脚本的ID
                if (result.result.__len__() > 0):
                    rs = result.result
                    for item in rs:
                        if (item.__len__() > 0):
                            ent.script_id = item[1].script_id
                            ent.script_name = item[1].script_name
                            ent.target_url = item[1].target_url
                            ent.log_path = item[1].log_path

                ent.creator_id=sys.argv[1]
                ent.creator_cn_name = sys.argv[2]
                ent.creator_en_name = sys.argv[3]
                ent.department_id = sys.argv[4]
                ent.department_cn_name = sys.argv[5]
                ent.department_en_name = sys.argv[6]
                ent.status = 1
                ent.result_error = result.error_count
                ent.result_failed = result.failure_count
                ent.result_pass = result.success_count
                ent.result_file = report_name
                if (result.error_count > 0):
                    ent.result_context = json.dumps(result.errors[0][1])
                elif (result.failure_count > 0):
                    ent.result_context = json.dumps(result.failures[0][1])

                ent.run_time = round(time.time() - beginDate, 4)

                endDateTime = datetime.datetime.now()
                # 结果插入数据库
                ent.add()

            except Exception as e:
                log.info("-------测试用例执行失败---------")
                ent = Na_Script_Result()
                # 读取脚本的ID
                ent.script_id = self.script
                ent.creator_id=sys.argv[1]
                ent.creator_cn_name = sys.argv[2]
                ent.creator_en_name = sys.argv[3]
                ent.department_id = sys.argv[4]
                ent.department_cn_name = sys.argv[5]
                ent.department_en_name = sys.argv[6]
                ent.status = 1
                ent.result_error = 1
                ent.result_failed = 0
                ent.result_pass = 0
                ent.result_context = e
                ent.run_time = round(time.time() - beginDate, 4)
                # 结果插入数据库
                endDateTime = datetime.datetime.now()
                ent.add()
                # log.info(json.dumps(e))

        f.close()
        endDate = time.time()


        try:
            # 写本地执行日志
            entLocal = DbRunLogs.create(
                script_id=ent.script_id
                , script_name=ent.script_name
                , target_url=ent.target_url
                , log_file=ent.log_path
                , report_file=ent.result_file
                , run_begin=beginDateTime.strftime("%Y-%m-%d %H:%M:%S")
                , run_end=endDateTime.strftime("%Y-%m-%d %H:%M:%S")
                , run_time=ent.run_time
                , created_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                , type=1
            )
            entLocal.save()
        except Exception as e:
            print(e)

        log.info("-------测试用例结束----(" + str(round(endDate - beginDate, 4)) + " s)-----")


if __name__ == '__main__':
    #try:
    #    if(sys.argv.__len__() > 7 ):
    #        for i in range(7, sys.argv.__len__() ):
    #            # print('argv len {0}'.format(sys.argv.__len__()))
    #            # print('argv {0}: {1}'.format(i, sys.argv[i]))
    #            Report().runs(script=sys.argv[i])
    #except Exception as e:
    #    print(e)
    Report().runs(script="test38.py")