# -*- coding: utf-8 -*-
import sys,os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import configparser
import peewee
from peewee import MySQLDatabase
from core.logger import Log

cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
全局配置
'''
class Config:
    def __init__(self):
        self.cfg= cfg
        self.log= Log(cfg.get("logs", "path"), cfg.get("logs", "pre"), cfg.get("logs", "level"))

'''
服务器数据库定义
'''
class dbClection:

    def __init__(self):
        self.log = Log(cfg.get("logs", "path"), cfg.get("logs", "pre"), cfg.get("logs", "level"))

    def Conn(self):
        return MySQLDatabase(
            host=cfg.get("mysql", "server")
            ,port=int(cfg.get("mysql", "port"))
            ,database=cfg.get("mysql", "database")
            , user=cfg.get("mysql", "user")
            , passwd=cfg.get("mysql", "passwd")
            , charset='utf8'
        )
        # return MySQLDatabase(self.connection)

'''本地数据库'''
class BaseDbModel(peewee.Model):
    class Meta:
        # curPath, filename = os.path.split(os.path.abspath(sys.argv[0]))
        # print( rootPath)
        database = peewee.SqliteDatabase(rootPath +'/../../../app/resource/data.db')


if __name__ == "__main__":
    db = dbClection()
    db.Conn().close()