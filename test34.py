from pymongo import MongoClient
from difflib import SequenceMatcher
import datetime
import ast



client = MongoClient(host="192.168.1.168", port=27017)
db = client['newaim_purchase_tlives']
db.authenticate(name="sys_purchase", password="sys_purchase")

coll = db.get_collection("na_sta_sales_forecast_in_comment")
soll = db.get_collection("na_sta_sales_forecast")
# 动态命名变量
prepare_list = locals()

def similar_ratio(strA, strB):
    # lambda 表达式表示忽略 “  ”（空格），空格不参与相似度地计算
    return SequenceMatcher(lambda x:x==" ", strA, strB).ratio()

def uid_chat2():

    pipeline = [{ "$unwind": "$sku" },{"$group": {"_id": "$sku"}},{"$sort":{"_id":1}}]

    list_chat = list(coll.aggregate(pipeline))

    sku = [d['_id'] for d in list_chat]

    for index in range(len(sku) - 1):

        prepare_list['sku' + str(index)] = sku[index]

        list_chats = list(soll.find({"sku":prepare_list['sku' + str(index)],"yr":2019,"wk":{"$lte": 50}},{"sku":1,"wk":1,"inNumber":1,"outNumber":1,"stockNumber":1,}).sort("sku"))

        inNumber = [d['inNumber'] for d in list_chats]

        inNumbers = ast.literal_eval(str(inNumber))

        for index in range(len(inNumbers) - 1):

            prepare_list['inNumbers' + str(index)] = inNumbers[index]



    for index in range(len(sku) - 1):

        prepare_list['sku' + str(index)] = sku[index]

        list_chats = list(soll.find({"sku":prepare_list['sku' + str(index)],"yr":2019,"wk":{"$lte": 50}},{"sku":1,"wk":1,"inNumber":1,"outNumber":1,"stockNumber":1,}).sort("sku"))

        outNumber = [d['outNumber'] for d in list_chats]

        outNumbers = ast.literal_eval(str(outNumber))

        for index in range(len(outNumbers) - 1):

            prepare_list['outNumbers' + str(index)] = (outNumbers[index])


    for index in range(len(sku) - 1):

        prepare_list['sku' + str(index)] = sku[index]

        list_chats = list(soll.find({"sku":prepare_list['sku' + str(index)],"yr":2019,"wk":{"$lte": 50}},{"sku":1,"wk":1,"inNumber":1,"outNumber":1,"stockNumber":1,}).sort("sku"))

        stockNumber = [d['stockNumber'] for d in list_chats]

        stockNumbers = ast.literal_eval(str(stockNumber))

        for index in range(len(stockNumbers) - 1):

            prepare_list['stockNumbers' + str(index)] = (stockNumbers[index])


    for index in range(len(sku) - 1):

        prepare_list['sku' + str(index)] = sku[index]

        list_chats = list(soll.find({"sku":prepare_list['sku' + str(index)],"yr":2019,"wk":{"$lte": 50}},{"sku":1,"wk":1,"inNumber":1,"outNumber":1,"stockNumber":1,}).sort("sku"))

        wk = [d['wk'] for d in list_chats]

        wks = ast.literal_eval(str(wk))

        for index in range(len(wks) - 1):

            prepare_list['wks' + str(index)] = (wks[index])


    for index in range(len(sku) - 1):

        print(prepare_list['inNumbers' + str(index)])
        print(prepare_list['outNumbers' + str(index)])
        print(prepare_list['stockNumbers' + str(index)])

        prepare_list['qty' + str(index+1)] = int(prepare_list['stockNumbers' + str(index)]) + int(prepare_list['inNumbers' + str(index+1)]) - int(prepare_list['outNumbers' + str(index+1)])

        #ratios = similar_ratio(str(qty), stockNumber[0])
        #print(wk[index])
        #print(type(wk[index]))

        #if int(wk[index]) != '1':

        ratios1 = similar_ratio(str(prepare_list['qty' + str(index+1)]), str(prepare_list['stockNumbers' + str(index+1)]))

        #print(prepare_list['sku' + str(index)],ratios1)

        #if ratios1 != 1:
            #print(prepare_list['sku' + str(index)],prepare_list['wks' + str(index)])





if __name__ == "__main__":
    #datetimes()
    #compute_similar()
    uid_chat2()
