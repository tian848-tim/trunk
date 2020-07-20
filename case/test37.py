#判断入库、出库、结余数是否有误
from pymongo import MongoClient
from difflib import SequenceMatcher
import datetime
import ast
import sys, os
import time, unittest, configparser


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

'''
加载配置选项
'''
cfg = configparser.ConfigParser()
cfg.read(rootPath + '/core/config.ini')

'''
测试用例
'''

#client = MongoClient(host="192.168.1.168", port=27017)
#db = client['newaim_purchase_tlives']
#db.authenticate(name="sys_purchase", password="sys_purchase")

#coll = db.get_collection("na_sta_sales_forecast_in_comment")
#soll = db.get_collection("na_sta_sales_forecast")


class Refund(unittest.TestCase):

    global db
    client = MongoClient(host=cfg.get("MongoDB", "server"), port=int(cfg.get("MongoDB", "port")))
    db = client['newaim_purchase_tlives']
    db.authenticate(name="sys_purchase", password="sys_purchase")

        #coll = database.get_collection("na_sta_sales_forecast_in_comment")
        #soll = db.get_collection("na_sta_sales_forecast")

    #base_url = cfg.get("projects", "base_url")
    #project_path = cfg.get("projects", "project_path")
    log_path = cfg.get("webdriver", "log") + '/' + cfg.get("webdriver", "logfile") + '-%s.log' % time.strftime("%Y-%m-%d %H_%M_%S")

    def setUp(self):
        # 脚本标识－标题
        self.script_name = '判断入库、出库、结余数是否有误'
        # 脚本标识－ID
        self.script_id = 'workflow_FinancialClass_bankaccount_FlowBankAccount'



    def test_uid_chat(self):

        coll = db.get_collection("na_sta_sales_forecast_in_comment")
        soll = db.get_collection("na_sta_sales_forecast")

        # 动态命名变量
        prepare_list = locals()

        time = datetime.datetime.now().isocalendar()
        for index in range(len(datetime.datetime.now().isocalendar())):
            print(time[index])

        #int类型转换为str
        #time = self.datetimes()

        pipeline = [{ "$unwind": "$sku" },{"$group": {"_id": "$sku"}},{"$sort":{"_id":1}}]

        list_chat = list(soll.aggregate(pipeline))

        sku = [d['_id'] for d in list_chat]

        print(len(sku))


        for i in range(len(sku) - 1):

            prepare_list['sku' + str(i)] = sku[i]

            list_chats = list(soll.find({"sku":prepare_list['sku' + str(i)],"yr":{"$gte": time[0] - 1}},{"sku":1,"wk":1,"inNumber":1,"outNumber":1,"stockNumber":1,"yr":1,}).sort("yr"))

            inNumber = [d['inNumber'] for d in list_chats]
            #转换为list
            inNumbers = ast.literal_eval(str(inNumber))

            outNumber = [d['outNumber'] for d in list_chats]

            outNumbers = ast.literal_eval(str(outNumber))

            stockNumber = [d['stockNumber'] for d in list_chats]

            stockNumbers = ast.literal_eval(str(stockNumber))

            yr = [d['yr'] for d in list_chats]

            yrs = ast.literal_eval(str(yr))

            wk = [d['wk'] for d in list_chats]

            wks = ast.literal_eval(str(wk))

            #print(inNumbers)

            for index in range(len(inNumbers)):

                #print(inNumbers[index])

                prepare_list['inNumbers' + str(index)] = (inNumbers[index])

                #print(prepare_list['inNumbers' + str(index)])


                prepare_list['outNumbers' + str(index)] = (outNumbers[index])

                #print(prepare_list['outNumbers' + str(index)])


                prepare_list['stockNumbers' + str(index)] = (stockNumbers[index])

                #print(prepare_list['stockNumbers' + str(index)])

                prepare_list['yrs' + str(index)] = (yrs[index])

                prepare_list['wks' + str(index)] = (wks[index])

                #print(prepare_list['wks' + str(index)])


            for index in range(len(inNumbers)):

                if index != 0 and  index < len(inNumbers) - 1:

                    prepare_list['qty' + str(index+1)] = prepare_list['stockNumbers' + str(index)] + prepare_list['inNumbers' + str(index+1)] - prepare_list['outNumbers' + str(index+1)]

                    #print(prepare_list['qty' + str(index+1)])


                    ratios1 = SequenceMatcher(lambda x:x==" ",str(prepare_list['qty' + str(index+1)]), str(prepare_list['stockNumbers' + str(index+1)])).ratio()

                    #print(prepare_list['sku' + str(i)],prepare_list['wks' + str(index+1)],ratios1)

                    if ratios1 != 1 :

                        print(prepare_list['sku' + str(i)],prepare_list['yrs' + str(index+1)],prepare_list['wks' + str(index+1)],ratios1,prepare_list['qty' + str(index+1)])





if __name__ == "__main__":
    #datetimes()
    #compute_similar()
    #uid_chat2()
    unittest.main()
