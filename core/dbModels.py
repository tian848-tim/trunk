# -*- coding: utf-8 -*-
import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import peewee
import time, socket
from core.config import Config
from core.config import dbClection, BaseDbModel

cfg = Config().cfg
log = Config().log

dbconn = dbClection().Conn()

'''运程服务器日志'''
class Na_Script_Result(peewee.Model):
    script_id = peewee.CharField()
    script_name = peewee.CharField()
    target_url = peewee.CharField()
    status = peewee.IntegerField()
    result_pass = peewee.IntegerField()
    result_wrong = peewee.IntegerField()
    result_failed = peewee.IntegerField()
    result_error = peewee.IntegerField()
    result_file = peewee.CharField()
    result_context = peewee.TextField()
    log_path = peewee.CharField()
    run_time = peewee.DoubleField()
    run_hostname = peewee.CharField()
    run_ip = peewee.CharField()
    creator_id = peewee.CharField()
    creator_cn_name = peewee.CharField()
    creator_en_name = peewee.CharField()
    department_id = peewee.CharField()
    department_cn_name = peewee.CharField()
    department_en_name = peewee.CharField()
    created_at = peewee.DateField()

    class Meta:
        database = dbconn

    def add(self):
        try:
            ISOTIMEFORMAT = '%Y-%m-%d %H-%M-%S'

            # log.info("-------初始插入数据-------: [ " + cfg.get("mysql", "server") + " : " + cfg.get("mysql", "database") + " ]")
            naScriptResult = Na_Script_Result(
                script_id=self.script_id,
                script_name=self.script_name,
                target_url=self.target_url,
                status=self.status,
                result_pass=self.result_pass,
                result_wrong=self.result_wrong,
                result_failed=self.result_failed,
                result_error=self.result_error,
                result_file=self.result_file,
                result_context= self.result_context,
                log_path= self.log_path,
                run_time= self.run_time,
                run_hostname= socket.getfqdn(socket.gethostname()),
                run_ip= socket.gethostbyname(socket.getfqdn(socket.gethostname())),
                creator_id=self.creator_id,
                creator_cn_name = self.creator_cn_name,
                creator_en_name = self.creator_en_name,
                department_id = self.department_id,
                department_cn_name = self.department_cn_name,
                department_en_name = self.department_en_name,
                # created_at=time.strftime("%Y-%m-%d %H_%M_%S")
                created_at= time.strftime( ISOTIMEFORMAT, time.gmtime(time.time()))
            )
            naScriptResult.save();
            dbconn.close();
            log.info("-------数据插入成功-------")
        except Exception as e:
            log.info("-------数据插入失败 {0}-------".format(e))


'''
本地脚本日志映射对象
'''
class DbRunLogs(BaseDbModel):
    id = peewee.PrimaryKeyField()
    script_id = peewee.TextField(null=False)
    script_name = peewee.TextField(null=False)
    target_url = peewee.TextField(null=False)
    target_path = peewee.TextField(null=True)
    log_file = peewee.TextField(null=True)
    report_file = peewee.TextField(null=True)
    type = peewee.IntegerField(null=False, default=1)
    run_begin = peewee.DateTimeField(null=False)
    run_end = peewee.DateTimeField(null=False)
    run_time = peewee.FloatField(null=False)
    created_at = peewee.DateTimeField(null=False)

    class Meta:
        order_by = ('created_at',)
        db_table = 'na_run_logs'


if __name__ == "__main__":
    nsr = Na_Script_Result()
    nsr.script_id = 'ssssssssssssss'
    nsr.status = 0
    nsr.result_error = 1
    nsr.result_failed = 1
    nsr.result_pass = 1
    nsr.run_time = 0
    nsr.add()

