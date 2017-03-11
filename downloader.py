# -*- coding:utf-8 -*-

import Threading
import Queue.Queue


class Workder(Threading.thread):
    def __init__(self, Queue, *args, **kwargs):
        super(Workder, self).__init__(*args, **kwargs)








class WorkManager(object):
    def __init__(self, num_threading = 1):
        self.workQueue = Queue.Queue()
        self.workers = []
        self._initThread(num_threading)


    def _initThread(self, num_threading):
        for num in xrange(num_threading):
            work = Woker(workQueue = self.workQueue)
            self.workers.append(work)

    def waitForthreadCompele(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not len(self.workers):
                self.workers.append(worker)

    def run(self):
        for w in self.workers:
            w.start()