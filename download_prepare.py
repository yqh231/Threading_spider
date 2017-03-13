# -*- coding:utf-8 -*-

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


    def _GET_Token(self):
        r = requests.get(self.login_url)
        self.nosec_session = r.cookies['_nosec_cas_session']
        html = r.text
        if len(html) > 0:
            page_src = etree.HTML(html.encode('utf-8').decode('utf-8'))
            self.token = page_src.xpath("//body//form[@id = 'login-form']/input[@name = 'authenticity_token']/@value")[0]
            print self.token

            self.lt = page_src.xpath("//body//form[@id = 'login-form']/input[@id = 'lt']/@value")[0]
            print self.lt

    def _GET_Cookie(self):

        headers = {
                   'Host':'i.nosec.org',
                   'User - Agent':'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:52.0) Gecko / 20100101Firefox / 52.0',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept - Language':"en-US,en;q=0.5",
                   'Connection':"keep-alive",
                   'Upgrade - Insecure - Requests': "1",
                   }
        cookie = {'_nosec_cas_session':self.nosec_session}
        r = self.s.post(self.login_url, headers = headers, data = {'utf8':'✓' ,'authenticity_token':self.token, 'lt':self.lt,
                                                  'username':self.username, 'password':self.passwd, 'button': ""}, cookies=cookie)
        #print r.text

        r = self.s.get(self.url)
        print r.headers['Set-Cookie']

        r = self.s.get(self.url, tmp)
        print r.text


    def run(self):
        r = requests.get(self.url)

test = Scrapy_Prepare("https://fofa.so/", "https://i.nosec.org/users/sign_in")