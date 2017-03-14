# -*- coding:utf-8 -*-

"""
这个文件用来实现爬取前的准备工作，获取必要的参数
"""


import requests
from lxml import etree

class Scrapy_Prepare(object):

    def __init__(self, URL = None, login_URL = None):
        if URL is not None and login_URL is not None:
            self.url = URL
            self.login_url = login_URL
            self.token = None
            self.lt = None
            self.username = '442621753@qq.com'
            self.passwd = 'a2316678BC'
            self.nosec_session = None
            self.s = requests.Session()

            self._GET_Token()
            self._GET_Cookie()

            self.cookie = None

#这个函数用来获取token和lt。提交表单的时候需要用到
    def _GET_Token(self):
        r = requests.get(self.login_url)
        self.nosec_session = r.cookies['_nosec_cas_session']
        html = r.text
        if len(html) > 0:
            page_src = etree.HTML(html.encode('utf-8').decode('utf-8'))
            self.token = page_src.xpath("//body//form[@id = 'login-form']/input[@name = 'authenticity_token']/@value")[0]

            self.lt = page_src.xpath("//body//form[@id = 'login-form']/input[@id = 'lt']/@value")[0]


#用来获取cookie，cookie用来登录网站的时候识别身份。
    def _GET_Cookie(self):
#构造一个伪装的头部
        headers = {
                   'Host':'i.nosec.org',
                   'User - Agent':'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:52.0) Gecko / 20100101Firefox / 52.0',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept - Language':"en-US,en;q=0.5",
                   'Connection':"keep-alive",
                   'Upgrade - Insecure - Requests': "1",
                   }
#这里获取一个无会话模式的cookie，提交登录表单的时候需要用到
        cookie = {'_nosec_cas_session':self.nosec_session}
        r = self.s.post(self.login_url, headers = headers, data = {'utf8':'✓' ,'authenticity_token':self.token, 'lt':self.lt,
                                                  'username':self.username, 'password':self.passwd, 'button': ""}, cookies=cookie)

#这里获取location，我分析网站的时候发现，要想拿到登录用的cookie，需要向这个location提供的网址申请
        location = r.history[0].headers['Location']
        res = location[:4] + 's' + location[4:]

        r = self.s.get(str(res))
#这个这里就能获取到登录用的cookie，可以用这个cookie来保持登录的状态
        self.cookie = r.history[0].cookies['_fofapro_ars_session']
