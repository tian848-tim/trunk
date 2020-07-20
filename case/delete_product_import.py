import sys, os
import time, unittest, configparser
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
from pymongo import MongoClient
import json

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')


client = MongoClient(host="13.54.79.205", port=16767)
db = client['shopify']
db.authenticate(name="shopify", password="shopify_123")

coll = db.get_collection("product_import")


def loadvendername():
    global result
    file = open(rootPath + '/data/delete_product_import.json', encoding='utf-8')
    data = json.load(file)
    result = [(d['user_id']) for d in data['user']]

    return result

def uid_chat():
    su = loadvendername()

    myquery = {"user_id":su[0]}

    x = coll.delete_many(myquery)

    print(x.deleted_count, "个文档已删除")


if __name__ == "__main__":
    uid_chat()