#encoding=utf-8
#author-夏晓旭
import sys,os
import logging,configparser
import logging.config
from var import *
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

#读取日志的配置文件
cfg = configparser.ConfigParser()
cfg.read('E:/web/python/trunk/var/logs')

#选择一个日志格式
logger=logging.getLogger("example02")

def error(message):
        #打印debug级别的信息
        logger.error(message)

def info(message):
        #打印info级别的信息
        logger.info(message)

def warning(message):
        #打印warning级别的信息
        logger.warning(message)

if __name__=="__main__":
        #测试代码
        info("hi")
        print ('E:/web/python/trunk/var/logs')
        error("world!")
        warning("gloryroad!")