# -*- coding:utf-8 -*-

import sys


class Command_Parser(object):
    #这里处理外部输入的参数，正确的参数,列表长度应该为3,5,7这三种，针对这三种参数做处理。
    def __init__(self, input_param):
        self.script_name = input_param[0]

        self.domainToSearch = None
        self.number_thread = None
        self.filename = None

        if len(input_param) == 3:
            self._deal_Three(input_param[1:])
        elif len(input_param) == 5:
            self._deal_Five(input_param[1:])
        elif len(input_param) == 7:
            self._deal_Seven(input_param[1:])

    def _deal_Three(self, input_param):
        if input_param[0] != '-k':
            print 'must input -k param'
        self.domainToSearch = input_param[1]


    def _deal_Five(self, input_param):
        if input_param[0] != '-k':
            print 'must input -k param'
        self.domainToSearch = input_param[1]

        if input_param[2] == '-t':
            self.number_thread = input_param[3]
        elif input_param[2] == '-d':
            self.filename = input_param[3]

    def _deal_Seven(self, input_param):
        if input_param[0] != '-k':
            print 'must input -k'
        self.domainToSearch = input_param[1]

        if input_param[2] == '-t':
            self.number_thread = input_param[3]

        if input_param[4] == '-d':
            self.filename = input_param[5]




if __name__ == "__main__":
    input_param = sys.argv[:]
    t = Command_Parser(input_param)
    print t.domainToSearch, t.number_thread, t.filename

