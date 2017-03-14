# -*- coding:utf-8 -*-
import sys
import Threading

from utilities import Get_Max_Page, Generate_Search_Url,Get_Insert_page
from download_prepare import Scrapy_Prepare


class Workder(Threading.thread):
    def __init__(self, param, start_position, *args, **kwargs):
        super(Workder, self).__init__(*args, **kwargs)
        self.param = param
        self.start_postion = None
    @property
    def start_position(self):
        return self.start_position

    @start_position.setter
    def start_position(self, value):
        self.start_position = value

    def run(self):
        while True:











class WorkManager(object):
    def __init__(self, num_threading = 1):
        self.param = []
        self.workers = []
        self._initThread(num_threading)


    def _initThread(self, num_threading):
        for num in xrange(num_threading):
            work = Woker(param = self.param)
            self.workers.append(work)

    def waitForthreadCompele(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not len(self.workers):
                self.workers.append(worker)

    def run(self):
        for w in self.workers:
            w.start_position = self.total_page
            w.start()
            self.total_page += 10

    @property
    def ParamForCraw(self):
        raise ReferenceError("READ ONLY")
    @ParamForCraw.setter
    def ParamForCraw(self, value):
        if not isinstance(value, tuple)
            print "type error"
            sys.exit(1)
        cookie, param = value
        self.total_page = Get_Max_Page(cookie, param)
        self.param.append(value)
        self.param.append(self.total_page)
