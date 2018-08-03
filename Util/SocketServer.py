# -*- coding: utf-8 -*-

import threading
import time

from Util.Dispatch import Dispatch

'''
此处以后再加入java互动
开始线程，本类其实是一个定时器作用
'''


class SocketServer(object):
    def everyMonth(self):
        while True:
            lock = True
            # todo:bug 此处循环无数次，如何设置为一次
            if time.strftime("%d") == '1' and lock == True:
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('everyMonth')
                lock = False
                pass
            if time.strftime("%d") == '2':
                lock = True

    def everyDay(self):
        while True:
            current_time = time.localtime(time.time())
            if (current_time.tm_hour == 0) and (current_time.tm_min == 0) and (current_time.tm_sec == 0):
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('everyDay')
            time.sleep(1)
        pass

    def everyHour(self):
        while True:
            current_time = time.localtime(time.time())
            if (current_time.tm_min == 0) and (current_time.tm_sec == 0):
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('everyHour')
            time.sleep(1)

    def startProject(self):
        t1 = threading.Thread(target=self.everyHour, name='everyHour')
        t2 = threading.Thread(target=self.everyDay, name='everyDay')
        t3 = threading.Thread(target=self.everyMonth, name='everyMonth')
        t1.start()
        t2.start()
        t3.start()
