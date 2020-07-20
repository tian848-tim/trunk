from pymongo import MongoClient
from difflib import SequenceMatcher
import datetime



client = MongoClient(host="192.168.1.168", port=27017)
db = client['newaim_purchase_tlives']
db.authenticate(name="sys_purchase", password="sys_purchase")

coll = db.get_collection("na_sta_sales_forecast_in_comment")
soll = db.get_collection("na_sta_sales_forecast")

def datetimes():
    global time
    time = datetime.datetime.now().isocalendar()
    for index in range(len(datetime.datetime.now().isocalendar())):
        print(time[index])
    return time

def uid_chats():
    #int类型转换为str
    time = list(map(str,datetimes()))
    pipeline = [{ "$unwind": "$sku" },{"$match":{"wk":time[1],"yr":time[0]}},{"$group": {"_id": "$sku","qty": { "$sum": "$qty" }}},{"$sort":{"_id":1}}]

    list_chat = list(coll.aggregate(pipeline))

    sku = [d['_id'] for d in list_chat]

    print(sku)

    return sku




def uid_chat():
    list_chats = list(soll.find({"wk":time[1],"yr":time[0],"inNumber":{"$gt": 0}},{"sku":1,"wk":1,"inNumber":1}).sort("sku"))

    sku1 = [d['sku'] for d in list_chats]

    print(sku1)

    return sku1

def uid_chats1():
    time = list(map(str, datetimes()))
    pipeline = [{ "$unwind": "$sku" },{"$match":{"wk":time[1],"yr":time[0]}},{"$group": {"_id": "$sku","qty": { "$sum": "$qty" }}},{"$sort":{"_id":1}}]

    list_chat = list(coll.aggregate(pipeline))

    qty = [d['qty'] for d in list_chat]

    print(qty)
    return qty




def uid_chat1():
    list_chats = list(soll.find({"wk":time[1],"yr":time[0],"inNumber":{"$gt": 0}},{"sku":1,"wk":1,"inNumber":1}).sort("sku"))

    qty1 = [d['inNumber'] for d in list_chats]

    print(qty1)
    return qty1


def similar_ratio(strA, strB):
    # lambda 表达式表示忽略 “  ”（空格），空格不参与相似度地计算
    return SequenceMatcher(lambda x:x==" ", strA, strB).ratio()

def similar_ratios(strA, strB):
    # lambda 表达式表示忽略 “  ”（空格），空格不参与相似度地计算
    return SequenceMatcher(lambda x:x==" " ,strA, strB).ratio()

#查找list里面相邻字符串之间的相似度
def compute_similar():
    sku = uid_chats()
    sku1 = uid_chat()
    qty = list(map(str,uid_chats1()))
    qty1 = list(map(str,uid_chat1()))
    for index in range(len(sku1) - 1):
        ratios = similar_ratio(sku[index], sku1[index])
        ratios1 = similar_ratios(qty[index], qty1[index])

        if ratios != 1:
            print(sku[index], sku1[index])
        if ratios1 != 1:
            print(qty[index], qty1[index], sku[index], sku1[index])

##查找list里面相邻字符串之间的相似度
#def compute_similars():
#    sku = uid_chats()
#    sku1 = uid_chat()
#    qty = list(map(str,uid_chats1()))
#    qty1 = list(map(str,uid_chat1()))
#    for index in range(0,len(qty1) - 1):
#        ratios1 = similar_ratios(qty[index], qty1[index])
#
#        if ratios1 != 1:
#            print(qty[index], qty1[index],sku[index], sku1[index])
#


if __name__ == "__main__":
    #datetimes()
    compute_similar()
