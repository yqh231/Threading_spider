# -*- coding:utf-8 -*-
"""
这个文件用来实现主要爬取功能
"""
import requests
from lxml import etree

def Parse_Save_Page(url, cookie):
    cook = {'locale':'en','_fofapra_ars_session':cookie}
    r = requests.get(url, cookies = cook)
    #print r.text

    html = etree.HTML(r.text)

    server = html.xpath(u"//body//div[@class='list_mod_c']//ul[@class='list_sx1']/li/a")
    test = html.xpath(u"//body//div[@class='auto-wrap']/text()")
    print test[3]









Parse_Save_Page('https://fofa.so/result?q=test&qbase64=dGVzdA%3D%3D',"98fb31547c12d970f062af5f760d3e40")