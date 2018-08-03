# -*- coding: utf-8 -*-
'''
将数据插入数据库中
'''
import configparser

import jaydebeapi


class InsertDataBase(object):
    def __init__(self):
        Config = configparser.ConfigParser()
        Config.read('../Resource/dbconfig.conf')
        self.dirver = Config.get('DATABASE2', 'dirver')
        self.url = Config.get('DATABASE2', 'url')
        self.user = Config.get('DATABASE2', 'user')
        self.password = Config.get('DATABASE2', 'password')
        self.jarFile = '../Resource/ojdbc6.jar'

    def insertDataBaseNextHour(self, result_NextHour):
        db = jaydebeapi.connect(
            self.dirver, [
                self.url, self.user, self.password], self.jarFile)
        try:
            curs = db.cursor()
            # todo:在此处加入sql，此处应该使用更新
            sqlx = ''
            curs.execute(sqlx)
        finally:
            db.close()
        # todo：此处加入插入数据
        print(result_NextHour)
        pass

    def insertDataBaseSameDay(self, result_SameDay):
        db = jaydebeapi.connect(
            self.dirver, [
                self.url, self.user, self.password], self.jarFile)
        try:
            curs = db.cursor()
            # todo:在此处加入sql，此处使用插入
            sqlx = ''
            curs.execute(sqlx)
        finally:
            db.close()
        pass

    # # 周的预测暂时用不到
    # def insertDataBaseAfterDay(self):
    #     pass
