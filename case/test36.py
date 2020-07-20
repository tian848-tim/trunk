#判断预测数量是否有误

from pymongo import MongoClient
from difflib import SequenceMatcher
import datetime
import ast



client = MongoClient(host="172.28.62.152", port=27017)
db = client['newaim_purchase_tlives']
db.authenticate(name="sys_purchase", password="sys_purchase")

coll = db.get_collection("na_sta_sales_forecast_in_comment")
soll = db.get_collection("na_sta_sales_forecast")

# 动态命名变量
prepare_list = locals()

def datetimes():
    global time
    time = datetime.datetime.now().isocalendar()
    for index in range(len(datetime.datetime.now().isocalendar())):
        print(time[index])
    return time

def similar_ratio(strA, strB):
    # lambda 表达式表示忽略 “  ”（空格），空格不参与相似度地计算
    return SequenceMatcher(lambda x:x==" ", strA, strB).ratio()

def uid_chats():
    #int类型转换为str
    time = list(map(str,datetimes()))

    pipeline = [{ "$unwind": "$sku" },{"$group": {"_id": "$sku"}},{"$sort":{"_id":1}}]

    list_chat = list(soll.aggregate(pipeline))

    sku = [d['_id'] for d in list_chat]

    print(len(sku))

    for i in range(len(sku) - 1):

        prepare_list['sku' + str(i)] = sku[i]

        #print(prepare_list['sku' + str(i)])

        for wk in range(52):

            if wk >= int(time[1]):

                pipeline = [{ "$unwind": "$sku" },{"$match":{"sku":prepare_list['sku' + str(i)],"yr":time[0],"wk":str(wk)}},{"$group": {"_id": "$sku","qty": { "$sum": "$qty" }}},{"$sort":{"_id":1}}]

                list_chat = list(coll.aggregate(pipeline))

                prepare_list['sku' + str(i) + str(wk)]  = [d['_id'] for d in list_chat]

                #print(prepare_list['sku' + str(i) + str(wk)])

                if len(prepare_list['sku' + str(i) + str(wk)]) == 0:

                    prepare_list['sku' + str(i) + str(wk)] = prepare_list['sku' + str(i)]

                #    print("123",prepare_list['sku' + str(i) + str(wk)])

                else:
                    # 转为str
                    prepare_list['sku' + str(i) + str(wk)] = ''.join(prepare_list['sku' + str(i) + str(wk)])

                prepare_list['qty' + str(i) + str(wk)] = [d['qty'] for d in list_chat]
                #转换为list
                prepare_list['qty' + str(i) + str(wk)] = ast.literal_eval(str(prepare_list['qty' + str(i) + str(wk)]))

                #print(prepare_list['qty' + str(i) + str(wk)])

                if len(prepare_list['qty' + str(i) + str(wk)]) == 0:

                    prepare_list['qty' + str(i) + str(wk)] = 0

                #    print("456",prepare_list['qty' + str(i) + str(wk)])

                else:
                    # 转为str
                    prepare_list['qty' + str(i) + str(wk)] = ''.join('%s' %id for id in prepare_list['qty' + str(i) + str(wk)])

                #print(prepare_list['qty' + str(i) + str(wk)])

                list_chats = list(soll.find({"sku":prepare_list['sku' + str(i)],"wk": wk, "yr": int(time[0])},{"sku": 1, "wk": 1, "inNumber": 1}))

                prepare_list['sku1' + str(i) + str(wk)]  = [d['sku'] for d in list_chats]

                #print(prepare_list['sku1' + str(i) + str(wk)])

                if len(prepare_list['sku1' + str(i) + str(wk)]) == 0:

                    prepare_list['sku1' + str(i) + str(wk)] = prepare_list['sku' + str(i)]

                    #print(type(prepare_list['sku1' + str(i) + str(wk)]))

                    #print("789",prepare_list['sku1' + str(i) + str(wk)])

                #print(prepare_list['sku1' + str(i) + str(wk)])

                else:
                    # 转为str
                    prepare_list['sku1' + str(i) + str(wk)] = ''.join(prepare_list['sku1' + str(i) + str(wk)])

                prepare_list['inNumber' + str(i) + str(wk)] = [d['inNumber'] for d in list_chats]
                #转换为list
                prepare_list['inNumber' + str(i) + str(wk)] = ast.literal_eval(str(prepare_list['inNumber' + str(i) + str(wk)]))

                #print(prepare_list['inNumber' + str(i) + str(wk)])

                if len(prepare_list['inNumber' + str(i) + str(wk)]) == 0:

                    prepare_list['inNumber' + str(i) + str(wk)] = 0

                    #print(type(prepare_list['inNumber' + str(i) + str(wk)]))

                    #print("159",prepare_list['inNumber' + str(i) + str(wk)])

                else:
                    #转为str
                    prepare_list['inNumber' + str(i) + str(wk)] = ''.join('%s' %id for id in prepare_list['inNumber' + str(i) + str(wk)])

                #prepare_list['inNumber' + str(i) + str(wk)] = str(prepare_list['inNumber' + str(i) + str(wk)])

                #print(type(prepare_list['inNumber' + str(i) + str(wk)]))

                #print(prepare_list['inNumber' + str(i) + str(wk)])


                #if len(prepare_list['qty' + str(i) + str(wk)]) > 0:

                    #print(prepare_list['sku' + str(i) + str(wk)],)
                    #print(prepare_list['qty' + str(i) + str(wk)],wk)

                #ratios = similar_ratio(str(prepare_list['sku' + str(i) + str(wk)]), str(prepare_list['sku1' + str(i) + str(wk)]))
                ratios1 = similar_ratio(str(prepare_list['qty' + str(i) + str(wk)]), str(prepare_list['inNumber' + str(i) + str(wk)]))

                if ratios1 != 1 :

                    print(prepare_list['sku' + str(i) + str(wk)],prepare_list['sku1' + str(i) + str(wk)],"predication:",prepare_list['qty' + str(i) + str(wk)],"inNumber:",prepare_list['inNumber' + str(i) + str(wk)],"wk:",wk)

                #print(ratios)

                #print(ratios1)


if __name__ == "__main__":
    uid_chats()
