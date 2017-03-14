# -*- coding:utf-8 -*-
"""
这个文件用来存放爬取过程中使用到的工具函数
"""
import base64

import requests
from lxml import etree

#这里用来需要爬取网页的列表
def Get_Max_Page(cookie, param):
    if not isinstance(cookie, str):
        return

    tmp_cotent = []

    search_url = Generate_Search_Url(param)
    r = requests.get(search_url, cookies= cookie)
    html = etree.HTML(r.text.encode('utf-8').decode('utf-8'))

    xobj = html.xpath("//body//div[@id='will_page']/a")

    for i in xobj:
        if isinstance(i, str):
            tmp_cotent.append(int(i))

    return max(tmp_cotent)


#https://fofa.so/result?q=test&qbase64=dGVzdA%3D%3D
#那个网站搜索时的url调用格式类似于上面，需要用到base64编码
def Generate_Search_Url(param):

    for i in xrange(len(param)):
        if param[i] == '=':
            search = param[i+1:]

    return 'https://fofa.so/result?q=' + search + '&qbase64=' + base64.b64decode(param)


def Get_Insert_page(number, param):

    for i in xrange(len(param)):
        if param[i] == '=':
            search = param[i+1:]

    return 'https://fofa.so/result?page=' + number + '&q=' + search + '&qbase64=' + base64.b64decode(param)